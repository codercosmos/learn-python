def manage_words():
    
    b=[]

    while True:
        
        a=input("Hi, wat is your word")
        if a in b:
            pass
        else:
            z=b.append(a)
        
        print('list: ', b)
        d=input("Continue?")
        if d=="yes":
            continue
        if d=="no":
            break


     



manage_words()
