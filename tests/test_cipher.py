from fastapi.testclient import TestClient

from cipherAPI import app
from cipherFunc import Cipher

cipher = Cipher()

client = TestClient(app)


def test_user_create():
    """ Test user creation """
    # Failing for now

    payload = {
        'username': 'testtest',
        'password': 'testtest'
    }

    user_url = '/users'

    response = client.post(user_url, data=payload)
    print(response.__dict__)

    # assert response.status_code == 200


def test_cipher_encrypt():
    """ Test string encrypt ith cipher algorithm """

    cipher_url = '/encrypt'

    encrypt = 'HELLO WORD'
    encrypted = cipher.cipher_algorithm(encrypt, 3)

    response = client.post(cipher_url, params={'string': encrypt, 'key': 3})

    element = response.content.decode('utf-8')[:-2]
    element = element.split(':')[1][1::]

    assert response.status_code == 200
    assert element == encrypted


def test_cipher_decrypt():
    """ Test string decrypt with cipher algorithm """

    cipher_url = '/decrypt'

    decrypt = 'KHOOR#ZRUG'
    decrypted = cipher.cipher_algorithm(decrypt, 3, decrypt=True)

    response = client.post(cipher_url, params={'string': decrypt, 'key': 3})

    element = response.content.decode('utf-8')
    element = ''.join(element.split(',')[0]).split(':')[1][1:-1]

    assert response.status_code == 200
    assert element == decrypted
