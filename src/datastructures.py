"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{'id': self._generate_id(),
                          'first_name': 'John',
                          'last_name': self.last_name,
                          'age': 33,
                          'lucky_numbers': [7, 13, 22]},
                         {'id': self._generate_id(),
                          'first_name': 'Jane',
                          'last_name': self.last_name,
                          'age': 35,
                          'lucky_numbers': [10, 14, 3]},
                         {'id': self._generate_id(),
                          'first_name': 'Jimmy',
                          'last_name': self.last_name,
                          'age': 5,
                          'lucky_numbers': [1]}]

    def _generate_id(self):
        # Read-only: Use this method to generate random members ID's when adding members into the list
        return randint(0, 99999999)

    def add_member(self, member):
        # Fill this method and update the return
        member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        print(member)
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        # Fill this method and update the return
        # buscar el elemento cuyo id sea igual al row['id']
        #    si lo enentra lo elimna
        # del self._members
        return id

    def get_member(self, id):
        # Opción 1 - for in
        
        for row in self._members:
            if row['id'] == id:
                # del row
                return row
        
        # Opción 2 - List comprehension
        result = [row for row in self._members if row['id'] == id]
        return result[0] if result else None



    def get_all_members(self):
        # This method is done, it returns a list with all the family members
        return self._members
        