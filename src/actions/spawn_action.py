from random import randint
from factories import EntityFactory


def SpawnAction(Action):
    """спавнер объектов на карте"""

    def execute(self, game_map, entity_type):

        nx, xy = randint(0, self.width - 1), randint(0, self.height - 1)
        if game_map.is_free(nx, ny):
            new_obj = EntityFactory.reate_entity(entity_type, nx, ny)
            game_map.add

