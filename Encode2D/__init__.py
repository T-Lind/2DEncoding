def encode(x, y) -> int:
    maximum = max(abs(x), abs(y))
    main_term = 4 * maximum ** 2
    if x < 0 < y:
        return main_term + maximum - 2 * y - x
    elif x > 0 and y > 0:
        return main_term - x + maximum - 2 * y
    elif x > 0 > y:
        return main_term - 2 * x - maximum + y
    elif x < 0 and y < 0:
        return main_term + maximum - y
    else:
        return 0


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
