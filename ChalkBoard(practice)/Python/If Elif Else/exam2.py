import random
mystring = "Secret agents are super good at staying hidden."

# for word in mystring.split():
#     first_letter = word.lower()[0]
#
#     if first_letter =='s':
#         print(word)

# for word in mystring.split():
#     if len(word)% 2 == 0:
#         print(word)

# word=[word[0] for word in mystring.split()]
# print(word)

# even=[n for n in range(0,11) if n%2==0]
# print(even)

# rangeex = list(range(0,11,2))
# print(rangeex)

# result = []
# for x in range(0,11):
#     result.append(random.randint(0,100))
# print(result)

# result = [random.randint(0,100) for n in range(0,11)]
# print(result)

result = 3

while result %2 != 0:
    num = int(input("enter a number"))
    if num%2 !=0:
        result = 3
    else:
        print("Thank you, that is an even number")
        result=2