
def My_Funk () :
    inp =''
    while inp.lower() != 'n':
        class Person :
            def __init__(self, name, lastName, age):
                self.name = name
                self.lastName = lastName
                self.age = age

            def showInfo(self):

                print(f'Name: {name}, Lastname: {lastName}, Age: {age}')

        name = str(input("Введіть ім'я: \t"))
        lastName = str(input("Введіть прізвище: \t"))
        age = int(input("Введідь вік: \t"))

        obj = Person(name, lastName, age)
        obj.showInfo()

        inp = input('Бажаєте продовжити? Y/N \t')
        if inp.lower() != 'y' and inp.lower() != 'n':
            print('Невірний символ!')
            break

My_Funk()