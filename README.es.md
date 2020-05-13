# ![alt text](https://assets.breatheco.de/apis/img/images.php?blob&random&cat=icon&tags=breathecode,32) Family Static API

¡La familia "Jackson" necesita una API estática! Necesitamos construir las *estructuras de datos (data structures)* y crear un API endpoint para interactuar con él utilizando ![Postman](https://postwoman.io/) o Postman.

## 💻 Instalación

Por favor clona este repositorio para comenzar a codificar tu ejercicio o ábrelo en gitpod.io (recomendado).

## 📝 Instrucciones

- Crea el código necesario para desarrollar los API endpoints descritos más adelante.
- Los únicos dos archivos que tienes que editar son:
	- `src/datastructure.py`: Contiene la estructura de datos `FamilyStructure` que se encarga de manejar la familia.
	- `src/app.py`: Es el código de tu API, aquí debes agregar los endpoints (rutas) y la logica de programación.
- Hemos preparado un conjunto de pruebas automatizadas que te darán una idea de si tu código es correcto, ejecute las pruebas escribiendo `$ pipenv run tests` en la línea de comandos (terminal o consola).

## Estructuras de datos (Data structures)

Cada **miembro** de la familia Doe debe ser un diccionario, equivalente a [Objetos literales en JS](https://www.dyn-web.com/tutorials/object-literal/) - y tienen estos valores:
```
    + id: Int
    + first_name: String
    + last_name: String (Always Doe)
    + age: Int > 0
    + gender: String
    + lucky_numbers: Array of int
```
La estructura de datos **family** será una clase con la siguiente estructura:

```python
class Family:

	def __init__(self, last_name):
		self.last_name = last_name
        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John"
            "last_name": this.last_name
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

	def add_member(self, member):
        ## you have to implement this method
        ## append the member to the list of _members
		pass

	def delete_member(self, id):
        ## you have to implement this method
        ## loop the list and delete the member with the given id
		pass

	def update_member(self, id, member):
        ## you have to implement this method
        ## loop the list and replace the memeber with the given id
		pass

	def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
		pass

	def get_all_members(self, id):
		return self._members
```

## Estos son los miembros iniciales de la familia.

```md
John Doe
33 Years old
Male
Lucky Numbers: 7, 13, 22

Jane Doe
35 Years old
Female
Lucky Numbers: 10, 14, 3

Jimmy Doe
5 Years old
Male
Lucky Numbers: 1
```

## Endpoints

Esta API debe tener dos endpoints, ambos devuelven JSON:

### 1) Obten todos los miembros de la familia:
Lo que devuelve la información de la familia de Doe.. Ejemplo:

```md
GET /members

RESPONSE (Application/JSON):

    código de estado: 200 si se agregó con éxito, 400 si no lo hace porque el cliente (solicitud) falla, 500 si el servidor encuentra un error
    content-type: Application/JSON
    body: un Objeto JSON que contiene:
        - miembros: Arreglo de miembros.
        - family_name: El apellido de la familia.
        - lucky_numbers: Una matriz con todos los números de la suerte de los miembros de la familia.
        - sum_of_lucky: Suma de todos los números de la suerte de los miembros de la familia.
```
Important: Hay dos campos que deben calcularse en tiempo de ejecución:
- lucky_numbers es la concatenación de todos los números de la suerte de los miembros de la familia
- sum_of_lucky es la suma de todos los números de la suerte de los miembros de la familia.


### 2) Recupera solo un miembro

```md
GET /member/<int:member_id>
Lo que retorna el miembro de la familia donde`id == member_id`. E, g:

RESPONSE (application/json):

    código de estado: 200 si se agregó con éxito, 400 si no lo hace porque el cliente (solicitud) falla, 500 si el servidor encuentra un error
    content_type: Application/JSON
    body: the member json object
```



### 3) Añadir (POST) un miembro

```md
POST /member
Lo que agrega un nuevo miembro a la estructura de datos de la familia

RESPONSE (application/json):

    código de estado: 200 si se agregó con éxito, 400 si no lo hace porque el cliente (solicitud) falla, 500 si el servidor encuentra un error
    content_type: Application/JSON
    body: the member json object
```



### 4) ELIMINA un miembro

```md
DELETE /member/<int:member_id>
Que elimina un miembro dado por el ID dado

RESPONSE (application/json):

    status_code: 200 if successfully deleted, 400 if it doesn't because the client-side (request) screw up, 500 if the server encouner an error
    content_type: Application/JSON
    body: the member json object
```

## Requisitos tecnológicos

- Todas las solicitudes y respuestas deben estar en content/type: application/json
- Los códigos de respuesta deben ser `200` para tener éxito,` 400` para una solicitud incorrecta o `404` para no encontrados.
- Este ejercicio no incluye una base de datos, todo se debe hacer en la memoria RAM.
