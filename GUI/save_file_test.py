import os
import csv

with open('csv_test.csv', newline='') as csv_file:
    spam_reader = csv.reader(csv_file, delimiter=';', quotechar='|') # Not sure if quotechar is useful
    for row in spam_reader:
        # print(row)
        for cell in row:
            print(cell)
        # print(', '.join(row))

with open("csv_test_2.csv", 'w', newline='') as csv_file_2:
    spam_writer = csv.writer(csv_file_2, delimiter=";", quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



# file_path = os.getcwd() + "/save_test" + "/saved_file.txt"
# with open(file_path, 'w') as f:
#     for data in output:
#         f.write(data)