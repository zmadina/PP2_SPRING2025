def palindrome(text):
    reversed_text = ''.join(reversed(text))
    if text == reversed_text:
        print("Is a palindrome")
    else:
        print("Is not a palindrome")

text = input()
palindrome(text)