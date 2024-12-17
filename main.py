import random

def print_board(board):
    """
    Выводит текущее состояние доски 3x3.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """
    Проверяет, есть ли победитель на доске.
    :param board: Игровое поле
    :param player: 'X' или 'O'
    :return: True, если есть победитель, иначе False
    """
    # Проверка строк, столбцов и диагоналей
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    """
    Проверяет, есть ли ничья (все ячейки заняты, и победителя нет).
    """
    return all(all(cell != ' ' for cell in row) for row in board)


def get_player_move(board):
    """
    Запрашивает у игрока ход и возвращает координаты.
    """
    while True:
        try:
            move = input("Введите ваш ход (строка и столбец от 1 до 3, например, 1 2): ")
            row, col = map(int, move.split())
            row -= 1  # Преобразование в индексы от 0 до 2
            col -= 1
            if board[row][col] == ' ':
                return row, col
            else:
                print("Эта ячейка уже занята. Попробуйте снова.")
        except (ValueError, IndexError):
            print("Неверный ввод. Введите два числа от 1 до 3, разделенные пробелом.")


def get_computer_move(board):
    """
    Компьютер выбирает случайную свободную ячейку.
    """
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_cells)


def main():
    """
    Основная логика игры.
    """
    print("Добро пожаловать в игру Крестики-Нолики!")
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Пустое игровое поле 3x3

    player_symbol = 'X'
    computer_symbol = 'O'

    print_board(board)

    while True:
        # Ход игрока
        print("\nВаш ход (вы играете за X)")
        row, col = get_player_move(board)
        board[row][col] = player_symbol
        print_board(board)

        if check_winner(board, player_symbol):
            print("Поздравляем! Вы победили!")
            break

        if is_draw(board):
            print("Ничья!")
            break

        # Ход компьютера
        print("\nХод компьютера (O)...")
        row, col = get_computer_move(board)
        board[row][col] = computer_symbol
        print_board(board)

        if check_winner(board, computer_symbol):
            print("Компьютер победил!")
            break

        if is_draw(board):
            print("Ничья!")
            break


if __name__ == "__main__":
    main()
