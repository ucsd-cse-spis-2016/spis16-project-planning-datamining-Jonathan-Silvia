import matplotlib.pyplot as plt
import numpy as np

def PieChart(hillary, trump, gary, jill, harambe):

    labels = 'Hillary', 'Trump', 'Gary', 'Jill', 'Harambe'
    sizes = [len(hillary), len(trump), len(gary), len(jill), len(harambe)]
    colors = ['burlywood', 'cornsilk', 'chartreuse', 'lightcoral', 'firebrick']
    explode = (0, 0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')

    #fig = plt.figure()
    plt.show()
    #ax = fig.gca()
    import numpy as np

def barGraph(h, t, g, j, hb):
    
    y = [avgPolarity(h), avgPolarity(t), avgPolarity(g), avgPolarity(j), avgPolarity(hb)] 
    N = len(y)
    x = range(N)
    width = 1/1.5
    plt.bar(x, y, width, colors=colors)

    fig = plt.gcf()
    plt.show()


##    ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
##           autopct='%1.1f%%', shadow=True, startangle=90,
##           radius=0.25, center=(0, 0), frame=True)
##    ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
##           autopct='%1.1f%%', shadow=True, startangle=90,
##           radius=0.25, center=(1, 1), frame=True)
##    ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
##           autopct='%1.1f%%', shadow=True, startangle=90,
##           radius=0.25, center=(0, 1), frame=True)
##    ax.pie(np.random.random(4), explode=explode, labels=labels, colors=colors,
##           autopct='%1.1f%%', shadow=True, startangle=90,
##           radius=0.25, center=(1, 0), frame=True)
##
##    ax.set_xticks([0, 1])
##    ax.set_yticks([0, 1])
##    ax.set_xticklabels(["Sunny", "Cloudy"])
##    ax.set_yticklabels(["Dry", "Rainy"])
##    ax.set_xlim((-0.5, 1.5))
##    ax.set_ylim((-0.5, 1.5))

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    #ax.set_aspect('equal')

    #plt.show()


