from csv import *

with open('exampleCSV.csv') as csvfile:
    readCSV = reader(csvfile, delimiter=',')

    dates = []
    colors = []

    for row in readCSV:
        date = row[0]
        color = row[3]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    try:
        whatColor = input('De que color deseas saber la fecha? ')
        colsec = colors.index(whatColor.lower())

        print(dates[colsec])
    except Exception as e:
        print(e)

