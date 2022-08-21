print("Press 1 for Celcius to Fahrenheit")
print("Press 2 for Fahrenheit to Celcius")
print("Press 3 for Celcius to Kelvin")
print("Press 4 for Kelvin to Celcius")
print("Press 5 for Fahrenheit to Kelvin")
print("Press 6 for Kelvin to Fahrenheit")
print("Enter choice:", end=" ")
choice = int(input())

match choice:
    case 1:
        print("Enter temperature in C for conversion:", end=" ")
        temp = float(input())
        newTemp = temp * (9 / 5) + 32
        print("Temperature is:", newTemp, "F")
    case 2:
        print("Enter temperature in F for conversion:", end=" ")
        temp = float(input())
        newTemp = (temp - 32) * (5 / 9)
        print("Temperature is:", newTemp, "C")
    case 3:
        print("Enter temperature in C for conversion:", end=" ")
        temp = float(input())
        newTemp = temp + 273.15
        print("Temperature is:", newTemp, "K")
    case 4:
        print("Enter temperature in K for conversion:", end=" ")
        temp = float(input())
        newTemp = temp - 273.15
        print("Temperature is:", newTemp, "C")
    case 5:
        print("Enter temperature in F for conversion:", end=" ")
        temp = float(input())
        newTemp = (temp - 32) * (5 / 9) + 273.15
        print("Temperature is:", newTemp, "K")
    case 6:
        print("Enter temperature in K for conversion:", end=" ")
        temp = float(input())
        newTemp = (temp - 273.15) * (9 / 5) + 32
        print("Temperature is:", newTemp, "F")
    case _:
        print("Error!")