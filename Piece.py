from enums import Player


class Piece:
    def __init__(self, name: str, row_number: int, col_number: int, player) -> None:
        self.name = name
        self.row_number = row_number
        self.col_number = col_number
        self.player = player

    def get_row_number(self):
        return self.row_number

    def get_col_number(self):
        return self.col_number

    def get_name(self):
        return self.name

    def get_player(self):
        return self.player

    def set_row_number(self, row_number: int):
        self.row_number = row_number

    def set_col_number(self, col_number: int):
        self.col_number = col_number

    def can_take(self, is_check):
        pass

    def is_player(self, checked_player):
        return self.player == checked_player


class Rook(Piece):
    def __init__(self, name: str, row_number: int, col_number: int, player) -> None:
        super().__init__(name, row_number, col_number, player)
        self.has_moved = False

    def get_valid_peaceful_moves(self, game_state):
        return self.traverse(game_state)[0]

    def get_valid_piece_takes(self, game_state):
        return self.traverse(game_state)[1]

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)

    def traverse(self, game_state):
        peaceful_moves = []
        piece_takes = []

        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1

        # Déplacement vers la gauche
        self.breaking_point = False
        while self.get_col_number() - self._left >= 0 and not self.breaking_point:
            if game_state.get_piece(self.get_row_number(), self.get_col_number() - self._left) is Player.EMPTY:
                peaceful_moves.append(
                    (self.get_row_number(), self.get_col_number() - self._left))
                self._left += 1
            elif game_state.get_piece(self.get_row_number(), self.get_col_number() - self._left) and not game_state.get_piece(self.get_row_number(), self.get_col_number() - self._left).is_player(self.get_player()):
                piece_takes.append(
                    (self.get_row_number(), self.get_col_number() - self._left))
                self.breaking_point = True
            else:
                self.breaking_point = True

        # Déplacement vers la droite
        self.breaking_point = False
        while self.get_col_number() + self._right < 8 and not self.breaking_point:
            if game_state.get_piece(self.get_row_number(), self.get_col_number() + self._right) is Player.EMPTY:
                peaceful_moves.append(
                    (self.get_row_number(), self.get_col_number() + self._right))
                self._right += 1
            elif game_state.get_piece(self.get_row_number(), self.get_col_number() + self._right) and not game_state.get_piece(self.get_row_number(), self.get_col_number() + self._right).is_player(self.get_player()):
                piece_takes.append(
                    (self.get_row_number(), self.get_col_number() + self._right))
                self.breaking_point = True
            else:
                self.breaking_point = True

        # Déplacement vers le bas
        self.breaking_point = False
        while self.get_col_number() + self._down < 8 and not self.breaking_point:
            if game_state.get_piece(self.get_row_number(), self.get_col_number() + self._down) is Player.EMPTY:
                peaceful_moves.append(
                    (self.get_row_number(), self.get_col_number() + self._down))
                self._down += 1
            elif game_state.get_piece(self.get_row_number(), self.get_col_number() + self._down) and not game_state.get_piece(self.get_row_number(), self.get_col_number() + self._down).is_player(self.get_player()):
                piece_takes.append(
                    (self.get_row_number(), self.get_col_number() + self._down))
                self.breaking_point = True
            else:
                self.breaking_point = True

        # Déplacement vers le haut
        self.breaking_point = False
        while self.get_col_number() - self._up < 8 and not self.breaking_point:
            if (game_state.get_piece(self.get_row_number(), self.get_col_number() - self._up)
                    is Player.EMPTY):
                peaceful_moves.append(
                    (self.get_row_number(), self.get_col_number() + self._up))
                self._up += 1
            elif (game_state.get_piece(self.get_row_number(), self.get_col_number() - self._up)
                    and not
                    game_state.get_piece(
                        self.get_row_number(), self.get_col_number() - self._up)
                  .is_player(self.get_player())):
                piece_takes.append(
                    (self.get_row_number(), self.get_col_number() - self._up))
                self.breaking_point = True
            else:
                self.breaking_point = True

        return (peaceful_moves, piece_takes)


class Knight(Piece):
    def get_valid_peaceful_moves(self, game_state):
        _moves = []
        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]

        for i in range(8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]

            square_eval = game_state.get_piece(new_row, new_col)
            if square_eval == Player.EMPTY:
                _moves.append((new_row, new_col))
        return _moves

    def get_valid_piece_takes(self, game_state):
        _moves = []
        row_change = [-2, -2, -1, -1, +1, +1, +2, +2]
        col_change = [-1, +1, -2, +2, -2, +2, +1, -1]

        for i in range(8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]

            square_eval = game_state.get_piece(new_row, new_col)
            if square_eval and not square_eval.is_player(self.get_player()):
                _moves.append((new_row, new_col))
        return _moves

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)


class Bishop(Piece):
    def __init__(self, name: str, row_number: int, col_number: int, player) -> None:
        super().__init__(name, row_number, col_number, player)

    def get_valid_peaceful_moves(self, game_state):
        return self.traverse(game_state)[1]

    def get_valid_piece_takes(self, game_state):
        return self.traverse(game_state)[0]

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)

    def traverse(self, game_state):
        _peaceful_moves = []
        _piece_takes = []

        self.breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1

        while self.get_col_number() - self._left >= 0 and not self.breaking_point:
            if game_state.get_piece(self.get_row_number(), self.get_col_number() - self._left) is Player.EMPTY:
                _peaceful_moves.append(
                    (self.get_row_number(), self.get_col_number() - self._left))
                self._left += 1
            elif game_state.get_piece(self.get_row_number(), self.get_col_number() - self._left) and not game_state.get_piece(self.get_row_number(), self.get_col_number() - self._left).is_player(self.get_player()):
                _piece_takes.append(
                    (self.get_row_number(), self.get_col_number() - self._left))
                self.breaking_point = True
            else:
                self.breaking_point = True

        self.breaking_point = FalseF
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_col_number() + self._right < 8 and not self.breaking_point:
            if game_state.get_piece(self.get_row_number(), self.get_col_number() + self._right) is Player.EMPTY:
                _peaceful_moves.append(
                    (self.get_row_number(), self.get_col_number() + self._right))
                self._right += 1
            elif game_state.get_piece(self.get_row_number(), self.get_col_number() + self._right) and not game_state.get_piece(self.get_row_number(), self.get_col_number() + self._right).is_player(self.get_player()):
                _piece_takes.append(
                    (self.get_row_number(), self.get_col_number() + self._right))
                self.breaking_point = True
            else:
                self.breaking_point = True

        self.breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_row_number() + self._down < 8 and not self.breaking_point:
            if game_state.get_piece(self.get_row_number() + self._down, self.get_col_number()) is Player.EMPTY:
                _peaceful_moves.append(
                    (self.get_row_number() + self._down, self.get_col_number()))
                self._down += 1
            elif game_state.get_piece(self.get_row_number() + self._down, self.get_col_number()) and not game_state.get_piece(self.get_row_number() + self._down, self.get_col_number()).is_player(self.get_player()):
                _piece_takes.append(
                    (self.get_row_number() + self._down, self.get_col_number()))
                self.breaking_point = True
            else:
                self.breaking_point = True

        self.breaking_point = False
        self._up = 1
        self._down = 1
        self._left = 1
        self._right = 1
        while self.get_row_number() - self._up >= 0 and not self.breaking_point:
            if game_state.get_piece(self.get_row_number() - self._up, self.get_col_number()) is Player.EMPTY:
                _peaceful_moves.append(
                    (self.get_row_number() - self._up, self.get_col_number()))
                self._up += 1
            elif game_state.get_piece(self.get_row_number() - self._up, self.get_col_number()) and not game_state.get_piece(self.get_row_number() - self._up, self.get_col_number()).is_player(self.get_player()):
                _piece_takes.append(
                    (self.get_row_number() - self._up, self.get_col_number()))
                self.breaking_point = True
            else:
                self.breaking_point = True

        return (_piece_takes, _peaceful_moves)


class Pawn(Piece):
    def get_valid_piece_takes(self, game_state):
        _moves = []
        if self.get_player() is Player.Player_1:
            if game_state.is_valid_piece(self.get_row_number() + 1, self.get_col_number() - 1) and game_state.get_piece(self.get_row_number() + 1, self.get_col_number() - 1).is_player(Player.Player_2):
                _moves.append((self.get_row_number() + 1,
                              self.get_col_number() - 1))
            if game_state.is_valid_piece(self.get_row_number() + 1, self.get_col_number() + 1) and game_state.get_piece(self.get_row_number() + 1, self.get_col_number() + 1).is_player(Player.Player_2):
                _moves.append((self.get_row_number() + 1,
                              self.get_col_number() + 1))
            if game_state.can_en_passant(self.get_row_number(), self.get_col_number()):
                _moves.append((self.get_row_number() + 1,
                              game_state.previous_en_passant()[1]))

        elif self.get_player() is Player.Player_2:
            if game_state.is_valid_piece(self.get_row_number() - 1, self.get_col_number() - 1) and game_state.get_piece(self.get_row_number() - 1, self.get_col_number() - 1).is_player(Player.Player_1):
                _moves.append((self.get_row_number() - 1,
                              self.get_col_number() - 1))
            if game_state.is_valid_piece(self.get_row_number() - 1, self.get_col_number() + 1) and game_state.get_piece(self.get_row_number() - 1, self.get_col_number() + 1).is_player(Player.Player_1):
                _moves.append((self.get_row_number() - 1,
                              self.get_col_number() + 1))
            if game_state.can_en_passant(self.get_row_number(), self.get_col_number()):
                _moves.append((self.get_row_number() - 1,
                              game_state.previous_en_passant()[1]))

        return _moves

    def get_valid_peaceful_moves(self, game_state):
        _moves = []
        # when the pawn is a white piece
        if self.is_player(Player.PLAYER_1):
            # when the square right below the starting_square is empty
            if game_state.get_piece(self.get_row_number() + 1, self.get_col_number()) == Player.EMPTY:
                # when the pawn has not been moved yet
                if self.get_row_number() == 1 and game_state.get_piece(self.get_row_number() + 2,
                                                                       self.get_col_number()) == Player.EMPTY:
                    _moves.append(
                        (self.get_row_number() + 1, self.get_col_number()))
                    _moves.append(
                        (self.get_row_number() + 2, self.get_col_number()))
                # when the pawn has already been moved
                else:
                    _moves.append(
                        (self.get_row_number() + 1, self.get_col_number()))
        # when the pawn is a black piece
        elif self.is_player(Player.PLAYER_2):
            # when the square right above is empty
            if game_state.get_piece(self.get_row_number() - 1, self.get_col_number()) == Player.EMPTY:
                # when the pawn has not been moved yet
                if self.get_row_number() == 6 and game_state.get_piece(self.get_row_number() - 2,
                                                                       self.get_col_number()) == Player.EMPTY:
                    _moves.append(
                        (self.get_row_number() - 1, self.get_col_number()))
                    _moves.append(
                        (self.get_row_number() - 2, self.get_col_number()))
                # when the pawn has been moved
                else:
                    _moves.append(
                        (self.get_row_number() - 1, self.get_col_number()))
        return _moves

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_piece_moves(game_state) + self.get_valid_piece_takes(game_state)
    

class Queen(Rook, Bishop):
    def get_valid_peaceful_moves(self, game_state):
        return (Rook.get_valid_peaceful_moves(Rook(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state) +
                Bishop.get_valid_peaceful_moves(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state))

    def get_valid_piece_takes(self, game_state):
        return (Rook.get_valid_piece_takes(Rook(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state) +
                Bishop.get_valid_piece_takes(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state))

    def get_valid_piece_moves(self, game_state):
        return (Rook.get_valid_piece_moves(Rook(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state) +
                Bishop.get_valid_piece_moves(Bishop(self.get_name(), self.get_row_number(), self.get_col_number(), self.get_player()), game_state))


class King(Piece):
    def get_valid_piece_takes(self, game_state):
        _moves = []
        row_change = [-1, +0, +1, -1, +1, -1, +0, +1]
        col_change = [-1, -1, -1, +0, +0, +1, +1, +1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = game_state.get_piece(new_row, new_col)
            # when the square with new_row and new_col contains a valid piece
            if game_state.is_valid_piece(new_row, new_col):
                # when the king is white and the piece near the king is black
                if self.is_player(Player.PLAYER_1) and evaluating_square.is_player(Player.PLAYER_2):
                    _moves.append((new_row, new_col))
                # when the king is black and the piece near the king is white
                elif self.is_player(Player.PLAYER_2) and evaluating_square.is_player(Player.PLAYER_1):
                    _moves.append((new_row, new_col))
        return _moves

    def get_valid_peaceful_moves(self, game_state):
        _moves = []
        row_change = [-1, +0, +1, -1, +1, -1, +0, +1]
        col_change = [-1, -1, -1, +0, +0, +1, +1, +1]

        for i in range(0, 8):
            new_row = self.get_row_number() + row_change[i]
            new_col = self.get_col_number() + col_change[i]
            evaluating_square = game_state.get_piece(new_row, new_col)
            if evaluating_square == Player.EMPTY:
                _moves.append((new_row, new_col))

        if game_state.king_can_castle_left(self.get_player()):
            if self.is_player(Player.PLAYER_1):
                _moves.append((0, 1))
            elif self.is_player(Player.PLAYER_2):
                _moves.append((7, 1))
        elif game_state.king_can_castle_right(self.get_player()):
            if self.is_player(Player.PLAYER_1):
                _moves.append((0, 5))
            elif self.is_player(Player.PLAYER_2):
                _moves.append((7, 5))
        return _moves

    def get_valid_piece_moves(self, game_state):
        return self.get_valid_peaceful_moves(game_state) + self.get_valid_piece_takes(game_state)
