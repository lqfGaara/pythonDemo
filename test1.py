class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def test(self):
        
        print(self.age)
        print(self.name)


T = Test("stone", 12)

T.test()
