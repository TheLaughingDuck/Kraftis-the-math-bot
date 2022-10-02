import math


def func_interpreter(func_name, input):
    print(func_name, str(input))
    # Trigonometric
    if func_name == "sin":
        return math.sin(input)
    if func_name == "cos":
        return math.cos(input)
    if func_name == "tan":
        return math.tan(input)
    
    # Others
    if func_name == "factorial":
        return math.factorial(input)
    if func_name == "abs":
        return math.fabs(input)
    if func_name == "sqrt":
        return math.sqrt(input)
    if func_name == "exp":
        return math.exp(input)
    if func_name == "gamma":
        return math.gamma(input)
    
    return("Unknown function specified")
    
