import csv
from tempfile import NamedTemporaryFile
import shutil 

class student():

    points= []
    first=[]
    last=[]
    full_name=[]

    def __init__(self,status,n1,n2,p, std_data,num_of_std,name):
        self.status = status
        self.n1 = n1
        self.n2 = n2
        self.p = p
        self.std_data=std_data
        self.num_of_std = len(self.full_name)
        self.name= name

    @classmethod
    def get_std_data(cls):

        while True:

            status = input("enter \'ok\' to fill in student data or \'exit\' to stop: ").capitalize()
            if status =="Ok":
                n1 = input("enter student first name:").capitalize()
                n2 = input("enter student last name:").capitalize()
                p = input("enter points optained by student:")
                try:
                    p.isdigit()
                except ValueError:
                    print('only numbers are accepted')
                if n1 == " " or n2 ==" ":
                    raise ValueError('Please enter a valid name')
                else:
                    cls.points.append(p)
                    cls.points = [int(i) for i in cls.points]
                    cls.first.append(n1)
                    cls.last.append(n2)
                    cls.full_name = list(map(lambda i,j: i + " "+ j,cls.first, cls.last))
                    cls.std_data = dict(zip(cls.full_name,cls.points))
                    cls.std_data = dict(sorted(cls.std_data.items()))
            else:
                break
        return cls.std_data

def create_file():
    #creates a new file and start filling it withthe result of the dict from the class
    f = input('Enter the file name with the extension .csv : ')
    with open (f , 'w', newline="") as file_name:
        w = csv.writer(file_name)
        w.writerow(['Student Name', 'Student Grade'])
        for key, value in student.std_data.items():
            w.writerow([key,value])
    return file_name

def update_file_with_added_grade():
    #for an existing file : chose the student and add grades to thier existing grade
    f = input('Enter the file name with the extension .csv : ')
    temp_file = NamedTemporaryFile(mode= 'w' , delete=False)
    fields = ['Student Name', 'Student Grade']
    name=input('enter the name of student you want to add grades for: ').title()
    grade = int(input('Enter the grade you want to add: '))
    with open (f , 'r+') as csv_file, temp_file:
        reader = csv.DictReader(csv_file , fieldnames=fields)
        writer = csv.DictWriter(temp_file, fieldnames=fields,lineterminator='\r')
        
        for item in reader:
           
            
            # if item['Student Name'] == name:
            #     if item['Student Grade'] != 'Student Grade':
            #         item['Student Grade']=int(item['Student Grade'])
            #         student_grade=list(item.values())[1]
            #         item.update({'Student Grade':student_grade})
            #         item['Student Grade']+=grade
            #     break
                      
            if item['Student Name'] != name:
                print('This student does not exist !')
                choice= input('Do you want to add them? (y/n) >').capitalize()
                if choice == 'Y':
                    # item.update({'Student Name':name,'Student Grade':grade})
                    item.update([('Student Name',name),('Student Grade',grade)])
                    print(f'New student:{name} with grade:{grade} will be added')
                    print(item)
                    # item['Student Name']=name
                    # item['Student Grade']=grade
                    # break
                elif choice =='N':
                    print(item)
                    print('Exiting...')
                    # break
            print(item)

    #         writer.writerow(item)
    # shutil.move(temp_file.name , f)
#     # fix this function: if the name is not found: add the name with the grade   
    

def update_student_name():
    result = False
    f = input('Enter the file name with the extension .csv : ')
    temp_file = NamedTemporaryFile(mode= 'w' , delete=False)
    fields = ['Student Name', 'Student Grade']
    with open (f , 'r') as csv_file,temp_file:
        reader = csv.DictReader(csv_file)
        writer = csv.DictWriter(temp_file, fieldnames=fields, lineterminator='\r')
        writer.writeheader()
        while True:
            old_name = input('Enter the name you would like to update/correct: ').title()
            new_name = input('Enter the new name: ').title()
            for data in reader:
                if data['Student Name'] == old_name:
                    data.update({'Student Name':new_name})
                    print(f'({old_name}) has been updated to ({data["Student Name"]})')
                    result = True
                writer.writerow(data)
            if not result:
                print("This name is not in the file. Please enter a valid name")
            else:
                break
    shutil.move(temp_file.name , f)

      




#function call

# #those  are working....
# std = student.get_std_data()
# print(student.std_data, type(student.std_data))
update_file_with_added_grade()
#create_file()
#update_student_name()

#\\\\\\opening files and checking if theyc can be opened could be in a class//////