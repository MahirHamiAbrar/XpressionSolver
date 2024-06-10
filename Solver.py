from typing import Callable
from Utils.Stack import Stack


class ExpressionSolver:
    
    StepsReturnAsList = 0
    StepsReturnAsStream = 1
    
    def __init__(self) -> None:
        
        # PEDMAS PRECEDENCE
        self._precedence = {
            '(' : 10,    # highest precedence
            ')' : 10,
            '^' : 9,
            '/' : 8,
            '*' : 7,
            '+' : 6,
            '-' : 5     # lowest precedence
        }
        
        self._streamer = None
    
    def stream(self, *args, **kwargs) -> None:
        if callable(self._streamer):
            self._streamer.__call__(*args, **kwargs)
    
    def setStreamerFunction(self, func: Callable) -> None:
        self._streamer = func
    
    def _is_operator(self, c: chr) -> bool:
        return (self._precedence.get(c) is not None)
    
    def toInfix(self, expression: str) -> list:
        # remove all the whitespaces
        expression = expression.replace(' ', '')
        
        item = ''       # temporarily store an item here
        infix = []      # the infix notation
        
        for char in expression:
            
            # add every character to the current item variable
            # until an operator is found
            if not self._is_operator(char):
                item += char
            
            # if an operator is found, add the item and the
            # operator to the infix list, and reset the 
            # item variable
            else:
                # check and skip black items/characters
                if item: infix.append(item)
                if char: infix.append(char)
                
                # reset item variable
                item = ''
            
        # add the remaining item variable to the infix list
        if item: infix.append(item)
        
        return infix
    
    def toPostfix(self, infix: list) -> list:
        postfix = []        # postfix list
        stack = Stack()
        
        # push parenthesis
        # stack.push('(')
        infix.insert(0, '(')
        infix.append(')')
        
        ifxeqn = infix.copy()
        brktStack = Stack()
        
        # now go through all the items in the infix notation
        for idx, item in enumerate(infix):
            
            # check if current item is an operator
            if self._is_operator(item):
                
                # push the left bracket if found one
                if item == '(':
                    brkt = [item, idx]
                    stack.push(brkt.copy())
                    brktStack.push(brkt[1])
                
                # if right bracket is encountered,
                # pop items and push them in the postfix notation list
                # until a left bracket found
                elif item == ')':
                    while stack.top()[0] != '(':
                        postfix.append(stack.pop())
                    
                    postfix[postfix.__len__() - 1].append([brktStack.pop(), idx])
                    stack.pop()         # pop the left parenthesis ['(']                    
                
                # for other operators, pop until they have equal or higher
                # precedence than the current operator and put them in the
                # postfix notation list
                else:
                    while (
                        stack.isNotEmpty() and 
                        stack.top()[0] != '(' and 
                        self._precedence[stack.top()[0]] >= self._precedence[item]
                        ):
                        
                        postfix.append(stack.pop())
                    
                    stack.push([item, idx])
            
            # push the current item if it's not an operator.
            # Not an operator indicates that, it's a numeric value (integer or float)
            else:
                postfix.append([item, idx])
        
        return ifxeqn, postfix
    
    def calculate(self, a: int | float, b: int | float, operator: chr) -> float:
        """Returns the output of: b operator a

        Args:
            a (int | float): Any Number
            b (int | float): Any Number
            operator (chr):  Operator in Character form

        Returns:
            int | float: The result of the calculation
        """
        if operator == '+': return b + a
        elif operator == '-': return b - a
        elif operator == '*': return b * a
        elif operator == '/': return b / a
        elif operator == '^': return b ** a
    
    def evaluate(
        self,
        ifxeqn: list,
        postfix: list,
        steps_return: int = StepsReturnAsList
    ) -> float:
        
        stack = Stack()     # create a stack object
        
        stepsList = []
                
        # iterate over all items in the postfix list
        for item in postfix:
            
            # check if the item is an operator
            # On encountering an operator, pop two top elements from the stack
            # and evaluate their result according to the encountered operator.
            if self._is_operator(item[0]):
                
                # pop top tow items from stack
                A = stack.pop()     # top-most item
                B = stack.pop()     # 2nd top-most item
                
                # calculate the value of B <operator> A
                value = self.calculate(A[0], B[0], item[0])
                
                ifxeqn[A[1]] = value
                ifxeqn[B[1]] = None
                ifxeqn[item[1]] = None
                
                if len(item) == 3:
                    idx1, idx2 = item[2]
                    ifxeqn[idx1] = ifxeqn[idx2] = None
                
                # push the value to the stack
                stack.push([value, A[1]])
                
                step = " ".join(
                        str(v)
                        for v in ifxeqn[1:len(ifxeqn)-1]
                        if v is not None
                    )
                
                if steps_return == self.StepsReturnAsList:
                    stepsList.append(step)
                else:
                    self.stream(step)
                            
            # If the item is not an operator, then simply
            # put it in the stack for later use.
            else:
                stack.push([float(item[0]), item[1]])
        
        # After all iterations are done, stack will be left with only
        # ONE value. That's the result we are looking for. Return it.
        return [stack.pop()[0], stepsList]
    
    def solve(self, expression: str, steps_return: int = StepsReturnAsList) -> float:
        # convert the expression to infix notation
        infix = self.toInfix(expression)
        # convert the infix notation to postfix notation
        ifxeqn, postfix = self.toPostfix(infix)
        # evaluate the postfix notation
        result = self.evaluate(ifxeqn, postfix, steps_return)
        
        # return the result
        return result


if __name__ == '__main__':
    expressions = [
        "5 * ( 6 + 2 ) - 12 / 4",   # [5, 6, 2, '+', '*', 12, 4, '/', '-'],
        "A + ( B * C - ( D / E ^ F ) * G ) * H",
        "10 + ( 20 * 2 - ( 54 / 3 ^ 3 ) * 2 ) * 5",
        "5 + (6 * 2) + 3"
    ]
    
    # expression = expressions[0].replace(' ', '')
    expression = expressions[2]
    print(f"Expression\t= {expression}")
    
    solver = ExpressionSolver()
    infix = solver.toInfix(expression)
    ifxeqn, postfix = solver.toPostfix(infix)
    solve = solver.evaluate(ifxeqn, postfix)
    solution = ''
    # solution = solver.solve(expression)
    
    print(f"Solution = {solve[0]}")
    # print(f"Solution = {solve[0]}\n{infix = }\n{postfix = }")
    
    # print(f"{expression = }\n{infix = }\n{postfix = }\n{solve = }\n{solution = }")
