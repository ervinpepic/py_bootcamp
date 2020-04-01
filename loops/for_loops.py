# use loop to create repetition

for number in range(1, 10, 2):
    print('Hello', number, number * ".")


# for - else

successfull = True
for num in range(5):
    print('Getting...')
    if successfull:
        print("Done with header request!")
        break

successfull_1 = False
for num_1 in range(10):
    print('Getting...')
    if successfull_1:
        print("Done with header request!")
        break
else:
    print("Error while getting headers...")
