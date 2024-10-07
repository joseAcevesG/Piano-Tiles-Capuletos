import time

import pygame

from .NoteFactory import NoteFactory


class GameManager:
    def _init_(self, screen_width, screen_height, speed):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.note_width = self.screen_width // 4
        self.note_height = self.screen_height // 10
        self.notes = []
        self.score = 0
        self.speed = speed
        self.note_factory = NoteFactory()
        self.last_note_time = time.time()
        self.note_interval = 1
        self.game_over = False

    def create_note(self):
        note = self.note_factory.create_note(
            note_width=self.note_width,
            note_height=self.note_height,
            screen_width=self.screen_width,
        )
        self.notes.append(note)

    def update_notes(self):
        for note in self.notes[:]:
            note.move(self.speed)
            if note.is_off_screen(self.screen_height):
                self.notes.remove(note)
                self.game_over = True  # El juego termina si una nota no es tocada
                break  # Salimos del ciclo, ya que el juego ha terminado
        current_time = time.time()
        if current_time - self.last_note_time > self.note_interval:
            self.create_note()
            self.last_note_time = current_time

    def check_hit(self, key):
        key_column_map = {pygame.K_a: 0, pygame.K_s: 1, pygame.K_d: 2, pygame.K_f: 3}

        if key not in key_column_map:
            return False

        column = key_column_map[key]
        column_x_start = column * self.note_width

        for note in self.notes:
            if (
                note.rect.x == column_x_start
                and self.screen_height - self.note_height
                <= note.rect.bottom
                <= self.screen_height
            ):
                self.notes.remove(note)
                self.score += 1
                return True
        return False
