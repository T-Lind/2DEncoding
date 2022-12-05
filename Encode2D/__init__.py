relative_x, relative_y = [], []
length = 1
value = 1


def add_series():
    global relative_x, relative_y, length, value
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


def encode(x, y) -> int:
    if x == y == 0:
        return 0

    maximum = max(abs(x), abs(y))
    min_term = 4 * maximum ** 2 - 4 * maximum
    max_term = 4 * maximum ** 2 + 6 * maximum
    print(min_term, max_term, x, y)
    if x < 0 and y > 0:
        return min_term + abs(x) * ((max_term - min_term) / (abs(x) * 2)) - y
    elif x > 0 and y > 0:
        return min_term + x * ((max_term - min_term) / (x * 2)) - y - (x + y)
    elif x > 0 and y < 0:
        return min_term + x * ((max_term - min_term) / (x * 2)) - y + x + abs(y)
    elif x < 0 and y < 0:  # TODO: Fix
        return min_term + abs(x) * ((max_term - min_term) / (abs(x) * 2)) - y



def slow_encode(x, y) -> int:
    maximum = max(abs(x), abs(y))
    min_term = 4 * maximum ** 2 - 4 * maximum
    max_term = 4 * maximum ** 2 + 6 * maximum
    for n in range(min_term, max_term + 1):
        extrapolated = decode(n)
        if extrapolated == (x, y):
            return n
    raise IndexError("No suitable n found!")


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
    while 4 * radius ** 2 + 4 * radius < n:
        radius += 1

    main_term = 4 * radius ** 2

    if n <= main_term - 2 * radius:
        difference = (main_term - 2 * radius) - n
        return (radius, radius - difference)
    elif n <= main_term:
        difference = n - (main_term - 2 * radius)
        return (radius - difference, radius)
    elif n <= main_term + 2 * radius:
        difference = (main_term + 2 * radius) - n
        return (-radius, -(radius - difference))
    elif n <= main_term + 4 * radius:
        difference = (main_term + 4 * radius) - n
        return (radius - difference, -radius)
    else:
        raise IndexError(f"{n} is out of range!")
