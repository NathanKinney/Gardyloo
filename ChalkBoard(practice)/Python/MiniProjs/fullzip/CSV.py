import csv

data = open('example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines)
print('\ n')
for row in data_lines[:5]:
    print(row)
print('\n')

all_emails = []

for row in data_lines[1:15]:
    all_emails.append(row[3])

print(all_emails)

file_to_output = open('madeup.csv', 'w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_Writer.writerow(['col1', 'col2', 'col3'])
csv_Writer.writerow([1,2,3],[4,5,6])
file_to_output.close()

