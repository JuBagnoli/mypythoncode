ISBN12 = input ("enter ISBN")
sum1 = 0
sum2 = 0
for index in range (0,12,2):
    temp = int(ISBN12[index])
    sum1 = sum1 + temp
for index2 in range (1, 12,2):
    sum2 = sum2 + temp2
total = sum1 + sum2
remain = total % 10
x13 = 10 - remain
#ISBN12 + str/x13 