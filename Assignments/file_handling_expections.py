try:
    with open("example.txt", "r") as file_obj:
        contents = file_obj.read()
        
except FileNotFoundError:
    print("can't read contents, file is not found")
else:
    print(contents)    
