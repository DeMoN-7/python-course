class  person:
    def __init__(self,n,o):
        print("Hello")
        self.name=n
        self.occ=o
        
    name = "Ayush"
    occ= "Developer"
    def info(self):
        print(self.name,"is a ",self.occ)

a=person("Ramu","Sweeper")
# a.name="Divya"
# a.occ="HR"
a.info()