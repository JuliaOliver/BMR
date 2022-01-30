import uuid


class MainRepo:
    def __init__(self):
        self.entities = {}

    def add_entity(self, entity):
        entity.id_num = str(uuid.uuid1())
        self.entities[entity.id_num] = entity
        return entity

    def update_entity(self, entity):
        if entity.id_num not in self.entities:
            return None
        self.entities[entity.id_num] = entity
        return entity

    def delete_entity(self, entity):
        if entity.id_num in self.entities:
            deleted = self.entities[entity.id_num]
            self.entities.pop(entity.id_num)
            return deleted
        else:
            return None

    def find_all(self):
        return self.entities.values()

    def find_by_id(self, id_num):
        if id_num not in self.entities:
            return None
        return self.entities[id_num]

    def count(self):
        return len(self.entities)

