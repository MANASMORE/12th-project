#Importing Required Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Linking csv file to python
df=pd.read_csv('Main\\pokedexfinal.csv')

#Creating a function to add a Pokemon
def add():
    while True:
        ask=int(input("Do you want to enter multiple pokemons?: \n"'''Press 1 for Yes, Press 2 for No'''))
        if ask==1:
            ask2=int(input('How many pokemons do you want to enter?: \n'))
            for i in range(0,ask2):
                n=str(input('Enter the name of pokemon: \n'))
                t1=str(input("Enter Primary Type of Pokemon: \n"'''Please enter from the following -['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic','steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal']'''))
                while t1 not in df.type1.unique():
                    print('Please Enter correct Primary Type')
                    t1=str(input("Enter Primary Type of Pokemon: \n"))
                t2=str(input("Enter Secondary Type of Pokemon: \n"'''Please enter from the following -['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic','steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal','none']'''))
                while t2 not in ['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic', 'steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal','none']:
                    print('Please Enter correct Secondary Type')
                    t2=str(input("Enter Primary Type of Pokemon: \n"))
                if t2=='none':
                    t2=np.NaN
                gen=int(input('Enter the Generation of your Pokemon: \n'))
                h=int(input('Height(in metres): \n'))
                w=int(input('Weight(in kilograms): \n'))
                l=str(input('Legendary(yes/no): \n'))
                p_no=len(df.index)+1
                df.loc[len(df.index)]=[p_no,n,t1.lower(),t2,gen,h,w,l]
                break
        elif ask==2:
            n=str(input('Enter the name of pokemon: \n'))
            t1=str(input("Enter Primary Type of Pokemon: \n"'''Please enter from the following -['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic','steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal']'''))
            while t1 not in ['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic', 'steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal','none']:
                print('Please Enter correct Primary Type')
                t1=str(input("Enter Primary Type of Pokemon: \n"))
            t2=str(input("Enter Secondary Type of Pokemon: \n"'''Please enter from the following -['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic','steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal','none']'''))
            while t2 not in ['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic', 'steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal','none']:
                print('Please Enter correct Secondary Type')
                t2=str(input("Enter Secondary Type of Pokemon: \n"))
            if t2=='none':
                t2=np.NaN
            gen=int(input('Enter the Generation of your Pokemon: \n'))
            h=int(input('Height(in metres): \n'))
            w=int(input('Weight(in kilograms): \n'))
            l=str(input('Legendary(yes/no): \n'))
            p_no=len(df.index)+1
            df.loc[len(df.index)]=[p_no,n,t1.lower(),t2,gen,h,w,l]
            break
        else:
            print('Please enter valid input')

#Creating a function to search for a  Pokemon
def search():
    query1=int(input("Search Pokemon Using: \n"'''Press 1 for Pokedex No, Press 2 for Pokemon Name \n'''))
    if query1==1:
        pno=int(input('Enter Pokedex No: \n'))
        print(df.loc[[pno-1]])
    elif query1==2:
        nam=str(input('Enter Pokemon Name: \n'))
        print(df.loc[df['name']==nam])

#Creating a function to remove a Pokemon
def remove():
    query2=int(input("Remove Pokemon Using: \n"'''Press 1 for Pokedex No, Press 2 for Pokemon Name \n'''))
    if query2==1:
        pno1=int(input('Enter Pokedex No: \n'))
        a=df.drop([pno1-1],inplace=True)
        print(df)
    elif query2==2:
        nam1=str(input("Enter Pokemon Name: \n"))
        b=df.drop(df.index[df['name']==nam1],inplace=True)
        print(df)

#Creating a function to update a Pokemon
def update():
    query3=int(input('Want to update through Pokemon name(Press 1) or Pokedex No(Press 2): \n'))
    if query3==1:
        q4=str(input('Enter Pokemon Name: \n'))
        q5=df.index[df['name']==q4]
        q6=df.index.get_loc(q5[0])
        print(q5)
        query5=int(input("What do you want to Update?: \n"'''Press 1 for Secondary Type, Press 2 for height, Press 3 for weight'''))
        if query5==1:
            ty2=input("Enter the new Secondary type: \n"'''Please enter from the following -['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic','steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal','none']''')
            while ty2 not in ['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic','steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal','none']:
                print('Please Enter correct Secondary T')
                ty2=str(input("Enter Secondary Type of Pokemon: \n"))
            if ty2=='none':
                ty2=np.NaN
            df.at[q6,'type2']=ty2

        elif query5==2:
            h=int(input('Enter new height of Pokemon(in metres): \n'))

        elif query5==3:
            w=int(input('Enter new weight of Pokemon(in kilograms): \n'))

        else:
            print('Please Enter a Valid Input')

    elif query3==2:
        q7=int(input('Enter Pokedex No: \n'))
        query6=int(input("What do you want to Update?: \n"'''Press 1 for Secondary Type, Press 2 for height, Press 3 for weight'''))
        if query6==1:
            ty3=input("Enter the new Secondary type: \n"'''Please enter from the following -['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic','steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal','none']''')
            while ty2 not in ['poison', 'flying', 'dark', 'electric', 'ice', 'ground','fairy', 'grass', 'fighting', 'psychic','steel', 'fire', 'rock','water', 'dragon', 'ghost', 'bug', 'normal','none']:
                print('Please Enter correct Secondary T')
                ty2=str(input("Enter Secondary Type of Pokemon: \n"))
            if ty2=='none':
                ty2=np.NaN
            df.at[q7-1,'type2']=ty3

        elif query5==2:
            h=int(input('Enter new height of Pokemon(in metres): \n'))
            df.at[q7-1,'height_m']=h

        elif query5==3:
            w=int(input('Enter new weight of Pokemon(in kilograms): \n'))
            df.at[q7-1,'weight_kg']=w

        else:
            print('Please Enter a Valid Input')

    else:
        print('Please Enter a Valid Input')

#Creating a function for seeing the statistical data
def stat():
    kk=int(input('Press 1 for getting graph of Number of pokemons v/s Primary type. \n Press 2 for getting graph of Number of pokemons v/s Secondary type. \n Press 3 for getting graph of Number of pokemons v/s Legendary status. \n Press 4 for getting graph of Number of pokemons v/s Generation. \n'))
    offset=.4
    if kk==1:
        kk1=plt.hist(df['type1'],bins=18,ec='k',align='mid')
        plt.xlabel('Primary type')
        plt.ylabel('No.of Pokemons')
        plt.xticks(rotation=90)
        plt.xticks(kk1[1][0:] + offset)
        plt.show()

    elif kk==2:
        kk2=plt.hist(df['type2'].dropna(),bins=18,ec='k',align='mid')
        plt.xlabel('Secondary type')
        plt.ylabel('No.of Pokemons')
        plt.xticks(rotation=90)
        plt.xticks(kk2[1][0:] + offset)
        plt.show()

    elif kk==3:
        bins1=np.arange(3)-0.5
        kk3=plt.hist(df['is_legendary'],bins1,ec='k')
        plt.xlabel('Is the pokemon Legendary')
        plt.ylabel('No. of pokemons')
        plt.xticks(df['is_legendary'])
        plt.show()
    
    elif kk==4:
        bins=np.arange(10)-0.25
        d=plt.hist(df['generation'],bins,width=0.5,align='mid')
        plt.xlabel('Generation Number')
        plt.ylabel('No. of pokemons')
        plt.xticks(np.arange(8))
        plt.xlim([0, 8])
        plt.show()
    
    else:
        print('Please Enter Valid Input')
        pass


#Creating a loop for user to use the Pokedex
while True:
    query=int(input('What do you want to do?\n Press 1 for adding a Pokemon.\n Press 2 for searching a Pokemon.\n Press 3 for removing a Pokemon. \n Press 4 for updating a Pokemon. \n Press 5 to see graphs \n Press 0 to exit \n'))
    if query==1:
        add()
        z1=int(input('Do you want to Continue or Not:\n Press 1 to continue \n Press 2 to stop \n'))
        if z1==2:
            print('Thank you for using the Pokedex!!!!! \n')
            df.to_csv('Main\\pokedexfinal.csv',index=False)
            break
            
        elif z1==1:
            pass

        else:
            print('Please Enter a Valid Input')
            pass

    elif query==2:
        search()
        z2=int(input('Do you want to Continue or Not:\n Press 1 to continue \n Press 2 to stop \n'))
        if z2==2:
            print('Thank you for using the Pokedex!!!!! \n')
            df.to_csv('Main\\pokedexfinal.csv',index=False)
            break
            
        elif z2==1:
            pass
        
        else:
            print('Please Enter a Valid Input')
            pass

    elif query==3:
        remove()
        z3=int(input('Do you want to Continue or Not:\n Press 1 to continue \n Press 2 to stop \n'))
        if z3==2:
            print('Thank you for using the Pokedex!!!!! \n')
            df.to_csv('Main\\pokedexfinal.csv',index=False)
            break

        elif z3==1:
            pass
        
        else:
            print('Please Enter a Valid Input')
            pass

    elif query==4:
        update()
        z4=int(input('Do you want to Continue or Not:\n Press 1 to continue \n Press 2 to stop \n'))
        if z4==2:
            print('Thank you for using the Pokedex!!!!! \n')
            df.to_csv('Main\\pokedexfinal.csv',index=False)
            break

        elif z4==1:
            pass
        
        else:
            print('Please Enter a Valid Input')
            pass
            
    elif query==5:
        stat()
        z5=int(input('Do you want to Continue or Not:\n Press 1 to continue \n Press 2 to stop \n'))
        if z5==2:
            print('Thank you for using the Pokedex!!!!! \n')
            df.to_csv('Main\\pokedexfinal.csv',index=False)
            break

        elif z5==1:
            pass
        
        else:
            print('Please Enter a Valid Input')
            pass
    
    elif query==0:
        print('Thank you for using the Pokedex!!!!! \n')
        break

    else:
        print('Please Enter a Valid Input')
        pass
