import os


def do_verify(filenames: list):
    for file in filenames:
        if not os.path.isfile(file):
            print(file + ' NOT A FILE')
            continue
        with open(file, 'r', encoding='utf-8') as f:
            previous = 'O'
            for line in f.readlines():
                ann = line.split()
                if len(ann) == 0:  # line == '\n'
                    previous = 'O'
                elif ann[-1][0] == 'I' and previous == 'O':
                    print(file + ' NON-COMPLIANCE')
                    break
                else:
                    previous = ann[-1][0]
        print('CHECKING {} DONE'.format(file))


if __name__ == '__main__':
    target = [
        '/tax_conll.train',
        '/tax_conll.dev'
    ]
    do_verify(target)
