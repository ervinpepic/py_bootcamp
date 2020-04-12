class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Custom appended..")
        return super().append(object)


list = TrackableList()
list.append("Ervin")

txt = Text("Ervin")
print(txt.duplicate())
