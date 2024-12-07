from collections import defaultdict
from foos import y1, y2

left_padding = 8
chars = 150


def x_calc(a: float, b: float, n: int) -> list[float]:
    step = abs(a - b) / n
    return [round(a + i * step, 4) for i in range(n + 1)]


def y_calc(foo: callable, x_vals: list[float]) -> dict[float, list[float]]:
    result = defaultdict(list)
    for x in x_vals:
        y = foo(x)
        result[y].append(x)
    return result


def extend_and_sort_y(
    y1_val: dict[float, list[float]], y2_val: dict[float, list[float]]
) -> list[tuple[float, list[float]]]:
    combined = defaultdict(list)
    for y_dict in (y1_val, y2_val):
        for y, x_vals in y_dict.items():
            combined[y].extend(x_vals)
    return sorted(combined.items())


def ox_val(x_vals: list[float], n: int) -> str:
    cell_width = chars // n
    return ''.join(f"{x:<{cell_width}.2f}" for x in x_vals)


def print_ox(x_val: list[float], n: int) -> None:
    print(f"{' ':>10}{"-"*chars}-> Ox")
    print(f"{' ':>10}{ox_val(x_val, n)}")


def print_graph(a: float, b: float, n: float) -> None:
    x_val = x_calc(a, b, n)
    y1_val = y_calc(y1, x_val)
    y2_val = y_calc(y2, x_val)
    y_all = extend_and_sort_y(y1_val, y2_val)

    print(f"{'Oy ':>{left_padding}} ^")
    print(f"{' ':>{left_padding}} |")
    for i in range(len(y_all)-1, -1, -1):
        current_column = 1
        y, x_ = y_all[i][0], y_all[i][1]
        print(f'{y:>{left_padding}} |', end='')

        for x in x_:
            padd = chars // n
            posx = x_val.index(x) * padd - current_column
            if posx >= chars:
                continue

            print(posx* " " + "*", end='')
            current_column += posx

        print()

    print_ox(x_val, n)


if __name__ == "__main__":
    ys = y_calc(y1, x_calc(0, 2, 20))
    ys2 = y_calc(y2, x_calc(0, 2, 20))
    print(extend_and_sort_y(ys, ys2))
