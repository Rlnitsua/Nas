#coding=utf-8

import os


def rename(originFilePath, targetFilePath):
    os.system('mv ' + originFilePath + " " + targetFilePath)

def move(filePath, targetPath):
    os.system('mv ' + filePath + " " + targetPath)
