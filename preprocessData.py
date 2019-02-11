#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np


# In[ ]:


def getNextLevelDirs(root):
     return next(os.walk(root))[1]

def getFileList(basePath):
    firstLevelDirs = getNextLevelDirs(basePath)
    return firstLevelDirs


# In[2]:


def extract_loudest_section(BasePathToFolder,FolderList,TargetFolderFullPath,callbackBeforeAction=None,callbackAfterAction=None):
    for folder in FolderList:
        D = os.path.join(BasePathToFolder,folder)
        files = [os.path.join(D,F) for F in next(os.walk(D))[2] if F.endswith('.wav')]
        for file in files:
            #call callback before action
            if callbackBeforeAction:
                callbackBeforeAction(file)
            #call extract wav loudest section
            extract_wav_loudest_section(file,TargetFolderFullPath)
            if callbackAfterAction:
                callbackAfterAction(file,TargetFolderFullPath)

def extract_wav_loudest_section(RawAudioFileFullName, TagetFolder):
    #print("processing file {}".format(RawAudioFile))
    call(["./extract_loudest_section", RawAudioFileFullName, TagetFolder])
    #print("{} has been processed.".format(RawAudioFileFullName))


# In[ ]:


def CreateGroupOfFolders(RootFolder,FolderNameList):
    for name in FolderNameList:
        dirname = RootFolder+name
        os.makedirs(dirname)

