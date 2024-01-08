
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

        # example list of members
        self._members = []


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

    def get_member(self, member_id):
        # fill this method and update the return

        selected_member = next((member for member in self._members if member['id'] == member_id), None)

        if selected_member:
            return selected_member
        else:
            raise ValueError(f"The id {member_id} couldn't be found")
    
    def add_member(self, member_data):
        # fill this method and update the return
        new_member = {
            "id": self._generateId(),
            "name": member_data['name'],
            "age": member_data['age'],
            "lucky_numbers": member_data['lucky_numbers']
        }

        self._members.append(new_member)
        return new_member


    def delete_member(self, member_id):
        # fill this method and update the return

        deleted_member = next((member for member in self._members if member['id'] == member_id), None)

        if deleted_member:
            self._members.remove(deleted_member)
            return deleted_member
        else:
            raise ValueError(f"The id {member_id} couldn't be found")
        

    def update_member(self, member_id, updated_member_data):
    # fill this method and update the return

        updated_member = next((member for member in self._members if member['id'] == member_id), None)

        if updated_member:
            updated_member.update(updated_member_data)
            return updated_member
        else:
            raise ValueError(f"The id {member_id} couldn't be found")
