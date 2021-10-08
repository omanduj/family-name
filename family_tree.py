'''
Authors: Oscar Mandujano and Kassian O'Keefe
Date: 10 December 2018
Purpose: To compare two file, and find which pairs of people are related based on a single variabl. This instance it is the last name Wright, but it could be anything
Class: CS109
'''

import csv
from FamTree3 import drawTree

def readInscription():
    '''
    Purpose: To read the file called Inscriptions
    Parameters: None
    Return Value: data
    '''
    with open('OCBG_CWBryant_Inscriptions.csv', encoding = 'utf-8') as csvFile:
        CVS1 = csv.reader(csvFile, delimiter=',')
        data = []
        for line in CVS1:
            data.append(line)

    return data

def readKinfinder():
    '''
    Purpose: To read the file called Kinfinder
    Parameters: None
    Return Value: data
    '''
    with open('OCBG_CWBryant_Kinfinder.csv', encoding = 'utf-8') as csvFile:
        CVS1 = csv.reader(csvFile, delimiter=' ')
        data = []
        for line in CVS1:
            data.append(line)
    return data

def readFunctions():
    '''
    Purpose: To go through each of the above functions, search for instances where the thing being looked for appeared Next it checks the Bryant Number to make sure it is one person.
             Finally it subsitutes the values at a given cell into another file.
    Parameters: 1) readKinfinder
                2) readInscription
    Return Value: None
    '''
    kinData = readKinfinder()
    inscription = readInscription()

    name = 'Wright'                                                             #This is the thing being searched for in the list
    listsThatContainInscriptionData = []
    listsThatContainKinData = []

    for line in inscription:
        if name in line:
            listsThatContainInscriptionData.append(line)
    for line in kinData:
        if name in line:
            listsThatContainKinData.append(line)

    print('First Name, Page #, Original Order Listed, Age at Death, Last Name, Sex, Date of Birth, Date of Death, Bryant#, Inscriptions \n')
    for line in listsThatContainInscriptionData:
        bNumber = line[2]
        for row in listsThatContainKinData:
            for cell in row:
                if bNumber == cell:
                    page = line[0]
                    originalOrderListed = line[1]
                    age = line[8]
                    row[1] = page
                    row[2] = originalOrderListed
                    row[3] = age
                    print(row)





def main():
    readInscription()
    readKinfinder()
    readFunctions()
    drawTree()         #Family Tree for the Wright Family

main()
