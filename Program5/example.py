# Data flow doesn't exist
def manipulate_data(data):
    # This function does not return any data
    return
    
def print_result(data):
    print("This program does not have data flow between input and print.")

user_input = input("Enter some text: ")
manipulate_data(user_input)
print_result(user_input)