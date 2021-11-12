# # import math
# #
# #
# # class User:
# #     def __init__(self):
# #         # self.possible_ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
# #         self.rank = -8
# #         self.progress = 0
# #         self.HUNDRED = 100
# #         self.highest = 8
# #
# #     def inc_progress(self, rank):
# #         if rank == 0 or rank > self.highest or rank < -self.highest:
# #             raise Exception('rank input out of range')
# #         if self.rank == self.highest:
# #             return None;
# #
# #         if (rank > 0 and self.rank < 0) or (rank < 0 and self.rank > 0):
# #             diff = abs(self.rank) + abs(rank)
# #         else:
# #             diff = rank - self.rank
# #
# #         if rank > 0 and self.rank < 0:
# #             diff -= 1
# #
# #         if rank < 0 and self.rank > 0:
# #             diff = -diff
# #
# #         if diff > 0:
# #             if rank == 1 and self.rank == -1:
# #                 self.progress += 10
# #             else:
# #                 self.progress += 10 * diff * diff
# #         else:
# #             if diff == 0:
# #                 self.progress += 3
# #             else:
# #                 self.progress += 1
# #         if self.progress > self.HUNDRED and self.rank < self.highest:
# #             self.rank = math.floor(self.progress / self.HUNDRED)
# #             if self.rank == 0:
# #                 self.rank += 1
# #             self.progress %= self.HUNDRED
# #         if self.rank == self.highest:
# #             self.progress = 0
# #         if self.progress == 100:
# #             self.progress = 0
# #             self.rank += 1
# #         return diff
# #
# class User:
#     RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
#
#     def __init__(self):
#         self.rank = -8
#         self.progress = 0
#
#     def inc_progress(self, rank):
#         if rank not in self.RANKS:
#             raise Exception('Rank does not exist')
#         self.progress += self.points(rank)
#         self.check_progress()
#
#     def points(self, rank):
#         if self.difference(rank) < -1:
#             return 0
#         if self.difference(rank) == -1:
#             return 1
#         if self.difference(rank) == 0:
#             return 3
#         return 10 * self.difference(rank) ** 2
#
#     def difference(self, rank):
#         return self.RANKS.index(rank) - self.RANKS.index(self.rank)
#
#     def check_progress(self):
#         while self.progress >= 100 and self.rank < 0:
#             self.increase_rank()
#         if self.rank == 8:
#             self.progress = 0
#
#     def increase_rank(self):
#         self.rank = self.RANKS[self.RANKS.index(self.rank)+1]
#         self.progress -= 100
#
#
# user = User()
# print(user.rank)  # -8
# print(user.progress)  # 0
# user.inc_progress(-7)
# print(user.progress)  # 10
# user.inc_progress(-5)  # add 90 progress
# print(user.progress)  # 0
# print(user.rank)  # -7
