from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result):
    with open('results.txt', 'a') as file: 
        file.write(result + '\n')


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
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldInde