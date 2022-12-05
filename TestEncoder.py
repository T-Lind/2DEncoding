from Encode2D import slow_encode, decode

if __name__ == '__main__':
    coord = (-1023, 30)
    n = slow_encode(*coord)
    print(n)
    new_coord = decode(n)
    print(new_coord)
