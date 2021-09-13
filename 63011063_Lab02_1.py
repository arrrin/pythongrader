class translator:

    def __init__(self):
        self.number = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        self.symbol = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        self.i = 12
    def deciToRoman(self, num):
        roman_symbol = ''
        if num == 0:
            return '0'
        while num:
            div = num // self.number[self.i]
            num %= self.number[self.i]
            while div>0:
                roman_symbol += self.symbol[self.i]
                div -= 1
            self.i -= 1
        return roman_symbol
    def romanToDeci(self, s):
        roman_str = list(s)
        sum = []
        sum_int = 0
        roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                          'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in roman_str:
            for j in roman_numerals.keys():
                if i == j:
                    sum.append(roman_numerals.get(j))
        for i in range(len(sum) - 1):
            if sum[i] < sum[i + 1]:
                sum[i] *= -1
        for i in range(len(sum)):
            sum_int += int(sum[i])

        return sum_int

num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))