import csv


def gen_new_dict(file_name):
    new_dict = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            if not 'см.' in line:
                line = line[:-1].split(' ')
                res = ''
                for l in line[1:]:
                    res += l
                    res += ' '
                res = res[:-1]
                line = [res, line[0]]
                print(line)
                new_dict.append(line)
    return new_dict


def to_csv(ls, file_name):
    with open(file_name, 'w') as fout:
        c = csv.writer(fout)
        c.writerows(ls)


to_csv(gen_new_dict('IT.txt'), 'IT.csv')
