from typing import Any


class Variable:
    def __init__(self, Name: str, Coefficient: int | float = 1, Power: int | float = 1) -> None:
        self._name = Name           # variable name
        self._coff = Coefficient    # coefficient
        self._pow = Power           # power of the variable
    
    def name(self) -> str:
        return self._name
    
    def coefficient(self) -> int | float:
        return self._coff
    
    def power(self) -> int | float:
        return self._pow
    
    def coff(self) -> int | float:
        return self._coff
    
    def pow(self) -> int | float:
        return self._pow
    
    def setCoefficient(self, coff: int | float) -> None:
        self._coff = coff
    
    def setPower(self, pow: int | float) -> None:
        self._pow = pow
    
    def setCoff(self, coff: int | float) -> None:
        self._coff = coff
    
    def setPow(self, pow: int | float) -> None:
        self._pow = pow
    
    def string(self) -> str:
        return self.__repr__()
    
    def isVar(self, v):
        return isinstance(v, Variable)
    
    def __repr__(self) -> str:
        if self._coff == 0:
            return '0'
        
        if self._pow == 0:
            return '1'
        
        return f"{self._coff if self._coff != 1 else ''}{self._name}" \
            f"{'^'+str(self._pow) if self._pow != 1 else ''}"
    
    def __add__(self, val):
        """ + or += operator """
        self._coff += val
        return self
    
    def __sub__(self, val):
        """ - or -= operator """
        self._coff -= val
        return self
    
    def __mul__(self, val):
        """ * or *= operator """
        self._coff -= val
        return self
    
    def __truediv__(self, val):
        """ / or /= operator """
        self._coff /= val
        return self
    
    def __floordiv__(self, val):
        """ // or //= operator """
        self._coff //= val
        return self
    
    def __mod__(self, val):
        """ % or %= operator """
        self._coff -= val
        return self
    
    def __pow__(self, val):
        """ ** or **= operator """
        self._pow *= val
        self._coff **= val
        return self
    
    def __radd__(self, val):
        """ Right Addition, eg: 10 + x """
        self.__add__(val)
        return self
    
    def __rsub__(self, val):
        """ Right Subtract, eg: 10 - x """
        self._coff = val - self._coff
        return self
    
    def __rmul__(self, val):
        """ Right Multiplication, eg: 10 * x """
        self.__mul__(val)
        return self
    
    def __rtruediv__(self, val):
        """ Right Division,  eg: 10 / x """
        self._coff = val / self._coff
        return self

    def __rfloordiv__(self, val):
        """ Right Floordiv """
        self._coff = val // self._coff
        return self

    def __rmod__(self, val):
        """ Right Modulo """
        self._coff = val % self._coff
        return self
    
    def differentiate(self):
        if self._coff == 0 or self._pow == 0: return 0
        
        self._coff *= self._pow
        self._pow -= 1
        return self
    
    def integrate(self):
        if self._coff == 0: return 0
        
        self._pow += 1
        self._coff /= self._pow
        
        return self


if __name__ == '__main__':
    x = Variable('x')
    y = Variable('y')
    
    # Addition
    x += 2
    print(x)
    
    # Subtraction
    x -= 5
    print(x)
    
    # Power
    x **= 2
    print(x)
    x **= 2
    print(x)
    
    x = x.differentiate()
    print(x)
    
    x = x.integrate()
    print(x)
    
    x.setPow(1)
    x.setCoff(1)
    print(x, end='\t')
    print(x.differentiate(), end='\t')
    print(x.integrate(), end='\n')
    print(x.differentiate(), end='\t')
    print(x.differentiate(), end='\t')
    print(x.differentiate(), end='\n')
    
    # x += y
    # print(x)
    