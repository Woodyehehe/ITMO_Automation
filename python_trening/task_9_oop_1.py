class Input:
    def __init__(self, Loc, text):
        self.Loc = Loc
        self.text = text

search = Input('Поиск', '/search')

print(search.Loc)

class Button:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search1 = Button('Знак', '/sign')

print(search1.loc)

class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search2 = Title ('Заголовок', '/title')

print(search2.loc)

class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search3 = Link ('Ссылка', '/link')

print(search3.loc)

