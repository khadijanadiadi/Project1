import csv
def insertData(Info_list):
    with open('StudentInfo.csv','a', newline='') as csvfile:
        writer=csv.writer(csvfile)
        if csvfile.tell()==0:
            writer.writerow(["NAME", "AGE", "CONTACT NUMBER", "EMAIL ID"])
        writer.writerow(Info_list)

condition = True
snum = 1

while (condition):
    student_info = input("Enter the information for student #{} in the following format (Name Age Contact_Number Email_ID): ".format(snum))
    student_info_list=student_info.split(' ')
    print("\n The entered Information is: \n Name: {} \nAge: {} \nContact Number: {}\nemail Id: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    choice_check = input("Is the entered Information correct? (yes/no) ")
    if choice_check == "yes":
        insertData(student_info_list)
        condition_check= input("You want to add other records? (yes/no): ")
        if condition_check=="yes":
            condition=True
            snum=snum+1
        elif condition_check == "no":
            condition = False
        elif choice_check == "no":
                print("\n Please re enter!")



