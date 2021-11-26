#3rd class
semester = int
courses_offered = int
courses = str
course_list = []
scores = int
score_list = []
grade = str
grade_list = []
gp = float
gp_list = []
point = int
point_list = []
point_unit = int
point_unit_list = []
unit = int
unit_list = []

def accept_courses():
    global courses_offered
    global courses
    global course_list
    global scores
    global score_list
    global grade
    global grade_list
    global point
    global point_list
    global point_unit
    global point_unit_list
    global unit
    global unit_list
    global semester
    #semester = int(input("How many semesters are you entering, please!! : "))
    courses_offered = int(input("How many courses are you entering? "))
    for i in range(courses_offered):
        i=+1
        courses = input("Enter the list of courses you offer respectively..: ")
        course_list.append(courses)
        
    for i in range(courses_offered):
        scores = int(input(f"Enter the score for, {course_list[i]} : "))
        score_list.append(scores)
    for i in range(courses_offered):
        unit = int(input(f"Enter the unit for {course_list[i]} : "))
        unit_list.append(unit)
    
            
def grade_score():
    global courses_offered
    global courses
    global course_list
    global scores
    global score_list
    global grade
    global grade_list
    global point
    global point_list
    global point_unit
    global point_unit_list
    global unit
    global unit_list
    for i in range(courses_offered):
        if score_list[i] >= 80 and score_list[i] <= 100:
            grade = "A"
            point = 6
        elif score_list[i] >= 70 and score_list[i] <=80:
            grade = "B"
            point = 5
        elif score_list[i] >= 50 and score_list[i] <= 69:
            grade = "C"
            point = 4
        elif score_list[i] >= 40 and score_list[i] <= 49:
            grade = "D"
            point = 3
        elif score_list[i] >= 30 and score_list[i] <= 39:
            grade = "E"
            point = 2
        elif score_list[i] >= 0 and score_list[i] <= 29:
            grade = "F"
            point = 1 
        else:
            print("INVALID!!!Error!!!!!raised!!!")
        grade_list.append(grade)
        point_list.append(point)
        
def point_u():
    global courses_offered
    global courses
    global course_list
    global scores
    global score_list
    global grade
    global grade_list
    global point
    global point_list
    global point_unit
    global point_unit_list
    global unit
    global unit_list
    for i in range(courses_offered):
        point_unit = unit_list[i]*point_list[i]
        point_unit_list.append(point_unit)    

def result_print():
    global courses_offered
    global courses
    global course_list
    global scores
    global score_list
    global grade
    global grade_list
    global gp
    global gp_list
    global point
    global point_list
    global point_unit
    global point_unit_list
    global unit
    global unit_list
    print("__________________________________")
    accept_courses()
    print("__________________________________")
    grade_score()
    print("__________________________________")
    point_u()
    print("COURSE\tSCORE\tGRADE\tPOINT\tUNIT\tPOINT UNIT")
    for i in range(courses_offered):
        print(f"{course_list[i]}\t{score_list[i]}\t{grade_list[i]}\t{point_list[i]}\t{unit_list[i]}\t{point_unit_list[i]}")
    print("__________________________________")
    print("POINT\t TOTAL_UNIT")
    print(f"{sum(point_unit_list)}\t\t{sum(unit_list)}")
    print("__________________________________")
    
def grade_point():
    global courses_offered
    global courses
    global course_list
    global scores
    global score_list
    global grade
    global grade_list
    global gp
    global gp_list
    global point
    global point_list
    global point_unit
    global point_unit_list
    global unit
    global unit_list
    global semester
    get_point = sum(point_unit_list)
    get_unit = sum(unit_list)
    gp = get_point/get_unit
    gp_round = round(gp,2)
    print(f"YOUR GP IS : {gp_round}")
    
def start_again():
    for i in range (courses_offered):
        i+=1 
        user_intent = input("Do you wish to continue to next semester (yes/no)")
        #capitalize info to avoid error
        convert_intent = user_intent.upper()
        
        while convert_intent == "YES":
            result_print()
            grade_point()
            start_again()
                
        else:
            print("THANK YOU!!!!")
        
    
result_print()
grade_point()
start_again()