import doc
from doc import student, create_file

# user choices:
def user_choice():
    ans=False
    print("\nHi there !\n")

    while not ans:
        print('Please chose a number from the list of actions:\n')
        print('1. Create a new file.\n2. Update an existing file.\n3. Delete an existing file\n')
        res = int(input('Enter youe choice: '))

        if res == 1:
            student.get_std_data(), create_file()
        elif res == 3:
            doc.delete_file()
        elif res == 2:
            print('What do you want to update in the file?. Please choose from the list')
            print('A. Update a name.\nB. Change a grade.\nC. Add grades.\nD. Delete a name.')
            ch = input('Your choice: ').capitalize()
            if ch =='A':
                pass
            elif ch == 'B':
                pass
            elif ch=='C':
                doc.update_file_with_added_grade()
            elif ch == 'D':
                pass
            else:
                print('please enter a valid choice (a, b, or c)\n')
        else:
            print('Please enter a valid number (1 or 2 or 3)\n')
        a = input('Do you want to exit ? (y/n): \n').capitalize()
        if a == 'Y':
            ans = True
            break
        elif a=='N':
            ans = False
        else:
            print('Please enter a valid choice (y/n')


user_choice()