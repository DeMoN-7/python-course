class aa:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.b
    def __sub__(self,other):
        return self.x+self.x #just for practice
class ba:
    def __init__(self,b):
        self.b=b
    # def __add__(self,other):
    #     return self.x+other.x

a=aa("Ayush")
b=ba(" Singh")
print(a+b)

print(a-b)