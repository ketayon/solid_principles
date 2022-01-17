class ExportCsv:
    def __init__(self, raw_data):
        self.data = self.prepare(raw_data)

    
    def prepare(self, raw_data):
        result = ''
        for item in raw_data:
            new_line = ','.join(
                (
                    item['name'],
                    item['surname'],
                    item['company']
                )
            )
            result += f"{new_line}\n"
        return result

    
    def write_file(self, filename):
        with open(filename, 'w', encoding='UTF8') as f:
            f.write(self.data)


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

exporter = ExportCsv(data)
exporter.write_file('principles/srp/out.csv')