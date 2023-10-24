print("Welcome to tip calculator ")
bill = float(input("What was the total bill ?"))
tip = int(input("What percentage tip would you like to give? 10 ,12 or 15?"))
person = int(input("How many people to split the bill ?"))
tot = bill + (tip) * bill / 100
print(f"Each person should pay: {tot/person}")
