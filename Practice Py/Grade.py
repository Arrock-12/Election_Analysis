#What is the score?
score = int(input("What is your test score?"))
# Determine the grade
if score > 90:
    print("Your grade is an A")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
elif score >= 60:
    print("D grade")
else:
    print("You fail")
    