import os
import csv
dir_path = "C:/Users/Pierre/Desktop"

os.chdir(dir_path)

with open('test_file.txt', 'r') as f:
   jpg_data = f.read()

print(jpg_data)

