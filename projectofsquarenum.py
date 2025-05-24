start = int(input("enter start number: "))
end = int(input("enter end number: "))

for num in range(start, end+ 1):
    square = num * num
    if square % 2 == 0:
        print(square, "is even")
    else:
        print(square, "is odd")
