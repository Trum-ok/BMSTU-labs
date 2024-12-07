from graph import print_graph


def main() -> None:
    a, b = map(float, input("Введите начало и конец интервала через пробел: ").split())
    n = int(input("Введите количество участков разбиения интервала: "))

    if a >= b:
        print("Интервал должен быть длиной > 0!")
    else:
        print_graph(a, b, n)


if __name__ == "__main__":
    main()
