import sys


def palindrome():
    while True:
        word = input("Enter a word or number: ")
        data = list(word)
        reverse_data = list(word[::-1])
        is_plaindrome = True

        for i in range(len(data)):
            for j in range(len(reverse_data)):
                if i == j:
                    if data[i] != reverse_data[j]:
                        is_plaindrome = False
                    break
            if not is_plaindrome:
                break
        if is_plaindrome:
            print("palindrome")
        else:
            print("not a palindrome")

        print("Want to check more?")
        while True:
            user = input("(Y)es or (Q)uit?\n")
            if user.lower() not in ["y", "q"]:
                print("Choose from (Y) and (Q)")
                continue
            else:
                break
        if user.lower() == "y":
            return palindrome()
        else:
            print("Bye Bye!")
            sys.exit("")


palindrome()
