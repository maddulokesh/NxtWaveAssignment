while(1):
    s=input('Waht do you want do to now Quit or Continue : ')
    if(s=='Quit'):
        break
    else:
        a=[[1,'Front End','Front End Task','Completed','23-03-2025','23-03-2025'],[2,'BAck End','Back End Task','In Progress','23-03-2025','23-03-2025'],[3,'Full Stack','Full Stack Task','In Progress','23-03-2025','23-03-2025'],[4,'Devops','Devops Task','In Progress','23-03-2025','23-03-2025'],[5,'Cyber Security','Cyber Security Task','Completed','23-03-2025','23-03-2025']]
        x=input('Enter Request Type (Foe Ex:Get, Post, Put, Delete) : ')
        if(x=='Get'):
            y=input('Enter ID or All : ')
            if(y=='All'):
                print(a)
            else:
                print(a[int(y)-1])
        elif(x=='Post'):
            z=input("Enter the data in the format of Id space Task space Description space Status space Due date : ")
            b=list(z.split())
            b[0]=int(b[0])
            a.append(b)
        elif(x=='Put'):
            p=input('Enter the data which you want to edit in the format of Id space Task space Description space Status space Due date : ')
            b=list(z.split())
            b[0]=int(b[0])
            a[b[0]-1]=b
        else:
            p=int(input('Enter Id which you want to delete : '))
            a.remove(a[p-1])
        print('Data Updated!')
