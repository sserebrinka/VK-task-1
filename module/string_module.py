def reverse_string(s: str) -> str:
    return s[::-1]

def count_vowels(s: str) -> int:
    vowels = 'aeiouyаоиыуэяюеё'
    return sum(1 for char in s.lower() if char in vowels)

def is_palindrome(s: str) -> bool:
    s = s.lower().strip()
    return s == reverse_string(s)