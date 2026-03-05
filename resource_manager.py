
class ResourceManager:
    game_objects = list()
    drawable_objects = list()
    resources = dict()

    @classmethod
    def get_res(cls, name):
        return cls.resources.get(name)

    @classmethod
    def add_res(cls, name, res):
        cls.resources[name] = res

    @classmethod
    def cleanup(cls):
        cls.game_objects.clear()
        cls.drawable_objects.clear()
        cls.resources.clear()


    