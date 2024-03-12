# Data flow exist
# Different Methods usage
def listDataflow(name):
    list1 = []
    list2 = []
    list1.append(name)
    list2.append(list1[0])
    return list2[0]

def main():
    name = input("Enter your name")
    result = listDataflow(name)
    print(result)

main()