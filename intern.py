def read_my_csv(filename):
    category = None
    header = None
    record_data = {}
    table = []

    def make_record():
        return [dict(zip(header, x)) for x in table]

    with open(filename, 'rU') as csv_data:
        reader = csv.reader(csv_data)

        for row in reader:
            if not row:
                if category:
                    record_data[category] = make_record()
                table = []
                category = next(reader)[0]
                header = tuple(x.strip() for x in next(reader))
            else:
                table.append([x.strip() for x in row])

    if category:
        record_data[category] = make_record()
    return record_data

#test code
import csv
data = read_my_csv('raw.csv')
for item in data.items():
    print(item[0])
    for records in item[1]:
        for record in records.items():
            print('   {}'.format(record))
        print()