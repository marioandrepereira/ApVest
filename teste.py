import zipfile

file_name = "Ap.zip"
password = "teste"

with zipfile.ZipFile(file_name, "r") as zip_ref:
    zip_ref.setpassword(password)
    zip_ref.extractall()


