
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members

        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": "Jackson",
                "age": 33,
                "lucky_numbers": [34,65,23,4,6]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": "Jackson",
                "age":35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": "Jackson",
                "age":5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        new_member={
            "id":self._generateId(),
            "first_name":member["first_name"],
            "last_name": self.last_name,
            "age":member["age"],
            "lucky_numbers":member["lucky_numbers"],            
        }
        self._members.append(new_member)
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        array=self._members
        for member in array:
            if member["id"] ==id:
                self._members.remove(member)
                return self._members
        #pass
    
    def update_member(self, id, member):
        for i, member in enumerate(self._members):
            if member["id"] == int(id):
                member["id"] = id
                self._members[i] = member
                return True
        return False

    def get_member(self, id):
        # fill this method and update the return
        array=self._members
        for member in array:
            if member["id"] ==id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members