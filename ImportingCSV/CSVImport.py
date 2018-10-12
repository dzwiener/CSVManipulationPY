import csv

positiveResponse = ["yes", "Yes", "Y", "y", "Ya", "ya", "YES", "YA", "OK"]

def getFileString():
	#Grabs the user's fileName/Path
	userInputFileName = input("Please enter the name/path of your file:\n")

	#Open the file read only
	try:
		userFile = open(userInputFileName, 'r')
		
		return csv.reader(userFile, delimiter=',')
	except:
		if(positiveResponse.__contains__(str(input("The file was unreadable or was not found at the path. \nWould you like to try again?")))):
			getFileString()

def main():
	csvArray = getFileString()
	#csvArray is now an iterable array of the rows in the csv
	
	#Example1:
	for row in csvArray:
		print(str(row))
main()