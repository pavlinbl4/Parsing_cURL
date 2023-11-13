
def calculate_limit(images_number:int) -> int:
    pages_number = images_number // 80
    if images_number % 80 == 0:
        return pages_number
    return pages_number + 1


if __name__ == '__main__':
    assert calculate_limit(80) == 1
    assert calculate_limit(77) == 1
    assert calculate_limit(81) == 2
    assert calculate_limit(160) == 2
    assert calculate_limit(159) == 2
    assert calculate_limit(169) == 3