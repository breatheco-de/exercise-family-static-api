class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generate_id()
        self.members.append(member)
        return member

    def _generate_id(self):
        existing_ids = [member["id"] for member in self.members]
        new_id = max(existing_ids, default=0) + 1
        return new_id

    def get_all_members(self):
        return self.members

    def get_member(self, member_id):
        return next((m for m in self.members if m["id"] == member_id), None)

    def delete_member(self, member_id):
        for member in self.members:
            if member["id"] == member_id:
                self.members.remove(member)
                return True
        return False