from audioop import reverse


def is_palindrome(word, lowercase):
    reversed = ""
    # the word isn't case sensitive
    if lowercase == True:
        word = word.lower()
        for index in range(len(word) - 1, -1 ,-1):
            reversed += word[index]
        # checks if the word is a palindrome
        if word == reversed:
            return lowercase
        else:
            return lowercase

    # the case is case sensitive
    else:
        for index in range(len(word) - 1, -1 ,-1):
            reversed += word[index]
        # Checks if the word is a palindrome
        if word == reversed:
            return lowercase
        else:
            return lowercase
# print(is_palindrome("Saippuakauppias", True)) # True
# print(is_palindrome("Saippuakauppias", False)) # False
# print(is_palindrome("saippuakauppias", True)) # True
print(is_palindrome("saippuakauppias", False)) # True
# print(is_palindrome("Minnaah", False)) # False
