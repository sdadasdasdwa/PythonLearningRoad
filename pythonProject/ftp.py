import ftplib
from ftplib import FTP
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = ''
FILE = ''

def main():
    try:
        f = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror) as e:
        print('error: cannot reach %s' % HOST)
        return
    print('connect %s' % HOST)
    try:
        f.login()
    except ftplib.error_perm:
        print('error: cannot login anonymously')
        f.quit()
        return
    try:
        f.transfercmd(DIRN)
    except ftplib.error_perm:
        print('cannot CD to %s' % DIRN)
    try:
        f.retrbinary('RETR %s' % FILE, open(FILE,'wb').write)
    except ftplib.error_perm:
        print('cannot read file %s'% FILE)
        os.unlink(FILE)
    else:
        print('Download %s to CWD' % FILE)
    f.quit()

if __name__=='__main__':
    main()

f = FTP('ftp.python.org')
f.login('anonymous', 'guido@python.org')