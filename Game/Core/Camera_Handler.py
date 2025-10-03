class Camera:
    def __init__(self, screen_width, screen_height,x,y):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = x
        self.y = y

    def apply(self, target_x, target_y):
        # Centraliza a camera no jogador
        self.x = target_x - self.screen_width // 2
        self.y = target_y - self.screen_height // 2
        return self.x, self.y

    #Atualiza a posicao da camera com base na posicao do jogador
    def update(self, player):
        self.x, self.y = self.apply(player.x, player.y)
