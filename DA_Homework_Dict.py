'---DICT---'

"---138---"

# my_dict = {
#     ('.', ',', '?','!') : 1,
#     ('A', 'B', 'C'): 2,
#     ('D', 'E', 'F') : 3,
#     ('G', 'H', 'I') : 4,
#     ('J', 'K', 'L') : 5,
#     ('M', 'N', 'O'): 6,
#     ('P', 'Q', 'R', 'S') : 7,
#     ('T', 'U', 'V') : 8,
#     ('W', 'X', 'Y', 'Z') : 9,
#     (' ') : 0
# }
# # print(my_dict)
# my_list = []
# my_text = 'HELLO, WORLD!'
# for i in my_dict:
#     for j in i:
#         for k in my_text:
#             if k == j:
#                 my_list.append(my_dict[i])
# print(my_list)


"---139---"   

# my_dict = {
#     'A' : '.-',
#     'B' : '-...',
#     'C' : '-.-.',
#     'D' : '-..'
# }
# my_string = ''
# word = input("Enter your word: ")
# for i in word:
#     for j in my_dict:
#         if i == j:
#             my_string += my_dict[j]
# print(my_string)

"---140---" 

# my_dict = {
#     'A' : 'Newfoundland',
#     'B' : 'Nova Scotia',
#     'C' : 'Prince Edward Island',
#     'E' : 'New Brunswick',
#     'X' : 'Nunavut',
#     'X' : 'Northwest Territories',
#     '0' : 'rural'
# }
# user_input = input("Enter your code: ")
# for i in my_dict:
#     for j in user_input:
#         if j == i:
#             if i == 'X':
#                 print('Nunavut' or 'Northwest Territories')
#             print(my_dict[i])

"---141---" 

# my_dinct = {
#     '1' : 'One',
#     '2' : 'two',
#     '40' : 'forty'
# }
# user_input = input("Enter your number: ")
# for i in my_dinct:
#         if user_input == i:
#             print(my_dinct[i])

"---142---" 

# my_list = []
# new_list = []
# user_input = input("Enter the word: ")
# for i in user_input:
#     my_list.append(i)
# print(my_list)
# my_list.sort()
# for j in my_list:
#     new_list.append(j)
#     my_list.remove(j)
# print(new_list)

"---143---" 

# my_list = []
# user_input = input("Enter the name: ")
# for i in user_input:
#     my_list.append(i)
# for i in my_list:
#     if i[:] == i[-1::-1]:
#         print("Anagram")

"---145---" 

# my_dict = {
#     ('A','E','I','L','N','O','R','S','T','U') : 1,
#     ('D', 'G') : 2,
#     ('B', 'C', 'M', 'P') : 3,
#     ('F', 'H', 'V', 'W', 'Y') : 4,
#     ('K') : 5,
#     ('J', 'X') : 8,
#     ('Q', 'Z') : 10
# }
# summ = 0
# user_input = input("Enter the word: ")
# for i in my_dict:
#     for j in i:
#         for k in user_input:
#             if k == j:
#                 summ += my_dict[i]
# print(summ)
