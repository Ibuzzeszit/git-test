class Playground:

    def Palindrome(x:int) -> bool:
        if x < 0:
            return False
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = int(x / 10)

        digitsReversed = []
        for i in range(len(digits)-1, -1, -1):
            digitsReversed.append(digits[i])

        for i in range(len(digits)):
            if digits[i] != digitsReversed[i]:
                return False
        return True

print(Playground.Palindrome(2154512))