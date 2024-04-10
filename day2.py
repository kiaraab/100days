while True:
    try:
        total = float(input("How much is the total: $"))
        break  
    except ValueError:
        print("Invalid input. How much is the total: $")

while True:
    try:
        tip = (float(input("How much would you like to tip AS A PERCENTAGE: "))/100)
        break  
    except ValueError:
        print("Invalid input. How much would you like to tip: ")

while True:
    try:
        persons = int(input("How many people are splitting the bill: "))
        break  
    except ValueError:
        print("Invalid input. How many people are splitting the bill: ")

# Now user_input contains a valid float value
print("Each person should pay: $", "{:.2f}".format((total+(total*tip))/persons,))
