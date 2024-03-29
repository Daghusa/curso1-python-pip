import utils
import read_csv
import charts
import pandas as pd


def run():

  '''  ## se cometo para usar la libreria pandas
  data = read_csv.read_csv('data.csv') # se elimina /app porque ya estamo en la ruta
  data = list(filter(lambda item : item["Continent"] == "South America", data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  '''

  ## se crean las mismas graficas pero utilizando la libreria pandas
  # df(dataframe)

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)


  data = read_csv.read_csv('data.csv') # se agrega para no corromper el resto de codigo
  country = input('Type Country => ')
  print(country)
  

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  
if __name__ == '__main__': # sirve para crear dualidad, es decir que se pueda ejecutar como script o que se pueda importar 
  run()