from random import randint
from ..factories import EntityFactory


class SpawnerService():
    """
        Спавнер объектов на карте
        Принимает тип объекта для спавна, ищет свободное метсо на карте
        и размещает его там

    """

    @staticmethod
    def spawn(game_map, entity_type):
        while True:
            nx, ny = randint(0, game_map.get_width() - 1), randint(0, game_map.get_height() - 1)
            if game_map.is_free(ny, nx):
                new_obj = EntityFactory.create_entity(entity_type, ny, nx)
                game_map.add_object(new_obj)
                break


