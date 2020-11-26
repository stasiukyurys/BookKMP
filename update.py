import hashlib
from datetime import datetime


def sensor():
    print(datetime.utcnow())
    print(get_hash('D:\\BDp.mdb'))


def get_hash(file_path, mode='sha1'):
    h = hashlib.new(mode)
    with open(file_path, 'rb') as file:
        data = file.read()
    h.update(data)
    digest = h.hexdigest()
    return digest
