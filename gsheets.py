from datetime import date
import pygsheets
from pygsheets import Cell

gc = pygsheets.authorize(service_file='C:\\Users\\Апгрейд\\Documents\\ИСИТ\\multitool_bot\\subjects-check-979e7e2059e3.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1KpnUXhWfcg8KK35JJpq4OeKNguBooMKgwkuF626j8Nc/edit#gid=0')


def add_subject(subject):
    existing_worksheets = sh.worksheets()
    found_worksheet = ""
    for current_sheet in existing_worksheets:
        if current_sheet.title.casefold() == subject.casefold():
            found_worksheet = subject
            break

    if found_worksheet == "":
        sh.add_worksheet(subject)
        found_worksheet = subject

    current_worksheet = sh.worksheet_by_title(found_worksheet)
    current_row = 1
    current_column = 2
    current_date = date.today().strftime("%Y-%m-%d")
    while current_worksheet.get_value((current_row, current_column)) and \
            current_worksheet.get_value((current_row, current_column)) != current_date:
        current_column += 1
    Cell(worksheet=current_worksheet, pos=(current_row, current_column)).set_value(current_date)
    return current_column


def add_students(students, subject, matching_column):
    current_worksheet = sh.worksheet_by_title(subject)
    students_list = students.split(',')
    print(students_list, students)
    for student in students_list:
        student = " ".join(student.split())
        current_row = 2
        current_column = 1
        while current_worksheet.get_value((current_row, current_column)) and \
                current_worksheet.get_value((current_row, current_column)) != student:
            current_row += 1
        Cell(worksheet=current_worksheet, pos=(current_row, current_column)).set_value(student)
        Cell(worksheet=current_worksheet, pos=(current_row, matching_column)).set_value("1")
