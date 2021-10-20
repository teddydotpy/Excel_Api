#!/usr/bin/env python3
import sqlite3
import openpyxl
db = sqlite3.connect('UserInfo.sqlite3')
t_cursor = db.cursor()

def pop_excel():
    t_cursor.execute('''
        SELECT * FROM ExcelApi_userinfo;
    ''')
    # Added the return to a variable so i chave acess to it in the future.
    db_info = t_cursor.fetchall()
    for data in db_info:
        wb = openpyxl.Workbook()
        sheet = wb.get_sheet_by_name('Sheet')
        User_db = db.connect('UserInfo.sqlite3')

        sheet['A1'] = 'Name & Surname'
        sheet['B1'] = 'Contact Number'
        sheet['C1'] = 'Age'
        sheet['D1'] = 'Number Of Children'
        sheet['E1'] = 'Bank ??'

        sheet['A'+ str(data[0])] = data[1] + ' ' + data[2]
        sheet['B'+ str(data[0])] = data[4]
        sheet['C'+ str(data[0])] = data[3]
        sheet['D'+ str(data[0])] = data[5]
        sheet['E'+ str(data[0])] = data[6]
     
    wb.save('fees.xlsx')

db.close()