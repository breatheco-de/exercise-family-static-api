# ![alt text](https://assets.breatheco.de/apis/img/images.php?blob&random&cat=icon&tags=breathecode,32) Family Static API

¡La familia "Jackson" necesita una API estática! Necesitamos construir las *estructuras de datos (data structures)* y crear un API endpoint para interactuar con él utilizando [Hoppscotch](https://hoppscotch.io/) (recomendado) o Postman.

## 💻 Instalación

1. Por favor clona este repositorio para comenzar a codificar tu ejercicio o ábrelo en [gitpod.io haciendo click aqui](https://www.gitpod.io#https://github.com/breatheco-de/exercise-family-static-api) (recomendado).

2. Instala las dependencias del proyecto `$ pipenv install`.

3. Entra dentro del **virtual environment** `$ pipenv shell`

4. Inicio al servidor flask `$ pipenv run start`

5. Prueba que el proyecto está correctamente terminado `$ pipenv run test`

## ✅ Autoevaluación

Evalúa tu código con el comando `$ pipenv run test`

## 📝 Instrucciones

1) Crea el código necesario para desarrollar los API endpoints descritos más adelante.

2) Los únicos dos archivos que tienes que editar son:

- `src/datastructure.py`: Contiene la estructura de datos `FamilyStructure` que se encarga de manejar la familia.
- `src/app.py`: Es el código de tu API, aquí debes agregar los endpoints (rutas) y la logica de programación.

3) Hemos preparado un conjunto de pruebas automatizadas que te darán una idea de si tu código es correcto, ejecuta las pruebas escribiendo `$ pipenv run test` en la línea de comandos (terminal o consola).

## Estructuras de datos (Data structures)

Cada **miembro** de la familia Jackson debe ser un diccionario, equivalente a [Objetos literales en JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects) - y tienen estos valores:

```python
    + id: Int
    + first_name: String
    + last_name: String (Siempre Jackson)
    + age: Int > 0
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
            "last_name": last_name
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
        ## loop the list and replace the member with the given id
        pass

    def get_member(self, id):
        ## you have to implement this method
        ## loop all the members and return the one with the given id
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

Esta API debe tener dos endpoints, ambos devuelven JSON:

### 1) Obten todos los miembros de la familia:

Devuelve todos los miembros de la familia.

```md
GET /members

status_code 200 si se agregó con éxito, 400 si no lo hace porque el cliente (solicitud) falla, 500 si el servidor encuentra un error

RESPONSE BODY (content-type: application/json):

[], // Lista de miembros de la familia.

```

### 2) Recupera solo un miembro

Devuelve el miembro de la familia para el cual `id == member_id`.

```md
GET /member/<int:member_id>

RESPONSE (content_type: application/json):

status_code: 200 si se agregó con éxito, 400 si no lo hace porque el cliente (solicitud) falla, 500 si el servidor encuentra un error

body: // el objeto json del miembro de la familia

{
    "id": Int,
    "first_name": String,
    "age": Int,
    "lucky_numbers": List
}

```

### 3) Añadir (POST) un miembro

Lo que agrega un nuevo miembro a la estructura de datos de la familia

```md
POST /member

REQUEST BODY (content_type: application/json):

{
    first_name: String,
    age: Int,
    lucky_numbers: [],
    id: Int *opcional
}

RESPONSE (content_type: application/json):

status_code: 200 si se agregó con éxito, 400 si no lo hace porque el cliente (solicitud) falla, 500 si el servidor encuentra un error

body: vacío
```

Ten en cuenta que el diccionario que envía la solicitud POST puede contener una propiedad y un valor para el `id` del miembro a crear.
- Si no lo incluye, tu API debe generar un `id` aleatorio al agregarlo a la familia.
- Si lo incluye, entonces este es el valor que deberás usar como `id` al agregarlo.

### 4) ELIMINA un miembro

Elimina el miembro de la familia para el cual `id == member_id`.

```md
DELETE /member/<int:member_id>

RESPONSE (content_type: application/json):

status_code: 200 si fue eliminado con éxito, 400 si no lo fue porque el cliente (solicitud) falla, 500 si el servidor encuentra un error

body: {
    done: True
}

```

## Requisitos tecnológicos

- Todas las solicitudes y respuestas deben estar en content/type: application/json
- Los códigos de respuesta deben ser `200` para tener éxito,` 400` para una solicitud incorrecta o `404` para no encontrados.
- Este ejercicio no incluye una base de datos, todo se debe hacer en la memoria RAM.
