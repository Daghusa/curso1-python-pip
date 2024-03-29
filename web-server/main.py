import store
from fastapi import FastAPI # para integrar el servidor web
from fastapi.responses import HTMLResponse  # para mostrar contenido en hatml



# se crea una instancia
app = FastAPI()

@app.get('/') #se conoce como un decorador, se utiliza para dar la ruta desde donde van a acceder en el navegador
def get_list():
    return[1,2,3]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
    <h1> Hola Primera Pagina en Python <h1>
    <p> ejemplo de parrafo<p>

    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()