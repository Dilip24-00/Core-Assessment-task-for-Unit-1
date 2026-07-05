# Ask the user to type their first name and store the value for later use
first_name = input("Enter your first name: ")

# Ask the user to type their last name and store the value separately
last_name = input("Enter your last name: ")

# Remove extra spaces before and after the first name
first_name = first_name.strip()

# Remove extra spaces before and after the last name
last_name = last_name.strip()

# Convert the first name so only the first letter is uppercase
first_name = first_name.capitalize()

# Convert the last name so only the first letter is uppercase
last_name = last_name.capitalize()

# Display the greeting using the properly formatted names
print("Hello " + last_name + ", " + first_name)

# Create a class to store discussion assignment information
class Discussions:

    # Store the maximum possible points per discussion assignment
    maximum_points_per_task = 50

    # Store the number of discussion assignments per semester
    tasks_per_semester = 8

    # Store the display name for discussions
    display_name = "Discussions"

# Create a class to store course project assignment information
class Course_projects:

    # Store the maximum possible points per course project assignment
    maximum_points_per_task = 50

    # Store the number of course project assignments per semester
    tasks_per_semester = 8

    # Store the display name for course projects
    display_name = "Course Projects"

# Create a class to store core assessment assignment information
class Core_assesments:

    # Store the maximum possible points per core assessment assignment
    maximum_points_per_task = 50

    # Store the number of core assessment assignments per semester
    tasks_per_semester = 4

    # Store the display name for core assessments
    display_name = "Core Assessments"

# Store Unit 1 discussion points
Unit1_discussion_points = 50

# Store Unit 2 discussion points
Unit2_discussion_points = 50

# Store Unit 3 discussion points
Unit3_discussion_points = 50

# Store Unit 1 course project points
Unit1_course_project_points = 50

# Store Unit 2 course project points
Unit2_course_project_points = 50

# Store Unit 3 course project points
Unit3_course_project_points = 50

# Store Unit 1 core assessment points
Unit1_core_assesment_points = 50

# Store Unit 2 core assessment points
Unit2_core_assesment_points = 50

# Store Unit 3 core assessment points
Unit3_core_assesment_points = 50

# Create a list containing all discussion grades
total_discussion_points = [
    Unit1_discussion_points,
    Unit2_discussion_points,
    Unit3_discussion_points
]

# Create a list containing all course project grades
total_course_project_points = [
    Unit1_course_project_points,
    Unit2_course_project_points,
    Unit3_course_project_points
]

# Create a list containing all core assessment grades
total_core_assessment_points = [
    Unit1_core_assesment_points,
    Unit2_core_assesment_points,
    Unit3_core_assesment_points
]

# Calculate the total discussion points earned
discussion_total = sum(total_discussion_points)

# Calculate the maximum possible discussion points
discussion_maximum = Discussions.tasks_per_semester * Discussions.maximum_points_per_task

# Display the discussion totals
print("Currently you have {} points for discussions out of {}".format(discussion_total, discussion_maximum))

# Calculate the total course project points earned
course_project_total = sum(total_course_project_points)

# Calculate the maximum possible course project points
course_project_maximum = Course_projects.tasks_per_semester * Course_projects.maximum_points_per_task

# Display the course project totals
print("Currently you have {} points for course projects out of {}".format(course_project_total, course_project_maximum))

# Calculate the total core assessment points earned
core_assessment_total = sum(total_core_assessment_points)

# Calculate the maximum possible core assessment points
core_assessment_maximum = Core_assesments.tasks_per_semester * Core_assesments.maximum_points_per_task

# Display the core assessment totals
print("Currently you have {} points for core assessments out of {}".format(core_assessment_total, core_assessment_maximum))

# Assume the student has maximum points for all discussions
discussion_maximum_check = True

# Loop through all discussion grades
for grade in total_discussion_points:

    # Check if any discussion grade is less than the maximum points
    if grade < Discussions.maximum_points_per_task:

        # Set the variable to False if a grade is lower than maximum
        discussion_maximum_check = False

# Display the correct message depending on the result
if discussion_maximum_check:

    # Display congratulations message if all grades are maximum
    print("Congrats! You got maximum points for ALL discussion homeworks so far!")

else:

    # Display message if not all grades are maximum
    print("Unfortunately you did not get maximum points for ALL discussion homeworks")

# Assume the student has maximum points for all course projects
course_project_maximum_check = True

# Loop through all course project grades
for grade in total_course_project_points:

    # Check if any course project grade is less than maximum
    if grade < Course_projects.maximum_points_per_task:

        # Set the variable to False if a lower grade is found
        course_project_maximum_check = False

# Display the correct course project result
if course_project_maximum_check:

    # Display congratulations message
    print("Congrats! You got maximum points for ALL course project homeworks so far!")

else:

    # Display failure message
    print("Unfortunately you did not get maximum points for ALL course project homeworks")

# Assume the student has maximum points for all core assessments
core_assessment_maximum_check = True

# Loop through all core assessment grades
for grade in total_core_assessment_points:

    # Check if any core assessment grade is less than maximum
    if grade < Core_assesments.maximum_points_per_task:

        # Set the variable to False if a lower grade exists
        core_assessment_maximum_check = False

# Display the correct core assessment result
if core_assessment_maximum_check:

    # Display congratulations message
    print("Congrats! You got maximum points for ALL core assessment homeworks so far!")

else:

    # Display failure message
    print("Unfortunately you did not get maximum points for ALL core assessment homeworks")
