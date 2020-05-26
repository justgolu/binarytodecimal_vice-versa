def binary_to_decimal(n):
    dec = 0
    i = 0
    rem = 0
    while(n != 0):
        rem = n % 10
        n = n//10
        dec = dec + rem*pow(2,i) 
        i= i+1
    print("The decimal value is: ",dec)

def decimal_to_binary(decimalnum):
    num =0
    if(decimalnum != 0):
        decimal_to_binary(decimalnum//2)
        num = decimalnum % 2  
    print(num, end = "")

print("\nChoose operation: ")
print("\n1. binary to decimal\n2. decimal to binary")
while (1):
    ch = int(input("\nEnter choice: "))

    if (ch == 1):
        res = int(input("Enter the decimal number: "))
        decimal_to_binary(res)
    elif ch==2:
        res = int(input("Enter the binary number: "))
        binary_to_decimal(res)
    else:
         exit("Thank you!!")



