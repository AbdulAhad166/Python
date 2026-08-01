#Program for Copying an Image
def imagecopy():
    try:
        with open("D:\\Python\\rcb.png","rb") as rp:
            with open("rcb.png","wb") as wp:
                #Read the Source File Content
                srcfile=rp.read()
                #Write the Source File Data Into Destination File
                dstfile=wp.write(srcfile)
                print("\t 1 Image File(s) Copied---Verify")
    except FileNotFoundError:
        print("\t File Does Not Exist")
#Main Program
imagecopy()

