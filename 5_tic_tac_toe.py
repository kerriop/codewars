# def is_solved(board):
#     not_yet = False
#     X_won = False
#     O_won = False
#     draw = False
#
#     def _lines(board):
#         yield from board
#         yield [board[i][i] for i in range(len(board))]
#
#     def lines(board):
#         yield from _lines(board)
#         yield from _lines(list(zip(*reversed(board)))
#
#     def who_won(board):
#         for line in lines(board):
#             if len(set(line)) == 1 and line[0] is not 0:
#                 return line[0]
#         return 0
#
#     if not_yet:
#         return -1
#     if X_won:
#         return 1
#     if O_won:
#         return 2
#     if draw:
#         return 0
#
#
# board = [[0, 0, 1],
#          [0, 1, 2],
#          [2, 1, 0]]
# print(is_solved(board))