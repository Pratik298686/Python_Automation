# Design atuomation script which performs following task.
# 1. Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files
# 2. Create one Directory named as Marvellous and inside that directory create log file file which
#   maintains all names of duplicate files which are deleted.
# 3. Accept duration in minutes from user and perform task of duplicate file removal after the specific time interval.
# 4. Accept Mail id from user and send the attachment of the log file.
#   Mail body should contains statistics about the operation of duplicate file removal.
#   Mail body should contains below things:
#       Starting time of scaning
#       Total number of files scanned
#       Total number of duplicate files found


from sys import *
import os
import hashlib
import time
import smtplib
from sys import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

fcnt = 0
def hashfile(path, blocksize = 1024):
    fd = open(path,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    global fcnt
    flags = os.path.isabs(path)

    if flags == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
                fcnt += 1
        return dups
    else:
        print("Invalid Path")


def PrintDuplicate(dict1, log_dir="Marvellous"):
    lisprocess = []
    dcnt = 0
    global fcnt
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    separator = "-"*80
    # Generate a filenamefriendly timestamp
    timestamp = time.ctime().replace(" ","_").replace(":","-")
    log_path = os.path.join(log_dir,"MarvellousLog%s.log"%timestamp)
    f = open(log_path,'w')
    f.write(separator+"\n")
    f.write("Process Logger: "+time.ctime()+"\n")
    f.write(separator+"\n")
    f.write("\n")
    
    results = list(filter(lambda x:len(x)>1, dict1.values()))

    if len(results)>0:
        print("Duplicates Found: ")
        print("The following files are identical.")
        
        for result in results:
            icnt = 0
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print("\t\t%s"%subresult)
                    f.write("%s\n"%subresult)
                    dcnt += 1
    else:
        print("No duplicate files found")
    print("Total Number Of file Scanned %d\n"%fcnt)
    f.write("Total Number Of file Scanned %d\n"%fcnt)
    f.write("Total Number of duplicate file %d\n"%dcnt)
    f.close()
    return log_path


def DeleteFile(dict1):
    results = list(filter(lambda x:len(x)>1, dict1.values()))
    icnt = 0

    if len(results)>0:
        
        for result in results:
            icnt = 0
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print("\t\t%s is Deleted"%subresult)
                    os.remove(subresult)

def send_email(log_file, recipient_email):
    sender_email = "pratikpadman125@gmail.com"
    sender_password = "maiy gyej qdil vmtu"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = "Process Log File"

    text = "Please find attached the process log file."
    message.attach(MIMEText(text,'plain'))

    attachment = open(log_file,'rb')

    part = MIMEApplication(attachment.read(), Name=os.path.basename(log_file))
    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(log_file)}"'
    message.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email,message.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email : ",str(e))

def main():
    print("Application name: "+argv[0])

    try:
        arr = {}
        arr = FindDuplicate(argv[1])

        log_file = PrintDuplicate(arr)
        send_email(log_file, argv[3])
        
        duration_minutes = int(argv[2])

        if duration_minutes > 0:
            print(f"Waiting for {duration_minutes} minutes before deleting duplicate files...")
            time.sleep(duration_minutes*60)

            print("Performing duplicate file removal after the specified time interval.")
            DeleteFile(arr)
        else:
            print("Invalid duration. Please enter a positive number of minutes")
    
    
    except ValueError:
        print("Error : Invalid datatypes of input")
    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()