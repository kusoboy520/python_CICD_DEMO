
def calculate_area_square(length: int | float) -> int | float:
    if not isinstance(length, (int, float)) or length <= 0:
        raise TypeError("Length must be a positive non-zero number")
    return length * length

