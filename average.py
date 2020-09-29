numberofTests = 0
score = 0
total = 0
average = 0.0
scoreCount = 0

numberofTests = int(input("Please enter the number of tests you want to average: "))
score = int(input("Please enter a score: "))
scoreCount = scoreCount + 1
total = total + score          
average = total/scoreCount
print("The average is ",average)
