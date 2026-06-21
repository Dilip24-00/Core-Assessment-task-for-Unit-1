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

# Store the Unit 1 discussion score in a variable so the value can be reused in calculations
Unit1_discussion_points = 50

# Store the Unit 1 course project score in a variable for later calculations and comparisons
Unit1_course_project_points = 50

# Store the Unit 1 core assessment score in a variable so it can be included in the total score
Unit1_core_assesment_points = 50

# Store the maximum possible points for a task so the same value can be reused in comparisons
task_maximum_points = 50

# Add all Unit 1 scores together to calculate the total number of points earned
total_points = Unit1_discussion_points + Unit1_course_project_points + Unit1_core_assesment_points

# Display the total points earned by the user
print("Total Points:", total_points)

# Compare the discussion score with the maximum possible score to check if full points were earned
print("Got maximum points for Unit 1 discussion?", Unit1_discussion_points == task_maximum_points)

# Compare the course project score with the maximum possible score to check if full points were earned
print("Got maximum points for Unit 1 course project?", Unit1_course_project_points == task_maximum_points)

# Compare the core assessment score with the maximum possible score to check if full points were earned
print("Got maximum points for Unit 1 core assessment?", Unit1_core_assesment_points == task_maximum_points)
