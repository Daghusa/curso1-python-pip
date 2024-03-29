import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))  ###para conocer el tipo de dato
    categories = r.json() ## conviete el archivo en formato JSON lo reconoce python como lista

    for category in categories:
        print(category['name'])   ## se hace una iteracion / buscamos el titulo que tiene como atributo "name"
