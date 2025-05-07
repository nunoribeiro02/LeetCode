class Solution:
    def checkCollision(self, stack, a):
        if len(stack) == 0:
            stack.append(a)
        else:
            asterStack = stack.pop()
            stack.append(asterStack)
            if asterStack > 0 and asterStack == -a:
                stack.pop()
            if asterStack > 0 and a < 0:
                if asterStack + a < 0:
                    stack.pop()
                    self.checkCollision(stack, a)
            else:
                stack.append(a)
        return stack

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            stack = self.checkCollision(stack, a)

        return stack
