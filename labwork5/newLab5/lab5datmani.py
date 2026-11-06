import pandas as pd

studentDF = pd.read_csv("students.csv")
scoreDF = pd.read_csv("scores.csv")
majors = ["ICT", "Data Science", "Cybersecurity", "Applied Mathematics"]

def execFirst():
    # Display first 5
    print("First 5 rows: ")
    print(studentDF.head(), "\n")
    
    print(f"Rows: {studentDF.shape[0]} \nColumns: {studentDF.shape[1]} \n")   # Rows & Columns

    # Handle Empty
    baseDF = studentDF.dropna()

    # First Select
    print("Select Name & GPA: \n")
    df3 = baseDF[["name", "GPA"]]
    print(df3, "\n")

    # Second Select
    print("Select GPA > 3.5: ")
    print(baseDF.loc[
        baseDF["GPA"] > 3.5,
        ["name", "GPA"]
    ], "\n")

    # Sorting
    print("Sorted Dataframe (by GPA): ")
    baseDF = baseDF.sort_values("GPA", ascending=False)
    print(baseDF, "\n")

    # Average
    dfs = []
    for major in majors:
        dfs.append(baseDF.loc[
            baseDF["major"] == major,
            ["student_id", "name", "age", "major", "GPA"]
        ])

    for df in dfs:
        totalGPA = 0
        major = df["major"].iloc[0]
        for gpa in df["GPA"]:
            totalGPA += gpa
        print(f"Major: {major}, Average GPA: {totalGPA / df.shape[0]}")
    print()
        
def execSecond():
    # Merge
    baseDF = pd.merge(studentDF.dropna(), scoreDF.dropna(), on="student_id")

    # Calculate AVG
    baseDF["average_score"] = (baseDF["python"] + baseDF["math"] + baseDF["database"]) / 3
    
    # Top 5
    print("Top 5 students (by average score): ")
    print(baseDF.sort_values("average_score", ascending=False).head(), "\n")

    # Average
    dfs = []
    for major in majors:
        dfs.append(baseDF.loc[
            baseDF["major"] == major,
            ["student_id", "name", "age", "major", "python", "math", "database"]
        ])

    print("Average score by major: ")
    for df in dfs:
        totalScore = 0
        major = df["major"].iloc[0]
        for score in df["python"]:
            totalScore += score
        for score in df["math"]:
            totalScore += score
        for score in df["database"]:
            totalScore += score
        print(f"Major: {major}, Average Score: {totalScore / (df.shape[0] * 3)}")
    print()

execFirst()
execSecond()