value_dict = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def romanToInteger(input):
    integer = 0
    length = len(input)
    for index in range(0, length):
        CurrentValue = value_dict[input[index]]

        if index < (length - 1):
            NextValue = value_dict[input[index + 1]]
            if NextValue > CurrentValue:
                integer += NextValue - CurrentValue
                continue

        if index >= 1:
            PreviousValue = value_dict[input[index - 1]]
            if PreviousValue < CurrentValue:
                continue
        
        integer += CurrentValue
    print(integer)

romanToInteger("MCMXCIV")
