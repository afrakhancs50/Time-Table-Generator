import json
from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


def getInput():
    no_of_tr = int(input('Enter no. of tr : '))
    tr_data_sem4 = {}
    tr_data_sem6 = {}
    tr_data_sem8 = {}
    faculty = []
    subject_sem4 = []
    subject_sem6 = []
    subject_sem8 = []
    
    print('\nFor sem-4')
    for i in range(no_of_tr):
        print('\nDetail of faculty ',i+1)
        key = input('Enter name : ')
        value = input('Enter Subject : ')
        key = key.upper()
        value = value.upper()
        tr_data_sem4[key] = value
        value = value + "-" + key
        subject_sem4.append(value)
        faculty.append(key)
    
    print('\nFor sem-6')
    for i in range(no_of_tr):
        print('\nDetail of faculty ',i+1)
        key = input('Enter name : ')
        value = input('Enter Subject : ')
        key = key.upper()
        value = value.upper()
        tr_data_sem6[key] = value
        value = value + "-" + key
        subject_sem6.append(value)
    
    print('\nFor sem-8')
    for i in range(no_of_tr):
        print('\nDetail of faculty ',i+1)
        key = input('Enter name : ')
        value = input('Enter Subject : ')
        key = key.upper()
        value = value.upper()
        tr_data_sem8[key] = value
        value = value + "-" + key
        subject_sem8.append(value)   

    return no_of_tr, faculty, tr_data_sem4, subject_sem4, tr_data_sem6, subject_sem6, tr_data_sem8, subject_sem8

def getInputPractical():
    no_of_pr = int(input('\nEnter no. of Practicals : '))
    tr_data_sem4 = {}
    tr_data_sem6 = {}
    tr_data_sem8 = {}
    faculty = []
    subject_sem4 = []
    subject_sem6 = []
    subject_sem8 = []
    
    print('\nFor sem-4')
    for i in range(no_of_pr):
        print('\nDetail of faculty ',i+1)
        key = input('Enter name : ')
        value = input('Enter Subject : ')
        key = key.upper()
        value = value.upper()
        tr_data_sem4[key] = value
        value = value + "-" + key
        subject_sem4.append(value)
        faculty.append(key)
    
    print('\nFor sem-6')
    for i in range(no_of_pr):
        print('\nDetail of faculty ',i+1)
        key = input('Enter name : ')
        value = input('Enter Subject : ')
        key = key.upper()
        value = value.upper()
        tr_data_sem6[key] = value
        value = value + "-" + key
        subject_sem6.append(value)
    
    print('\nFor sem-8')
    for i in range(no_of_pr):
        print('\nDetail of faculty ',i+1)
        key = input('Enter name : ')
        value = input('Enter Subject : ')
        key = key.upper()
        value = value.upper()
        tr_data_sem8[key] = value
        value = value + "-" + key
        subject_sem8.append(value)   

    return no_of_pr, faculty, tr_data_sem4, subject_sem4, tr_data_sem6, subject_sem6, tr_data_sem8, subject_sem8

def generate_tt1(subject):
    tt1 = []
    mon = []
    tue = []
    wed = []
    thu = []
    fri = []

    for row in range(5):
        for col in range(6):
            if row == 0:
                if row == col or col == row + 1:
                    mon.append(subject[row])
                else:
                    mon.append(subject[col - 1])
            elif row == 1:
                if row == col or col == row + 1:
                    tue.append(subject[row])
                elif col > row:
                    tue.append(subject[col-1])
                else:
                    tue.append(subject[col])
            elif row == 2:
                if row == col or col == row + 1:
                    wed.append(subject[row])
                elif col > row:
                    wed.append(subject[col-1])
                else:
                    wed.append(subject[col])
            elif row == 3:
                if row == col or col == row + 1:
                    thu.append(subject[row])
                elif col > row:
                    thu.append(subject[col-1])
                else:
                    thu.append(subject[col])
            elif row == 4:
                if row == col or col == row + 1:
                    fri.append(subject[row])
                elif col > row:
                    fri.append(subject[col-1])
                else:
                    fri.append(subject[col])
        if row == 0:
            tt1.append(mon)
        elif row == 1:
            tt1.append(tue)
        elif row == 2:
            tt1.append(wed)
        elif row == 3:
            tt1.append(thu)
        elif row == 4:
            tt1.append(fri)
    return tt1

def three_column_of_two(tt1):
    col01 = []
    col23 = []
    col45 = []
    temp1 = []
    temp2 = []
    temp3 = []

    for row in range(5):
        for col in range(2):
            temp1.append(tt1[row][col])
        col01.append(temp1.copy())
        temp1.clear()

    for row in range(5):
        for col in range(2,4):
            temp2.append(tt1[row][col])
        col23.append(temp2.copy())
        temp2.clear()

    for row in range(5):
        for col in range(4,6):
            temp3.append(tt1[row][col])
        col45.append(temp3.copy())
        temp3.clear()

    return col01,col23,col45

def generate_tt2(col01,col23,col45):
    tt2 = []
    mon = []
    tue = []
    wed = []
    thu = []
    fri = []
    for row in range(5):
        for col in range(1):
            if row == 0:
                mon.append(col23[row][col])
                mon.append(col23[row][col+1])
                mon.append(col45[row][col])
                mon.append(col45[row][col+1])
                mon.append(col01[row][col])
                mon.append(col01[row][col+1])
            if row == 1:
                tue.append(col23[row][col])
                tue.append(col23[row][col+1])
                tue.append(col45[row][col])
                tue.append(col45[row][col+1])
                tue.append(col01[row][col])
                tue.append(col01[row][col+1])
            if row == 2:
                wed.append(col23[row][col])
                wed.append(col23[row][col+1])
                wed.append(col45[row][col])
                wed.append(col45[row][col+1])
                wed.append(col01[row][col])
                wed.append(col01[row][col+1])
            if row == 3:
                thu.append(col23[row][col])
                thu.append(col23[row][col+1])
                thu.append(col45[row][col])
                thu.append(col45[row][col+1])
                thu.append(col01[row][col])
                thu.append(col01[row][col+1])
            if row == 4:
                fri.append(col23[row][col])
                fri.append(col23[row][col+1])
                fri.append(col45[row][col])
                fri.append(col45[row][col+1])
                fri.append(col01[row][col])
                fri.append(col01[row][col+1])
        if row == 0:
            tt2.append(mon)
        elif row == 1:
            tt2.append(tue)
        elif row == 2:
            tt2.append(wed)
        elif row == 3:
            tt2.append(thu)
        elif row == 4:
            tt2.append(fri)
    return tt2

def generate_tt3(col01,col23,col45):
    tt3 = []
    mon = []
    tue = []
    wed = []
    thu = []
    fri = []
    for row in range(5):
        for col in range(1):
            if row == 0:
                mon.append(col45[row][col])
                mon.append(col45[row][col+1])
                mon.append(col01[row][col])
                mon.append(col01[row][col+1])
                mon.append(col23[row][col])
                mon.append(col23[row][col+1])
            if row == 1:
                tue.append(col45[row][col])
                tue.append(col45[row][col+1])
                tue.append(col01[row][col])
                tue.append(col01[row][col+1])
                tue.append(col23[row][col])
                tue.append(col23[row][col+1])
            if row == 2:
                wed.append(col45[row][col])
                wed.append(col45[row][col+1])
                wed.append(col01[row][col])
                wed.append(col01[row][col+1])
                wed.append(col23[row][col])
                wed.append(col23[row][col+1])
            if row == 3:
                thu.append(col45[row][col])
                thu.append(col45[row][col+1])
                thu.append(col01[row][col])
                thu.append(col01[row][col+1])
                thu.append(col23[row][col])
                thu.append(col23[row][col+1])
            if row == 4:
                fri.append(col45[row][col])
                fri.append(col45[row][col+1])
                fri.append(col01[row][col])
                fri.append(col01[row][col+1])
                fri.append(col23[row][col])
                fri.append(col23[row][col+1])
        if row == 0:
            tt3.append(mon)
        elif row == 1:
            tt3.append(tue)
        elif row == 2:
            tt3.append(wed)
        elif row == 3:
            tt3.append(thu)
        elif row == 4:
            tt3.append(fri)
    return tt3

def change_sub_sem6(faculty, faculty_sem4,faculty_sem6,tt2):
    for row in range(5):
        for col in range(6):
            val = tt2[row][col]
            if faculty[0] in val:
                tt2[row][col] = val.replace(faculty_sem4[faculty[0]], faculty_sem6[faculty[0]])
            elif faculty[1] in val:
                tt2[row][col] = val.replace(faculty_sem4[faculty[1]], faculty_sem6[faculty[1]])
            elif faculty[2] in val:
                tt2[row][col] = val.replace(faculty_sem4[faculty[2]], faculty_sem6[faculty[2]])
            elif faculty[3] in val:
                tt2[row][col] = val.replace(faculty_sem4[faculty[3]], faculty_sem6[faculty[3]])
            elif faculty[4] in val:
                tt2[row][col] = val.replace(faculty_sem4[faculty[4]], faculty_sem6[faculty[4]])
    return tt2

def change_sub_sem8(faculty,faculty_sem4,faculty_sem8, tt3):
    for row in range(5):
        for col in range(6):
            val = tt3[row][col]
            if faculty[0] in val:
                tt3[row][col] = val.replace(faculty_sem4[faculty[0]], faculty_sem8[faculty[0]])
            elif faculty[1] in val:
                tt3[row][col] = val.replace(faculty_sem4[faculty[1]], faculty_sem8[faculty[1]])
            elif faculty[2] in val:
                tt3[row][col] = val.replace(faculty_sem4[faculty[2]], faculty_sem8[faculty[2]])
            elif faculty[3] in val:
                tt3[row][col] = val.replace(faculty_sem4[faculty[3]], faculty_sem8[faculty[3]])
            elif faculty[4] in val:
                tt3[row][col] = val.replace(faculty_sem4[faculty[4]], faculty_sem8[faculty[4]])
    return tt3

def which_row(tt):
    for row in range(5):
        if tt[row][0] == tt[row][5]:
            return row
def max_len_sub(subject_sem4, subject_sem6, subject_sem8,pr_subject_sem4,pr_subject_sem6,pr_subject_sem8):
    temp = []
    for sub in subject_sem4:
        temp.append(len(sub))
    for sub in subject_sem6:
        temp.append(len(sub))
    for sub in subject_sem8:
        temp.append(len(sub))
    for sub in pr_subject_sem4:
        temp.append(len(sub))
    for sub in pr_subject_sem6:
        temp.append(len(sub))
    for sub in pr_subject_sem8:
        temp.append(len(sub))
    return max(temp)

def add_practical(tt,pr_sub):
    for row in range(5):
        for col in range(6):
            if row == 0:
                if row == col or col == row + 1:
                    tt[row][col] = pr_sub[row]
            elif row == 1:
                if row == col or col == row + 1:
                    tt[row][col] = pr_sub[row]                    
            elif row == 2:
                if row == col or col == row + 1:
                    tt[row][col] = pr_sub[row]                    
            elif row == 3:
                if row == col or col == row + 1:
                    tt[row][col] = pr_sub[row]
            elif row == 4:
                if row == col or col == row + 1:
                    tt[row][col] = pr_sub[row]
    return tt


# n, faculty, faculty_sem4, subject_sem4, faculty_sem6, subject_sem6, faculty_sem8, subject_sem8 = getInput()
# no_pr, pr_faculty, pr_faculty_sem4, pr_subject_sem4, pr_faculty_sem6, pr_subject_sem6, pr_faculty_sem8, pr_subject_sem8 = getInputPractical()
# print(no_pr, pr_faculty, pr_faculty_sem4, pr_subject_sem4, pr_faculty_sem6, pr_subject_sem6, pr_faculty_sem8, pr_subject_sem8)

# tt1 = generate_tt1(subject_sem4)
# col01,col23,col45 = three_column_of_two(tt1)
# tt2 = generate_tt2(col01,col23,col45)
# tt3 = generate_tt3(col01,col23,col45)

# tt2 = change_sub_sem6(faculty, faculty_sem4,faculty_sem6,tt2)
# tt3 = change_sub_sem8(faculty, faculty_sem4,faculty_sem8,tt3)

# tt1row = which_row(tt1)
# tt2row = which_row(tt2)
# tt3row = which_row(tt3)

# max_len = max_len_sub(subject_sem4,subject_sem6,subject_sem8,pr_subject_sem4,pr_subject_sem6,pr_subject_sem8)

# tt1 = add_practical(tt1,pr_subject_sem4)
# tt2 = add_practical(tt2,pr_subject_sem6)
# tt3 = add_practical(tt3,pr_subject_sem8)

# print('\nSEM-4 TT')
# for row in range(5):
#     if row == tt2row:
#         print(end = '    ')
#         for i in range(max_len):
#             print(end = ' ')
#     if row == tt3row:
#         print(end = '    ')
#         for i in range(max_len):
#             print(end = ' ')
#     for col in range(6):
#         print(tt1[row][col],end = '')
#         for i in range(max_len - len(tt1[row][col])):
#             print(end=' ')
#         print(end = '    ')
#     print()

# print()

# print('SEM-6 TT')
# for row in range(5):
#     if row == tt1row:
#         print(end = '    ')
#         for i in range(max_len):
#             print(end = ' ')
#     if row == tt3row:
#         print(end = '    ')
#         for i in range(max_len):
#             print(end = ' ')
#     if tt2[row][0] == tt2[row][5]:
#         for col in range(5,6):
#             print(tt2[row][col],end = '')
#             for i in range(max_len - len(tt2[row][col])):
#                 print(end=' ')
#             print(end = '    ')
#         for col in range(5):
#             print(tt2[row][col],end = '')
#             for i in range(max_len - len(tt2[row][col])):
#                 print(end=' ')
#             print(end = '    ')
#         print()
#     else:
#         for col in range(6):
#             print(tt2[row][col],end = '')
#             for i in range(max_len - len(tt2[row][col])):
#                 print(end=' ')
#             print(end = '    ')
#         print()

# print()

# print('SEM-8 TT')
# for row in range(5):
#     if row == tt1row:
#         print(end = '    ')
#         for i in range(max_len):
#             print(end = ' ')
#     if row == tt2row:
#         print(end = '    ')
#         for i in range(max_len):
#             print(end = ' ')
#     if tt3[row][0] == tt3[row][5]:
#         for col in range(5,6):
#             print(tt3[row][col],end = '')
#             for i in range(max_len - len(tt3[row][col])):
#                 print(end=' ')
#             print(end = '    ')
#         for col in range(5):
#             print(tt3[row][col],end = '')
#             for i in range(max_len - len(tt3[row][col])):
#                 print(end=' ')
#             print(end = '    ')
#         print()
#     else:
#         for col in range(6):
#             print(tt3[row][col],end = '')
#             for i in range(max_len - len(tt3[row][col])):
#                 print(end=' ')
#             print(end = '    ')
#         print()


#Code By Dawood Khatri

@app.route("/TT",methods=["GET","POST"])
def TT():
    data = request.get_data()
    data = data.decode()
    data = json.loads(data)
    print(data)
    
    faculty_sem4 = {}
    faculty_sem6 = {}
    faculty_sem8 = {}
    faculty = []
    subject_sem4 = []
    subject_sem6 = []
    subject_sem8 = []
    
    pr_faculty_sem4 = {}
    pr_faculty_sem6 = {}
    pr_faculty_sem8 = {}
    pr_faculty = []
    pr_subject_sem4 = []
    pr_subject_sem6 = []
    pr_subject_sem8 = []


    for i in range(len(data["faculty_sem4"])):
        key = data["faculty_sem4"][i]
        value = data["subject_sem4"][i]
        key = key.upper()
        value = value.upper()
        faculty_sem4[key] = value
        value = value + "-" + key
        subject_sem4.append(value)
        faculty.append(key)

    for i in range(len(data["faculty_sem6"])):
        key = data["faculty_sem6"][i]
        value = data["subject_sem6"][i]
        key = key.upper()
        value = value.upper()
        faculty_sem6[key] = value
        value = value + "-" + key
        subject_sem6.append(value)
        faculty.append(key)

    for i in range(len(data["faculty_sem8"])):
        key = data["faculty_sem8"][i]
        value = data["subject_sem8"][i]
        key = key.upper()
        value = value.upper()
        faculty_sem8[key] = value
        value = value + "-" + key
        subject_sem8.append(value)
        faculty.append(key)

    for i in range(len(data["pr_faculty_sem4"])):
        key = data["pr_faculty_sem4"][i]
        value = data["pr_subject_sem4"][i]
        key = key.upper()
        value = value.upper()
        pr_faculty_sem4[key] = value
        value = value + "-" + key
        pr_subject_sem4.append(value)
        pr_faculty.append(key)

    for i in range(len(data["pr_faculty_sem6"])):
        key = data["pr_faculty_sem6"][i]
        value = data["pr_subject_sem6"][i]
        key = key.upper()
        value = value.upper()
        pr_faculty_sem6[key] = value
        value = value + "-" + key
        pr_subject_sem6.append(value)
        pr_faculty.append(key)

    for i in range(len(data["pr_faculty_sem8"])):
        key = data["pr_faculty_sem8"][i]
        value = data["pr_subject_sem8"][i]
        key = key.upper()
        value = value.upper()
        pr_faculty_sem8[key] = value
        value = value + "-" + key
        pr_subject_sem8.append(value)
        pr_faculty.append(key)


    tt1 = generate_tt1(subject_sem4)
    col01,col23,col45 = three_column_of_two(tt1)
    tt2 = generate_tt2(col01,col23,col45)
    tt3 = generate_tt3(col01,col23,col45)

    tt2 = change_sub_sem6(faculty, faculty_sem4,faculty_sem6,tt2)
    tt3 = change_sub_sem8(faculty, faculty_sem4,faculty_sem8,tt3)

    tt1row = which_row(tt1)
    tt2row = which_row(tt2)
    tt3row = which_row(tt3)

    max_len = max_len_sub(subject_sem4,subject_sem6,subject_sem8,pr_subject_sem4,pr_subject_sem6,pr_subject_sem8)

    tt1 = add_practical(tt1,pr_subject_sem4)
    tt2 = add_practical(tt2,pr_subject_sem6)
    tt3 = add_practical(tt3,pr_subject_sem8)

    finalTT = []

    finalTT.append(tt1)
    finalTT.append(tt2)
    finalTT.append(tt3)

    print(finalTT)
    return json.dumps(finalTT)

if __name__ == "__main__": 
 app.run()