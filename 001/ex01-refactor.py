import numpy as np


def max_len(operand1, operand2):
    len1 = len(operand1)
    len2 = len(operand2)

    return (np.fmax(len1, len2))


def esp(operand, maxLen):
    if (len(operand) < maxLen):
        return (maxLen-len(operand))*" "
    else:
        return ""


def calculate(operator1, operator2, operand):
    if (operand == "+"):
        return operator1 + operator2
    else:
        return operator1 - operator2


def arithmetic_arranger(operations):
    result = ["", "", "", ""]

    if len(operations) > 5:
        return ('Error: too many problems')
    else:
        for oper in operations:
            aux = oper.split()
            if (len(aux) < 3):
                return ("Error: too few arguments")

            operand1 = int(aux[0])
            operator = aux[1]
            operand2 = int(aux[2])
            maxLen = max_len(aux[0], aux[2])

            # Error control
            if (np.isnan(operand1) or np.isnan(operand2)):
                return ("Error: operands MUST be numbers")
            if (operator != "+" and operator != "-"):
                return ("Operation MUST be + or -")
            if (len(aux[0]) > 4 or len(aux[2]) > 4):
                return ("Error: Numbers cannot be more than four digits")

            operationResult = calculate(operand1, operand2, operator)
            if (operationResult < 0):
                addSpaces = " "
            else:
                addSpaces = "  "
            if (len(str(operationResult)) > 4 and operationResult > 0):
                addSpaces = " "

            separator = 4*" "
            line = (maxLen+2)*"-"

            esp0 = esp(aux[0], maxLen)
            esp1 = esp(aux[2], maxLen)
            esp3 = esp(str(operationResult), maxLen)

            result[0] = result[0] + "  " + esp0 + \
                f"{operand1}{separator}"
            result[1] = result[1] + \
                f"{operator} {esp1}{operand2}{separator}"
            result[2] = result[2] + line + separator
            result[3] = result[3] + addSpaces + esp3 + \
                str(operationResult) + separator

        resultStr = ""
        for line in result:
            resultStr = resultStr + line + "\n"

    return resultStr


result = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
print(result)
