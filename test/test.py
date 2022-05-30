

def isPalindrome(s: str) -> bool:
    p = ""
    for char in s:
        if char.isalnum():
            p += char.lower()
        print(p)

    left = 0
    right = len(p)-1
    while left <= right:
        if p[left] != p[right]:
            return False
        print(left)
        print(right)
        left += 1
        right -= 1

    return True


teststring = "Helloolleh"

print(isPalindrome(teststring))


