from Encode2D import slow_encode, encode, decode

if __name__ == '__main__':
    coord = (13, -785)
    n = slow_encode(*coord)
    print(n)
    n = encode(*coord)
    print(n)
    new_coord = decode(n)
    print(new_coord)
