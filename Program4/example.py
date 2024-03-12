# Data flow exist
def process_data(data):
    def format_output(text):
        return "Processed: " + text
    
    result = format_output(data)
    return result

user_input = input("Enter text: ")
formatted_result = process_data(user_input)
print(formatted_result)