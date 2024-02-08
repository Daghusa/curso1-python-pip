# los modulos creados pueden tener variables, definiciones
''''
def get_population():
  keys =['col', 'bol']
  values = [300, 400]
  return keys, values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country,data))
  return result
'''
# buena practica es nombrar de una forma diciente

def get_population(country):
  population_dict ={
    '2022' :int(country['2022 population']),
    '2020' :int(country['2020 population']),
    '2015' :int(country['2015 population']),
    '2010' :int(country['2010 population']),
    '2000' :int(country['2000 population']),
    '1990' :int(country['1990 population']),
    '1980' :int(country['1980 population']),
    '1970' :int(country['1970 population'])
  }
  labels= population_dict.key()
  values= population_dict.values()
  return labels,values

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country,data))
  return result