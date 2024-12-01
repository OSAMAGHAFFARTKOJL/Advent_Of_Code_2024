def solve_problem(lines):
    left_numbers = []
    right_numbers = []

    for line in lines:
        # Split each line into two numbers
        left, right = map(int, line.split())
        left_numbers.append(left)
        right_numbers.append(right)

    # Sort both arrays
    left_numbers.sort()
    right_numbers.sort()

    total_difference = 0
    for left, right in zip(left_numbers, right_numbers):
        total_difference += abs(left - right)

    return total_difference

def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]

if __name__ == "__main__":
    # Replace 'input.txt' with the actual input file name
    filename = '/content/input.txt'
    input_lines = read_input_file(filename)
    # Process the input to separate and sort the numbers
    res= solve_problem(input_lines)
    print(res)
###################################################################
#Puzzle 2




def solve_problem(lines):
    """
    Separate left and right numbers into two arrays, sort each, and return the results.
    :param lines: List of lines from the input file.
    :return: Tuple of sorted arrays (left_numbers, right_numbers).
    """
    left_numbers = []
    right_numbers = []

    for line in lines:
        # Split each line into two numbers
        left, right = map(int, line.split())
        left_numbers.append(left)
        right_numbers.append(right)
    total = 0
    for i in left_numbers:
      mup = i*right_numbers.count(i)
      total += mup

    return total




def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]


if __name__ == "__main__":
    # Replace 'input.txt' with the actual input file name
    filename = '/content/input.txt'
    input_lines = read_input_file(filename)

    # Process the input to separate and sort the numbers
    res= solve_problem(input_lines)
    print(res)
