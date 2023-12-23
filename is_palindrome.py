def is_palindrome(text):
    return 'YES' if text.lower() == text.lower()[::-1] else 'NO'


print(is_palindrome('Шалаш'))
print(is_palindrome('Кулак'))
