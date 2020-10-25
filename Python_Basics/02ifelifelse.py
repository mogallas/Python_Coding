
def main():
    print("enter your Total marks in Mathematics")
    marks = input()
    percent = (int(marks) / 100) * 100  
    print("Your percentage", percent)

    if (percent >= 35):
       if(percent >= 80):
           print("You are Awesome, you got distiniction)"
       elif (percent >= 60):
            print("you got first class")
       else: print("you got second class")

    else: print("Sorry, You are failed")
       

if __name__ == "__main__":
    main()