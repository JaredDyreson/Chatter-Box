import pyglet
import multiprocessing
import sys
import os

print(os.getcwd())

class Mixer:
    def __init__(self):
        self.basedir = "MathGames/assets/soundeffects"
        self.happySound = pyglet.resource.media(f'{self.basedir}/sliced-yay-sound-effec.mp3')
        self.sadSound = pyglet.resource.media(f'{self.basedir}/aww-sound-effect.mp3')

    def playJingle(self, functionPointer, delay=2.5):
        process = multiprocessing.Process(target=functionPointer, name="Sound Effect")
        process.start()
        process.join(delay)
        if(process.is_alive()):
            process.terminate()
            process.join()

    def playHappy(self):
        self.happySound = pyglet.resource.media(f'{self.basedir}/sliced-yay-sound-effec.mp3')
        self.happySound.play()
        

    def playSad(self):
        self.sadSound = pyglet.resource.media(f'{self.basedir}/aww-sound-effect.mp3')
        self.sadSound.play()
