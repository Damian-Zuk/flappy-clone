import hashlib
import array

def get_special_key():
        return 'FAB24604CD9ABA'

def save_highscore(highscore):
    hs_hash = hashlib.sha256(str(highscore).encode('utf-8') + get_special_key().encode('utf-8')).hexdigest()
    hs_bytes = []
    for c in hs_hash:
        hs_bytes.append(int(c, 16))
    for c in str(highscore):
        hs_bytes.append(int(c))
    hs_file = open('highscore', 'wb')
    hs_file.write(array.array('B', hs_bytes))
    hs_file.close()

def load_highscore():
    hs_bytes = []
    hs_hash = ''
    hs = ''
    try:
        with open('highscore', 'rb') as f:
            byte = f.read(1)
            while byte:
                hs_bytes.append(str(hex(ord(byte)))[-1])
                byte = f.read(1)
        for i in range(0, 64):
            hs_hash += hs_bytes[i]
        for i in range(64, len(hs_bytes)):
            hs += hs_bytes[i]
        hs = int(hs)
        if hs_hash == hashlib.sha256(str(hs).encode('utf-8') + get_special_key().encode('utf-8')).hexdigest():
            return hs
    except:
        pass
    return 0