def readData(fname):
    
    fname = "/content/" + fname
    fp = open(fname, 'r', encoding='utf-8')
    data = fp.readlines()
    fp.close()

    return data