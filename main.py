# Name = Parker Grimes
# Collaborator = Miguel Elie

def encode(password="12345678"):
    encoded_pass_list = []
    encoded_pass_string = ""

    for digit in password:
        if digit.isdigit() == True:
            encoded_pass_list.append(str(int(digit) + 3))

    for num in encoded_pass_list:
        if int(num) >= 10:
            encoded_pass_list[encoded_pass_list.index(num)] = encoded_pass_list[encoded_pass_list.index(num)][1]

    encoded_pass_string = "".join(encoded_pass_list)

    return encoded_pass_string


if __name__ == "__main__":
    print("Menu")
    print("-------------")

    # Encoded password variable
    encoded_password = "000000"

    menu = [
        "1. Encode",
        "2. Decode",
        "3. Quit"
    ]

    for i in menu:
        print(i, end="\n")

    option = int(input("\nPlease enter an option: "))
    inputted_pass = input("Please enter your password to encode: ")

    if option == 1:
        encoded_password = encode(password=inputted_pass)
        print("Your password has been encoded and stored!")
    elif option == 2:
        pass
    elif option == 3:
        exit()