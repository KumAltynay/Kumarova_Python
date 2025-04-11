def main():
    # Check if number is greater than 7
    try:
        number = int(input("Enter a number: "))
        if number > 7:
            print("Hello")
    except ValueError:
        print("That's not a valid number.")

    # Hello, John
    name = input("Enter your name: ")
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

    # Output array elements that are multiples of 3
    list_input = input("Enter numbers separated by spaces: ")
    try:
        number_list = list(map(int, list_input.strip().split()))
        divisible_by_3 = []
        for num in number_list:
            if num % 3 == 0:
                divisible_by_3.append(num)
        print("Numbers divisible by 3:", divisible_by_3)
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces.")

main()