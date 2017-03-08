import os
from pygame.locals import *

from menu import *

data_py = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.normpath(os.path.join(data_py, '..', 'data'))


def filepath(filename):  # Method to name a filepath
    return os.path.join(data_dir, filename)


def load(filename, mode='rb'):  # Method to open a loaded filepath
    return open(os.path.join(data_dir, filename), mode)


def load_image(filename):  # Method to load an image in the program
    filename = filepath(filename)
    try:
        image = pygame.image.load(filename)
        image = pygame.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))
    except pygame.error:
        raise SystemExit, "Unable to load: " + filename
    return image.convert_alpha()


def load_sound(filename, volume=0.5):  # Method to load a sound in the program
    filename = filepath(filename)
    try:
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(volume)
    except:
        raise SystemExit, "Unable to load: " + filename  # Exit system & show exception error when unable to load a sound
    return sound


def play_music(filename, volume=0.5, loop=-1):  # Play sound
    filename = filepath(filename)
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)
    except:
        raise SystemExit, "Unable to load: " + filename


def stop_music():   # Stop sound
    pygame.mixer.music.stop()
