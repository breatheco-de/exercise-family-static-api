# ![alt text](https://assets.breatheco.de/apis/img/images.php?blob&random&cat=icon&tags=breathecode,32) Family Static API

The Jackson Family needs a static API! We need to build the *data structures* and create API endpoint to interact with it using Postman.

## 💻 Installation

1. Please clone the current project to start working your exercise or open it locally or in gitpod.io (recomended).

2. Install the project dependencies by running `$ pipenv install`.

3. Get inside the virtual environment by running `$ pipenv shell`

4. Start the server by running `$ pipenv run start`

5. Test your code by running `$ pipenv run test`

## ✅ Automatic grading

Test your code by running `$ pipenv run test`

## 📝 Instructions

- Create the code needed to implement the API endpoints described further below.  

- The only two files you have to edit are:  

	- `src/datastructure.py`: Contains the class with the rules on how to manage the fammily members.  
	
	- `src/app.py`: Contains the API, it uses the Family as datastructure. 
	
- We have prepared a set of automated tests that will give you an idea if your code is correct, run the tests by typing `$ pipenv run tests` on the command line.  

## Data structures

Every **member** of the Jackson family must be a dictionary - equivalent of [Objects Literals in JS](https://www.dyn-web.com/tutorials/object-literal/) - and have these values:

```js
    + id: Int
    + first_name: String
    + last_name: String (Always Doe)
    + age: Int > 0
    + lucky_numbers: Array of int
```
The **family** data-structure will be a class with the following structure:

```python
class Family:

	def __init__(self, last_name):
		self.last_name = last_name
        # example list of members
		self._members = [{
			"id": self._generateId(),
			"first_name": "John"
		}]

    	# read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return random.randint(0, 99999999) //import random 

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

	def get_all_members(self):
		return self._members
```

Note: don't forget to Initialize the class: `doe_family = Family('Doe')` *before* the routes.

## These are the initial Family Members

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

This API must have 4 endpoints. They all return JSON:

### 1) Get all family members:

```md
GET /members

RESPONSE (content-type: Application/JSON):
{
	status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error
    body: { 
    	members: [], //Array of members.
		family_name: "", //the family's last name.
		lucky_numbers: [], //An array with all family member's lucky numbers.
		sum_of_lucky: Int //Sum of all family member's lucky numbers.
}
```
Important: There are two fields that must be calculated on runtime:
- lucky_numbers is the concatenation of all the lucky numbers from the family members.
- sum_of_lucky is the sum of all the lucky numbers of the family members.


### 2) Retrieve one member
Which returns the member of the family where `id == member_id`.

```md
GET /member/<int:member_id>

RESPONSE (content_type: Application/JSON):
status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

BODY: //the member's json object

{
    "first_name": String,
    "age": Int,
    "lucky_numbers": List
}

```



### 3) Add (POST) new member

```md
POST /member

REQUEST Body (content_type: Application/JSON):
{
    name: String,
    age: Int,
    lucky_numbers: []
}

RESPONSE (content_type: Application/JSON):
status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error
body: empty
```



### 4) DELETE one member

```md
DELETE /member/<int:member_id>

RESPONSE (content_type: Application/JSON):
{
    status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error
    done: True
}
```

## Requirements

- All requests and reponses should be in content/type: application/json
- Response codes must be `200` for success, `400` for bad request or `404` for not found.
- This exercise does not include a database, everything must be done in Runtime (RAM).
