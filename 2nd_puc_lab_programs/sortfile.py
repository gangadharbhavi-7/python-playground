def sort_file(source,destination):
    with open(source,'r') as file:
        lines=file.readlines()
       

    cleaned=[]
    
    for line in lines:
        cleaned.append(line.strip())
    cleaned.sort()
    with open(destination,'w') as file:
        for line in cleaned:
            file.write(line+'\n')
    print("File sorted and saved to ",destination)
source=input("Enter the path of the source file: ")
destination=input("Enter the path of the destination file: ")
sort_file(source,destination)
