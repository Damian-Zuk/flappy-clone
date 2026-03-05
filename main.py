import graphic_engine
import game
import event_handler

app = game.Game()
while graphic_engine.is_running:
    graphic_engine.frame_time = graphic_engine.clock.get_time() / 1000
    event_handler.EventHandler.update()
    app.update()
    app.render()
    graphic_engine.update_display()
    graphic_engine.clock.tick(graphic_engine.fps_cap)
