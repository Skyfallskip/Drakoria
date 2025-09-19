import arcade as arc
from Game import screen_width, screen_height

class User_Interface(arc.View):
    def __init__(self):
        super().__init__()
        self.ui_elements = []
        self.ui_visible = True

    def add_ui_element(self, element):
        self.ui_elements.append(element)

    def remove_ui_element(self, element):
        if element in self.ui_elements:
            self.ui_elements.remove(element)

    def toggle_ui(self):
        self.ui_visible = not self.ui_visible

    def on_draw(self):
        if self.ui_visible:
            arc.start_render()
            for element in self.ui_elements:
                element.draw()

    def on_key_press(self, key, modifiers):
        if key == arc.key.U:  # Example key to toggle UI visibility
            self.toggle_ui()
    