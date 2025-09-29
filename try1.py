a = float(input())
b = float(input())
l = input()
if l == "*":
    print(a * b)
elif l == ":":
    print(a / b)
elif l == "+":
    print(a + b)
elif l == "-":
    print(a - b)
elif l == "^":
    print(a ** b)
else:
    print("Error")
