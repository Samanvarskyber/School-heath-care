import Student
import Tools


arr_classA=[]
arr_classB=[]

def get_info():
  std=Student.Student()
  std.name=input('\nPlease enter your name :\t')
  std.birth_year=int(input('\nPlease enter your birth year :\t'))
  std.height=int(input('\nPlease enter your height :\t'))
  std.weight=int(input('\nPlease enter your weight :\t'))
  return std

print('\n-----------------------WELCOME TO SCHOOL HEALTH CARE------------------------\n')
howmany=int(input('\nHow many student in each class :\t'))
print('\n---------------------entry for class A-------------------------\n')
for i in range(howmany):
  arr_classA.append(get_info())


print('\n---------------------entry for class B-------------------------\n')
for i in range(howmany):
  arr_classB.append(get_info())


print('\n---------------------show data class A-------------------------\n')
for i in range(howmany):
  print(arr_classA[i].display())
   


print('\n---------------------show data class B-------------------------\n')
for i in range(howmany):
  print(arr_classB[i].display())


print('\n---------------------show average class A-------------------------\n')
Tools.Tool.Ave_height(arr_classA)
Tools.Tool.Ave_weight(arr_classA)
Tools.Tool.Ave_age(arr_classA)
Dict_arr_classA=Tools.Tool.dict_ave.copy()

for key,value in Dict_arr_classA.items():
    print(key,':',value)

print('\n---------------------show average class B-------------------------\n')

Tools.Tool.Ave_height(arr_classB)
Tools.Tool.Ave_weight(arr_classB)
Tools.Tool.Ave_age(arr_classB)
Dict_arr_classB=Tools.Tool.dict_ave.copy()#point: az dataye avali estefade nshe

for key,value in Dict_arr_classB.items():
    print(key,':',value)

print('\n------------------------SHOW COMPARE RESULT------------------\n')

if Dict_arr_classA['aveheight'] > Dict_arr_classB['aveheight']:
    print('class A is bigger.\n')
elif Dict_arr_classA['aveheight'] < Dict_arr_classB['aveheight']: 
    print('class B is bigger.\n')  
else:
    print('weight')

    if Dict_arr_classA['aveweight'] > Dict_arr_classB['aveweight']: 
        print('class A is bigger.\n')
    elif Dict_arr_classA['aveweight'] < Dict_arr_classB['aveweight']: 
        print('class B is bigger.\n')
    else:
        print('age')
        if Dict_arr_classA['aveage'] > Dict_arr_classB['aveage']: 
          print('class A is bigger.\n')
        elif Dict_arr_classA['aveage'] < Dict_arr_classB['aveage']: 
          print('class B is bigger.\n')
        else:
            print('Same  :/ \n')  
#einjaro nemikhone

