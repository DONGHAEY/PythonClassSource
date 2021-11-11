# 리스트 결합 : zip() dict(zip(area, temp))
with open('/content/11월전국기온.txt','r', encoding='utf-8') as fp:
  data = fp.readlines()

#making empty arrays named area and temp
area = []
temp = []


for line in data:
  #deleting enter
  line = line.replace('\n','')
  #separate index to find ','
  item = line.split(',')
  #append item[1] at temp, append item[0] at area
  temp.append(item[1])
  area.append(item[0])

#making dictionary
dt = dict(zip(area, temp))
print(dt)

#find temp that area
q = input('지역을 입력하세요 : ')
print(dt[q])

#write area[0] at 지역.txt
fp = open('지역.txt', 'w', encoding = 'utf-8')
fp.write(area[0])
fp.close()

#write temp at 기온.txt
with open('기온.txt', 'w', encoding = 'utf-8') as fp:
  for item in temp :
    fp.write(str(item) + '\n')
#write area at 지역.tx
with open('지역.txt', 'w', encoding = 'utf-8') as fp:
  for item in area :
    fp.write(str(item) + '\n')