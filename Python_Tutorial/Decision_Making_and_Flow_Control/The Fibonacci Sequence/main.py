count = int(input("Enter the number of Fibonacci numbers to display: "))

if count <= 0:
    print("Please enter a positive integer.")
else:
    fib_sequence = [0, 1]

    while len(fib_sequence) < count:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

print("Fibonacci sequence:", fib_sequence[:count])