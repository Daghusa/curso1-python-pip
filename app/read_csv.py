import csv

def read_csv(path):
  with open(path, 'r' ) as csvfile:
    reader =csv.reader(csvfile, delimiter=',')
    header = next(reader) # obtenemos el nombre de la primera fila, es decir el nombre de la columna
    data =[]
    for row in reader:
      iterable= zip (header, row)
      #print(list(iterable)) # convertimos en listas (tuplas)
      #print ('***' * 5)
      #print(row)
      country_dict= {key: value for key, value in iterable}
      #print(country_dict) # convertimos en diccionario
      data.append(country_dict)
      return data
      

if __name__ == '__main__':
  data = read_csv("data.csv")
  print(data[0])
           