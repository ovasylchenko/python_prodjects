import sys
import collections

if len(sys.argv) == 1:
    print('Code example \n')
    print('... \n')

class Molecule:
    def __init__(self, structure1, filds1):
        self.structure1 = []
        self.filds1 = collections.OrderedDict()

filename2 = sys.argv[1]  # small sdf
idnumber_small = sys.argv[2]  # idnumber small sdf
filename1 = sys.argv[3]  # big sdf
idnumber_big = sys.argv[4]  # idnumber big sdf
range1 = sys.argv[5]  # 0.1-0.05
range2 = sys.argv[6]  # 1
write_name = str(filename2)[:-4] + '_out.txt'
writefile = open(write_name, "w")
sdf_all_big = collections.OrderedDict()
sdf_all_small = collections.OrderedDict()
empty_list = []
final_list = []
input_list = []


def load_sdf_big():
    print('\n' + '=' * 45)
    linex = ''
    openfile1 = open(filename1, "r")
    a = []
    b = collections.OrderedDict()
    counter1 = 0
    counter2 = 0
    my_id = 0
    filds = []
    fields_value = []
    field_value = []
    for line in openfile1:
        if counter1 == 0:
            if line[:-1] == 'M  END':
                counter1 = 1
                counter2 = 0
                continue
        else:
            if counter2 == 1 and line[0] == '>':
                fields_value.append(field_value)
                field_value = []
                counter2 = 0
            if line[:-1] == '$$$$':
                my_id += 1
                fields_value.append(field_value)
                z11 = Molecule(a, b)
                xraniliwe4 = collections.OrderedDict()
                for i in range(len(filds)):
                    xraniliwe3 = {filds[i]: fields_value[i]}
                    xraniliwe4.update(xraniliwe3)
                z11.filds1.update(xraniliwe4)
                xraniliwe2 = {str(my_id): z11}
                sdf_all_big.update(xraniliwe2)
                filds = []
                field_value = []
                fields_value = []
                counter1 = 0
                continue
            if line[:4] == '>  <':
                counter2 = 1
                line = line[4:-1]
                for z in line:
                    if z != '>':
                        linex = linex + str(z)
                filds.append(linex)
                linex = ''
                continue
            elif line[:3] == '> <':
                counter2 = 1
                line = line[3:-1]
                for z in line:
                    if z != '>':
                        linex = linex + str(z)
                filds.append(linex)
                linex = ''
                continue
            else:
                if line[:-1] == '':
                    pass
                else:
                    field_value.append(line[:-1])
    openfile1.close()
    print('big sdf loaded\n')
    print('number of big base molecules = ' + str(len(sdf_all_big)) + '\n')


def load_sdf_small():
    print('\n' + '=' * 45)
    linex = ''
    openfile2 = open(filename2, "r")
    a = []
    b = collections.OrderedDict()
    counter1 = 0
    counter2 = 0
    my_id = 0
    filds = []
    fields_value = []
    field_value = []
    for line in openfile2:
        if counter1 == 0:
            if line[:-1] == 'M  END':
                counter1 = 1
                counter2 = 0
                continue
        else:
            if counter2 == 1 and line[0] == '>':
                fields_value.append(field_value)
                field_value = []
                counter2 = 0
            if line[:-1] == '$$$$':
                my_id += 1
                fields_value.append(field_value)
                z12 = Molecule(a, b)
                xraniliwe4 = collections.OrderedDict()
                for i in range(len(filds)):
                    xraniliwe3 = {filds[i]: fields_value[i]}
                    xraniliwe4.update(xraniliwe3)
                z12.filds1.update(xraniliwe4)
                xraniliwe2 = {str(my_id): z12}
                sdf_all_small.update(xraniliwe2)
                filds = []
                field_value = []
                fields_value = []
                counter1 = 0
                continue
            if line[:4] == '>  <':
                counter2 = 1
                line = line[4:-1]
                for z in line:
                    if z != '>':
                        linex = linex + str(z)
                filds.append(linex)
                linex = ''
                continue
            elif line[:3] == '> <':
                counter2 = 1
                line = line[3:-1]
                for z in line:
                    if z != '>':
                        linex = linex + str(z)
                filds.append(linex)
                linex = ''
                continue
            else:
                if line[:-1] == '':
                    pass
                else:
                    field_value.append(line[:-1])
    openfile2.close()
    print('small sdf loaded\n')
    print('number of qvery molecules = ' + str(len(sdf_all_small)) + '\n')


def input_list_fill():
    openfile3 = open('1.txt', "r")
    for sdf3 in sdf_all_small:
        input_list.append(sdf_all_small.get(sdf3).filds1.get(idnumber_small)[0])
    print('input list filed\n')
    for line in openfile3:
        if line[:-1] not in input_list:
            input_list.append(line[:-1])
    openfile3.close()
    print(str(len(input_list)))


def find_by_pt():
    counter1 = 0
    status = 0
    er = 0
    total_found = 0
    for sdf in sdf_all_small:
        counter1 += 1
        if counter1 == 300:
            er += 300
            print('search total ' + str(er) + ' molecules\n')
            counter1 = 0
        a = float(sdf_all_small.get(sdf).filds1.get('SlogP')[0])
        SlogP_a = a + a * float(range1)
        SlogP_d = a - a * float(range1)
        b = float(sdf_all_small.get(sdf).filds1.get('TPSA')[0])
        TPSA_a = b + b * float(range1)
        TPSA_d = b - b * float(range1)
        c = float(sdf_all_small.get(sdf).filds1.get('AMW')[0])
        AMW_a = c + c * float(range1)
        AMW_d = c - c * float(range1)
        d = float(sdf_all_small.get(sdf).filds1.get('NumHeavyAtoms')[0])
        NumHeavyAtoms_a = d + d * float(range1)
        NumHeavyAtoms_d = d - d * float(range1)
        e = float(sdf_all_small.get(sdf).filds1.get('NumHBD')[0])
        NumHBD_a = e + float(range2)
        NumHBD_d = e - float(range2)
        f = float(sdf_all_small.get(sdf).filds1.get('NumHBA')[0])
        NumHBA_a = f + float(range2)
        NumHBA_d = f - float(range2)
        g = float(sdf_all_small.get(sdf).filds1.get('NumRings')[0])
        NumRings_a = g + float(range2)
        NumRings_d = g - float(range2)
        h = float(sdf_all_small.get(sdf).filds1.get('NumRotatableBonds')[0])
        NumRotatableBonds_a = h + float(range2)
        NumRotatableBonds_d = h - float(range2)
        # count_in = 0
        for sdf2 in sdf_all_big:
            if sdf_all_big.get(sdf2).filds1.get(idnumber_big)[0] in input_list:
                continue
            if sdf_all_small.get(sdf).filds1.get('SlogP') != empty_list:
                if SlogP_d <= float(sdf_all_big.get(sdf2).filds1.get('SlogP')[0]) <= SlogP_a:
                    pass
                else:
                    continue
            else:
                continue
            if sdf_all_small.get(sdf).filds1.get('TPSA') != empty_list:
                if TPSA_d <= float(sdf_all_big.get(sdf2).filds1.get('TPSA')[0]) <= TPSA_a:
                    pass
                else:
                    continue
            else:
                continue
            if sdf_all_small.get(sdf).filds1.get('AMW') != empty_list:
                if AMW_d <= float(sdf_all_big.get(sdf2).filds1.get('AMW')[0]) <= AMW_a:
                    pass
                else:
                    continue
            else:
                continue
            if sdf_all_small.get(sdf).filds1.get('NumHeavyAtoms') != empty_list:
                if NumHeavyAtoms_d <= float(sdf_all_big.get(sdf2).filds1.get('NumHeavyAtoms')[0]) <= NumHeavyAtoms_a:
                    pass
                else:
                    continue
            else:
                continue
            if sdf_all_small.get(sdf).filds1.get('NumHBD') != empty_list:
                if NumHBD_d <= float(sdf_all_big.get(sdf2).filds1.get('NumHBD')[0]) <= NumHBD_a:
                    pass
                else:
                    continue
            else:
                continue
            if sdf_all_small.get(sdf).filds1.get('NumHBA') != empty_list:
                if NumHBA_d <= float(sdf_all_big.get(sdf2).filds1.get('NumHBA')[0]) <= NumHBA_a:
                    pass
                else:
                    continue
            else:
                continue
            if sdf_all_small.get(sdf).filds1.get('NumRings') != empty_list:
                if NumRings_d <= float(sdf_all_big.get(sdf2).filds1.get('NumRings')[0]) <= NumRings_a:
                    pass
                else:
                    continue
            else:
                continue
            if sdf_all_small.get(sdf).filds1.get('NumRotatableBonds') != empty_list:
                if NumRotatableBonds_d <= float(sdf_all_big.get(sdf2).filds1.get('NumRotatableBonds')[0]) <= NumRotatableBonds_a:
                    pass
                else:
                    continue
            else:
                continue
            final_list.append(sdf_all_big.get(sdf2).filds1.get(idnumber_big)[0])
            status = 1
            input_list.append(sdf_all_big.get(sdf2).filds1.get(idnumber_big)[0])
            writefile.write(str(sdf_all_small.get(sdf).filds1.get(idnumber_small)[0]) + '\t')
            writefile.write(str(sdf_all_big.get(sdf2).filds1.get(idnumber_big)[0]) + '\n')
            print(str(sdf_all_big.get(sdf2).filds1.get(idnumber_big)[0]) + '\n')
            # count_in += 1
            # if count_in == 3:
            break
        if status == 0:
            writefile.write(str(sdf_all_small.get(sdf).filds1.get(idnumber_small)[0]) + '\t')
            writefile.write('no found\n')
            print(str('no found\n'))
        else:
            status = 0
            total_found += 1
        if total_found > 100:
            break
    print(str(len(final_list)))
    writefile.close()


if __name__ == "__main__":
    load_sdf_big()
    load_sdf_small()
    input_list_fill()
    find_by_pt()
