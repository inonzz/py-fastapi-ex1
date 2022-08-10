from fastapi import FastAPI
from fastapi_utils.inferring_router import InferringRouter
import consts
from controller.InstallScriptController import InstallScriptController

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = ""
    app = consts.app
    c = InstallScriptController(url)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
