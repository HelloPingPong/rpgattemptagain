import pygame, sys # Import pygame and sys
from settings import * # Import settings
from debug import debug # Import debug
from level import Level

class Game: # Create game class and initializer. lines 5-8 are essential for pygame to work
    def __init__(self):
        pygame.init() # Initialize pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set screen size and create screen
        pygame.display.set_caption('Dungeons and Python') # Set caption
        self.clock = pygame.time.Clock() # Create clock

        self.level = Level(self) # Create instance of level class

    def run(self): # Main run method
        self.playing = True # Game loop
        while self.playing: # Game loop
            for event in pygame.event.get(): # Game loop to check for events
                if event.type == pygame.QUIT: # Game loop to check if user quits
                    self.playing = False # Game loop to change playing to false
                    pygame.quit() # Game loop to quit game
                    sys.exit() #game loop to quit game

            self.screen.fill('black') # fill screen with black
            self.level.run() # run level
            pygame.display.update() # updating screen
            self.clock.tick(FPS) # tick clock to FPS

if __name__ == "__main__": # Check if main
    g = Game() # Create game object
    g.run() # Run game loop