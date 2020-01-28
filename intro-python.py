import re
import sys
class Tools:
        def Calculator(self):
            a = re.findall('[*+-/%]', self)
            b = re.split('[*+-/%a-zA-Z]', self)
            signs = ["+","-","*","/","%"]
            if not a:
                a = [""]
            while(not a[0] in signs):
                a[0] = input("Re-enter arithmethic sign: ")
            while(not b[0].isdigit() or not b[1].isdigit()):
                b[0] = input("1st number: ")
                b[1] = input("2nd number: ")

            if a[0] == "*":
                print(f"Result: {int(b[0]) * int(b[1])}")
            elif a[0] == "+":
                print(f"Result: {int(b[0]) + int(b[1])}")
            elif a[0] == "-":
                print(f"Result: {int(b[0]) - int(b[1])}")
            elif a[0] == "/":
                print(f"Result: {int(b[0]) / int(b[1])}")
            elif a[0] == "%":
                print(f"Result: {int(b[0]) % int(b[1])}")
            else :
                print("Try Again!")

        def CurrencyConverter(self):
            exchange = {"EUR": 4.72, "USD": 4.26, "BGN": 2.41, "GBP": 5.26, "CHF": 4.33}
            x = re.search('\d+', self)
            y = re.findall('[a-zA-Z]+', self)
            print(f"RON: {(int(x[0]) * exchange[y[0].upper()]):.2f}")

def MainMenu(code):
    c = code
    choices = {1: "Calculator", 2: "Currency Converter"}
    print(f'1. %s \n2. %s' % (choices[1], choices[2]))
    
    while(not int(c)):
        try:
            c = int(input("Select a tool: "))
            pass
        except ValueError:
            print("Try Again!")
            pass
    
    if c == 1:
        d = input("Enter: ")
        Tools.Calculator(d)
    if c == 2:
        d = input("Amount: ")
        Tools.CurrencyConverter(d)
    if c == 3:
        d = input("string")
        Tools.Weight(d)
    if c > 4:
        print("Goodbye")
        quit()

MainMenu(0)
