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

def decode(encoded_password):
    decode_list = []
    for i in encoded_password:
        if int(i) <= 2:
            if int(i) == 0:
                decode_list.append(str(7))
            elif int(i) == 1:
                decode_list.append(str(8))
            else:
                decode_list.append(str(9))
        else:
            decode_list.append(str(int(i)-3))
    decoded_password = "".join(decode_list)
    return decoded_password

if __name__ == "__main__":
    # Encoded password variable
    encoded_password = "000000"

    while True:
        print("Menu")
        print("-------------")

        menu = [
            "1. Encode",
            "2. Decode",
            "3. Quit"
        ]

        for i in menu:
            print(i, end="\n")

        option = int(input("\nPlease enter an option: "))

        if option == 1:
            inputted_pass = input("Please enter your password to encode: ")
            encoded_password = encode(password=inputted_pass)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}")
        elif option == 3:
            exit()