from typing import Optional


def check_empty(*args: list) -> bool:
    return any(not arg for arg in args)


def print_matrix(matrix: list[list[int]], side_info: Optional[list] = None) -> None:
        if not matrix:
            return "Matrix([])"

        max_width = max(len(str(item)) for row in matrix for item in row)

        rows = []
        for i, row in enumerate(matrix):
            formatted_row = " ".join(f"{item:>{max_width}}" for item in row)
            if side_info and i < len(side_info):
                formatted_row += f" | {side_info[i]}"
            rows.append(formatted_row)
        print("\n".join(rows))

