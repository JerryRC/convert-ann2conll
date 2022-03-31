'''
用于讲conll格式的NER数据按句子为单位,分别抽取成对应的 源文本source 和 标签 label 的两个文件,字符间以空格分割
'''


def extract(filename: str):
    write_source = []
    write_labels = []
    with open(filename, 'r', encoding='utf-8') as f:
        source = []
        labels = []
        for line in f.readlines():
            data = line.strip().split()
            if data:
                source.append(data[0])
                labels.append(data[1])
            else:
                if len(source) > 0:
                    write_source.append(source)
                    write_labels.append(labels)
                source = []
                labels = []
        if len(source) > 0:
            write_labels.append(source)
            write_labels.append(labels)
    with open('tax_source.txt', 'w', encoding='utf-8') as f:
        for data in write_source:
            f.write(' '.join(data) + '\n')
    with open('tax_labels.txt', 'w', encoding='utf-8') as f:
        for data in write_labels:
            f.write(' '.join(data) + '\n')


if __name__ == '__main__':
    target = 'Tax.conll'
    extract(target)
