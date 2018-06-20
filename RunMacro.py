import os, os.path
import win32com.client

os.chdir("S:\\Sam\\IRM\\ACPP\\exports\\Python Export\\Analysis Draft\\")


def run_macro(sheet_name):  # sheet name includes .xlsm extension
    if os.path.exists(sheet_name):
        xl = win32com.client.Dispatch("Excel.Application")
        xl.Workbooks.Open(os.path.abspath(sheet_name))
        xl.Application.Run(sheet_name + "!Ctrl.UIRunAll")
        xl.Application.Save()  # if you want to save then uncomment this line and change delete the ", ReadOnly=1" part from the open function.
        xl.Application.Quit()  # Comment this out if your excel script closes
        del xl


run_macro("PV_Template.xlsm")
run_macro("FX_Template.xlsm")
run_macro("DV01_Template.xlsm")
