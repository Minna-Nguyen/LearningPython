from audioop import reverse


def is_palindrome(word, lowercase):
    reversed = ""
    # reversing the string
    for i in word:
        reversed = i + reversed
    # comparing if it's a palindrome
    if word == reversed:
        return lowercase
    else:
        lowercase = False
        return lowercase
print(is_palindrome("saippuakauppias", lowercase=True)) # True
print(is_palindrome("Saippuakauppias", lowercase=True)) # False
print(is_palindrome("Minnaah", lowercase=True)) # False
