from random import randint

def quickSort(input: list) -> list:
    if len(input) > 1:
        pivot_idx = randint(0, len(input) - 1)

        smaller_list = []
        equal_list = []
        greater_list = []

        for index in range(len(input)):
            if index == pivot_idx:
                equal_list.append(input[index])
            else:
                if input[index] < input[pivot_idx]:
                    smaller_list.append(input[index])
                elif input[index] > input[pivot_idx]:
                    greater_list.append(input[index])
                else:
                    equal_list.append(input[index])

        equal_list = quickSort(smaller_list) + equal_list
        del smaller_list
        equal_list = equal_list + quickSort(greater_list)
        del greater_list

        return equal_list

    else:
        return input
    


if __name__ == "__main__":
    input = [4, 5, 6, 3, 2, 6, 7, 6, 4, 43,
                     34, 3, 2, 12, 12, 45, 5, 467, 78, 568]
    print(quickSort(input))
    
