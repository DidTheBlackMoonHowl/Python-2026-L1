import pandas as pd
import matplotlib.pyplot as pl

scoreDF = pd.read_csv("scores.csv").dropna()
courses = ["math", "python", "database"]

'''def getScoreGroups(frame, course):
    returnList = []
    scoreGroup = [70, 75, 80, 85, 90, 95, 100]
    for group in scoreGroup:
        c = 0
        frame2 = (frame[course] <= group) & (frame[course] > (group - 5))
        for i in frame2:
            if (i == True):
                c += 1
        returnList.append(c)

    return returnList

# scoreGroup = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"]
scoreGroup = ["66-70", "71-75", "76-80", "81-85", "86-90", "91-95", "96-100"]
scorePython = getScoreGroups(scoreDF, "python")
scoreMath = getScoreGroups(scoreDF, "math")
scoreDatabase = getScoreGroups(scoreDF, "database")

pl.plot(scoreGroup, scorePython, marker = "o", label = "Python")
pl.plot(scoreGroup, scoreMath, marker = "o", label = "Math")
pl.plot(scoreGroup, scoreDatabase, marker = "o", label = "DB")
pl.title("Student Scores")
pl.xlabel("Score Group")
pl.ylabel("Number of Students")
pl.grid(True)
pl.legend()
pl.savefig("scores.pdf")'''

# Scattered Plot
pl.figure(figsize=(8, 5))
for course in courses:
    pl.scatter(
        scoreDF.index,
        scoreDF[course],
        label=course
    )

pl.title("Student Scores")
pl.xlabel("Student")
pl.ylabel("Marks")
pl.legend()
pl.grid(True)
pl.savefig("scattered.png")

# Histogram
fig, axes = pl.subplots(1, 3, figsize=(15, 5))

for i, course in enumerate(courses):
    # i = iteration
    # course = courses[i]
    axes[i].hist(scoreDF[course], bins=5, edgecolor="black")
    axes[i].set_title(course.capitalize() + " Scores")
    axes[i].set_xlabel("Marks")
    axes[i].set_ylabel("Frequency")
    axes[i].grid(axis="y")

pl.savefig("histo.png")

# Box Plot
pl.figure(figsize=(8, 5))
pl.boxplot(
    [scoreDF[course] for course in courses],
    tick_labels=courses
)

pl.title("Score Distribution by Course")
pl.xlabel("Course")
pl.ylabel("Marks")
pl.grid(axis="y")
pl.savefig("box.png")