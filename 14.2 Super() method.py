'''
super().__init__()              # CALL SUPER CLASS CONSTRUCTOR
super().__init__(Arguments)     # CALL SUPER CLASS CONST AND PASS ARGS
super().method()                # CALL SUPER CLASS METHOD
'''

class A:

    def __init__(self):
        print('in A Init')
       

    def feature1(self):
        print('Feature 1-A ')

    def feature2(self):
        print('Feature 2 working')


class B:
    def __init__(self):
        print('in B Init')
        print('- - - - -')

    def feature1(self):
        print('Feature 1-B ')

    def feature4(self):
        print('Feature 2 working')

class C(A,B):
    def __init__(self):
        super().__init__()    #acc to MRO (Method Resolution Order) it will take left to right
        print('in C Init')


#a1 = A()
#a1 = B()
a1 = C()
a1.feature1()
print('---------------')
print()
