import random
import time

from note import Note  # Importa la clase Note desde el archivo note.py


class GameManager:
    def __init__(self, screen_width: int, screen_height: int, speed: float):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.notes = [[None for _ in range(4)] for _ in range(6)]  # Matriz de 6x4
        self.score = 0
        self.speed = speed
        self.running = True  # Controla el ciclo del juego

    def create_note(self):
        """Crea una nueva nota en una columna aleatoria en la primera fila (0)."""
        column = random.randint(0, 3)  # Escoge una columna aleatoria (0-3)

        # Definir rectángulo y color de la nueva nota
        rect = [
            column * (self.screen_width // 4),
            0,
            self.screen_width // 4,
            50,
        ]  # Ejemplo de rectángulo
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )  # Color aleatorio

        note = Note(rect, color)  # Crear la instancia de la nota

        self.notes[0] = [
            note if i == column else None for i in range(4)
        ]  # Asignar la nota a la matriz

    def update_notes(self):
        """Actualiza las notas moviéndolas una fila hacia abajo y crea una nueva nota en la fila superior."""
        # Mueve las notas hacia abajo
        for row in range(5, 0, -1):  # Desde la penúltima fila a la primera
            self.notes[row] = self.notes[row - 1]

        # Mover todas las notas
        for row in range(6):
            for note in self.notes[row]:
                if note:
                    note.move()
        # Crea una nueva nota en la fila de hasta arriba
        self.create_note()

    def check_hit(self, mouse_pos: int) -> bool:
        """Verifica si el clic en la posición 'mouse_pos' coincide con la nota en la fila inferior."""
        bottom_row = self.notes[5]
        if bottom_row[mouse_pos] is not None:
            self.notes[5][mouse_pos] = None  # Elimina la nota si se acierta
            self.score += 1  # Incrementa la puntuación
            return True
        return False

    def run(self):
        """Simula un ciclo de juego donde las notas se mueven continuamente."""
        print("Juego iniciado. Presiona Ctrl+C para detener.")
        try:
            while self.running:
                # Actualizar notas
                self.update_notes()

                # Imprimir el estado actual de la matriz
                self.print_matrix()

                # Controlar la velocidad del ciclo usando la propiedad 'speed'
                time.sleep(self.speed)
        except KeyboardInterrupt:
            self.running = False
            print("Juego detenido.")

    def print_matrix(self):
        """Método auxiliar para imprimir la matriz en consola (para pruebas)."""
        for row in self.notes:
            row_display = []
            for note in row:
                if note:
                    row_display.append(f"Note({note.color})")
                else:
                    row_display.append("None")
            print(row_display)
        print(f"Score: {self.score}")


# Ejemplo de uso:
gm = GameManager(
    screen_width=800, screen_height=600, speed=1
)  # 1 segundo entre actualizaciones
gm.run()  # Inicia el ciclo del juego
