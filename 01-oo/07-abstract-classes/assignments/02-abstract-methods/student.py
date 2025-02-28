from abc import ABC, abstractmethod


class A(ABC):
    def a(self):
        self.b()
        
    @abstractmethod
    def b(self):
        self.c()

    def e(self):
        self.c()
    
    @abstractmethod
    def c(self):
        pass


class B(A):
    def b(self):
        self.a()

    def c(self):
        self.e()


class C(B):
    def f(self):
        pass


class D(A):
    def b(self):
        self.f()

    @abstractmethod
    def f(self):
        self.a()


class E(D):
    def c(self):
        self.a()

    def f(self):
        self.e()

    def g(self):
        self.f()


class F(ABC):
    def a(self):
        self.b()
        self.f()

    @abstractmethod
    def b(self):
        self.a()
    
    @abstractmethod
    def f(self):
        pass
