relative_x, relative_y = [], []
length = 1
value = 1


def encode(x, y) -> int:
    # global relative_x, relative_y
    pass


def slow_decode(n) -> [int, int]:
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
        return slow_decode(n)


def decode(n) -> [int, int]:
    radius = 0
    while 4 * radius ** 2 < n:
        radius += 1
    radius -= 1

    main_term = 4 * radius ** 2

    if n < main_term - 2*radius:
        value = 4
        # From top right corner
        pass
    elif n < main_term:
        # From top left corner
        pass
    elif n < main_term + 2*radius:
        # From bottom left corner
        pass
    else:
        # From bottom right corner
        pass
