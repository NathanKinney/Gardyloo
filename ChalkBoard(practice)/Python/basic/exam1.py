with open('exam.txt') as test:
        read = test.readlines()
        read = read[6]

        print(read.count)

num_lines = sum(1 for line in open('exam.txt'))

# print(num_lines)