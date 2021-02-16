import random as rnd
"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
# Настройки для создания школьных данных
classesNumber = 11
classLetters = ['а', 'б', 'в' , 'г']
scoresCount = 5

def generateScores():
    scores = []
    for score in range(scoresCount):
        scores.append(rnd.randint(2, 5))
    return scores

def generateSchoolData():
    school = []
    for number in range(1, classesNumber + 1):
        for letter in classLetters:
            school.append({'school_class': f'{number}{letter}', 'scores': generateScores()})
    return school

def averageScore(scores):
    if len(scores) == 0:
        return 0

    average = 0
    for score in scores:
        average += score
    return average / len(scores)

def printSchoolData(schoolData):
    for school_class in schoolData:
        print(school_class)

def printSchoolAverage(average):
    print(f'Средний балл по всей школе: {format(float(average), ".1f")}')

def main():
    schoolAverage = 0.0
    schoolData = generateSchoolData()
    classCount = len(schoolData)
    for school_class in schoolData:
        school_class['average'] = averageScore(school_class.get('scores', []))
        schoolAverage += school_class.get('average', 0)

    schoolAverage /= classCount
    printSchoolData(schoolData)
    printSchoolAverage(schoolAverage)

if __name__ == "__main__":
    main()
