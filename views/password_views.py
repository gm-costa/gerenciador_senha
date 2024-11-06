from base64 import b64encode
from hashlib import sha256
from string import ascii_letters, digits, punctuation
from secrets import choice
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken


class FernetHasher:
    RANDOM_STRING_CHARS = ascii_letters + digits + punctuation
    BASE_DIR = Path(__file__).resolve().parent.parent
    KEY_DIR = BASE_DIR / 'keys'

    
    def __init__(self, key):
        if not isinstance(key, bytes):
            key = key.encode()

        self.fernet = Fernet(key)
    
    @classmethod
    def _get_random_string(cls, lenght=16):
        string = ''
        for i in range(lenght):
            string += choice(cls.RANDOM_STRING_CHARS)

        return string
    
    @classmethod
    def create_key(cls, archive=False):
        value = cls._get_random_string()
        hasher = sha256(value.encode('utf-8')).digest()
        key = b64encode(hasher)
        # print(f'value: {value}\nhasher: {hasher}\nkey: {key}')
        if archive:
            return key, cls.archive_key(key)
        return key, None

    @classmethod
    def archive_key(cls, key):
        file = 'key.key'
        if not cls.KEY_DIR.exists():
            cls.KEY_DIR.mkdir()

        if Path(cls.KEY_DIR / file).exists():
            file = f'key_{cls._get_random_string(5)}.key'
        
        with open(cls.KEY_DIR / file, 'wb') as arq:
            arq.write(key)
        
        return cls.KEY_DIR / file
    
    def encrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode('utf-8')
        return self.fernet.encrypt(value)

    def decrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode('utf-8')
        
        try:
            return self.fernet.decrypt(value).decode()
        except InvalidToken as e:
            return 'Token incorreto !'
