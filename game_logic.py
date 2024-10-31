class ChineseChessGame:
    def __init__(self):
        self.board = self.create_initial_board()
        self.current_turn = 'r'  # 'r' cho quân đỏ, 'b' cho quân đen

    def create_initial_board(self):
        # Khởi tạo bàn cờ với các quân cờ ở vị trí ban đầu
        board = [
            ["rR", "rN", "rM", "rG", "rK", "rG", "rM", "rN", "rR"],
            ["", "", "", "", "", "", "", "", ""],
            ["", "rC", "", "", "", "", "", "rC", ""],
            ["rP", "", "rP", "", "rP", "", "rP", "", "rP"],
            ["", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["bP", "", "bP", "", "bP", "", "bP", "", "bP"],
            ["", "bC", "", "", "", "", "", "bC", ""],
            ["", "", "", "", "", "", "", "", ""],
            ["bR", "bN", "bM", "bG", "bK", "bG", "bM", "bN", "bR"],
        ]
        return board

    def move(self, from_pos, to_pos):
        # Hàm thực hiện nước đi từ from_pos tới to_pos
        if self.is_valid_move(from_pos, to_pos):
            piece = self.board[from_pos[0]][from_pos[1]]
            self.board[from_pos[0]][from_pos[1]] = ""
            self.board[to_pos[0]][to_pos[1]] = piece
            self.current_turn = 'b' if self.current_turn == 'r' else 'r'
            return True
        return False

    def is_valid_move(self, from_pos, to_pos):
        # Hàm kiểm tra tính hợp lệ của nước đi
        piece = self.board[from_pos[0]][from_pos[1]]
        if piece == "":
            return False
        if (piece[0] == 'r' and self.current_turn != 'r') or (piece[0] == 'b' and self.current_turn != 'b'):
            return False
        # Implement thêm các kiểm tra khác cho từng loại quân cờ
        return True

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

# Khởi tạo game và in bàn cờ
game = ChineseChessGame()
game.print_board()
