#take marks as input from the user
print("The marks obtained in 4 subjects: ")
math= int(input("maths: "))
science= int(input("science: "))
english= int(input("english: "))
history= int(input("history: "))

#let's calculate the percentage
sum=math+science+english+history
print("the sum of 4 subjects is: ", sum)

perc=(sum/400)*100
print("percentage is: ", perc)