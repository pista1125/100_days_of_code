'''
for num in range(11,0, -1):
    for i in range(num):
        print(i, end="  ")
    print()

input_number = input("Adj meg egy egész számot")
if not input_number.isdecimal():
    print("nem jo")
else:
    print(int(input_number)*5)
'''

