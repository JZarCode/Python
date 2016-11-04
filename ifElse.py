def Main():

    i = int(input("Enter small postive integer: "))

    if i<0:
        print "please read directions next time"
    elif i==0:
        print "i is equal to 0"
    elif i==1:
        print "i is equal to 1"
    else:
        print "i is greater than 1"

if __name__ == "__main__":
    Main()
