from ftplib import FTP

ftp = FTP('domainname.com')
ftp.login(user='username', passwd='password')
ftp.cwd('/specificdomain-or-location/')

def grabFile():
    fileName = 'fileName.txt'
    localFile = open(fileName, 'wb')
    ftp.retrbinary('RETR ' + fileName, localFile.write, 1024)

    ftp.quit()
    localFile.close()

def placeFile():
    fileName = 'fileText.txt'
    ftp.storbinary('STOR '+fileName, open(fileName, 'rb'))
    ftp.quit()