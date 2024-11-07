from typing import List, TypeVar, Generic, Optional

T = TypeVar('T', bound=int)


class Matrix(Generic[T], list[List[T]]):
    def __init__(self, rows: Optional[List[List[T]]] = [], side_info: Optional[List[T]] = None):
        super().__init__(rows)
        self.side_info = side_info

    def __repr__(self) -> str:
        if not self:
            return "Matrix([])"

        max_width = max(len(str(item)) for row in self for item in row)

        rows = []
        for i, row in enumerate(self):
            formatted_row = " ".join(f"{item:>{max_width}}" for item in row)
            if self.side_info and i < len(self.side_info):
                formatted_row += f" | {self.side_info[i]}"
            rows.append(formatted_row)
        return "\n".join(rows)
