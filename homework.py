h = int(input("Enter the number to know it's decimal equivalent: "))
def binaryToDecimal(binary):
    decimal = 0 
    for i in range(len(binary)):
        decimal += int(binary[len(binary) - 1 - i]) * (2 ** i)
    return decimal
print("the decimal of is", binaryToDecimal(str(h)))
