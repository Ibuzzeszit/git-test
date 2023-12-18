class playground:

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


    def romanToInt(s:str) -> int:
        romanNum = []
        total = 0
        for i in s:
            if i == "I":
                romanNum.append(1)
            elif i == "V":
                romanNum.append(5)
            elif i == "X":
                romanNum.append(10)
            elif i == "L":
                romanNum.append(50)
            elif i == "C":
                romanNum.append(100)
            elif i == "D":
                romanNum.append(500)
            else:
                romanNum.append(1000)
            print(romanNum)

            lenRomanNum = len(romanNum)
            print(lenRomanNum)
            
        for i, x in enumerate(romanNum):
            if i != lenRomanNum-1:
                if romanNum[i] < romanNum[i+1]:
                    romanNum[i] = -romanNum[i]
            total = total + romanNum[i]
        return total
    
print(playground.romanToInt("XCIX"))