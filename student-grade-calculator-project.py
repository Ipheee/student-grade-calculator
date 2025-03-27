# Function to calculate grades based on input scores
def calculate_grades(scores):
    """
    This function takes a list of student scores, evaluates each score based on predefined grading criteria, and prints out the corresponding grade for each score.

    Grades are assigned based on the following criteria:
    - 100 to 70 => A
    - 69 to 65 => B
    - 64 to 55 => C
    - 54 to 45 => D
    - 44 to 0  => F

    Parameters:
    scores (list): A list of integers, each representing a student's score. The list can contain any number of scores.

    Output:
    Prints the grade corresponding to each student's score in the format:
    "Score: [score] => Grade: [grade]"

    Notes:
    - The function assumes the scores are integers. If any score is outside the valid range of 0-100, it will be flagged as "Invalid score".
    - The function uses control flow (if-elif-else) to categorize each score and print the corresponding grade.
    - It is important to provide a list of integers, as other data types (like strings or floating-point numbers) may lead to errors or unexpected behavior.

    Edge cases:
    - Scores below 0 or above 100 are considered invalid and will be flagged with the message "Invalid score".
    - If the list of scores is empty, the function will not produce any output.
    """
    
    # Iterate through each score in the input list
    for score in scores:
        # Determine the grade using control flow (if-elif-else)
        if 70 <= score <= 100:
            grade = "A"
        elif 65 <= score <= 69:
            grade = "B"
        elif 55 <= score <= 64:
            grade = "C"
        elif 45 <= score <= 54:
            grade = "D"
        elif 0 <= score <= 44:
            grade = "F"
        else:
            # If the score is outside the valid range
            grade = "Invalid score"
        
        # Print the score with the corresponding grade
        print(f"Score: {score} => Grade: {grade}")

# For instance
if __name__ == "__main__":
    # List of student scores
    student_scores = [93, 68, 60, 51, 40, 80, 66, 56, 46, 30]
    
    # Call the function with the list of scores
    calculate_grades(student_scores)
