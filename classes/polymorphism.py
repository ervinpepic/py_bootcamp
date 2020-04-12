from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Drawing a text box...")


class DropDownList(UIControl): #we can remove this inheritance in the parentheses, 
                                #beacuse python is da Dynamic typing language...
                                # that is called DuckTyping
    def draw(self):
        print("Drawing a drop down list...")


def draw(uiControlObjects):  # here we get polymorphism, which is the object possibilities to behave differently in diffrerent cases
    for uiControlObject in uiControlObjects:
        uiControlObject.draw()


ddl = DropDownList()
tbx = TextBox()


draw([ddl, tbx])
