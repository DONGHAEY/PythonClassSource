from readData import *
data = readData('지역평균기온.txt')

def showdt(indata):
    dt = {}
    for line in data :
      line = line.replace('\n', '')
      items = line.split(',')
      dt[items[0]] = int(items[1])
    return dt;