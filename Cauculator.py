print("Select the calculation you want to perform (+, -, /, *)")

def choosing():
    global type, a, b  # Sử dụng biến toàn cục để truy cập trong hàm khác
    type = input("Enter operation: ")

    if type not in ('+', '-', '/', '*'):
        print("Invalid keyword!")
        return choosing()  # Nếu sai, yêu cầu nhập lại

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

def cauculate():
    if type == '+':
        print("The Answer is:", a + b)
    elif type == '-':
        print("The Answer is:", a - b)
    elif type == '/':
        if b == 0:
            print("Error: Division by zero!")
        else:
            print("The Answer is:", a / b)
    elif type == '*':
        print("The Answer is:", a * b)

def Again():
    again = input("Another operation? (Y/N): ").lower()

    if again not in ('y', 'n'):
        print("Invalid keyword!")
        return Again()  # Yêu cầu nhập lại nếu sai

    if again == 'y':
        main()  # Gọi lại chương trình chính
    else:
        exit()

def main():
    choosing()
    cauculate()
    Again()

main()  # Chạy chương trình



        

