
from os import listdir,mkdir,rename,getcwd
from os.path import isfile, join, exists, isdir


fileToFolderMapper = {

    "ani bmp cal fax jbg jpg png jpeg" : "images",
    "wemb mkv flv ogv avi mp4 wmv amv m4p m4v mpg mpeg svi" : "videos",
    "tar bz bz2 zip 7z " : "compressed",
    "doc docx pdf" : "documents",
    "aspx axd" : "asp",
    "class java jsp jspx jar": "java",
    "css": "css",
    "html htm xhtml jhtml rhtml shtml phtml": "html",
    "action js" :"js",
    "php php4 php3": "php",
    "rb" : "ruby",
    "py" : "python",
    "c" : "C",
    "cpp" : "cpp",
    "h hpp hxx Hxx HXX": "headers",
    "gif" : "gif",
    "txt" : "text"
    
}

def banner():
    print("[+]----------------------------------------------------------")
    print("[+] hola!")
    print("[+] press 1 to organize")
    print("[+] ps :this will take the current directory and organize it")
    print("[+] to change directory 2 two")
    print("[+] press 3 to quit")
    print("[+] ./")

def goodbye() :
    print("[+] goodbye :) ")

def getFileExtension(file) :
     return file.split(".")[-1]

def mapExtensionToFolder(extension,file) :
    
    folderName = "others"
    for extensionList , destinationFolder in fileToFolderMapper.items():
        if extension in extensionList.split(" ") :
            folderName = destinationFolder
            break 

    createFolder(folderName)
    moveFileToFolder(file,folderName)       

def createFolder(name):
    if not exists(join(path,name)):
        mkdir(join(path,name))


def moveFileToFolder(file,folder) :
    rename(join(path,file),join(path,folder,file))


def main() : 
    for item in items :
        if isfile(join(path,item)) :
            
            extension =  getFileExtension(item)
            mapExtensionToFolder(extension,item)

def getPath():
    userPath = input("[+] your path")
    return userPath



if __name__ == '__main__':
    
    banner()
    userInput = input()    

    if(userInput.isdigit()):
        
        userInput = int(userInput)

        if(userInput == 1) :
            
            path = getcwd()
            items = listdir(path)

            main()
        elif(userInput == 2) :
            
            newPath = input("[+] enter new path\n")
        
            if isdir(newPath) :
                path = newPath
                items = listdir(path)
                
                main()
            else :
                print("[+] it is not a directory")
                goodbye()
                exit(0)    
        else :
            
            print("[+] undefined option")
            goodbye()
            exit(0)    
    else:
        print("[+] invalid option selected,exiting")
        goodbye()
        exit(0)


