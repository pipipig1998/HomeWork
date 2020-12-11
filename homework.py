#coding=utf-8
import csv
import matplotlib.pyplot as plt
with open(r'./test1.csv',encoding='utf-8') as f:
    data = list(csv.reader(f))[1:]
ranks = {}
for each in data:
    date = each[3]
    if date in ranks:
        ranks[date].append({each[0]:int(each[2])})
    else:
        ranks[date] = [{each[0]:int(each[2])}]
data={}
plt.rcParams['font.sans-serif']='SimHei'
plt.ion()
plt.figure(figsize=(30,30))

for date in ranks.keys():
    for each in ranks[date]:
        for country,num in each.items():
            if country not in data.keys():
                data[country]=num
            else:
                data[country]=data[country]+num

            plt.clf()
            plt.xlabel('国家')
            plt.ylabel('感染人数')
            plt.bar(data.keys(),data.values(),color='y',alpha=0.5)
            plt.show()
            plt.pause(0.2)
plt.ioff()







