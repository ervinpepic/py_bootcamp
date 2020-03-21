# and
# or
# not

high_income = False
good_credit = True
student = True

# AND
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# OR
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

# NOT
if not student:
    print("Eligible")
else:
    print("Not eligible")

if (high_income and good_credit) and not student:
    print("Eligible")


# short circuit evaulation
if high_income or good_credit and not student:
    print("Eligible")

# if we leave AND operator in this logical statement we will get the short circuit evaulation
# because on the first condition python interpreter will interupt the rest of the statement and
# leave the if statement and will not consider other condition


