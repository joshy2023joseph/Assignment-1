#Joshy Joseph - Mini Project on Interactive Dictionary using Python

import json
import time, datetime
import re

#Dictionary object to store the openned JASON file
data = json.load(open("dictionary.json","r"))

#Function to search user input in Dictionary file
def translate(user_input):
    user_input = user_input.lower()
    count=0
    match=True
    for i,j in data.items():
         if i == user_input:
             print('\n')
             print(i,':\n')
             splt = re.split(r'\d',j)
             splt = list(filter(None, splt))
             h=0
             for i in splt:
                 print(h+1,i,'\n')
                 h +=1
             count +=1
         elif i != user_input:
             match = False
    if match == False and count == False:
        print('\nNo match found in the Dictionary')
    print('\nDo you want search words starting with:\'',user_input,'\'?')
    print('Enter your choice,(Y/N) : ', end = '')
    mat = input()
    usr_in = mat.lower()
    if usr_in == 'y' or usr_in == 'yes':
        match1 = False
        for i,j in data.items():
            if i.startswith(user_input) == True and i != user_input:
                match1 = True
                #Prints the search keys
                print(i,':\n')
                #splits the result-values according to the listed number inside file
                splt1 = re.split(r'\d',j)
                #removes the blank elements from the list
                splt1 = list(filter(None, splt1))
                h=0
                for i in splt1:
                    print(h+1,i,'\n')
                    h +=1
        if match1 == False:
            print('\nNo item found in Dictionary starting with word\'',user_input,'\'')
    else:
        return

print('\t\t\tWelcome To Interactive English Dictionary\t\t\t')
print('\t\t\t^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\t\t\t')
#Prints current date and time
print('\t\t\t\t',time.ctime())
print('\n')
word = input("ENTER SEARCH WORD: ")
translate(word)
preference = 'Y'
while preference == 'Y' or preference == 'y':
    print('\nSearch another word in Dictionary?  ', end='')
    p1 =input(" Type Y/N: ")
    p1 = p1.lower()
    if p1 == 'n' or p1 == 'no':
        preference = None
        break
    elif p1 == 'y' or p1 == 'yes' or p1 == '\r':
        word = input("\nENTER SEARCH WORD: ")
        translate(word)
        preference ='y'
    else:
        print('\nEnter a valid option, \'Y\' for Yes, \'N\' for No')
        preference ='y'
exit()            





