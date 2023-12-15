import chess



class Turn:
    def __init__(self):
        self.turns = {}

    def make_move(self, name, start_square, end_square):
        self.turns[name] = (start_square, end_square)
        # name.move(end_square)
        print(self.turns)

    def undo(self) -> None:
        if self.turns:
            name, start_square, end_square = self.turns.pop()
            name.move(start_square)


class Game:
    def __init__(self) -> None:
        self.board = chess.Chessboard()
        self.turn = Turn()
        self.history = []
        self.log_list = []

    def make_move(self, figure: chess.Piece):
       start_square = figure.square
       end_square = self.board[figure.move]
       self.turn.make_move(figure, start_square, end_square)
       self.history.append((figure, start_square, end_square))

    def show_log(self):
        res = ''
        for i in self.history:
            for num in range(len(self.history)):
                res += f'#{num}: {i}'

        return res
    
    def return_to(self):
        pass 

    def create(self):
        self.board
