def palindrome():
    word = input("Enter a word or number: ")
    if word == word[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")


palindrome()
