def calculate_average(num_list):
    total_sum = sum(num_list)
    average = total_sum / len(num_list)
    return average

user_input = input("Enter numbers separated by spaces: ")
num_list = [float(num) for num in user_input.split()]

print(f"The average is: {calculate_average(num_list)}")