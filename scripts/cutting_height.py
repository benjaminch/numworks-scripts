class Log:
    def __init__(self, saw_blade_height_millimeters):
        self.boards = []
        self.saw_blade_height_millimeters = saw_blade_height_millimeters

    def __repr__(self):
        output = ""

        for i, board in enumerate(reversed(self.boards)):
                output += "|\t" + board + "\t|"

                if i == 0:
                    output += " <= " + self.current_blade_height_millimeters()

                output += "\n"

        return output

    def add_board(self, board):
        self.boards.append(board)

    def pop_board(self):
        board = self.boards.pop()

    def current_blade_height_millimeters(self):
        height_millimeters = 0

        for board in self.boards:
            height_millimeters += board.height_millimeters

        return height_millimeters + ((len(self.boards) - 1) * self.saw_blade_height_millimeters)

class Board:
    def __init__(self, height_millimeters, is_saw_blade_placeholder=False):
        self.is_saw_blade_placeholder = is_saw_blade_placeholder
        self.height_millimeters = height_millimeters

    def __repr__(self):
        return str(self.height_millimeters)


def cutting_height():
    default_saw_blade_height_millimeters = 3

    saw_blade_height_millimeters = int(input("Hauteur de lame en millimetres (default: 3mm): ").strip() or "0") or default_saw_blade_height_millimeters

    log = Log(saw_blade_height_millimeters)
    current_height = 0

    while True:
        user_input = input("Hauteur de planche en millimetres: (tapez '-' pour depiler la derniere planche): ").strip()

        if user_input == "-":
            log.pop_board()

        else:
            current_board_height_millimeters = int(user_input or "0")

            if current_board_height_millimeters <= 0:
                print("La hauteur de planche doit etre > 0")
                continue

            log.add_board(Board(current_board_height_millimeters))

        print("\n" + log + "\n")


if __name__ == "__main__":
    cutting_height()
