import json

def change_value(id, value, dict, list='tests'):
    ver = 0
    for i in dict[list]:
        for k, v in i.items():
            if v == id and k == 'id':
                i['value'] = value
                ver = 1
                break
        if ver == 1:
            break
    if ver != 1:
        for i in dict[list]:
            for k in i.keys():
                if k == 'values':
                    change_value(id, value, i, k)
    return data2

with open("values.json", "r") as read_file1, open("tests.json", "r") as read_file2:
    data1 = json.load(read_file1)
    data2 = json.load(read_file2)

for val in data1['values']:
    id_value = val['id']
    same_value = val['value']
    change_value(id_value, same_value, data2)
with open("report.json", "w") as write_file:
    json.dump(data2, write_file, indent=2, sort_keys=True)
