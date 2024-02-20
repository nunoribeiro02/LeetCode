class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        
        for n in tokens:
            if (n in ("+", "-", "*", "/")):
                x = stack.pop()
                y = stack.pop()

                match n:
                    case "+":
                        stack.append(x + y)
                    case "-":
                        stack.append(y - x)
                    case "*":
                        stack.append(x * y)
                    case "/":
                        stack.append(int(y / x))
            else:
                stack.append(int(n))

        return stack.pop()

"""
Space: O(n)
Time: O(2n) = O(n), n is the size of the initial array
"""