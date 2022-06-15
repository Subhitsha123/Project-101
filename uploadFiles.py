import dropbox
import os

class TransferData:
    def __init__(self, access_token) :
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path , mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BJhikcrGqhFhjqk_q91eSQaNl0FToA66VVuEFeI3KGDbIsP6W6-OVRrxAp4qZi5lpNdqG3W8L0kKw53jsdZd4T-6IIyc4tDa4TGvphU7qN8tGttR-pMCT6pLACk1Aiq-CU3C5YE'
    transferData = TransferData(access_token) 

    file_from = input("Enter the file path to transfer: ")  
    file_to = input("Enter the full path to upload to dropbox: ")   

    transferData.upload_file(file_from, file_to)    
    print("File has been moved!")       