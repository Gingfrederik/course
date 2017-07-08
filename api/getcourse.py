import requests
import pandas as pd
import io

times = [{
    "flag": "A",
    "time": "07:10 ~ 08:00"
}, {
    "flag": "1",
    "time": "08:10 ~ 09:00"
}, {
    "flag": "2",
    "time": "09:10 ~ 10:00"
}, {
    "flag": "3",
    "time": "10:10 ~ 11:00"
}, {
    "flag": "4",
    "time": "11:10 ~ 12:00"
}, {
    "flag": "B",
    "time": "12:10 ~ 13:00"
}, {
    "flag": "5",
    "time": "13:10 ~ 14:00"
}, {
    "flag": "6",
    "time": "14:10 ~ 15:00"
}, {
    "flag": "7",
    "time": "15:10 ~ 16:00"
}, {
    "flag": "8",
    "time": "16:10 ~ 17:00"
}, {
    "flag": "C",
    "time": "17:05 ~ 17:55"
}, {
    "flag": "D",
    "time": "18:00 ~ 18:50"
}, {
    "flag": "E",
    "time": "18:55 ~ 19:45"
}, {
    "flag": "F",
    "time": "19:50 ~ 20:40"
}, {
    "flag": "G",
    "time": "20:45 ~ 21:35"
}]
columnNames = ["CU_VALID", "BET_BLN", "BET_DEPT", "AUTOSET", "IS_STOP", "LANG_CODE",
               "OP_CODE", "OP_TYPE", "ADMIN_DEPT_NAME", "DEPT_ABVI_C", "CURS_NM_C_S",
               "OP_STDY", "OP_QUALITY", "SEX", "OP_CREDIT", "TEACHER_CNAME",
               "OP_TIME_1", "CLS_NAME_1", "OP_TIME_2", "CLS_NAME_2", "OP_TIME_3",
               "CLS_NAME_3", "MEMO1", "AUTHORITY_NAME", "OP_MAN", "FINAL_MAN",
               "DISTANCE", "DIV", "OP_T_COUNT", "TCH_T_COUNT", "ENG_COURSE", "ANOTHER",
               "CROSS_NAME", "IDCODE", "ACT_MAN", "CURS_LANG", "DEPT_BLN_ADMIN",
               "ACT_REMAIN"]

columnMap = {
    "CU_VALID": "課綱",
    "BET_BLN": "跨部",
    "BET_DEPT": "跨系",
    "AUTOSET": "已選",
    "IS_STOP": "停修與否",
    "LANG_CODE": "語音代碼",
    "OP_CODE": "課程代碼",
    "CURS_NM_C_S": "課程名稱",
    "OP_TYPE": "課程類別",
    "DEPT_ABVI_C": "開課班級",
    "OP_STDY": "必選修",
    "OP_QUALITY": "性質",
    "OP_CREDIT": "學分",
    "TEACHER_CNAME": "授課教師",
    "OP_TIME_1": "時間1",
    "CLS_NAME_1": "教室1",
    "OP_TIME_2": "時間2",
    "CLS_NAME_2": "教室2",
    "OP_TIME_3": "時間3",
    "CLS_NAME_3": "教室3",
    "MEMO1": "備註",
    "AUTHORITY_NAME": "權責單位",
    "OP_MAN": "開課人數",
    "FINAL_MAN": "實際修課人數",
    "OP_T_COUNT": "開課鐘點數",
    "TCH_T_COUNT": "教師授課鐘點數",
    "ACT_MAN": "選課登記人數",
    "CURS_LANG": "授課語言",
    "DEPT_BLN_ADMIN": "系代碼",
    "ACT_REMAIN": "選課餘額"
}

yearTerm = 1052
r = requests.get(
    "https://itouch.cycu.edu.tw/active_system/CourseQuerySystem/GetCourses.jsp?yearTerm="+str(yearTerm))
data = str(r.text)
data = data[2:len(data) - 5]
data = data.replace("@@", "\n")
csv = pd.read_csv(io.StringIO(data), header=None, sep="\|")
csv = csv.fillna(-1)
csv = csv.drop(csv.columns[[38]],axis=1)
csv.columns = columnNames
csv['BET_BLN'] = csv['BET_BLN'].map({'V': 1, -1:-1})
csv['BET_DEPT'] = csv['BET_DEPT'].map({'V': 1, -1:-1})
csv.to_json("./course.txt",orient='records', force_ascii=False)

