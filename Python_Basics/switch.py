def switchfunc(value):
    switcher = {
        0: " this is zero ",
        1: "this is one",
    }
    return switcher.get(value, "nothing")



if __name__ == "__main__":
    print("enter value")
    value = input()
    print(switchfunc(value))