from Encode2D import encode, decode

if __name__ == '__main__':
    coord = (968, -185)
    n = encode(*coord)
    print(n)
    new_coord = decode(n)
    print(new_coord)
