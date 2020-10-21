def binary_search_row(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2
        if mid >= len(arr) - 1:
            return mid
        elif arr[mid + 1] > x >= arr[mid]:
            return mid

        elif arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

    # If we reach here, then the element was not present
    return -1


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return True

            # If we reach here, then the element was not present
    return False

    while (True):

        if guess >= len(rows) - 1 or guess == 0:
            return guess
        elif rows[guess + 1] > target >= rows[guess]:
            return guess
        elif target < rows[guess]:
            mx = guess
            guess = guess // 2
        else:
            guess = guess + (mx - guess) // 2


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row_starts = [r[0] for r in matrix]
        if len(row_starts) == 1:
            return binary_search(matrix[0], target)

        if matrix[-1][-1] < row_starts[-1]:
            row_starts.append(matrix[-1][-1])

        print("row_starts ", row_starts)

        row = binary_search_row(row_starts, target)
        print(row)

        if row == -1:
            return False

        return binary_search(matrix[row], target)
