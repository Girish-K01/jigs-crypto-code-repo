from multiprocessing import Pool
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import ec
from ecdsa import SigningKey
from hashlib import sha256
import secrets,pyaes,pickle,os,time, socket,pyaes, binascii

def generate_random_seed():
    return os.urandom(32)  
def derive_keys(seed):
    hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,  
        salt=None,
        info=b'key derivation',
        backend=default_backend()
    )
    derived_key = hkdf.derive(seed)
    return derived_key
def key_generation():
    seed = generate_random_seed() 
    ecc_key = derive_keys(seed)
    return ecc_key

def generate_ECC_pair(key):
    curve = ec.SECP256R1()
    private_key = ec.derive_private_key(int.from_bytes(key, 'big'), curve, default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def key_exchange(client_private_key, client_public_key, client_socket):
    server_public_key_bytes = client_socket.recv(1024)
    server_public_key = serialization.load_pem_public_key(server_public_key_bytes, default_backend())
    client_public_key_bytes = client_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    client_socket.send(client_public_key_bytes)
    shared_key = client_private_key.exchange(ec.ECDH(), server_public_key)

    #print("Shared key:", binascii.hexlify(shared_key))
    return shared_key
def sign_message(message):
    signature = signing_key.sign_deterministic(message, hashfunc=sha256)
    return signature+message
def nget_data_block(data, i):
    preprocessed_block = secrets.token_bytes(block_size) + data[i:i + block_size]
    return preprocessed_block
def encrypt_block(block,i):
    aes = pyaes.AESModeOfOperationCTR(SHARED_KEY, pyaes.Counter(IV+i))
    return aes.encrypt(block)

def generate_combined_message(signed_message, encrypted_message):
    return signed_message + encrypted_message

def preprocess_and_encrypt(data):
    x = [(data, i) for i in range(0, len(data), block_size)]
    with Pool() as pool:
        preprocessed_blocks = pool.starmap(nget_data_block, x)
        encrypted_blocks = pool.starmap(encrypt_block, [ (preprocessed_blocks[i],i) for i in range(len(preprocessed_blocks))])
        signatures = pool.map(sign_message, [block for block in encrypted_blocks])
    return signatures

def send_combined_message(combined_blocks, client_socket):
    data = pickle.dumps(combined_blocks)
    client_socket.send(data)

block_size = 8
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creating a socket object
host = socket.gethostname() # Get local machine name
port = 9999
client_socket.connect((host, port)) # Connecting to the server
    
ECC_KEY = key_generation()
PRIVATE_KEY, PUBLIC_KEY= generate_ECC_pair(ECC_KEY)
SHARED_KEY = key_exchange(PRIVATE_KEY, PUBLIC_KEY, client_socket)
with open("./data_files/onemb.txt") as file: #change the file name here according to necessary file size
    message = file.read().encode("utf-8")
#print("\nMessage Chosen: ", message)
private_key_bytes = PRIVATE_KEY.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
signing_key = SigningKey.from_pem(private_key_bytes)
IV = secrets.randbits(128)
start = time.time()
finalmessage = preprocess_and_encrypt(message)
end = time.time()
print(end - start) #prints the client processing time
client_socket.send(IV.to_bytes(16, byteorder="big"))    
send_combined_message(finalmessage, client_socket)
client_socket.close()
