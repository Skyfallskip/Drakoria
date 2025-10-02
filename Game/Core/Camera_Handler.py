class Camera:
    def __init__(self, screen_width, screen_height,x,y):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = x
        self.y = y

    def apply(self, target_x, target_y):
        # Center the camera on the target (player)
        self.x = target_x - self.screen_width // 2
        self.y = target_y - self.screen_height // 2
        return self.x, self.y

    def update(self, player):
        self.x, self.y = self.apply(player.x, player.y)
