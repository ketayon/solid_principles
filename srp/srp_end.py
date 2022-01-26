class DataFormater:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    
    def prepare(self):
        result = ''
        for item in self.raw_data:
            new_line = ','.join(
                (
                    item['name'],
                    item['surname'],
                    item['company']
                )
            )
            result += f"{new_line}\n"
        return result


class FileWriter:
    def __init__(self, filename):
        self.filename = filename


    def write(self, data):
        with open(self.filename, 'w', encoding='UTF8') as f:
            f.write(data)


data = [
  {
    'name': 'Bill',
    'surname': 'Gates',
    'company': 'Microsoft'
  },
  {
    'name': 'Steve',
    'surname': 'Jobs',
    'company': 'Apple'
  }
]

formatter = DataFormater(data)
formatted_data = formatter.prepare()

writer = FileWriter('solid_principles/srp/out.csv')
writer.write(formatted_data)