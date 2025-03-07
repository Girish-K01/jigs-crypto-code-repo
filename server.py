from multiprocessing import Pool, Value, Array
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.asymmetric import ec
from ecdsa import VerifyingKey, BadSignatureError
from hashlib import sha256
import pyaes,pickle,os,time,binascii, socket,pyaes
from ecdsa import SigningKey
from hashlib import sha256

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

def key_generation():
    seed = generate_random_seed() 
    ecc_key = derive_keys(seed)
    return ecc_key

def generate_ECC_pair(key):
    curve = ec.SECP256R1()
    private_key = ec.derive_private_key(int.from_bytes(key, 'big'), curve, default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def key_exchange(server_private_key, server_public_key, client_socket):
    server_public_key_bytes = server_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    client_socket.send(server_public_key_bytes)
    client_public_key_bytes = client_socket.recv(1024)
    client_public_key = serialization.load_pem_public_key(client_public_key_bytes, default_backend())
    shared_key = server_private_key.exchange(ec.ECDH(), client_public_key)
    return client_public_key_bytes, shared_key

def receive_combined_message(client_socket):
    data = b''
    while True:
        chunk = client_socket.recv(1024 * 1024 * 2)  # Receive up to 1 MB of data
        if not chunk:
            break
        data += chunk
    combined_blocks = pickle.loads(data)
    return combined_blocks


def decrypt(message, i):
    aes = pyaes.AESModeOfOperationCTR(SHARED_KEY, pyaes.Counter(IV+i))
    x = aes.decrypt(message)
    nonce,message = x[:8], x[8:]
    if nonce in previous_nonces:
        print("Replay attack detected! Terminating program")
        exit()
    with open("nonce_database.bin", "ab") as database:
        database.write(nonce)
        database.write(b"\n")
    return message
def verify_signature(block):
    signature, nmessage = block[:64], block[64:]
    try:
        verifying_key.verify(signature, nmessage, hashfunc=sha256)
    except BadSignatureError:
        print("Signature verification not successful")
        exit()
    return nmessage

def preprocess_and_decrypt(data):
    with Pool() as pool:
        message_blocks = pool.map(verify_signature, data)
    y = [(message_blocks[i],i) for i in range(len(message_blocks))]
    with Pool() as pool:
        decrypted_blocks = pool.starmap(decrypt,y)
    return decrypted_blocks

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
server_socket.bind((host, port))
server_socket.listen(5)
print("Server listening...")
client_socket, addr = server_socket.accept()
print("Connection from: ", addr)

ECC_KEY = key_generation()
PRIVATE_KEY, PUBLIC_KEY = generate_ECC_pair(ECC_KEY)
public_key_bytes, SHARED_KEY = key_exchange(PRIVATE_KEY, PUBLIC_KEY, client_socket)


IV = int.from_bytes(client_socket.recv(16), byteorder="big")
verifying_key = VerifyingKey.from_pem(public_key_bytes)

with open("nonce_database.bin", "rb") as database:
    previous_nonces = set(database.read().split(b"\n"))

start = time.time()
combined_blocks = receive_combined_message(client_socket)
finalmessage = preprocess_and_decrypt(combined_blocks)
end = time.time()
print(end - start) #prints the server processing time
byte_data = b''.join(finalmessage)
complete_message = byte_data.decode("utf-8")
#print(complete_message)
client_socket.close()
server_socket.close()