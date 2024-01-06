
# Place your student_school_list function after this line
def student_school_list(file, school):
    """Returns a list of students each stored as dictionaries with the same 
    school as the input parameter.

    Preconditions: The file exists, The school is in the file

    >>> student_school_list('student-mat.csv','GP')
    [{'Age':18, 'StudyTime':1.8, 'Failures': 0, 'Health': 3, 'Absences': 6,    'G1': 5, 'G2': 6, 'G3': 6},...]

    >>> student_school_list('student-mat.csv','CF')
    [{'Age':16, 'StudyTime':2, 'Failures': 1, 'Health': 5, 'Absences': 4,    'G1': 10, 'G2': 12, 'G3': 12},...]
    """
    infile = open(file, 'r')
    my_list = []
    count = 0

    for line in infile:
        line = line.replace("\n", "").split(',')
        if count == 0:
            header = line

        elif line[0] == school:
            student = {header[1]: line[1], header[2]: line[2], header[3]: line[3], header[4]: line[4],
                       header[5]: line[5], header[6]: line[6], header[7]: line[7], header[8]: line[8]}
            my_list.append(student)
        count += 1
    infile.close()
    return my_list


#==========================================#
# Place your student_health_list function after this line
def student_health_list(filename: str, health_in_list: int) -> list:
    """ This function returns all the students with the same health number.
    >>> student_health_list('student-mat.csv', 2)
    [{'School': 'MS', 'Age': 20, 'StudyTime': 1.2, 'Failures': 1, 'Absences': 10,
    'G1': 9, 'G2': 11, 'G3': 7}, {another element}, …]
    """
    students = []
    infile = open(filename, 'r')
    
    for line in infile:
        word_list = line.split(",")
        
        if word_list[4] == str(health_in_list):
            student = {'School': word_list[0], 'Age': int(word_list[1]), 'Studytime': float(word_list[2]), 'Failures': int(word_list[3]), 'Absences': int(word_list[5]), 'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            
            students.append(student)
    infile.close()
    return students

#==========================================#
# Place your student_age_list function after this line
def student_age_list(filename: 'student-mat.csv', Age: int) -> list[str]:
    """This function returns all the data associated with the input age number as a part of a dictionary. 
    parameters: school: str, StudyTime: float, Failures: int, Health: int, Absences: int, G1: int, G2: int, G3: int.
    >>> student_age_list('student-mat.csv', 15)
    [ {'School': 'GP', 'StudyTime': 4.2, 'Failures': 3, 'Health': 3, 'Absences': 6, 'G1': 7, 'G2': 8, 'G3': 10},
    {another element},
     … ]
    """
    students = []
    infile = open(filename, 'r')
    for line in infile:
        word_list = line.split(",")
        if word_list[1] == str(Age):
            student = {'School': str(word_list[0]), 'StudyTime': float(word_list[2]), 'Failures': int(word_list[3]), 'Health': int(
                word_list[4]), 'Absences': int(word_list[5]), 'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}

            students.append(student)
    infile.close()
    return students



#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(filename: str,fail_num: int) -> list:
    """ Returns a list of students each represented as a dictionary, who have failed the same number of times
       as specified by fail_num.
       
       Parameters: fail_num >= 0.
    
    Examples:
    >>>>>> student_failures_list('student-mat.csv', 20)
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7,
      'G1': 12, 'G2': 13, 'G3': 14},
      {another element},
      ...
    ]
    """
    students = []
    infile = open(filename, "r")
    
    for line in infile:
        word_list = line.split(",")
        
        
        
        
        if word_list[3]   == str(fail_num):
            student = {'School': word_list[0],'Age': int(word_list[1]),'StudyTime': float(word_list[2]), 'Health': int(word_list[4]), 'Absences': int(word_list[5]),'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            
            students.append(student)
    infile.close()       
    return students


#==========================================#
# Place your load_data function after this line

# Place your load_data function after this line
def load_data(file: str, attribute: tuple) -> list:
    """
    Returns a list of students (stored as a dictionary) where the keys of the dictionary are the labels for all attributes in the file except for the attribute that's called.
    Parameters: attribute must have only two values as a tuple, the first one is the data and the second one being the value of the attribute. If "All" is called the second one can be ignored
    
    >>> load_data('student-mat.csv', ('Failures', 0))
    [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14},
    {another element},
    ...
    ]
    >>> load_data('student-mat.csv', ('All',-1))
    [{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
    'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14}, {another element},
    ...]
    >>> load_data('student-mat.csv', (‘G1’, 10)) 
     [] 
    """
    if attribute[0] == 'School':
        return student_school_list(file, attribute[1])
    elif attribute[0] == 'Age':
        return student_age_list(file, attribute[1])
    elif attribute[0] == 'Health':
        return student_health_list(file, attribute[1])
    elif attribute[0] == 'Failures':
        return student_failures_list(file, attribute[1])
    elif attribute[0] == "All":
        infile = open(file, "r")
        lines = infile.readlines()[1:]
        emp = []
        for i in lines:
            word_list = i.strip().split(",")
            
            student = {'School': word_list[0],'Age': int(word_list[1]),'StudyTime': float(word_list[2]),'Failures': int(word_list[3]), 'Health': int(word_list[4]), 'Absences': int(word_list[5]),'G1': int(word_list[6]), 'G2': int(word_list[7]), 'G3': int(word_list[8])}
            emp.append(student)
        infile.close()
        return emp        
          
            
    else:
        return []


#==========================================#
# Place your add_average function after this line
def add_average(avg : list[dict]) -> list[dict]:
    """ Returns the average of the student's grades (G1, G2, and G3) given a list of student dictionaries.
    Preconditions: The student dictionaries should contain only the keys 'G1', 'G2', and 'G3'.
    Example: 
    >>> add_average([ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7,
                              'G1': 5, 'G2': 6, 'G3': 6},
                           {another element},...])
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
    'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6,
    'G_Avg': 5.67 }, {another element},...]
    
    >>> add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0,
    'Abscences': 0, 'G1': 10, 'G2': 8, 'G3': 9}])
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0,
    'Abscences': 0, 'G1': 10, 'G2': 8, 'G3': 9, 'G_avg': 9.0}]
    
    >>>add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0,
    'Abscences': 0, 'G1': 11, 'G2': 11, 'G3': 11}])
    [{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0,
    'Abscences': 0, 'G1': 11, 'G2': 11 'G3': 11,'G_avg':11.0}]
    """
    empty_list = []
    for i in avg:
        marks  = (i['G1'] + i ['G2'] + i['G3']) / 3
        
        list  = i['G_Avg'] =  round(marks,2)
        
        empty_list.append(i)
        
    return empty_list
        



