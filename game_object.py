import graphic_engine

from resource_manager import ResourceManager

class GameObject:
    def update(self):
        pass

    def delete(self):
        if self.exist_in_game_objects_list:
            ResourceManager.game_objects.remove(self)
        del self
    
    def __init__(self, active = True, add_to_game_objects_list = True):
        self.active = active
        if add_to_game_objects_list:
            ResourceManager.game_objects.append(self)
        self.exist_in_game_objects_list = add_to_game_objects_list


        
            