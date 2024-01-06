
#import check module here
import check 
#import load_data module here
from load_data import student_school_list
from load_data import student_age_list
from load_data import student_health_list
from load_data import student_failures_list
from load_data import load_data
from load_data import add_average



# Place test_return_list function here 
def test_return_list():
    #Complete the function with your test cases
    
    #test that student_school_list returns a list (3 different test cases required)
    check.equal(isinstance(student_school_list('student-test.csv','GP'), list), True)
    check.equal(isinstance(student_school_list('student-test.csv',''), list), True)
    check.equal(isinstance(student_school_list('student-test.csv','hello'), list), True)
    
    #test that student_age_list returns a list (3 different test cases required)
    check.equal(isinstance(student_age_list('student-test.csv',18), list), True)
    check.equal(isinstance(student_age_list('student-test.csv', 0), list), True)
    check.equal(isinstance(student_age_list('student-test.csv', -19), list), True)
    #test that student_health_list returns a list (3 different test cases required)
    check.equal(isinstance(student_health_list('student-test.csv',8), list), True)
    check.equal(isinstance(student_health_list('student-test.csv', 12), list), True)
    check.equal(isinstance(student_health_list('student-test.csv', 100), list), True)    
    
    #test that student_failures_list returns a list (3 different test cases required)
    check.equal(isinstance(student_failures_list('student-test.csv',0), list), True)
    check.equal(isinstance(student_failures_list('student-test.csv', 2), list), True)
    check.equal(isinstance(student_failures_list('student-test.csv', 3), list), True)    
        
    
    #test that load_data returns a list (6 different test cases required)
    check.equal(isinstance(load_data('student-test.csv',('School', 'MB')), list), True)
    check.equal(isinstance(load_data('student-test.csv',('Age', 19)), list), True)        
    check.equal(isinstance(load_data('student-test.csv',('Health', 5)), list), True)
    check.equal(isinstance(load_data('student-test.csv',('Failures', 'MB')), list), True)
    check.equal(isinstance(load_data('student-test.csv',('All')), list), True)
    check.equal(isinstance(load_data('student-test.csv',('G1', 10)), list), True)
     #test that add_average returns a list (3 different test cases required)
    check.equal(isinstance(([{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0,
    'Abscences': 0, 'G1': 11, 'G2': 11, 'G3': 11}]), list), True)
    check.equal(isinstance(([{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0,
    'Abscences': 0, 'G1': 10, 'G2': 8, 'G3': 9}]), list), True)
    check.equal(isinstance(([{'School': 'AP', 'Age': 19, 'StudyTime': 3, 'Failures': 1,
    'Abscences': 5, 'G1': 9, 'G2': 8, 'G3': 9}]), list), True)     
    check.summary()



# Place test_return_list_correct_lenght function here
def test_return_list_correct_lenght():
    # Complete the function with your test cases

    # test that student_school_list returns a list with the correct lenght (3 different test cases required)
    check.equal(len(student_school_list('student-test.csv', 'GP')), 3)
    check.equal(len(student_school_list('student-test.csv', 'MP')), 0)
    check.equal(len(student_school_list('student-test.csv', 'BD')), 3)
    # test that student_age_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_age_list("student-test.csv", 15)), 3)
    check.equal(len(student_age_list("student-test.csv", 18)), 4)
    check.equal(len(student_age_list("student-test.csv", 21)), 0)
    # test that student_health_list returns a list  with the correct lenght (3 different test cases required)
    check.equal(len(student_health_list("student-test.csv", 3)), 8)
    check.equal(len(student_health_list("student-test.csv", 5)), 3)
    check.equal(len(student_health_list("student-test.csv", 2)), 0)
    # test that student_failures_list returns a list   with the correct lenght(3 different test cases required)
    check.equal(
        len(student_failures_list("student-test.csv", 3)), 1)
    check.equal(
        len(student_failures_list("student-test.csv", 2)), 2)
    check.equal(
        len(student_failures_list("student-test.csv", 1)), 1)
    # test that load_data returns a list  with the correct lenght (6 different test cases required)
    check.equal(len(load_data("student-test.csv", ("All", -1))), 15)
    check.equal(len(load_data("student-test.csv", ("Failures", 4))), 0)
    check.equal(len(load_data("student-test.csv", ("Health", 3))), 8)
    check.equal(len(load_data("student-test.csv", ("Age", 15))), 3)
    check.equal(len(load_data("student-test.csv", ("School", "GP"))), 3)
    check.equal(len(load_data("student-test.csv", ("All", "4"))), 15)
    # test that add_average returns a list   with the correct lenght (3 different test cases required)
    check.equal(len(add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2,
                'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])), 1)
    check.equal(len(add_average([{'School': 'MB', 'Age': 16, 'StudyTime': 2,
                'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}])), 1)
    check.equal(len(add_average([{'School': 'CF', 'Age': 15, 'StudyTime': 5,
                'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}])), 1)


    check.summary()

#Place test_return_correct_dict_inside_list function here
def test_return_correct_dict_inside_list():
    # Complete the function with your test cases
    
    # test that student_school_list returns a correct dictionary inside the list (3 different test cases required)
    school_1 = student_school_list('student-test.csv', 'GP')
    school_2 = student_school_list('student-test.csv', 'BD')
    school_3 = student_school_list('student-test.csv', 'MS')
    
    # case 1
    check.equal(school_1[0],{'Age': 18, 'Studytime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    # case 2
    check.equal(school_2[-1], ({'Age': 17, 'Studytime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}))
    #case 3
    check.equal(school_3[1], ({'Age': 17, 'Studytime': 3.0, 'Failures': 0, 'Health': 1, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}))
    
    
    # test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)
    age_1 = student_age_list('student-test.csv', 15)
    age_2 = student_age_list('student-test.csv', 17)
    age_3 = student_age_list('student-test.csv', 18)
    
    #case 1
    check.equal(age_1[0],{'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    # case 2
    check.equal(age_2[-1], {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14})
    #case 3
    check.equal(age_3[1], {'School': 'BD', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8})
    
    # test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)
    health_1 = student_health_list('student-test.csv', 3)
    health_2 = student_health_list('student-test.csv', 4)
    health_3 = student_health_list('student-test.csv', 1)
    
    #case 1
    check.equal(health_1[0],{'School': 'GP', 'Age': 18, 'Studytime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    # case 2
    check.equal(health_2[-1], {'School': 'MS', 'Age': 17, 'Studytime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14})
    #case 3
    check.equal(health_3[0], {'School': 'MS', 'Age': 17, 'Studytime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9})
    
    
    
    
    
    # test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)
    failure_1 = student_failures_list('student-test.csv', 2)
    failure_2 = student_failures_list('student-test.csv', 0)
    failure_3 = student_failures_list('student-test.csv', 1)
    
    #case 1
    check.equal(failure_1[0],{'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7})
    # case 2
    check.equal(failure_2[-1], {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8})
    #case 3
    check.equal(failure_3[0], {'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12})
        
    
    # test that load_data returns a correct dictionary inside the list (6 different test cases required)
    data_1 = load_data('student-test.csv',('Failures', 0))
    data_2 = load_data('student-test.csv',('Health', 3))
    data_3 = load_data('student-test.csv',('Age' , 15))
    data_4 = load_data('student-test.csv',('School', 'GP'))
    data_5 = load_data('student-test.csv', ('All',))
    data_6 = load_data('student-test.csv', ('G1', 10))
    
    #case 1
    check.equal(data_1[0],{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    # case 2
    check.equal(data_2[0], {'School': 'GP', 'Age': 18, 'Studytime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    #case 3
    check.equal(data_3[0],{'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    
    #case 4
    check.equal(data_4[0],{'Age': 18, 'Studytime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    # case 5
    check.equal(data_5[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    #case 6
    check.equal(data_6,[])
        
    #Place test_add_average function here
    average_1 = add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6}])
    average_2 = add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0,
    'Abscences': 0, 'G1': 10, 'G2': 8, 'G3': 9}])
    average_3 = add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0,'Abscences': 0, 'G1': 11, 'G2': 11, 'G3': 11}, {'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Abscences': 0, 'G1': 11, 'G2': 11,'G3': 11,'G_avg':11.0}])
    
    #case 1
    check.equal(data_1,[{'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1, 'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}])
    # case 2
    check.equal(data_2, [{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Abscences': 0, 'G1': 10, 'G2': 8, 'G3': 9, 'G_Avg': 9.0}])
    #case 3
    check.equal(data_3,[{'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Abscences': 0, 'G1': 11, 'G2': 11, 'G3': 11, 'G_Avg': 11.0}, {'School': 'GP', 'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Abscences': 0, 'G1': 11, 'G2': 11, 'G3': 11, 'G_avg': 11.0, 'G_Avg': 11.0}])
    
    check.summary()



def test_add_average():
    # Complete the function with your test cases

    # test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    check.equal(len(add_average(load_data('student-test.csv', ('School', 'BD')))),
                len(load_data('student-test.csv', ('School', 'BD'))))
    check.equal(len(add_average(load_data('student-test.csv', ('Health', '3')))),
                len(load_data('student-test.csv', ('Health', '3'))))
    check.equal(len(add_average(load_data('student-test.csv', ('Age', '15')))),
                len(load_data('student-test.csv', ('Age', '15'))))
    check.equal(len(add_average(load_data('student-test.csv', ('Failures', 0)))),
                len(load_data('student-test.csv', ('Failures', 0))))
    check.equal(len(add_average(load_data('student-test.csv', ('All', 5)))),
                len(load_data('student-test.csv', ('All', 5))))

    # test that the function returns an empty list when it is called whith an empty list
    check.equal(len(add_average([])), 0)

    # test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    check.equal(len((add_average(load_data('student-test.csv', ('School', 'BD'))))[0].keys()),
                len((load_data('student-test.csv', ('School', 'BD')))[0].keys()) + 1)
    check.equal(len((add_average(load_data('student-test.csv', ('Health', '3'))))[0].keys()),
                len((load_data('student-test.csv', ('Health', 3)))[0].keys()) + 1)
    check.equal(len((add_average(load_data('student-test.csv', ('Age', '15'))))[0].keys()),
                len((load_data('student-test.csv', ('Age', '15')))[0].keys()) + 1)
    check.equal(len((add_average(load_data('student-test.csv', ('Failures', 0))))[0].keys()),
                len((load_data('student-test.csv', ('Failures', 0)))[0].keys()) + 1)
    check.equal(len((add_average(load_data('student-test.csv', ('All', 5))))[0].keys()),
                len((load_data('student-test.csv', ('All', 5)))[0].keys()) + 1)

    # test that the G_Avg value is properly calculated  (5 different test cases required)
    check.equal(add_average(load_data('student-test.csv',
                                                          ('School', 'BD')))[0].get('G_Avg'), 8.0)   # school
    check.equal(add_average(load_data('student-test.csv',
                                                          ('Health', 3)))[0].get('G_Avg'), 5.67)     # health
    check.equal(add_average(load_data('student-test.csv',
                                                          ('Age', '15')))[2].get('G_Avg'), 7.0)      # age
    check.equal(add_average(load_data('student-test.csv',
                                                          ('Failures', 0)))[-1].get('G_Avg'), 8.33)  # failures
    check.equal(add_average(load_data('student-test.csv', ('All', 5)))[0].get('G_Avg'), 5.67)  # all

    check.summary()

    




    
