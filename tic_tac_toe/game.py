from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


# Вот она - новая функция!
def save_result(result):
    # Открыть файл results.txt в режиме "добавление".
    # Если нужно явно указать кодировку, добавьте параметр encoding='utf-8'.
    file = open('results.txt', 'a')
    # Записать в файл содержимое переменной result.
    file.write(result + '\n')
    file.close()


def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ходит {current_player}')

        while True:
            try:
           