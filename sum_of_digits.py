import csv

def sum_of_digits_csv("numbers.csv"):
    with open("numbers.csv") as csvfile:
        reader = csv.reader("numbers.csv")
        for row in reader:
            for number in row:
                if not number.isdigit():
                    continue
                n = int(number)
                if n < 0:
                    n = abs(n)
                if n < 1 or n > 9999999999:
                    raise ValueError("Input integer must have between 1 and 10 digits")
                sum = 0
                while n > 0:
                    sum += n % 10
                    n //= 10
                print(f"Input number: {number}, Result: {sum}")
