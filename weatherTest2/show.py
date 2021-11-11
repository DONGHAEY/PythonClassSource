

def show(dt):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 5))
    
    x = list(dt.keys())
    y = list(dt.values())

    plt.plot(x,y,'go--', color='skyblue')
    plt.title('지역평균기온')
    plt.xticks(rotation=0)
    plt.draw() 
    
    fig = plt.gcf()
    fig.savefig('/content/myfile.png', dpi=fig.dpi)