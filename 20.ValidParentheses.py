def ValidParenthesis(input):
    dictOpening = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
    }
    input = list(input)
    expected = []
    for element in input:
        if element in dictOpening:
            expected.insert(0, dictOpening[element])
        elif len(expected) == 0:
            print("False")
            return False
        elif element == expected[0]:
            del expected[0]
        else:
            print(False)
            return False
    if len(expected) != 0:
        print(False)
        return False
    else:
        print(True)
        return True

ValidParenthesis("[()]{}")