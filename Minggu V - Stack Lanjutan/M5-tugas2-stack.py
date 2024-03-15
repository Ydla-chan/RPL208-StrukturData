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

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None


def check_parentheses(expression):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty():
                return False
            else:
                top = stack.pop()
                if opening_brackets.index(top) != closing_brackets.index(char):
                    return False

    return stack.is_empty()


def main():
    expressions = [
        "A + [ B * (C - D) - E] / F",
        "[A + B * (C - D)] - E / F",
        "[A + B * (C - D)} - E / F",
        "{ A + B * (C - D)] - E / F"
    ]

    for expression in expressions:
        print(expression)
        if check_parentheses(expression):
            print("BENAR")
        else:
            print("SALAH")


if __name__ == "__main__":
    main()
