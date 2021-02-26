import re
import sys

def convert_num(n):
    ''' function to convert a given number to words
        INPUT: can be integer or string
    '''
    n = str(n)
    if not re.match("^[0-9 -]+$", str(n)):
        print ("number invalid")
    n = int(n)
    
    if isinstance(n, int):
        ones = ['zero', 'one', 'two', 'three', 'four','five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        tens = ['zero', 'ten', 'twenty', 'thirty', 'forty','fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        
        # negative case
        if n < 0:
            return "negative {0}".format(convert_num(abs(n)))
        
        # thousands and more 
        for num, word in [(10**12, "trillion"), (10**9, "billion"), (10**6, "million"), (10**3, "thousand")]:
            if n >= num:
                return "{0} {1}{2}".format(convert_num(n // num), word, " {0}".format(convert_num(n % num)) if n % num else "")
       
        # takes care of numbers 100-999
        if n >= 100:
            if n % 100:
                return "{0} hundred and {1}".format(convert_num(n // 100), convert_num(n % 100))
            else:
                return "{0} hundred".format(convert_num(n // 100))
        # takes care of numbers 0-99
        if n < 20:
            return ones[n]
        else:
            return "{0}{1}".format(tens[n // 10], "-{0}".format(convert_num(n % 10)) if n % 10 else "")   
 
 #output to test function
value1, value2 = convert_num("123456"), convert_num("66723107008")
print(value1, value2, sep=' / ', end='\n', file=sys.stdout)

sys.stdout = open('result.txt', 'w')
print(value1)
sys.stdout.close()


