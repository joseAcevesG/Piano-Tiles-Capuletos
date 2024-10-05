import random
from note import Note

class NoteFactory:

    def __init__(self):
        pass

    def create_note(self, screen_width, note_width, note_height):
        # Generar posición aleatoria dentro de los límites de la pantalla
        x = random.randint(0, screen_width - note_width)
        y = 0
        
        # Crear una instancia de Note
        note_rect = (x, y, note_width, note_height)
        note_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        return Note(note_rect, note_color)