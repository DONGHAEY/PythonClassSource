import matplotlib.pyplot as plt

plt.rc('font', family='NanumGothic')


import csv
f = open('서울특별시_백신접종률.csv')


data = csv.reader(f)

name = input('찾고싶은 지역을 입력하세요 ')

m = input('1차예방접종률은 a를 입력 2차예방접종률은 b를 입력 ')

result = []
lastResult = []

for i in data :
  if name in i[0] :
    result = i
    break

k = [1, 3, 5, 7, 9] #1차 접종률
k2 = [2, 4, 6, 8, 10] #2차 접종률

if m == 'a' :
  for p in k :
    lastResult.append(int(result[p]))
elif m=='b' :
  for p in k2 :
    lastResult.append(int(result[p]))

plt.title(name)

plt.style.use('ggplot')

plt.rc('font', family = 'NanumGothic')
plt.title('서울 ' +name +' 지역의' + '백신 접종률')
x=['2~6월', '7월', '8월', '9월', '10월']
plt.bar(x,lastResult)
plt.show()
