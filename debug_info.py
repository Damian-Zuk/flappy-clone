from text_manager import Text

class DebugInfo:
    monitor = dict()
    printed = dict()
    frames = 0

    @classmethod
    def update(cls):
        # Display every 2 frames
        if cls.frames % 2 == 0:
            print_offset = 0
            for label in cls.monitor:
                if cls.printed.get(label):
                    del cls.monitor[label]
                    del cls.printed[label]
                else:
                    cls.monitor[label].pos.y = print_offset
                    cls.printed[label] = True
                    print_offset += cls.monitor[label].height
        cls.frames = (cls.frames + 1) % 60

    @classmethod
    def print_info(cls, var, label):
        if label in cls.monitor:
            cls.monitor[label].change_text(str(label) + ': ' + str(var))
        else:
            cls.monitor[label] = Text(str(label) + ': ' + str(var), 0, 0, 14, (255, 0, 255), 1000, True, 'joystix')
        cls.printed[label] = False
