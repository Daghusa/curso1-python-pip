import matplotlib.pyplot as plt

def genrate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots() # se obtine la figura y las coordenadas
    ax.pie(values, labels=labels) #
    plt.savefig('pie.png')
    plt.close()

genrate_pie_chart() # se llama la funcion par auqe genere la imagen en ambieste de ubuntu