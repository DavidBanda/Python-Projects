'''
text = 'Simple texto a guardar\nOtra linea'

saveFile = open('exampleText.txt', 'w')

saveFile.write(text)
saveFile.close()
'''

añadir = '\nAñadir otra linea'

appendFile = open('exampleText.txt', 'a')
appendFile.write(añadir)
appendFile.close()


