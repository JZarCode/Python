def Main():

    print "\nFor loop counting up"
    for x in range(1,5):
        print "%d" % (x)

    print "\nWhile loop counting down"
    while x != 0:
        print "%d" % (x)
        x -= 1

if __name__ == "__main__":
    Main()
