from scmdirhelper import SCMDirHelper


ticket_number = "1408"

dirhelper = SCMDirHelper(ticket_number)
print(dirhelper.getWorkingDir())
if dirhelper.changeWorkDirToSCMPath():
    print("change is done")
    print(dirhelper.getWorkingDir())
else:
    print("error changing dir")

dirhelper.checkExpectedScmFolders()
