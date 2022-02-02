#BONK!
#-W3SLAV
import os.path
print("BONK! A NDS programming tool")
if (os.path.exists("main.blin") == True):
    print("file found")
    with open('main.blin', 'r') as file :
        filedata = file.read()
    # Replace the target string
    cwd = os.getcwd()
    fid = os.listdir(cwd+"/commands")
    n = 0
    length = len(fid)
    length = length -1
    while (length >= n):
        book = (cwd+"/commands/"+fid[n])
        with open(book, 'r') as filez :
            out = filez.read()
        oof = fid[n].replace(".bcf", "")
        print(oof)
        filedata = filedata.replace(oof, out)
        n = n+1
    if (os.path.exists("main.c") == True):
        os.remove("source/main.c")
    # Write the file out again
    with open('source/main.c', 'w') as file:
        file.write(filedata)
    print("finished writing to file")
    print("compiling...")
    
    #os.system('cmd /k "cd "+cwd+"/source && make"')
    os.system('cmd /k "make"')
    print("done!")

else:
    print("error, no file named main.py, try renaming your file to main.blin")
