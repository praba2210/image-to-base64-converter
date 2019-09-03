import base64
i = 0

def encode(picture):
    with open(picture, "rb") as img_file: 
        my_string = base64.b64encode(img_file.read()) #base64 encoding 
        my_string = my_string.decode('utf-8') #decoding to 'utf-8' standard format
        my_string1 = str(my_string) #converting to string 
        my_string2 = "data:image/"+img_format+";base64,"+my_string #adding neccessary formats to display the base64 image in the html file
        #appending the string to the html file
        f.write("<DOCTYPE html>\n<html>\n<title>Hey there I'm prabakaran</title>\n<body><img style='display:block; width:400px; height:400px;'src="+my_string2+"></body></html>")
        #appending the string to the text file
        f1.write(my_string1)


while i==0:
    picture = input("Image path:") 
    img_format = str(input("Input image format:"))
    file_name = str(input("Output file name:"))
    f = open(file_name+".html", "w+") #creating .html file with user defined name 
    f1 = open(file_name+".txt", "w+") #creating .txt file with user defined name
    encode(picture) #function call for base64 encoding 
    i = int(input("Want to continue encoding(0/1)?"))
    if i==1:
        break





