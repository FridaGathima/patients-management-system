def main():

    #initialize patients list
    patientsList = []
    infile = open("allPatientsList", "r") #open the txt file when program loads
    line = infile.readline() # to read line by line
    while line:
        patientsList.append(line.rstrip("\n)").split(","))
        line = infile.readline() #will append and read the txt file
    choice = 0
    while choice != 4: # exit the loop when 4 is selected
        print("***Patients Management System***")
        print("1) Add a Patient")
        print("2) Lookup a Patient")
        print("3) Display Patients")
        print("4) Quit")
        choice = int(input()) # convert input to integer

        if choice == 1:
            print("Adding a Patient...")
            patientName = input("Enter the name of the Patient: ")
            patientIdNumber = input("Enter the ID Number of the Patient: ")
            patientPhoneNumber = input("Enter the Phone Number of the Patient: ")
            patientAge = input("Enter the age of the patient: ")
           
            patientsList.append([patientName, patientIdNumber, patientPhoneNumber, patientAge])

        elif choice == 2:
            print("Looking up a Patient...")
            keyword = input("Enter the ID Number: ")
            for patient in patientsList: #iterate over patients that exist in PatientsList
                if keyword in patient:  
                    print(patient)   

        elif choice == 3:
            print("Displaying all Patients...")
            for i in range(len(patientsList)):    #iterate over the patientsList length
                print(patientsList[i]) #display all patients in the patientsList

        else:
            print("Quitting Program")

    print("Program Terminated!")


# saving to external txt file. unable to save to connect with database

    allPatientsFile = open("allPatientsList.txt", "w") #open method takes 2 arguments, the name of the file and the mode
    for patient in patientsList: # iterate over the patientsList
        allPatientsFile.write(",".join(patient) + "\n") #.join()-concatenates any number of strings, \n- to save in a new line
    allPatientsFile.close() # to close the file

if __name__ == "__main__":
    main()