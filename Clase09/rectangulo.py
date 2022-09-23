# -*- coding: utf-8 -*-
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)
  
    
class Rectangulo(Punto):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def base(self):
        base = abs(self.x - self.y)
        return base
    
    def altura(self):
        altura = abs(self.x - self.y)
        return altura
    
    def area(self):
        return Rectangulo(self.base() * self.altura())
    
    

ul = Punto(0,2)
lr = Punto(1,0)
ll = Punto(0,0)
ur = Punto(1,2)
rect1 = Rectangulo(ul,lr)
rect2 = Rectangulo(ll,ur)
