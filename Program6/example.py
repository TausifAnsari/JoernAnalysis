class StringManipulator:
    def __init__(self, data=""):
        self.data = data

    def set_data(self, data):
        self.data = data

    def append_data(self, text_to_append):
        self.data += text_to_append

    def reverse_data(self):
        self.data = self.data[::-1]

    def uppercase_data(self):
        self.data = self.data.upper()

    def lowercase_data(self):
        self.data = self.data.lower()

    def get_data(self):
        return self.data

def main():
    user_input = input("Enter a string: ")

    # Create three StringManipulator objects
    obj1 = StringManipulator()
    obj2 = StringManipulator()
    obj3 = StringManipulator()

    # Set data in the first object
    obj1.set_data(user_input)

    # Perform operations on the objects
    obj2.set_data(obj1.get_data())  # Pass data from obj1 to obj2
    obj2.reverse_data()  # Reverse the string in obj2
    obj3.set_data(obj2.get_data())  # Pass data from obj2 to obj3
    obj3.uppercase_data()  # Uppercase the string in obj3

    final_result = obj3.get_data()

    # Print the final result
    print(final_result)

main()


























# class StringManipulator:
#     def __init__(self, data=""):
#         self.data = data

#     def set_data(self, data):
#         self.data = data

#     def get_data(self):
#         return self.data


# user_input = input("Enter a string: ")

# # Create three StringManipulator objects
# obj1 = StringManipulator()

# # Set data in the first object
# obj1.set_data(user_input)

# final_result = obj1.get_data()

# # Print the final result
# print(final_result)

