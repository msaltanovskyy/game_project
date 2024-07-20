import hashlib


def encryption(password):
    password = password.encode('utf-8')
    sha512_hash = hashlib.sha512(password)
    hashed_password = sha512_hash.hexdigest()
    return hashed_password


def check_password(input_password, hashed_password):
    input_hashed_password = encryption(input_password)
    print(f"input_hashed_password: {input_hashed_password}, hashed_password: {hashed_password}")
    return input_hashed_password == hashed_password
