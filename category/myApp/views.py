from django.db import connection
from django.shortcuts import render
import pandas as pd

outputStudents = []
outputProfessors = []
outputCounties = []
outputCovids = []


def clearDB(table):
    clearQuery = "truncate table {}"
    with connection.cursor() as cursor:
        cursor.execute(clearQuery.format(table))


def init_StudDB(request):
    df_stud = pd.read_csv('./myApp/templates/myApp/student_csv.csv', header=None, delimiter=',')
    df_stud.columns = ['id', 'name', 'score', 'county']

    clearDB('students')
    for i in range(1, len(df_stud)):
        stud_id = df_stud.iloc[i]['id']
        name = df_stud.iloc[i]['name']
        score = float(df_stud.iloc[i]['score'])
        county = df_stud.iloc[i]['county']

        insertQuery = "INSERT INTO students (studentID, name, score, county) VALUES('{}','{}','{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(stud_id, name, score, county))

    global outputStudents
    with connection.cursor() as cursor:
        sqlQueryStudents = "SELECT studentID, name, score, county FROM students;"
        cursor.execute(sqlQueryStudents)
        fetchResultStudents = cursor.fetchall()

    connection.commit()
    connection.close()

    for temp in fetchResultStudents:
        eachRow = {'studentID': temp[0], 'name': temp[1], 'score': temp[2], 'county': temp[3]}
        outputStudents.append(eachRow)

    return render(request, 'myApp/index.html', {"students": outputStudents,
                                                "professors": outputProfessors,
                                                "counties": outputCounties,
                                                "covids": outputCovids, })


def init_ProfDB(request):
    df_prof = pd.read_csv('./myApp/templates/myApp/professor_csv.csv', header=None, delimiter=',')
    df_prof.columns = ['facultyId', 'name', 'age', 'county']

    clearDB('professors')
    for i in range(1, len(df_prof)):
        faculty_id = df_prof.iloc[i]['facultyId']
        name = df_prof.iloc[i]['name']
        age = int(df_prof.iloc[i]['age'])
        county = df_prof.iloc[i]['county']

        insertQuery = "INSERT INTO professors (facultyID, name, age, county) VALUES('{}','{}','{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(faculty_id, name, age, county))

    global outputProfessors
    with connection.cursor() as cursor:
        sqlQueryProfessors = "SELECT facultyID, name, age, county FROM professors;"
        cursor.execute(sqlQueryProfessors)
        fetchResultProfessors = cursor.fetchall()

    connection.commit()
    connection.close()

    for temp in fetchResultProfessors:
        eachRow = {'facultyID': temp[0], 'name': temp[1], 'age': temp[2], 'county': temp[3]}
        outputProfessors.append(eachRow)

    return render(request, 'myApp/index.html', {"students": outputStudents,
                                                "professors": outputProfessors,
                                                "counties": outputCounties,
                                                "covids": outputCovids, })


def init_CountyDB(request):
    df_county = pd.read_csv('./myApp/templates/myApp/county_csv.csv', header=None, delimiter=',')
    df_county.columns = ['countyName', 'population', 'city']

    clearDB('counties')
    for i in range(1, len(df_county)):
        countyName = df_county.iloc[i]['countyName']
        population = int(df_county.iloc[i]['population'])
        city = df_county.iloc[i]['city']

        insertQuery = "INSERT INTO counties (countyName, population, city) VALUES('{}','{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(countyName, population, city))

    with connection.cursor() as cursor:
        sqlQueryCounties = "SELECT countyName, population, city FROM counties;"
        cursor.execute(sqlQueryCounties)
        fetchResultCounties = cursor.fetchall()

    connection.commit()
    connection.close()

    global outputCounties
    for temp in fetchResultCounties:
        eachRow = {'countyName': temp[0], 'population': temp[1], 'city': temp[2]}
        outputCounties.append(eachRow)

    return render(request, 'myApp/index.html', {"students": outputStudents,
                                                "professors": outputProfessors,
                                                "counties": outputCounties,
                                                "covids": outputCovids, })


def init_CovidDB(request):
    df_covid = pd.read_csv('./myApp/templates/myApp/covid_csv.csv', header=None, delimiter=',')
    df_covid.columns = ['patientId', 'city']

    clearDB('covid')
    for i in range(1, len(df_covid)):
        patient_id = df_covid.iloc[i]['patientId']
        city = df_covid.iloc[i]['city']

        insertQuery = "INSERT INTO covid (patientID, city) VALUES('{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(patient_id, city))

    with connection.cursor() as cursor:
        sqlQueryCovids = "SELECT patientID, city FROM covid;"
        cursor.execute(sqlQueryCovids)
        fetchResultCovids = cursor.fetchall()

    connection.commit()
    connection.close()

    global outputCovids
    for temp in fetchResultCovids:
        eachRow = {'patientID': temp[0], 'city': temp[1]}
        outputCovids.append(eachRow)

    return render(request, 'myApp/index.html',{"students": outputStudents,
                                               "professors": outputProfessors,
                                               "counties": outputCounties,
                                               "covids": outputCovids,})


def display(request):
    clearDB('students')
    clearDB('professors')
    clearDB('counties')
    clearDB('covid')
    return render(request, 'myApp/index.html')
