import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.player = 'X'
        self.board = [' ' for _ in range(9)]
        self.win_combination = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        self.window = tk.Tk()
        self.window.title('Tic Tac Toe')
        self.buttons = []
        for i in range(9):
            buttons = tk.Button(self.window, text='', width=3,
                                height=1,
                                font=('Helvetica', '20'),
                                command=lambda x=i: self.move(x))
            buttons.grid(row=i // 3, column=i % 3)
            self.buttons.append(buttons)

    def move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_win():
                print(f'{self.player} wins!')
                self.window.quit()
            elif ' ' not in self.board:
                print('Draw!')
                self.window.quit()
            else:
                self.player = 'O' if self.player == 'X' else 'X'

        else:
            print('Invalid move')

    def check_win(self):
        for combination in self.win_combination:
            if (self.board[combination[0]] == self.board[combination[1]] ==
                    self.board[combination[2]] != ' '):
                print(f'Winning combination: {combination}')
                return True
            
        print('No winning combination found')
        return False
        

    def play(self):
        self.window.mainloop()
        


if __name__ == '__main__':
    game = TicTacToe()
    game.play()
    
