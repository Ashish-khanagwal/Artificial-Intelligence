def palindrome():
    word = input("Enter a word or number: ")
    data = list(word)
    reverse_data = list(word[::-1])

    # Compare whole list at once instead of nested loops
    if data == reverse_data:
        print("palindrome")
    else:
        print("not a palindrome")


palindrome()
