import os

entity_dict = {
    '纳税人': 'TaxPayer',
    '征税对象': 'Taxobj',
    '税种': 'Tax',
    '动作': 'Action'
}


class Annotation():
    '''作为ann文件中代表实体T的类,即文件每一行为一个Annotation类实例'''

    def __init__(self, entity_info: list):
        self.begin = int(entity_info[2])
        self.end = int(entity_info[3])
        self.word = entity_info[1]
        self.label = entity_dict[self.word]


def read_ann(filename: str) -> list:
    ann_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            info = line.split()
            if 'T' in info[0] and info[1] in entity_dict.keys():
                ann_list.append(Annotation(info))
    return sorted(ann_list, key=lambda x: x.begin)


def write_conll(filename: str):
    if not os.path.isfile(filename + '.ann'):
        return
    print("开始处理 " + filename)
    ann_list = read_ann(filename + '.ann')
    txt = ''  # 原始文本
    with open(filename + '.txt', 'r', newline='', encoding='utf-8') as f:
        # 这里在原文含多行时会把换行符纳入,后面再处理
        txt = ''.join(f.readlines())
    with open('Tax.conll', 'a', encoding='utf-8') as f:
        # 此处是以追加写的方式进行写入,如需新建数据集请删除原文件
        pointer = 0
        for ann in ann_list:
            for i in range(pointer, ann.begin):
                # if txt[i].isspace(): continue
                f.write(txt[i] + '\tO\n')
            f.write(txt[ann.begin] + '\tB-' + ann.label + '\n')
            for i in range(ann.begin + 1, ann.end):
                # if txt[i].isspace: continue
                f.write(txt[i] + '\tI-' + ann.label + '\n')
            pointer = ann.end
        for i in range(pointer, len(txt)):
            # if txt[i].isspace: continue
            f.write(txt[i] + '\tO\n')
        # 最后以换行分割每个句子
        f.write('\n')


def convert():
    for i in range(10):
        write_conll('000' + str(i))
    for i in range(10, 100):
        write_conll('00' + str(i))
    write_conll("00" + str(471))
    write_conll("0" + str(100))

    # # 处理当前路径下的ann文件
    # for f in os.listdir():
    #     if os.path.isfile(f) and f[-4:]=='.ann':
    #         write_conll(f[:-4])


if __name__ == '__main__':
    convert()
