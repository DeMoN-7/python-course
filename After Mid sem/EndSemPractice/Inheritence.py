class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show_detail(self):
        print("Name",self.name)
        print("ID:",self.id)
class Manager(Employee):
    # def __init__(self):
    #     print("Aachaman ")
    def show_language(self):
        print("Hindi")
# e=Employee("Ayush",420)
# e.show_detail()
a=Manager("Ayush",32)
a.show_detail()
a.show_language()