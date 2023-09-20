from sharepoint import SharePoint

# set file name
file_name = 'Santander_Controle_Jobs_Coligadas_230728.xlsx'

# set the folder name
folder_name = 'Gerenciamento'

# get file
file  = SharePoint().download_file(file_name, folder_name)

# save file
with open(file_name, 'wb') as f:
    f.write(file)
    f.close()
