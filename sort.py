

#==========================================#

def sort_students_age_bubble(students: list[dict], order: str) -> list[dict]:
    """Function takes a list of dictionaries of student profiles, and sorts 
    the list based on increasing or decreasing order ('A' for ascending, 'D' for 
    descending) of age. If the key 'Age' is present in the dictionary, the list 
    is sorted as described above. If the key 'Age' is not present, an error 
    message is displayed, and the original list is returned. 

    Preconditions: Keys in all dictionaries in the the list 'students' must be 
    the same. 

    >>>sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}],
    "D")

    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]

    >>>sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")

    "Age" key is not present.
    [{"School":"GP"}, {"School":"MS"}]

    >>>sort_students_age_bubble([{"School": "GP", "Age": 45}, {"School": "MS", 
    "Age": 33}], "A")

    [{"School": "MS", "Age": 33}, {"School": "GP", "Age": 45}]
    """
    if "Age" in students[0]:
        if order == "A":
            swap = True
            while swap:
                swap = False
                for i in range(len(students) - 1):
                    if students[i]["Age"] > students[i + 1]["Age"]:
                        students[i], students[i +
                                              1] = students[i + 1], students[i]
                        swap = True
        elif order == "D":
            swap = True
            while swap:
                swap = False
                for j in range(len(students) - 1):
                    if students[j]["Age"] < students[j + 1]["Age"]:
                        students[j], students[j +
                                              1] = students[j + 1], students[j]
                        swap = True
        else:
            print("Invalid order input, please enter either 'A' or 'D'")

    else:
        print("Error, dictionary key 'Age' not found in dictionaries of list 'students'")

    return students

#==========================================#


def sort_students_time_selection(study_time: list[dict[str, float]], order: str) -> list[dict[str, float]]:
    """
    Sorts a list of dictionaries by the 'StudyTime' key in ascending or descending order.
    
    Preconditions: order is either 'A' for ascending order or 'D' for descending order.
    
    Examples:
    >>> sort_students_time_selection([{"StudyTime":10.2,"School":"GP"}, {"StudyTime":19.1,"School":"MS"}], "D")
    [{'StudyTime': 19.1, 'School': 'MS'}, {'StudyTime': 10.2, 'School': 'GP'}]
    
    >>> sort_students_time_selection([{"School":"GP"},{"School":"MS"}], "D")
    "StudyTime" key is not present
    [{"School":"GP"}, {"School":"MS"}]
    
    >>> sort_students_time_selection([{"StudyTime":5.5, "School":"LS"}, {"StudyTime":12.1, "School":"KL"}, {"StudyTime":9.3, "School":"OP"}], "A")
    [{'StudyTime': 5.5, 'School': 'LS'}, {'StudyTime': 9.3, 'School': 'OP'}, {'StudyTime': 12.1, 'School': 'KL'}]
    
    >>> sort_students_time_selection([{"StudyTime":1.5,"School":"MP"}, {"StudyTime":0.5,"School":"CN"}, {"StudyTime":2.5,"School":"IK"}], "D")
    [{'StudyTime': 2.5, 'School': 'IK'}, {'StudyTime': 1.5, 'School': 'MP'}, {'StudyTime': 0.5, 'School': 'CN'}]
    
    """
    if "StudyTime" in study_time[0]:
        nums = []
        for i in study_time:                # convert dict to list with tuples
            variable = 'StudyTime', i['StudyTime']
            nums.append(variable)
            
        if order == "D":           
            for index in range (len(nums)):         # sorting algorithm in descending order
                max_index = index
                
                for j in range(index + 1, len(nums)):
                    if nums[max_index][1] < nums[j][1]:
                        nums[max_index], nums[j] = nums[j], nums[max_index]
                study_time[index]['StudyTime'] = nums[index][1]
                
            return study_time    
        
        elif order == "A":            
            for index in range (len(nums)):         # sorting algorithm in ascending order
                min_index = index
                            
                for j in range(index + 1, len(nums)):
                    if nums[min_index][1] > nums[j][1]:
                        nums[min_index], nums[j] = nums[j], nums[min_index]
                study_time[index]['StudyTime'] = nums[index][1]
                
            return study_time 
    
    else:
        print("'StudyTime' key is not present")
        return study_time
        


#==========================================#

def sort_students_g_avg_insertion(sort: list, method: str) -> list:
    """
    >>> sort_students_g_avg_insertion( [{"G_Avg":7.2,"School":"GP"},
    {"G_Avg":9.1,"School":"MS"}], "D")
    [{"G_Avg": 9.1, "School":"MS"}, {"G_Avg":7.2, "School":"GP"}]

    >>> sort_students_g_avg_insertion([{"School":"GP"},{"School":"MS"}], "D")
    "G_Avg" key is not present  [{"School":"GP"}, {"School":"MS"}]
    """
    
    
    if "G_Avg" not in sort[0]:
        print("G_Avg is not present in the list")
        return

    n = len(sort)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if method == "A":
                if sort[j]["G_Avg"] > sort[j + 1]["G_Avg"]:
                    sort[j], sort[j + 1] = sort[j + 1], sort[j]
                    swapped = True
            elif method == "D":
                if sort[j]["G_Avg"] < sort[j + 1]["G_Avg"]:
                    sort[j], sort[j + 1] = sort[j + 1], sort[j]
                    swapped = True
            else:
                print(
                    "Invalid input parameter. Choose either A for ascending or D for descending order")
                return
        if not swapped:
            break
    return sort


#==========================================#
# Place your sort_students_failures_bubble function after this line
def sort_students_failures_bubble(sort: list, method: str) -> list:
    """Function sorts the given list in ascending order if method is A and descending order if method is D and returns a list in the specified order. sort has to be a list and method has to be either A or D otherwise function returns an error message. Also if the key failures is not present in the list, the function returns a message saying that the key failures is not present and returns the list without it. It is advised to edit my_list and input the list you wish to sort before calling the function.

    sort_students_failures_bubble(
    [{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    >>>[{"Failures": 19, "School":"MS"}, {"Failures":10, "School":"GP"}]

    sort_students_failures_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    >>>"Failures" key is not present.
    [{"School":"GP"}, {"School":"MS"}]
    """

    if "Failures" not in sort[0]:
        print("Failures key is not present.")
        return sort

    n = len(sort)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if method == "A":
                if sort[j]["Failures"] > sort[j + 1]["Failures"]:
                    sort[j], sort[j + 1] = sort[j + 1], sort[j]
                    swapped = True
            elif method == "D":
                if sort[j]["Failures"] < sort[j + 1]["Failures"]:
                    sort[j], sort[j + 1] = sort[j + 1], sort[j]
                    swapped = True
            else:
                print(
                    "Invalid input parameter. Choose either A for ascending or D for descending order")
                return sort
        if not swapped:
            break
    return sort


#==========================================#

def sort(students_info: list[dict[str, float]], arrange: str, att: str) -> list[dict]:
    """
    Sorts the list of students' dictionaries based on the given attribute and order.
    
    Parameters:
    -students_info must be a list of dictionaries, where each dictionary represents information about a student.
    -order must be a string of 'A' or 'D'.
    - attribute must be a string 'Age', 'StudyTime', 'G_Avg', or 'Failures' to determine the attribute used for sorting.

    Examples:
    >>> sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}], "D", "Age")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}] 

    >>> sort([{"School":"GP"},{"School":"MS"}], "D", "School")
    Cannot be sorted by "School"
    [{"School":"GP"}, {"School":"MS"}]

    >>> sort([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}], "A", "StudyTime")
    [{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}]

    """
    
    if att == 'StudyTime':
        return sort_students_time_selection(students_info, arrange)
    elif att == 'G_Avg':
        return sort_students_g_avg_insertion(students_info, arrange)   
    elif att == 'Failures':
        return sort_students_failures_bubble(students_info, arrange)
    elif att == 'Age':
        return sort_students_age_bubble(students_info, arrange)
    else:
        print("Cannot be sorted by '{}'".format(att))
        return students_info
    
