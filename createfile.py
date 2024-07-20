#creating function to create file and write content inside it 
def fileCreation(filename,filecontent):
    #creatinh the file and accessing it
    with open(filename,"w") as f:
        #writing content inside file
        f.write(filecontent)
        print(f"the file {filename} has been created Successfully")


filename="hello.txt"
filecontent="hello i am zala nirbhay from(TY-BCA)"
#call the function and pass the file name and content that you want to write
fileCreation(filename,filecontent)

#written by zala nirbhay(TY-BCA)