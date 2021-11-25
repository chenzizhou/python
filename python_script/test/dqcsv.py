import csv
lines=csv.reader(open(r'E:\python_script\info.csv','r',encoding='utf-8'))
for line in lines:
    print(line[0])
