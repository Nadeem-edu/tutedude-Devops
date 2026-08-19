# Menu Driven Calculator Program
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("\n Error: Cannot divide by zero")
        return None


while True:
    print("\n Py Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. To Exit")

    opt = input("Enter your Option (1-5):")

    if opt == '5':
        print("Closing Py Calculater")
        break

    if opt in ('1','2','3','4'):
        try:
            a = int(input("Enter 1st Number: \n"))
            b = int(input("Enter 2nd Number: \n"))
        except ValueError:
            print("Enter valid input only")
            continue

        if opt =='1':
            ans = add(a,b)
            print("\nResult:  ", ans)

        elif opt =='2':
            ans = sub(a,b)
            print("\nResult:  ", ans)

        elif opt =='3':
            ans = mul(a,b)
            print("\nResult:  ", ans)

        elif opt =='4':
            ans = div(a,b)
            if ans is not None:
                print("\nResult: ", ans)
        
                
        else:
            print("Please select a valid option from 1 to 5.")

