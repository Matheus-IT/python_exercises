city = input('\033[1;33mQual o nome da cidade? \033[m').strip()
print((city[:5].upper() == 'SANTO') or (city[:5].upper() == 'SANTA'))
