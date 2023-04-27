def binarySearch(input: list, target: int) -> int:
    if len(input) > 0:
        left_idx = 0
        right_idx = len(input) - 1

        if target > input[left_idx] and target < input[right_idx]:
            while left_idx <= right_idx:
                mid_idx = (right_idx + left_idx) // 2

                if target > input[mid_idx]:
                    left_idx = mid_idx + 1
                elif target < input[mid_idx]:
                    right_idx = mid_idx - 1
                else:
                    return mid_idx
        elif target == input[left_idx]:
            return left_idx
        elif target == input[right_idx]:
            return right_idx

    return None

if __name__ == "__main__":
    input = [2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6,
             7, 12, 12, 34, 43, 45, 78, 467, 568]
    print(binarySearch(input, 45))
