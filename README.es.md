<!--hide-->
# API Estática Familiar
<!--endhide-->

¡La familia "Jackson" necesita una API estática! Necesitamos construir las *estructuras de datos (data structures)* y crear un API endpoint para interactuar con él utilizando [Hoppscotch](https://hoppscotch.io/) (recomendado) o Postman.

## 🌱 Cómo comenzar este proyecto

Este proyecto viene con los archivos necesarios para comenzar a trabajar de inmediato.

Recomendamos abrir este mismo repositorio usando un entorno de desarrollo como [Codespaces](https://4geeks.com/es/lesson/tutorial-de-github-codespaces) (recomendado) o [Gitpod](https://4geeks.com/es/lesson/como-utilizar-gitpod). Alternativamente, puedes clonarlo en tu computadora local usando el comando `git clone`.

Este es el repositorio que necesitas abrir:

```txt
https://github.com/breatheco-de/exercise-family-static-api
```

## 💻 Instalación

1. Instala las dependencias del proyecto `$ pipenv install`.

2. Entra dentro del *virtual environment* `$ pipenv shell`

3. Inicia el servidor flask `$ pipenv run start`

## ✅ Autoevaluación

+ Evalúa tu código con el comando `$ pipenv run test`

## 📝 Instrucciones

1. Crea el código necesario para desarrollar los API endpoints descritos más adelante.

2. Los únicos dos archivos que tienes que editar son:

- `src/datastructure.py`: Contiene la estructura de datos `FamilyStructure` que se encarga de manejar la familia.
- `src/app.py`: Es el código de tu API, aquí debes agregar los endpoints (rutas) y la lógica de programación.

3. Hemos preparado un conjunto de pruebas automatizadas que te darán una idea de si tu código es correcto, ejecuta las pruebas escribiendo `$ pipenv run test` en la línea de comandos (terminal o consola).

## Estructuras de datos (Data structures)

Cada **miembro** de la familia Jackson debe ser un diccionario, equivalente a [Objetos literales en JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects) - y tienen estos valores:

```python
+ id: Int
+ first_name: String
+ last_name: String (Siempre Jackson)
+ age: Int > 0
+ lucky_numbers: List of integers
```

La estructura de datos **family** será una clase con la siguiente estructura:

```python
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        ## Debes implementar este método
        ## Agrega un nuevo miembro a la lista de _members
        pass

    def delete_member(self, id):
        ## Debes implementar este método
        ## Recorre la lista y elimina el miembro con el id proporcionado
        pass

    def get_member(self, id):
        ## Debes implementar este método
        ## Recorre la lista y obtén el miembro con el id proporcionado
        pass

    def get_all_members(self, id):
        return self._members
```

Nota: no olvides inicializar la clase: `jackson_family = FamilyStructure('Jackson')` *antes* de las rutas.

## Estos son los miembros iniciales de la familia.

```md
John Jackson
33 Years old
Lucky Numbers: 7, 13, 22

Jane Jackson
35 Years old
Lucky Numbers: 10, 14, 3

Jimmy Jackson
5 Years old
Lucky Numbers: 1
```

## Endpoints

Esta API debe tener 4 endpoints, todos devuelven JSON:

### 1) Obtén todos los miembros de la familia:

Devuelve todos los miembros de la familia.

```md
GET /members

status_code 200 si se realizó con éxito, 400 si hubo un error por parte del cliente, 500 si el servidor encuentra un error

RESPONSE BODY (content-type: application/json):

[]  <!--- Lista de miembros de la familia -->
```

### 2) Recupera solo un miembro

Devuelve el miembro de la familia para el cual `id == member_id`.

```md
GET /member/<int:member_id>

RESPONSE (content_type: application/json):

status_code 200 si se realizó con éxito, 400 si hubo un error por parte del cliente, 500 si el servidor encuentra un error

body:  <!--- el objeto json del miembro de la familia --> 
{
    "id": Int,
    "first_name": String,
    "age": Int,
    "lucky_numbers": List
}
```

### 3) Añadir (POST) un miembro

Agrega un nuevo miembro a la estructura de datos de la familia.

```md
POST /member

REQUEST BODY (content_type: application/json):
{
    id: Int,
    first_name: String,
    age: Int,
    lucky_numbers: []
}

RESPONSE (content_type: application/json):

status_code 200 si se realizó con éxito, 400 si hubo un error por parte del cliente, 500 si el servidor encuentra un error
```


### 4) ELIMINA un miembro

Elimina el miembro de la familia para el cual `id == member_id`.

```md
DELETE /member/<int:member_id>

RESPONSE (content_type: application/json):

status_code 200 si se realizó con éxito, 400 si hubo un error por parte del cliente, 500 si el servidor encuentra un error

body: {
    done: True
}
```

## Requisitos tecnológicos

- Todas las solicitudes y respuestas deben estar en content/type: application/json
- Los códigos de respuesta deben ser `200` para solicitudes exitosas, `400` para una solicitud incorrecta o `404` para no encontrados.
- Este ejercicio no incluye una base de datos, todo se debe hacer en durante el tiempo de ejecución del programa (memoria RAM).

Este y otros proyectos son usados para [aprender a programar](https://4geeksacademy.com/es/aprender-a-programar/aprender-a-programar-desde-cero) por parte de los alumnos de 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) realizado por [Alejandro Sánchez](https://twitter.com/alesanchezr) y muchos otros contribuyentes. Conoce más sobre nuestros [Cursos de Programación](https://4geeksacademy.com/es/curso-de-programacion-desde-cero?lang=es) para convertirte en [Full Stack Developer](https://4geeksacademy.com/es/coding-bootcamps/desarrollador-full-stack/?lang=es), o nuestro [Data Science Bootcamp](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning).
