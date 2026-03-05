from resource_manager import ResourceManager

class Scene:
    def toggle_scene(self, mode):
        if mode != self.mode:
            for obj in self.scene_objects:
                obj.active = mode
            self.mode = mode

    def add_scene_obj(self, obj):
        self.scene_objects.append(obj)
        self.scene_objects[-1].active = self.mode

    def __init__(self, scene_name, *args):
        self.mode = False
        self.scene_name = scene_name
        self.scene_objects = list()
        for arg in args:
            self.add_scene_obj(ResourceManager.get_res(arg))

        SceneManager.scenes[scene_name] = self

class SceneManager:
    scenes = dict()

    @classmethod
    def get_scene(cls, name):
        return cls.scenes.get(name)

    

