class Solution:
    def numberToWords(self, num: int) -> str:
        def help(num):
            if num < 20:
                s = belowTe[num]
            elif num < 100:
                s = tens[num// 10] + " " + belowTe[num % 10]
            elif num < 1000:
                s = help(num // 100) + ' Hundred ' + help(num % 100)
            elif num < 1000000:
                s = help(num // 1000) + ' Thousand ' + help(num % 1000)
            elif num < 1000000000:
                s = help(num // 1000000) + ' Million ' + help(num % 1000000)
            else:
                s = help(num // 1000000000) + ' Billion ' + help(num % 1000000000)

            return s.strip()
        if num == 0:
            return 'Zero'
        belowTe = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight','Nine', 'Ten', 'Eleven', 'Twelve','Thirteen', 'Fourteen', 'Fifteen','Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        return help(num)
