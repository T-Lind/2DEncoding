relative_x, relative_y = [], []
length = 1
value = 1

def encode(x, y) -> int:
    # global relative_x, relative_y
    pass


def decode(n) -> [int, int]:
    global relative_x, relative_y
    if len(relative_x) >= n:
        return sum(relative_x[:n]), sum(relative_y[:n])
    else:
        global length, value
        while len(relative_x) <= n:
            for _ in range(length):
                relative_x.append(value)
            for _ in range(length):
                relative_x.append(0)
            for _ in range(length):
                relative_y.append(0)
            for _ in range(length):
                relative_y.append(value)

            value *= -1
            length += 1
        return decode(n)
