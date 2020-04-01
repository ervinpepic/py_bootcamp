temperature = 30
if temperature > 30:
    print("it's hot")
    print("Please refresh your body with water")
elif temperature > 20:
    print("Take care of yourself")
else:
    print("Not bad...")
print("exiting...")


# ternary operator...
age = 20
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# or
age_1 = 19
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)

# or
age_2 = 21
message1 = "Eligible" if age_2 >= 18 else "Not Eligible"
