import csv  # csv is abbreviation for Comma Separated Values

# write into csv file
with open("datas.csv", "w") as file_obj:
    writer = csv.writer(file_obj)
    writer.writerow(["transaction_id", "product_id", "price_value"])
    writer.writerow([100, 93, 13])
    writer.writerow([103320, 13, 3433])

# read from CSV

with open("datas.csv") as file_read:
    reader = csv.reader(file_read)
    for row in file_read:
        print(row)
