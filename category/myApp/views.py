from django.db import connection
from django.shortcuts import render
from django.shortcuts import redirect
import pandas as pd


def clearDB(table):
    clearQuery = "truncate table {}"
    with connection.cursor() as cursor:
        cursor.execute(clearQuery.format(table))


def init_StudDB(request):
    df_stud = pd.read_csv('./myApp/templates/myApp/students.csv', header=None, delimiter=',')
    df_stud.columns = ['id', 'name', 'score', 'county']

    clearDB('students')
    for i in range(len(df_stud)):
        stud_id = df_stud.iloc[i]['id']
        name = df_stud.iloc[i]['name']
        score = float(df_stud.iloc[i]['score'])
        county = df_stud.iloc[i]['county']

        insertQuery = "INSERT INTO students (studentID, name, score, county) VALUES('{}','{}','{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(stud_id, name, score, county))

    return redirect('show')


def init_ProfDB(request):
    df_prof = pd.read_csv('./myApp/templates/myApp/professors.csv', header=None, delimiter=',')
    df_prof.columns = ['facultyId', 'name', 'age', 'county']

    clearDB('professors')
    for i in range(len(df_prof)):
        faculty_id = df_prof.iloc[i]['facultyId']
        name = df_prof.iloc[i]['name']
        age = int(df_prof.iloc[i]['age'])
        county = df_prof.iloc[i]['county']

        insertQuery = "INSERT INTO professors (facultyID, name, age, county) VALUES('{}','{}','{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(faculty_id, name, age, county))

    return redirect('show')


def init_CountyDB(request):
    df_county = pd.read_csv('./myApp/templates/myApp/counties.csv', header=None, delimiter=',')
    df_county.columns = ['countyName', 'population', 'city']

    clearDB('counties')
    for i in range(len(df_county)):
        countyName = df_county.iloc[i]['countyName']
        population = int(df_county.iloc[i]['population'])
        city = df_county.iloc[i]['city']

        insertQuery = "INSERT INTO counties (countyName, population, city) VALUES('{}','{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(countyName, population, city))
    return redirect('show')


def init_CovidDB(request):
    df_covid = pd.read_csv('./myApp/templates/myApp/covid.csv', header=None, delimiter=',')
    df_covid.columns = ['patientId', 'city']

    clearDB('covid')
    for i in range(len(df_covid)):
        patient_id = df_covid.iloc[i]['patientId']
        city = df_covid.iloc[i]['city']

        insertQuery = "INSERT INTO covid (patientID, city) VALUES('{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(patient_id, city))

    return redirect('show')


def get_studData():
    # SELECT students table data
    outputStudents = []
    with connection.cursor() as cursor:
        sqlQueryStudents = "SELECT studentID, name, score, county FROM students;"
        cursor.execute(sqlQueryStudents)
        fetchResultStudents = cursor.fetchall()

    connection.commit()
    connection.close()

    for temp in fetchResultStudents:
        eachRow = {'studentID': temp[0], 'name': temp[1], 'score': temp[2], 'county': temp[3]}
        outputStudents.append(eachRow)

    return outputStudents


def get_profData():
    # SELECT professors table data
    outputProfessors = []
    with connection.cursor() as cursor:
        sqlQueryProfessors = "SELECT facultyID, name, age, county FROM professors;"
        cursor.execute(sqlQueryProfessors)
        fetchResultProfessors = cursor.fetchall()

    connection.commit()
    connection.close()

    for temp in fetchResultProfessors:
        eachRow = {'facultyID': temp[0], 'name': temp[1], 'age': temp[2], 'county': temp[3]}
        outputProfessors.append(eachRow)

    return outputProfessors


def get_countyData():
    # SELECT counties table data
    outputCounties = []
    with connection.cursor() as cursor:
        sqlQueryCounties = "SELECT countyName, population, city FROM counties;"
        cursor.execute(sqlQueryCounties)
        fetchResultCounties = cursor.fetchall()

    connection.commit()
    connection.close()

    for temp in fetchResultCounties:
        eachRow = {'countyName': temp[0], 'population': temp[1], 'city': temp[2]}
        outputCounties.append(eachRow)

    return outputCounties


def get_covidData():
    # SELECT covid table data
    outputCovids = []
    with connection.cursor() as cursor:
        sqlQueryCovids = "SELECT patientID, city FROM covid;"
        cursor.execute(sqlQueryCovids)
        fetchResultCovids = cursor.fetchall()

    connection.commit()
    connection.close()

    for temp in fetchResultCovids:
        eachRow = {'patientID': temp[0], 'city': temp[1]}
        outputCovids.append(eachRow)

    return outputCovids


def query_one():
    # ---------------- Query 1 Start ---------------- #
    outputQuery1 = []
    with connection.cursor() as cursor:
        sqlQuery1 = '''
            SELECT county as countyName, round(avg(score), 4) as averageScore 
            FROM students 
            GROUP BY county 
            ORDER BY county ASC;
        '''
        cursor.execute(sqlQuery1)
        fetchResult1 = cursor.fetchall()

    connection.commit()
    connection.close()

    for temp in fetchResult1:
        eachRow = {'countyName': temp[0], 'averageScore': temp[1]}
        outputQuery1.append(eachRow)

    # ---------------- Query 1 END ---------------- #
    return outputQuery1


def query_two():
    # ---------------- Query 2 Start ---------------- #
    outputQuery2 = []
    with connection.cursor() as cursor:
        sqlQuery2 = '''
            SELECT city as cityName, round((avg(score)), 4) as averageScore
            FROM students s1, counties c1
            WHERE s1.county = c1.countyName
            GROUP BY city
            ORDER BY city ASC;
        '''
        cursor.execute(sqlQuery2)
        fetchResult2 = cursor.fetchall()

    connection.commit()
    connection.close()

    for temp in fetchResult2:
        eachRow = {'cityName': temp[0], 'averageScore': temp[1]}
        outputQuery2.append(eachRow)

    # ---------------- Query 2 END ---------------- #
    return outputQuery2


def query_three():
    outputQuery3 = []

    return outputQuery3


def query_four():
    outputQuery4 = []

    return outputQuery4


def query_five():
    outputQuery5 = []

    return outputQuery5


def show_Data(request):
    outputStudents = get_studData()
    outputProfessors = get_profData()
    outputCounties = get_countyData()
    outputCovids = get_covidData()

    # ---------------- Query statement START ---------------- #
    outputQuery1 = query_one()
    outputQuery2 = query_two()
    outputQuery3 = query_three()
    outputQuery4 = query_four()
    outputQuery5 = query_five()
    # ---------------- Query statement END ---------------- #

    return render(request, 'myApp/index.html', {"students": outputStudents,
                                                "professors": outputProfessors,
                                                "counties": outputCounties,
                                                "covids": outputCovids,
                                                "query1s": outputQuery1,
                                                "query2s": outputQuery2,
                                                "query3s": outputQuery3,
                                                "query4s": outputQuery4,
                                                "query5s": outputQuery5})


def display(request):
    clearDB('students')
    clearDB('professors')
    clearDB('counties')
    clearDB('covid')
    return render(request, 'myApp/index.html')
