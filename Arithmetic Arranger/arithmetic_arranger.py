def arithmetic_arranger(problems, second=False):

    #check the limit of problem is five

    if len(problems) > 5:
        return "Error: Too many problems."

    top = ""
    bottom = ""
    dash = ""
    result = ""

    for i in problems:
        operand1, operator, operand2 = i.split()
        operand1.strip(), operator.strip(), operand2.strip()
        #The operators will only accept are addition and subtraction
        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
#Each number (operand) should only contain digits.
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."


#Each operand has a max of four digits in width
        length = max(len(operand1), len(operand2)) + 2
        if length - 2 > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator == "+":
            res = str(int(operand1) + int(operand2))
        elif operator == "-":
            res = str(int(operand1) - int(operand2))

        #There should be a single space between the operator and the longest of the two operands
        if i != problems[-1]:
            bottom += operator + str(operand2).rjust(length - 1) + " " * 4
            top += str(operand1).rjust(length) + " " * 4
            dash += "-" * length + " " * 4
            result += str(res).rjust(length) + " " * 4
        else:
            bottom += operator + str(operand2).rjust(length - 1)
            top += str(operand1).rjust(length)
            dash += "-" * length
            result += str(res).rjust(length)
    if second:
        arranged_problems = top + "\n" + bottom + "\n" + dash + "\n" + result
    else:
        arranged_problems = top + "\n" + bottom + "\n" + dash

    return arranged_problems