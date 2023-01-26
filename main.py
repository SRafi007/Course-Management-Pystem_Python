courses_box = {"MATH1":["MAT1102","DIFFERENTIAL CALCULUS & CO-ORDINATE GEOMETRY","3"],
                "IP":["CSC1102","INTRODUCTION TO PROGRAMMING","3"],
                "DM": ["CSC1204", "DISCRETE MATHEMATICS", "3"],
                "OOP1": ["CSC1205", "OBJECT ORIENTED PROGRAMMING 1 (JAVA)", "3"],
                "DS": ["CSC2106", "DATA STRUCTURE", "3"],
                "DSL": ["CSC2107", "DATA STRUCTURE LAB", "1"],
                "ALGORITHMS": ["CSC2211", "ALGORITHMS", "3"]}

prerequisites = {"DM": ["MAT1102", "CSC1102"], "OOP1": ["CSC1102"],"DS":["CSC1204","CSC1205"],
                 "DSL":["CSC1204","CSC1205"],"ALGORITHMS":["CSC2106","CSC2107"]}
def add_new_course(courses, prerequisites):
    """Add new course by user input"""
    new_course = input('Enter new Course: ')
    course_code = input('Enter course Code: ')
    course_title = input('Enter course title: ')
    course_credit = input('Enter course Credit: ')
    new_list = [course_code, course_title, course_credit]
    courses[new_course] = new_list
    prerequisite_check = True
    while prerequisite_check:
        print("1. Add prerequisite/0. Not Applicatble")
        choice = int(input('Enter Your Choice :'))
        if choice == 0:
            prerequisite_check = False
        elif choice == 1:
            add_prerequisite(new_course, prerequisites)
            prerequisite_check = False
        else:
            print("please Enter a Valid Option")


def add_course_by_name(course, courses):
    """Add new course When searched result not found on Courses"""
    new_course = course
    course_code = input('Enter course Code: ')
    course_title = input('Enter course title: ')
    course_credit = input('Enter course Credit: ')
    course_list = [course_code, course_title, course_credit]
    courses[new_course] = course_list
    prerequisite_check = True
    while prerequisite_check:
        choice = int(input('Enter Your Choice(1. Add prerequisite/0. Not Applicable ):'))
        if choice == 0:
            prerequisite_check = False
        elif choice == 1:
            add_prerequisite(new_course, prerequisites)
            prerequisite_check = False
        else:
            print("Enter Valid Option")


def update_course(courses):
    """To update an existing course"""
    get_course = input("Enter Course You Want to update:")
    while get_course not in courses:
        get_course = input("Enter A Valid Course You Want to update:")
    else:
        print(courses[get_course])
        course_code = courses[get_course][0]
        course_title = input('Enter new course title/(press enter to skip): ')
        if course_title == '':
            course_title = courses[get_course][1]
        course_credit = input('Enter new course Credit/(press enter to skip): ')
        if course_credit == '':
            course_credit = courses[get_course][2]
        updated_list = [course_code, course_title, course_credit]
        courses[get_course] = updated_list
        if get_course in prerequisites:
            new_prereq_list=[]
            for prereq in prerequisites[get_course]:
                print("Previous prerequisite:",prereq)
                course_code = input('Enter new prerequisite code/(press enter to skip): ')
                if course_code == '':
                    new_prereq_list.append(prereq)
                else:
                    new_prereq_list.append(course_code)
            prerequisites[get_course]=new_prereq_list
        else:
            print("This course Does not have any prerequisite course")
            preq_option=int(input("Do you want to add prerequisite for this curse(1.Yes 0.No)"))
            if preq_option==0:
                print("This Successfully updated.")
            elif preq_option==1:
                add_prerequisite(get_course,prerequisites)
            else:
                print("invalid option")
        print("This Successfully updated.")


def remove_course(courses):
    """Remove item if user input is valid"""
    show_courses()
    delete_course = input("Enter Course you want to Delete:")
    if delete_course not in courses:
        print("The option you entered is not valid, Try again")
        remove_course(courses)
    delete_code=courses_box[delete_course][0]
    del courses[delete_course]
    for course in prerequisites:
        for code in prerequisites[course]:
            if delete_code==code:
                prerequisites[course].remove(delete_code)


def check_course(input):
    """To check user input course exist or not"""
    if input not in courses_box:
        print("Adding ",input," To Courses:")
        add_course_by_name(input,courses_box)


def search_course(courses):
    """Show Information for searched course"""
    course = input("Enter course Name (example:OS,DM):")
    if course in courses:
        print(courses[course])
    else:
        choice = int(input("Do you want to add this Course 0. No , 1. Yes :"))
        if choice == 1:
            check_course(course)


def show_courses():
    """Display all available Courses and their information's"""
    print("Bachelor of Science in Computer Science & Engineering ")
    for course_title in courses_box:
        print(course_title , "-", courses_box[course_title][0], "-", courses_box[course_title][1],
              "-Credit:-", courses_box[course_title][2], "- Prerequisite", check_prerequisite(course_title))

def display_particular_course():
    """Display a Course and it's information's"""
    count=0
    courses_temp_list=[]
    for item in courses_box:
        count+=1
        courses_temp_list.append(item)
        print(count," :",courses_box[item][1])
    selected_option=int(input("Enter option:"))
    selected_course=courses_temp_list[selected_option-1]
    for info in courses_box[selected_course]:
        print(info)
    print("Prerequisite:-",check_prerequisite(selected_course))

def store_file(courses):
    """Add new course by user input"""
    with open('courses.txt', 'w') as f:
        for course in courses:
            prerequisites_str = ""
            prerequisite_list = check_prerequisite(course)
            if prerequisite_list== "Not Applicable":
                prerequisite_list=["Not Applicable"]
            for prereq in prerequisite_list:
                prerequisites_str += prereq + ","
            text = course + "-Code:" + courses[course][0] + "-Title:" + courses[course][1] + "-Credit:" + courses[course][
                2] +"-Prerequisite:-"+ prerequisites_str + "\n"
            f.write(text)
            print("Course Info Store, Successful")


def show_menu():
    """Display Available options"""
    print("1. Add new Course")
    print("2. Update Exsiting Course")
    print("3. Remove Course")
    print("4. Display Courses information")
    print("5. Display a Course")
    print("6. Search Course")
    print("7. Save courses in txt file")
    print("0. Exit")


def add_prerequisite(course, prerequisites):
    prerequisite_count = True
    prerequisites_list = []
    while prerequisite_count:
        print("Enter prerequisite Course Code for",course, " :")
        prerequisite_of_course = input("Enter prerequisite Course :")
        check_course(prerequisite_of_course)
        if len(prerequisites_list) == 0:
            prerequisites_list = [courses_box[prerequisite_of_course][0]]
        else:
            prerequisites_list.append(courses_box[prerequisite_of_course][0])
        print("Do you want to add more prerequisite for",course, " :")
        print("1. Yes/0. No")
        add_more = int(input("Enter Your Choice:"))
        if add_more == 0:
            prerequisite_count = False
        elif add_more == 1:
            continue
    prerequisites[course] = prerequisites_list


def check_prerequisite(course_name):
    if course_name not in prerequisites:
        return "Not Applicable"
    else:
        return prerequisites[course_name]


main_loop = True
while main_loop:
    show_menu()
    choice = int(input('Enter Your Choice :'))
    if choice == 1:
        add_new_course(courses_box, prerequisites)
    elif choice == 2:
        show_courses()
        update_course(courses_box)
    elif choice == 3:
        remove_course(courses_box)
    elif choice == 4:
        show_courses()
    elif choice == 5:
        display_particular_course()
    elif choice == 6:
        search_course(courses_box)
    elif choice == 7:
        store_file(courses_box)
    elif choice == 0:
        exit()
    else:
        print("Enter Valid Choice")
