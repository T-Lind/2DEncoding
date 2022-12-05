from Encode2D import slow_decode, decode

if __name__ == '__main__':
    for i in range(3, 16, 2):
        print(slow_decode(4 * i ** 2 + 4 * i - 2))
        print(decode(4 * i ** 2 + 4 * i - 2), end="\n\n")
    # print(decode(16_777_215))
