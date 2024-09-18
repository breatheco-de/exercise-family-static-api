from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return member

    def delete_member(self, member_id):
        for index, member in enumerate(self._members):
            if member['id'] == member_id:
                return self._members.pop(index)
        return None

    def get_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                return member
        return None

    def get_all_members(self):
        return self._members
