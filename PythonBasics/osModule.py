import os, time

curDir = os.getcwd()
print(curDir)


os.mkdir('example')
time.sleep(2)

os.rename('example', 'example2')
time.sleep(2)

os.rmdir('example2')


