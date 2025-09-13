class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        
    def pop(self):
        return self.__items.pop()
        
    def peek(self):
        return self.__items[-1]
        
    def size(self):
        return len(self.__items)
    
    def is_empty(self):
        return len(self.__items) == 0


def is_correct_bracket_seq(s):
    stack = Stack()
    brackets_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty() or stack.peek() != brackets_map[char]:
                return False
            stack.pop()
    
    return stack.is_empty()


sequence = input()
print(is_correct_bracket_seq(sequence))