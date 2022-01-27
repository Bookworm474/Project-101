import dropbox, os

class TransferData():
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_files(self, file_from, file_to):
        access_token = self.access_token
        dbx = dropbox.Dropbox(access_token)
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = "CdPBbRXVbd8AAAAAAAAAAelcZttLqI2VOdPEHQMDgUda8qFBOkd8oveWFMnC1YsV"
    transferData = TransferData(access_token)
    file_from = "test2.text"
    file_to = "text_dropbox/text2.text"
    transferData.upload_files(file_from, file_to)

main()