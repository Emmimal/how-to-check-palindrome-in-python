
**palindrome_checker.py** (All key functions + demo at the bottom)

```python
# palindrome_checker.py
# Code examples from: https://emitechlogic.com/how-to-check-palindrome-in-python/
# Feel free to use, modify, and share!

def is_palindrome_slice(s: str) -> bool:
    """Method 1: String slicing – fastest and most Pythonic"""
    return s == s[::-1]


def is_palindrome_reversed(s: str) -> bool:
    """Method 2: Using reversed() and join"""
    return "".join(reversed(s)) == s


def is_palindrome_two_pointers(s: str) -> bool:
    """Method 3: Two-pointer – O(1) space"""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_number(x: int) -> bool:
    """Method 4: Mathematical reversal for integers"""
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    return original == reversed_num


def is_palindrome_recursive(s: str) -> bool:
    """Method 5: Recursive check"""
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])


def is_valid_palindrome(s: str) -> bool:
    """Real-world: Ignore case, spaces, punctuation"""
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def is_near_palindrome(s: str) -> bool:
    """Almost palindrome – remove at most one character"""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Try skipping one side
            return (s[left:left+1] + s[left+1:right+1] == (s[left:left+1] + s[left+1:right+1])[::-1] or
                    s[left:right] == s[left:right][::-1])
        left += 1
        right -= 1
    return True  # Already perfect (adjust if you want "exactly one" removal)


# Demo / Tests
if __name__ == "__main__":
    tests = [
        "racecar", "hello", "A man, a plan, a canal: Panama",
        "abca", 1221, -121, "deified"
    ]
    
    print("Testing methods...\n")
    for test in tests:
        if isinstance(test, int):
            print(f"{test} (number): {is_palindrome_number(test)}")
        else:
            print(f"'{test}'")
            print(f"  Slicing: {is_palindrome_slice(test)}")
            print(f"  Two-pointer: {is_palindrome_two_pointers(test)}")
            print(f"  Valid (cleaned): {is_valid_palindrome(test)}")
            print(f"  Near palindrome: {is_near_palindrome(test)}")
            print("---")
