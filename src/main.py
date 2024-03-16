from typing import Union


def calculate_area_square(length: Union[int ,float]) -> Union[int ,float]:
    if not isinstance(length, (int, float)) or length <= 0:
        raise TypeError("Length must be a positive non-zero number")
    return length * length

