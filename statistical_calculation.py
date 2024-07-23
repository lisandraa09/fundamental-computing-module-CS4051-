### Python Code for Part 1,2 & 3 with Comments:

def calculate_mean(numbers):
    #Calculate the mean of a list of numbers entered by the user
    return formatNumber(sum(numbers) / len(numbers))

def calculate_median(numbers):
    #Calculate the median of a list of numbers entered by the user
    num_sort = sorted(numbers)
    n = len(num_sort)
    midpoint = n // 2
    if n % 2 == 0:
        # If the number of elements is even, return the average of the two middle elements
        return formatNumber((num_sort[midpoint - 1] + num_sort[midpoint]) / 2)
    else:
        # If the number of elements is odd, return the middle element
        return formatNumber(num_sort[midpoint])

def calculate_mode(numbers):
    #Calculate the mode of a list of numbers entered by the user
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    # Find the maximum frequency count
    max_freq = max(frequency.values())
    # Identify numbers that have the maximum frequency amongst the input
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes

def calculate_standard_deviation(numbers, mean):
    #Determine the standard deviation of a user-entered list of numbers by using Bessel's correction (n-1)
    var = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    return var ** 0.5

def calculate_skewness(numbers):
    #Calculate the skewness of a list of numbers entered by the user
    n = len(numbers)
    if n < 3:
        return "Not enough numbers entered to calculate skewness."
    
    #Getting Mean, Standard Devialtion, Numerator and Denominator skewness for skewness calculation
    mean = calculate_mean(numbers)
    std_dev = calculate_standard_deviation(numbers, mean)
    
    skewness_numera = sum((x - mean) ** 3 for x in numbers)
    skewness_denomi = (n - 1) * (n - 2) * (std_dev ** 3)
    
    # Calculating skewness
    skewness = (n / skewness_denomi) * skewness_numera
    # Rounding the value to 2 decimal places
    rounded_skewness = round(skewness, 2)
    return formatNumber(rounded_skewness)

def read_numbers_from_file(file_path):
    #Read numbers from a file provided by the user and return them as a list of integers
    try:
        # Opening and reading the file based on the input file path provided
        with open(file_path, 'r') as file:
            # Getting the comma seperated values from the file
            numbers = file.read().split(", ")
            # Returning the comma seperated values as list of integers
            return [int(number) for number in numbers]
    except ValueError:
        return "File contains either non-numeric data or they are not in comma seperated format. Please clean the data."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    #Main function to manage user interactions with menu and perform statistical calculations on numbers provided by them
    numbers = []

    while True:
        entry = input("Enter mark or multiple marks separated by commas, or 'finish' to finish the input: ")
        # Handling terminating entry from user
        if entry.lower() == 'finish':
            if len(numbers) >= 2:
                print(f"Total numbers entered by you: {len(numbers)}")
                break
            else:
                # Handle unexpected value
                print("At least two numbers are required from you to perform calculations. Please enter more numbers to get statistics.")
                continue
        try:
            # Handling multiple entries entered by user separated by commas
            new_numbers = [int(num.strip()) for num in entry.split(',')]
            numbers.extend(new_numbers)
        except ValueError:
            # Handle unexpected value
            print("Invalid number input. Please enter valid numbers separated by commas.")

    while True:
        print("\nMenu:")
        print("1. Calculate Mean of the marks entered")
        print("2. Calculate Median of the marks entered")
        print("3. Calculate Mode of the marks entered")
        print("4. Calculate Skewness of the marks entered")
        print("5. Enter a new list of numbers")
        print("6. Append numbers from a file in the file path")
        print("7. close")

        choice = input("Choose an option: ")
        print("")

        if choice == '1':
            print("Mean of the marks entered:", calculate_mean(numbers))
        elif choice == '2':
            print("Median of the marks entered:", calculate_median(numbers))
        elif choice == '3':
            print("Mode of the marks entered:", calculate_mode(numbers))
        elif choice == '4':
            print("Skewness of the marks entered:", calculate_skewness(numbers))
        elif choice == '5':
            # Clear previous data
            numbers.clear()
            print("Previous data is cleared. Please enter new marks data.")
            # Get new numbers from the user
            while True:
                new_entry = input("Enter a new mark or marks (separated by commas), or 'finish' to finish entering new numbers: ")
                # Handling terminating entry from user
                if new_entry.lower() == 'finish':
                    if len(numbers) >= 2:
                        print(f"Total new number of marks entered: {len(numbers)}")
                        break
                    else:
                        # Handle unexpected value
                        print("At least two number of marks are required to perform statistical calculations. Please enter more numbers.")
                        continue
                try:
                    # Handle multiple entries separated by commas entered by the users
                    new_numbers = [int(num.strip()) for num in new_entry.split(',')]  
                    numbers.extend(new_numbers)
                except ValueError:
                    # Handle unexpected value
                    print("Invalid number input. Please enter valid numbers separated by commas.")
        elif choice == '6':
            # Get file path for the input file from the user.
            print("[Please make sure that the file contains numbers seperated by a comma. For eg. 10, 20, 30]")
            file_path = input("Enter the file_path to get numbers from: ")
            file_result = read_numbers_from_file(file_path)
            if isinstance(file_result, list):
                # Add the numbers from file to the number's list
                numbers.extend(file_result)
                print(f"Appended {len(file_result)} numbers from the file.")
                print(f"New list: {numbers}")
            else:
                print(file_result)
        elif choice == '7':
            # Handle terminating input from user
            print("close the application.")
            break
        else:
            # Handle unexpected value
            print("Invalid option. Please choose a valid option.")

# Format any decimal value. Eg. if value is 2.3, it returns 2.3 ,but if value is 1.0 it returns 1.0 (removes trailing zeros)
formatNumber = lambda n: n if n%1 else int(n) 

if __name__ == "__main__":
    main()
