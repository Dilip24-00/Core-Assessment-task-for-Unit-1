# Ask the user to type their first name and store the value so it can be used later in the program
first_name = input("Enter your first name: ")

# Ask the user to type their last name and store the value in a separate variable
last_name = input("Enter your last name: ")

# Remove any spaces before or after the first name to make the input clean and properly formatted
first_name = first_name.strip()

# Remove any spaces before or after the last name so extra spaces do not affect the output
last_name = last_name.strip()

# Convert the first name so only the first letter is uppercase and the remaining letters are lowercase
first_name = first_name.capitalize()

# Convert the last name so only the first letter is uppercase and the remaining letters are lowercase
last_name = last_name.capitalize()

# Display a greeting message in the required format using the cleaned and formatted names
print("Hello " + last_name + ", " + first_name)

# Store the Unit 1 discussion score in a variable so the value can be reused later
Unit1_discussion_points = 50

# Store the Unit 1 course project score in a variable
Unit1_course_project_points = 50

# Store the Unit 1 core assessment score in a variable
Unit1_core_assesment_points = 50

# Store the Unit 2 discussion score in a variable
Unit2_discussion_points = 50

# Store the Unit 2 course project score in a variable
Unit2_course_project_points = 50

# Store the Unit 2 core assessment score in a variable
Unit2_core_assesment_points = 50

# Store the maximum possible points per assignment
task_maximum_points = 50

# Create a list for discussion grades using Unit 1 and Unit 2 variables
total_discussion_points = [Unit1_discussion_points, Unit2_discussion_points]

# Create a list for course project grades using Unit 1 and Unit 2 variables
total_course_project_points = [Unit1_course_project_points, Unit2_course_project_points]

# Create a list for core assessment grades using Unit 1 and Unit 2 variables
total_core_assessment_points = [Unit1_core_assesment_points, Unit2_core_assesment_points]

# Calculate the current total discussion points using the list
discussion_total = sum(total_discussion_points)

# Calculate the maximum possible discussion points
discussion_maximum = 8 * task_maximum_points

# Display current and maximum discussion points using string formatting
print("Currently you have {} points for discussions out of {}".format(discussion_total, discussion_maximum))

# Calculate the current total course project points using the list
course_project_total = sum(total_course_project_points)

# Calculate the maximum possible course project points
course_project_maximum = 8 * task_maximum_points

# Display current and maximum course project points using string formatting
print("Currently you have {} points for course projects out of {}".format(course_project_total, course_project_maximum))

# Calculate the current total core assessment points using the list
core_assessment_total = sum(total_core_assessment_points)

# Calculate the maximum possible core assessment points
core_assessment_maximum = 4 * task_maximum_points

# Display current and maximum core assessment points using string formatting
print("Currently you have {} points for core assessments out of {}".format(core_assessment_total, core_assessment_maximum))
