from ftplib import FTP
ftp = FTP()
HOST = 'ftp.cse.buffalo.edu'
PORT = 12345
ftp.connect(HOST, PORT)

print (ftp.login())
#'230 Guest login ok, access restrictions apply.'