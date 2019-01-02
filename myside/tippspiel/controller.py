import hashlib
from uuid import uuid4
from . import sniffer


def newUser(request):
    Hasher = hashlib.sha256()
    salt = str(uuid4)
    Hasher.update(bytes(salt+password))
    hash = Hasher.hexdigest()
