 
import dropbox 
from dropbox.files import WriteMode
import os

class Transferdata:
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadfile(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(filefrom):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path= os.path.relpath(local_path, filefrom)
                dropbox_path=os.path.join(fileto,relative_path)
                with open(local_path,"rb") as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))


def main():
    access_token="ELU5gdsaELMAAAAAAAAAAabhfDhtfAnF1w5NuGEeJIsG4g-KmHRRSw5jIDdp-KpE"
    transferdata=Transferdata(access_token)
    filefrom = str(input("Enter the file from which u want to upload: "))
    fileto = input("Enter the file to which u want to upload: ")

    transferdata.uploadfile(filefrom,fileto)
    print("The files have been uploaded")

main()