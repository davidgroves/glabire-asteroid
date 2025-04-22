import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        # The "image" attribute is required by pygame Sprites, even if you're not using it.
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)  # Create a transparent surface
        self.rect = self.image.get_rect()  # Define the "rect" attribute
        self.rect.center = (x, y)  # Position the rect at the initial position

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass