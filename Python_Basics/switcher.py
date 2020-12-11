
def main(option):
    switcher = {
        1: " Node report ",
        2: " Pods Report ",
        3: " Resource util ",
    }
    return switcher.get(option, "nothing")



if __name__ == "__main__":
    print("Health Check Report")
    print("-------------------\n please select below options \n")
    print("1.Node report")
    print("2.Pods report")
    print("3.Resource utilization")
    option = input()
    
    print(main(option))