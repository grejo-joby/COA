mem = [['P',3,1],['F',4,1],['P',6,2],['F',5,2],['P',1,3],['F',2,3]]
newP = int(input("Enter size of new Process: "))
ch = int(input("1. First Fit\n2. Best Fit\n3. Worst Fit\n4. Next Fit\n\nEnter your choice: "))
while(ch!=-1):
    if(ch==1):
        print("First Fit Output")
        memory=mem.copy()
        print("Before : \n")
        for i in range(len(memory)):
            if(memory[i][0]=='P'):
                print("Process P",memory[i][2],": ",memory[i][1],'K')
            elif(memory[i][0]=='F'):
                print("Free Space ",memory[i][2],": ",memory[i][1],'K')
        for i in range(len(memory)):
            if(memory[i][0]=='F'):
                if(memory[i][1]>=newP):
                    if(memory[i][1]-newP>0):
                        tempspace = memory[i][1]-newP
                        tempcount = memory[i][2]
                        memory.pop(i)
                        memory.insert(i,['F',tempspace,tempcount])
                        memory.insert(i,['P',newP,4])
                        break
                    elif(memory[i][1]-newP==0):
                        memory[i][0]='P'
                        memory[i][2]=4
                        break
        print("After:\n")
        for i in range(len(memory)):
            if(memory[i][0]=='P'):
                print("Process P",memory[i][2],": ",memory[i][1],'K')
            elif(memory[i][0]=='F'):
                print("Free Space ",memory[i][2],": ",memory[i][1],'K')
    
    if(ch==2):
        print("Best Fit Output")
        memory=mem.copy()
        print("Before : \n")
        for i in range(len(memory)):
            if(memory[i][0]=='P'):
                print("Process P",memory[i][2],": ",memory[i][1],'K')
            elif(memory[i][0]=='F'):
                print("Free Space ",memory[i][2],": ",memory[i][1],'K')
        bestch=[99,-1]
        for i in range(len(memory)):
            if(memory[i][0]=='F'):
                if(memory[i][1]-newP<bestch[0]):
                    bestch[0]=memory[i][1]-newP
                    bestch[1]=memory[i][2]
        print(bestch)
        for i in range(len(memory)):
            if(memory[i][0]=='F'):
                if(memory[i][2]==bestch[1]):
                    if(bestch[0]==0):
                        memory[i][0]='P'
                        memory[i][2]=4
                        break
                    elif(bestch[0]>0):
                        tempspace = memory[i][1]-newP
                        tempcount = memory[i][2]
                        memory.pop(i)
                        memory.insert(i,['F',tempspace,tempcount])
                        memory.insert(i,['P',newP,4])
                        break
        print("After:\n")
        for i in range(len(memory)):
            if(memory[i][0]=='P'):
                print("Process P",memory[i][2],": ",memory[i][1],'K')
            elif(memory[i][0]=='F'):
                print("Free Space ",memory[i][2],": ",memory[i][1],'K')

    if(ch==3):
        print("Worst Fit Output")
        memory=mem.copy()
        print("Before : \n")
        for i in range(len(memory)):
            if(memory[i][0]=='P'):
                print("Process P",memory[i][2],": ",memory[i][1],'K')
            elif(memory[i][0]=='F'):
                print("Free Space ",memory[i][2],": ",memory[i][1],'K')
        bestch=[-1,-1]
        for i in range(len(memory)):
            if(memory[i][0]=='F'):
                if(memory[i][1]-newP>bestch[0]):
                    bestch[0]=memory[i][1]-newP
                    bestch[1]=memory[i][2]
        print(bestch)
        for i in range(len(memory)):
            if(memory[i][0]=='F'):
                if(memory[i][2]==bestch[1]):
                    if(bestch[0]==0):
                        memory[i][0]='P'
                        memory[i][2]=4
                        break
                    elif(bestch[0]>0):
                        tempspace = memory[i][1]-newP
                        tempcount = memory[i][2]
                        memory.pop(i)
                        memory.insert(i,['F',tempspace,tempcount])
                        memory.insert(i,['P',newP,4])
                        break
        print("After:\n")
        for i in range(len(memory)):
            if(memory[i][0]=='P'):
                print("Process P",memory[i][2],": ",memory[i][1],'K')
            elif(memory[i][0]=='F'):
                print("Free Space ",memory[i][2],": ",memory[i][1],'K')

    if(ch==4):
        print("Next Fit Output")
        memory=mem.copy()
        print("Before : \n")
        for i in range(len(memory)):
            if(memory[i][0]=='P'):
                print("Process P",memory[i][2],": ",memory[i][1],'K')
            elif(memory[i][0]=='F'):
                print("Free Space ",memory[i][2],": ",memory[i][1],'K')
        if(memory[len(memory)-1][0]=='F'):
            if(memory[i][1]-newP>0):
                tempspace = memory[i][1]-newP
                tempcount = memory[i][2]
                memory.pop(i)
                memory.insert(i,['F',tempspace,tempcount])
                memory.insert(i,['P',newP,4])
            elif(memory[i][1]-newP==0):
                memory[i][0]='P'
                memory[i][2]=4
        else:
            for i in range(len(memory)):
                if(memory[i][0]=='F'):
                    if(memory[i][1]-newP>0):
                        tempspace = memory[i][1]-newP
                        tempcount = memory[i][2]
                        memory.pop(i)
                        memory.insert(i,['F',tempspace,tempcount])
                        memory.insert(i,['P',newP,4])
                        break
                    elif(memory[i][1]-newP==0):
                        memory[i][0]='P'
                        memory[i][2]=4
                        break
        
        print("After:\n")
        for i in range(len(memory)):
            if(memory[i][0]=='P'):
                print("Process P",memory[i][2],": ",memory[i][1],'K')
            elif(memory[i][0]=='F'):
                print("Free Space ",memory[i][2],": ",memory[i][1],'K')

    ch = int(input("1. First Fit\n2. Best Fit\n3. Worst Fit\n4. Next Fit\n\nEnter your choice: "))

    
