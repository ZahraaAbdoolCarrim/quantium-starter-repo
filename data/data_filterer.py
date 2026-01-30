import csv

writer = csv.writer(open('data/daily_sales_data_improved.csv', 'a', newline=''))
def copy(old_file):
    with open(old_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            if row[0] == 'pink morsel':
                sales = float(row[1].replace('$', '')) * int(row[2])
                writer.writerow([f'${sales:.2f}', row[3], row[4]])


writer.writerow(['sales', 'date', 'region'])
for i in range(0, 3):
    copy(f'data/daily_sales_data_{i}.csv')