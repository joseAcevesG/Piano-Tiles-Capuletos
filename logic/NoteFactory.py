import random

from .note import Note


class NoteFactory:
    def _init_(self):
        pass

    def create_note(self, note_width, note_height, screen_width):
        columns = [i * note_width for i in range(4)]
        x = random.choice(columns)
        y = -note_height
        note_color = (0, 0, 0)  # Notas negras
        return Note(x, y, note_width, note_height, note_color)
