def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    print ("You meet the requirements to graduate!")
  if (gpa >= 2.0) and not (credits >= 120):
    print ("You do not have enough credits to graduate.")
  if not (gpa >= 2.0) and (credits >= 120):
    print ("Your GPA is not high enough to graduate.")

graduation_reqs(3.0, 130)

#to run in anaconda prompt, type python college.py while in same directory

