class Log:
    def __init__(self, saw_blade_height_millimeters):
        self.boards = []
        self.saw_blade_height_millimeters = saw_blade_height_millimeters

    def __str__(self):
        output = ""

        for i, board in enumerate(self.boards):
                output += "| {0:>6} |".format(str(board))

                if i == len(self.boards) - 1:
                    output += " <= " + str(self.current_blade_height_millimeters())

                output += "\n"

        return output

    def add_board(self, board):
        self.boards.append(board)

    def pop_board(self):
        board = self.boards.pop()

    def boards_count(self):
        return len(self.boards)

    def current_blade_height_millimeters(self):
        height_millimeters = 0

        for board in self.boards:
            height_millimeters += board.height_millimeters

        return height_millimeters + ((len(self.boards) - 1) * self.saw_blade_height_millimeters)

class Board:
    def __init__(self, height_millimeters, is_saw_blade_placeholder=False):
        self.is_saw_blade_placeholder = is_saw_blade_placeholder
        self.height_millimeters = height_millimeters

    def __str__(self):
        return str(self.height_millimeters)


def cutting_height():
    default_saw_blade_height_millimeters = 3

    saw_blade_height_millimeters = int(input("Hauteur de lame en mm\n (default: 3mm): ").strip() or "0") or default_saw_blade_height_millimeters

    log = Log(saw_blade_height_millimeters)
    current_height = 0

    while True:
        input_text = "Hauteur de planche mm" + ("\n ('-' pour depiler): " if log.boards_count() > 0 else ":")
        user_input = input(input_text).strip()

        if user_input == "-":
            if log.boards_count() > 0:
                log.pop_board()
            else:
                continue

        else:
            current_board_height_millimeters = int(user_input or "0")

            if current_board_height_millimeters <= 0:
                print("La hauteur doit etre > 0")
                continue

            log.add_board(Board(current_board_height_millimeters))

        print("\n" + str(log) + "\n")


cutting_height()
