def y1(x: float) -> float:
    return x


def y2(x: float) -> float:
    if x == 0:
        x += 0.001
    return round((x**2 - 1) / abs(x), 5)
