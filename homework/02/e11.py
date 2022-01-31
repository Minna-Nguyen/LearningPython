from audioop import reverse


def isPalindrome(word, lowercase):
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
print(isPalindrome("saippuakauppias", lowercase=True)) # True
print(isPalindrome("Saippuakauppias", lowercase=True)) # False
print(isPalindrome("Minnaah", lowercase=True)) # False
