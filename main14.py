#take input from the student that can attend the exam
medical_cause=input("did you have a medical cause Y or N: ")

#take input of attendence
attend=int(input("Enter your attendence: "))

if medical_cause == 'Y':
    print("You are allowed")
else:
    if attend >= 75:
        print("Allowed")
    else:
        print("Not allowed")