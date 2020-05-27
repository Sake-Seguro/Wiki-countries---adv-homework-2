import json
import hashlib



class WikiCountry:

    def __init__(self, index, countries):

        self.url = 'https://en.wikipedia.org/wiki/'
        self.name = countries[0]
        self.start = 0
        self.index = index - 1
        self.all = countries

    def __iter__(self):
        return self

    def __next__(self):

        self.name = self.all[self.start]
        initial = self.name.split()
        final_definition = '_'.join(initial)
        self.url = 'https://en.wikipedia.org/wiki/' + final_definition
        self.start += 1
        if self.start == self.index:
            raise StopIteration
        return self.name, self.url


def yielding_countries(data):
    
    """
    Collecting the very data from provided JSON

    """
    
    world_countries = []

    for each in data:
        world_countries.append(each['name']['common'])
    return world_countries


def generator(file_path):

    with open(file_path, encoding='UTF-8') as criteria:

        for line in criteria:
            strip_line = line.strip()
            byte_line = strip_line.encode('utf-8')
            yield hashlib.md5(byte_line)



def main():

    with open('countries.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)
    countries = yielding_countries(json_data)
    counted_countries = len(countries)

    with open('List of countries with WiKi references.txt', 'w', encoding='utf-8') as file:
        file.write(f'\nThe list of {counted_countries} world countries\n\n')
    for state in WikiCountry(counted_countries, countries):
        with open('List of countries with WiKi references.txt', 'a', encoding='utf-8') as file:
            file.write(f'The state of {state[0]} has\
 the following link in Wikipedia - {state[1]}\n')

    print('\nBelow hashed codes for each line are provided:\n\n')

    for result in generator('List of countries with WiKi references.txt'):
        print(result.hexdigest())


      

if __name__ == '__main__':

  main()

