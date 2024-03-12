# Data flow exist
# Different Methods usage 2
def listDataflow(name):
    list1 = []
    list2 = []
    list1.append(name)
    list2.append(list1[0])
    print(list2[0])

def main():
    name = input("Enter your name")
    listDataflow(name)

main()