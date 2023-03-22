def encoder(encode):
    encode_list = []
    encode_list[:0] = encode
    encoded_list = [int(n) + 3 for n in encode_list]
    encoded_str = ""
    for i in encoded_list:
        encoded_str += str(i)
    return encoded_str

def decoder(encoded_str,encode):
    print(f"The encoded password is {encoded_str}, and the original password is {encode}.\n")


def menu():
    global option
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit\n")

    option = int(input("Please enter an option: "))


def main():
    while True:
        menu()
        if option == 1:
            encode = input("Please enter your password to encode: ")
            encoder(encode)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decoder(encoder(encode), encode)
        else:
            break


if __name__ == "__main__":
    main()
