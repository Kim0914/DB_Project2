from django.db import connection
from django.shortcuts import render
import pandas as pd


def init_studDB():
    df_stud = pd.read_csv('./myApp/templates/myApp/student_csv.csv', header=None, delimiter=',')
    df_stud.columns = ['id', 'name', 'score', 'county']

    clearQuery = "truncate table students"
    with connection.cursor() as cursor:
        cursor.execute(clearQuery)

    for i in range(1, len(df_stud)):
        stud_id = df_stud.iloc[i]['id']
        name = df_stud.iloc[i]['name']
        score = float(df_stud.iloc[i]['score'])
        county = df_stud.iloc[i]['county']

        insertQuery = "INSERT INTO students (studentID, name, score, county) VALUES('{}','{}','{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(stud_id, name, score, county))


def init_FacultyDB():
    df_prof = pd.read_csv('./myApp/templates/myApp/professor_csv.csv', header=None, delimiter=',')
    df_prof.columns = ['facultyId', 'name', 'age', 'county']

    clearQuery = "truncate table professors"
    with connection.cursor() as cursor:
        cursor.execute(clearQuery)

    for i in range(1, len(df_prof)):
        faculty_id = df_prof.iloc[i]['facultyId']
        name = df_prof.iloc[i]['name']
        age = int(df_prof.iloc[i]['age'])
        county = df_prof.iloc[i]['county']

        insertQuery = "INSERT INTO professors (facultyID, name, age, county) VALUES('{}','{}','{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(faculty_id, name, age, county))


def init_CountyDB():
    df_county = pd.read_csv('./myApp/templates/myApp/county_csv.csv', header=None, delimiter=',')
    df_county.columns = ['countyName', 'population', 'city']

    clearQuery = "truncate table counties"
    with connection.cursor() as cursor:
        cursor.execute(clearQuery)

    for i in range(1, len(df_county)):
        countyName = df_county.iloc[i]['countyName']
        population = int(df_county.iloc[i]['population'])
        city = df_county.iloc[i]['city']

        insertQuery = "INSERT INTO counties (countyName, population, city) VALUES('{}','{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(countyName, population, city))


def init_CovidDB():
    df_covid = pd.read_csv('./myApp/templates/myApp/covid_csv.csv', header=None, delimiter=',')
    df_covid.columns = ['patientId', 'city']

    clearQuery = "truncate table covid"
    with connection.cursor() as cursor:
        cursor.execute(clearQuery)

    for i in range(1, len(df_covid)):
        patient_id = df_covid.iloc[i]['patientId']
        city = df_covid.iloc[i]['city']

        insertQuery = "INSERT INTO covid (patientID, city) VALUES('{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(patient_id, city))


def display(request):

    init_studDB()
    init_FacultyDB()
    init_CountyDB()
    init_CovidDB()

    outputStudents = []
    outputProfessors = []
    outputCovids = []
    outputCounties = []

    outputOfQuery1 = []
    with connection.cursor() as cursor:
        sqlQueryStudents = "SELECT studentID, name, score, county FROM students;"
        cursor.execute(sqlQueryStudents)
        fetchResultStudents = cursor.fetchall()

        sqlQueryProfessors = "SELECT facultyID, name, age, county FROM professors;"
        cursor.execute(sqlQueryProfessors)
        fetchResultProfessors = cursor.fetchall()

        sqlQueryCounties = "SELECT countyName, population, city FROM counties;"
        cursor.execute(sqlQueryCounties)
        fetchResultCounties = cursor.fetchall()

        sqlQueryCovids = "SELECT patientID, city FROM covid;"
        cursor.execute(sqlQueryCovids)
        fetchResultCovids = cursor.fetchall()

        sqlQuery1 = "SELECT categoryname, categorydescription FROM categories WHERE categoryid=7;"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultStudents:
            eachRow = {'studentID': temp[0], 'name': temp[1], 'score': temp[2], 'county': temp[3]}
            outputStudents.append(eachRow)

        for temp in fetchResultProfessors:
            eachRow = {'facultyID': temp[0], 'name': temp[1], 'age': temp[2], 'county': temp[3]}
            outputProfessors.append(eachRow)

        for temp in fetchResultCounties:
            eachRow = {'countyName': temp[0], 'population': temp[1], 'city': temp[2]}
            outputCounties.append(eachRow)

        for temp in fetchResultCovids:
            eachRow = {'patientID': temp[0], 'city': temp[1]}
            outputCovids.append(eachRow)

        for temp in fetchResultQuery1:
            eachRow = {'categoryname': temp[0], 'categorydescription': temp[1]}
            outputOfQuery1.append(eachRow)

    return render(request, 'myApp/index.html',{"students": outputStudents,
                                               "professors": outputProfessors,
                                               "counties": outputCounties,
                                               "covids": outputCovids,
                                               "output1": outputOfQuery1}
                  )
