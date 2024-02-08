import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('data.csv') # se elimina /app porque ya estamo en la ruta
  data = list(filter(lambda item : item["Continent"] == "South America", data))


  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  country = input('Country => ')
  print(country)
  

  result =utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'],labels, values)
  
if __name__ == '__main__': # sirve para crear dualidad, es decir que se pueda ejecutar como script o que se pueda importar 
  run()