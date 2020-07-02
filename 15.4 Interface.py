from abc import ABC, abstractmethod

class Myclass(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass

class Oracle(Myclass):
    def connect(self):
        print('Connecting to oracle database')
    def disconnect(self):
        print('Disconnecting from oracle database')

class Sybase(Myclass):
    def connect(self):
        print('Connecting to Sybase database')
    def disconnect(self):
        print('Disconnecting from Sybase database')

class Database:
    str = input('Enter a database : ')
    classname = globals()[str]              # CONVERTING THE STRING INTO CLASSNAME
    x = classname()

    x.connect()
    x.disconnect()