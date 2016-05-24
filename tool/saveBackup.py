# -*- coding:utf-8 -*- #

import sys
import dropbox
import os
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
import myLogging
from config import TOKEN_PATH

# Add OAuth2 access token here.
# You can generate one for yourself in the App Console.
TOKEN = ''


def getTokenStr():
    with open(TOKEN_PATH, 'r') as f:
        return f.read()


class BackUpByDropBox(object):

    """docstring for CombXlsData"""

    def __init__(self):
        super(BackUpByDropBox, self).__init__()
        self.dbx = self.initDropBoxInfo()
        # self.folders = []
        # self.files = []

    def initDropBoxInfo(self):
        global TOKEN
        if TOKEN == '':
            TOKEN = getTokenStr()

        # Check for an access token
        if (len(TOKEN) == 0):
            myLogging.logging.error(
                "Looks like you didn't add your access token.")
            sys.exit()

        # Create an instance of a Dropbox class, which can make requests to the
        # API.
        #print("Creating a Dropbox object...")
        dbx = dropbox.Dropbox(TOKEN)

        # Checkt that the access token is valid
        try:
            user = dbx.users_get_current_account()
        except AuthError:
            myLogging.logging.error(
                "Invalid access token. try re-generating an access token from the app console on the web.")
            sys.exit()
        myLogging.logging.info(
            "Weclome " + user.name.display_name + '\'s Dropbox.')

        return dbx

    def uploadFile(self, uploadFileName, dropBoxPath):
        with open(uploadFileName, 'r') as f:
            # We use WriteMode=overwrite to make sure that settings in the file
            # are changed on Upload
            myLogging.logging.info(
                "Uploading " + uploadFileName + " to Dropbox as " + dropBoxPath + " ...")
            try:
                self.dbx.files_upload(
                    f, dropBoxPath, mode=WriteMode('overwrite'))
            except ApiError as err:
                # This checks for the specific error where a user doesn't have
                # enough Dropbox space quota to upload this file
                if (err.error.is_path() and
                        err.error.get_path().error.is_insufficient_space()):
                    myLogging.logging.error(
                        "Cannot back up; insufficient space.")
                    sys.exit()
                elif err.user_message_text:
                    myLogging.logging.error(err.user_message_text)
                    sys.exit()
                else:
                    myLogging.logging.error(err)
                    sys.exit()

    def isFileExist(self, dropboxFileName):
        folderName, fileName = os.path.split(dropboxFileName)
        isExist = False
        result = self.dbx.files_search(folderName, fileName)
        #print result
        if len(result.matches) > 0:
            isExist = True
        return isExist

    def delFile(self, dropboxFileName):
        isExist = self.isFileExist(dropboxFileName)
        if isExist:
            self.dbx.files_delete(dropboxFileName)

    # def get_all_file_and_folder_name(self,path, rs):
        #  folders = dbx.files_list_folder(path)
        #  for content in folders.entries:
        #      if isinstance(content, dropbox.files.FolderMetadata):
        #          get_all_file_and_folder_name(content.path_display, rs)
        #          print "folder name:", content.path_display
        #      if isinstance(content, dropbox.files.FileMetadata):
        #          print "file name", content.name
        #          rs.append(content.path_display)
