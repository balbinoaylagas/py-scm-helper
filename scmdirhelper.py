import os


class SCMDirHelper:
    def __init__(self, ticket_number):
        self.__scm_path = "C:\\scm_manage"
        self.__ticket_number = ticket_number
        self.__expected_scm_dirs = ["scripts", "com", "cmt_packages"]
        self.__exist_scm_dirs = False

    def getWorkingDir(self):
        return os.getcwd()

    def changeWorkDirToSCMPath(self):
        path = self.__scm_path
        change = False
        path = self.setTicketNumberPath(path)
        if os.path.exists(path):
            os.chdir(path)
            change = True
        return change

    def setTicketNumberPath(self, path):
        if self.__ticket_number is not None:
            path += "\\_naas_pnt_" + self.__ticket_number
        return path

    def checkExpectedScmFolders(self):
        path = self.getWorkingDir()
        scm_folders = self.__expected_scm_dirs
        exist = False
        for folder in scm_folders:
            print(folder)
