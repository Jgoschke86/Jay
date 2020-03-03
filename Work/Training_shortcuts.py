from tkinter import *
import xlrd, time, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

train_info = (r"C:\Users\jgoschke\Desktop\Training info.xlsx")
sheet = train_info.sheet_by_index(0)


