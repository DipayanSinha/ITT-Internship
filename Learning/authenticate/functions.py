import string
def handle_uploaded_file(f): #Storing Files in Directory
    with open('G:\Romu\PycharmProjects\\'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def write_temp_file(str):
    list_of_strings = str.split()
    if(["public","class"] in list_of_strings):
        i = list_of_strings.index("class")
    else:
        i = list_of_strings.index("class")
    f_name = list_of_strings[i+1]+".java"
    f_classname = list_of_strings[i+1]+".class"
    f = open("G:\\Romu\\PycharmProjects\\"+f_name, "w+")
    f.write(str)
    f.close()
    return f_name,f_classname
