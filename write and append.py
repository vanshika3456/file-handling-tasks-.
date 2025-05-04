#Write and Append Data to a File
# take input from the user
data = input("Enter the data to be written in the file: ")
#open the file into write mode 
with open("output.txt","w") as file:
  content=file.write(data)
  print("data sucessfully written in the 'output.txt'")
  # append the data into th efile  in append mode 
with open('output.txt','a') as file:
  content=file.write("\nlearning file handling in python")
  print("data suceesfully appended in the 'output.txt'")
  file.close()

#read and display the final content  of the file 
with open('output.txt','r') as file:
  content=file.read()
  print("final content of the file is:")
  print(content)
  file.close()
        
  
