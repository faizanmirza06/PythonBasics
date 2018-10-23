class Parent:
    def config(self):
        print("This is parent Class")

class Child(Parent):

    def childmsg(self):
        print("This is child class")

con=Parent()

ch=Child()
ch.config()
ch.childmsg()