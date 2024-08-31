def My_Func():
    inp = ''

    while inp.lower() != 'n':
        class Rectangle:

            def __init__(self, width, height):
                self.width = width
                self.height = height

            def showInfo(self):

                print(f'Площа прямокутника дорівнює: {width*height}')
                print(f'Периметр прямокутника дорівнює: {(width + height) * 2}')
                print(f'Ширина: {width}, Висота: {height}')

        width = float(input("Введіть ширину прямокутника: \t"))
        height = float(input("Введіть висоту прямокутника: \t"))

        obj = Rectangle(width, height)
        obj.showInfo()

        inp = input('Бажаєте продовжити? Y/N \t')
        if inp.lower() != 'y' and inp.lower() != 'n':
            print('Невірний символ!')
            break

My_Func()

