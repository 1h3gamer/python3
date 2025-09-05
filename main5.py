#taking input amounts from the user
amount=int(input("input the amount you want to withdraw: "))

#calculating the number of notes from different denominations
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10

#printing the amount
print("notes of 100 dollars: ", note1)
print("notes of 50 dollars: ", note2)
print("notes of 10 dollars: ", note3)