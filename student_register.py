'''
This is a program to add students marks, show all students marks, find a students
marks etc. This is to learn python dictionary

'''


students = {}
choice = "yes"
while choice.lower() == "yes":
    print("Hello, This is where you make your on Student Data Dictionary")
    print("1. Add student")
    print("2. Show all students")
    print("3. Show to students with the greatest and least marks")
    print("4. Find a student")
    print("5. Finish Program")
    nice=int(input("Enter your choice (1-5): "))
    if nice == 1:
             name = input("Enter the students name: ")
             marks = int(input("Enter the marks of the student: "))
             students[name] = marks

    elif nice == 2:
        for f in students.keys():
            print("")
            print(f, students[f])
            print("")

    elif nice == 3:
        
        key_list = list(students.keys())
        val_list = list(students.values())

        h = max(students.values())
        l = min(students.values())

        max_index=val_list.index(h)
        min_index=val_list.index(l)

        key_list[max_index]
        key_list[min_index]

        print("The student that scored least is", key_list[val_list.index(l)])
        print("")
        print("The student that scored most is", key_list[val_list.index(h)])
        print("")


    elif nice == 4:
       
        k = input("Enter the name of the student you wish to choose: ")

        if k in students.keys():
            print("")
            print(k, students[k])
            print("")

        else:
            print("Invalid Name. Please try again")

    elif nice == 5:
            print("Bye..... ")
            break
        

     
        




        
        
            
            
            
            
    
    
    
