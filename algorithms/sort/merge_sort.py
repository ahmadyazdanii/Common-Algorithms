def mergeSort(input: list) -> list:
    if len(input) > 1:
        median_index = len(input) // 2
        left_list, right_list = input[:median_index], input[median_index:]

        mergeSort(left_list)
        mergeSort(right_list)

        left_idx = 0
        right_idx = 0
        merged_idx = 0

        while left_idx < len(left_list) and right_idx < len(right_list):
            if left_list[left_idx] < right_list[right_idx]:
                input[merged_idx] = left_list[left_idx]
                left_idx += 1
            elif right_list[right_idx] < left_list[left_idx]:
                input[merged_idx] = right_list[right_idx]
                right_idx += 1
            else:
                input[merged_idx] = left_list[left_idx]
                merged_idx += 1
                input[merged_idx] = right_list[right_idx]
                left_idx += 1
                right_idx += 1
            merged_idx += 1

        while left_idx < len(left_list):
            input[merged_idx] = left_list[left_idx]
            left_idx += 1
            merged_idx += 1

        while right_idx < len(right_list):
            input[merged_idx] = right_list[right_idx]
            right_idx += 1
            merged_idx += 1

        return input
    else:
        return input


if __name__ == "__main__":
    print(mergeSort([4, 5, 6, 3, 2, 6, 7, 6, 4, 43,
                     34, 3, 2, 12, 12, 45, 5, 467, 78, 568]))
