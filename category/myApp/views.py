from django.db import connection
from django.shortcuts import render
import pandas as pd


def display(request):
    df_stud = pd.read_csv('./student_csv.csv', header=None, delimiter=',')
    df_stud.columns = ['id', 'name', 'score', 'county']

    for i in range(1, len(df_stud)):
        stud_id = df_stud.iloc[i]['id']
        name = df_stud.iloc[i]['name']
        score = float(df_stud.iloc[i]['score'])
        county = df_stud.iloc[i]['county']

        insertQuery = "INSERT INTO students (studentID, name, score, county) VALUES('{}','{}','{}','{}')"

        with connection.cursor() as cursor:
            cursor.execute(insertQuery.format(stud_id, name, score, county))

    outputCategories = []
    outputOfQuery1 = []
    with connection.cursor() as cursor:
        sqlQueryCategories = "SELECT categoryid, categoryname, categorydescription FROM categories;"
        cursor.execute(sqlQueryCategories)
        fetchResultCategories = cursor.fetchall()

        sqlQuery1 = "SELECT categoryname, categorydescription FROM categories WHERE categoryid=7;"
        cursor.execute(sqlQuery1)
        fetchResultQuery1 = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultCategories:
            eachRow = {'categoryid': temp[0], 'categoryname': temp[1], 'categorydescription': temp[2]}
            outputCategories.append(eachRow)

        for temp in fetchResultQuery1:
            eachRow = {'categoryname': temp[0], 'categorydescription': temp[1]}
            outputOfQuery1.append(eachRow)

    return render(request, 'myApp/index.html',{"categories": outputCategories, "output1": outputOfQuery1})
