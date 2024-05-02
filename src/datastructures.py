"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # Método privado para generar ID de manera interna
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id    

    # Método para agregar un miembro a la familia
    def add_member(self, member):
        member["id"] = self._generateId()
        self._members.append(member)
        return self._members    

    # Método para eliminar un miembro de la familia por ID
    def delete_member(self, id):
        for i in range(len(self._members)):
            if self._members[i]["id"] == id:
                del self._members[i]
                break
        return self._members

    # Método para obtener un miembro de la familia por ID
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member

    # Método para obtener todos los miembros de la familia
    def get_all_members(self):
        return self._members