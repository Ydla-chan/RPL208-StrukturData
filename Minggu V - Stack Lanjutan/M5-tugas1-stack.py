class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


def check_parentheses(expression):
    stack = Stack()

    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop()

    return stack.is_empty()


def main():
    expressions = [
        "A + B *  C - D / E",
        "A + B * (C - D) / E",
        "(A + B) * (C - D) / E",
        "(A + B * (C - D) / E)",
        "(A + B * (C - D) / E",
        "(A + B) * C - D) / E",
        ")A + B * (C - D / E",
        "(A + B ( * (C - D) / E",
        "(A + B) * )C - D) / E"
    ]

    for expression in expressions:
        print(expression)
        if check_parentheses(expression):
            print("BENAR")
        else:
            print("SALAH")


if __name__ == "__main__":
    main()
