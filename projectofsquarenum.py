start = int(input("enter start number: "))
end = int(input("enter end number: "))

for num in range(1, 2 + 1):
    square = num * num
    if square % 2 == 0:
        print(square, "is even")
    else:
        print(square, "is odd")