class Calculator:

    @staticmethod
    def add(*args):
        result = sum(args)
        return result

    @staticmethod
    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    @staticmethod
    def divide(*args):
        result = args[0] / args[1]
        for x in range(2, len(args)):
            result = result / args[x]
        return result

    @staticmethod
    def subtract(*args):
        result = args[0] - args[1]
        for x in range(2, len(args)):
            result = result - args[x]
        return result

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(1000, 2, 2, 2, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
