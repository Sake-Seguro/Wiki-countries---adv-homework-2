
import hashlib


def generator(file_path):

    with open(file_path, encoding='UTF-8') as criteria:

        for line in criteria:
            strip_line = line.strip()
            byte_line = strip_line.encode('utf-8')
            yield hashlib.md5(byte_line)


if __name__ == '__main__':

    for result in generator('List of countries with WiKi references.txt'):
        print(result.hexdigest())

