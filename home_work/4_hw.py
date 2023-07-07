class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        if self.width >= 1 and self.height >= 1:
            print(self.width * self.height)
        else:
            print('Введите данные')

    def perimetr(self):
        if self.width >= 1 and self.height >= 1:
            print((self.width + self.height) * 2)
        else:
             print('Введите данные')

wh1 = Rectangle(2, 5)
wh2 = Rectangle(0, 1)
wh3 = Rectangle(8,7)
wh1.square()
wh2.square()
wh3.square()
wh1.perimetr()
wh2.perimetr()
wh3.perimetr()

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addiction(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

number = Math(7, 14)
number.addiction()
number.multiplication()
number.division()
number.subtraction()

print(f'Сумма = {number.addiction()}')
print(f'Произведение = {number.multiplication()}')
print(f'Частное = {number.division()}')
print(f'Разность = {number.subtraction()}')

class SecondButtons:
    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return f'Клик по кнопке {self.text}'

button1 = SecondButtons('Text Box', 'Кнопка', '')
button2 = SecondButtons('Check Box', 'Кнопка', '')
button3 = SecondButtons('Radio Button', 'Кнопка', '')
button4 = SecondButtons('Web Tables', 'Кнопка', '')
button5 = SecondButtons('Buttons', 'Кнопка', '')
button6 = SecondButtons('Links', 'Кнопка', '')
button7 = SecondButtons('Broken Links - Images', 'Кнопка', '')
button8 = SecondButtons('Upload and Download', 'Кнопка', '')
button9 = SecondButtons('Dynamic Properties', 'Кнопка', '')
button10 = SecondButtons('Practice Form', 'Кнопка', '')
button11 = SecondButtons('Browser Windows', 'Кнопка', '')
button12 = SecondButtons('Alerts', 'Кнопка', '')
button13 = SecondButtons('Frames', 'Кнопка', '')
button14 = SecondButtons('Nested Frames', 'Кнопка', '')
button15 = SecondButtons('Modal Dialogs', 'Кнопка', '')
button16 = SecondButtons('Accordian', 'Кнопка', '')
button17 = SecondButtons('Auto Complete', 'Кнопка', '')
button18 = SecondButtons('Date Picker', 'Кнопка', '')
button19 = SecondButtons('Slider', 'Кнопка', '')
button20 = SecondButtons('Progress Bar', 'Кнопка', '')
button21 = SecondButtons('Tabs', 'Кнопка', '')
button22 = SecondButtons('Tool Tips', 'Кнопка', '')
button23 = SecondButtons('Menu', 'Кнопка', '')
button24 = SecondButtons('Select Menu', 'Кнопка', '')
button25 = SecondButtons('Sortable', 'Кнопка', '')
button26 = SecondButtons('Selectable', 'Кнопка', '')
button27 = SecondButtons('Resizeble', 'Кнопка', '')
button28 = SecondButtons('Droppable', 'Кнопка', '')
button29 = SecondButtons('Dragabble', 'Кнопка', '')
button30 = SecondButtons('Login', 'Кнопка', '')
button31 = SecondButtons('Book Store', 'Кнопка', '')
button32 = SecondButtons('Profile', 'Кнопка', '')
button33 = SecondButtons('Book Store API', 'Кнопка', '')

print(button1.text)
print(button2.text)
print(button3.text)
print(button4.text)
print(button5.text)
print(button6.text)
print(button7.text)
print(button8.text)
print(button9.text)
print(button10.text)
print(button11.text)
print(button12.text)
print(button13.text)
print(button14.text)
print(button15.text)
print(button16.text)
print(button17.text)
print(button18.text)
print(button19.text)
print(button20.text)
print(button21.text)
print(button22.text)
print(button23.text)
print(button24.text)
print(button25.text)
print(button26.text)
print(button27.text)
print(button28.text)
print(button29.text)
print(button30.text)
print(button31.text)
print(button32.text)
print(button33.text)

print(button1.click())
print(button2.click())
print(button3.click())
print(button4.click())
print(button5.click())
print(button6.click())
print(button7.click())
print(button8.click())
print(button9.click())
print(button10.click())
print(button11.click())
print(button12.click())
print(button13.click())
print(button14.click())
print(button15.click())
print(button16.click())
print(button17.click())
print(button18.click())
print(button19.click())
print(button20.click())
print(button21.click())
print(button22.click())
print(button23.click())
print(button24.click())
print(button25.click())
print(button26.click())
print(button27.click())
print(button28.click())
print(button29.click())
print(button30.click())
print(button31.click())
print(button32.click())
print(button33.click())

