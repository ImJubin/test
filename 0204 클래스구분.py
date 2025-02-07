class A:
    def __init__(self):
        super().__init__()
        self.value = "나는 A값이야"
        print("A생성됨")

    def goodmorning(self):
        print("A의 goodmorning")

class B:
    def __init__(self):
        super().__init__()
        self.value = "나는 B값이야"
        print("B생성됨")    

    def goodmorning(self):
        print("B의 goodmorning")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C생성됨")

c = C()
c.goodmorning()
