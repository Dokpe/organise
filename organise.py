import os
import shutil
import glob

def checkDir(path):
    # return path if it exists; else prompt user
    while True:
        try:
            os.chdir(path)
            return path
        except FileNotFoundError:
            print("\nInvalid username or directory, please re-enter both.")
            name = input("Name: ")
            direct = input("Directory: ")
            path = os.path.join("C:\\Users\\", name, direct)
        
        
def getExtensions(path):
    # return list containing all filenames and fileexte
    fileList = os.listdir(path)
    fileExtensions = []
    fileNames = []
    for filename in fileList:
        index = len(filename.split(".")) -1
        
        # try if filename is not folder
        if (os.path.exists(path+"\\"+filename+"\\") != True and index > 0): 
            fileExtensions.append(filename.split(".")[index])      
            fileNames.append(filename)
        elif (os.path.exists(path+"\\"+filename+"\\") != True and index == 0):
            print("Encountered file without file extension, will save in folder 'other.' ")
            
    newlist = []
    # remove duplicates
    for extension in fileExtensions:
        if (extension not in newlist) and (extension != "tmp" and extension != "ini" and extension != "partial"):
            newlist.append(extension)
            
    fileExtensions = newlist[:]
    fileExtensions.sort()
    ExtAndName = [fileNames, fileExtensions]
    return ExtAndName

def shiftFileToFolder(path, extensions, fullname):
    video = ["Video","mp4", "avi", "mkv", "srt"]
    music = ["Music", "mp3"]
    docs = ["Documents","txt", "docx", "doc", "csv", "rtf", "pdf", "numbers"]
    torrents = ["Torrents","torrent"]
    pictures = ["Pictures","jpg", "png", "bmp", "gif"]
    apps = ["Applications","exe", "apk"]
    compressed = ["Compressed Files","zip", "iso", "gz"]
    programs = ["Programs","c", "py", "pyw", "cpp", "java"]
    comics = ["Comics", "cbr"]
    books = ["Books", "epub"]
    folders = [video, music, docs, torrents, pictures, apps, compressed, programs, comics, books]
    
    # make folders
    for foldername in folders:
        for fileExtension in foldername:
            if fileExtension in extensions:
                try:
                    os.mkdir(foldername[0])
                except FileExistsError:
                    pass 
            else:
                try:
                    os.mkdir("Other")
                except FileExistsError:
                    pass 
    
    # move files to appropriate folders
    for i in fullname:
        file = i.split(".")
        index = len(file) - 1
        for j in folders:
            if file[index] in j:
                try:
                    shutil.move(path+"\\"+i, path+"\\"+j[0])
                except:
                    pass
                
name = input("Enter your Windows username: ")
direct = input("Enter the directory you wish to organise: ")
dirname = os.path.join("C:\\Users\\", name, direct)
dirname = checkDir(dirname)
extensionsList = getExtensions(dirname)
shiftFileToFolder(dirname, extensionsList[1], extensionsList[0])


