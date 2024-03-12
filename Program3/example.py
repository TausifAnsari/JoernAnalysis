# Data flow exist
def main():
    name = input("Enter your name")
    list1 = []
    list2 = []
    list1.append(name)
    list2.append(list1[0])
    print(list2[0])

main()