user_input = input("Enter numbers separated by spaces: ")
arr = [float(num) for num in user_input.split()]

print("Original list:", arr)

n = len(arr)
for i in range(n):
    swapped = False
    
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True
    
    if not swapped:
        break

print("Sorted list:", arr)