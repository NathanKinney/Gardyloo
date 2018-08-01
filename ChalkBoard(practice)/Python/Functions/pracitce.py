# def report_agent():
#     print('Report Agent')
#
# report_agent()
#
# def report(name='Jason'):
#     print ('Reporting {}'.format(name))
#
# report('Nate')
# report()
#
# def add(n1,n2):
#     return(n1+n2)
#
# result = add(2,4)
# print(result)
#
# def secret_check(mystring):
#     return 'secret' in mystring.lower()
# print(secret_check('this is a lie'))
# print(secret_check('this is a Secret'))
#
# def code_maker(mystring):
#     '''
#     INPUT: IS A STRING
#     OUTPUT: SAME STRING BUT ALL VOWELS ARE CONVERTED TO AN X
#     '''
#     output =list(mystring)
#     for i,letter in enumerate(mystring):
#         for vowel in ['a', 'e', 'i', 'o', 'u']:
#             if letter.lower() == vowel:
#                 output[i] ='x'
#     return output
# result = code_maker('hello')
# print(result)

# def check_ten(n1,n2):
#     if n1+n2 == 10:
#         return True
#     else:
#         return False
#
# print(check_ten(7,0))

# def check_ten(n1,n2):
#     if n1+n2 == 10:
#         return True
#     else:
#         return n1+n2
#
# print(check_ten(10,0))

# def first_upper(mystring):
#     return mystring.upper()[0]
#
# print(first_upper('hello'))

# def last_two (mystring):
#     if len(mystring) < 2:
#         return 'Error'
#     else:
#         return mystring[-2:]
#
# print(last_two('a'))

# def seq_check(nums):
#     for i in range(len(nums)-2):
#         if nums[i] == 1 and nums [i+1]==2 and nums[i+2]==3:
#             return True
#     else:
#         return False
#
# print(seq_check([1,2,3]))

# def compare_len(s1,s2):
#     return abs(len(s1)-len(s2))
#
# print(compare_len('adfwefwef','wfw'))