Try:
with open('sample.text','r') as file:
    for line in file:
            # Print the line, removing extra spaces/newlines
            print(line.strip())    
except fileNotFoundError:
    # If file is not found, print an error message
print("Error: The file 'sample.text' does not exist")                 

