'''
If there is a bird, if its walking like a duck, quaking like a duck, swimming like a duck, that bird is a duck.
Means if the behaviour of the bird is matching with a duck, than that's a duck .
'''


class Duck():
    def talk(self):
        print('Quack, quack karo !')

class Human():
    def talk(self):
        print('Hi, hello!')

def call_talk(obj):
    obj.talk()

x = Duck()
call_talk(x)

x = Human()
call_talk(x)
