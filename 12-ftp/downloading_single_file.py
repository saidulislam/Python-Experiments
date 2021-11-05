from ftplib import FTP

ftp = FTP('ftp.debian.org')
print(ftp.login())
#'230 Login successful.'

print(ftp.cwd('debian')  )
#'250 Directory successfully changed.'


out = 'README'
with open(out, 'wb') as f:
    ftp.retrbinary('RETR ' + 'README.html', f.write)