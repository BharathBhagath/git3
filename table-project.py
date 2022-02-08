print('s = single table\n d = diff table')
option=input('please choose option :')
if option == 's':
    table=int(input('please chooose the table :'))
    table_range=int(input('please chooode table range :'))
    for i in range(1,table_range):
        print(table,'*',i,'=',table*i)
elif option == 'd':
    table_from=int(input('please enter table from :'))
    table_to = int(input('please enter table to :'))
    table_range=int(input('please enter table tange :'))
    for i in range(table_from,table_to):
        for j in range(1,table_range):
            print(i,'*',j,'=',i*j)
        print('*'*10)
            
else:
    print('invalid option selected')

       
