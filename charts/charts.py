import matplotlib.pyplot as plt # type: ignore

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200, 24, 120]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()