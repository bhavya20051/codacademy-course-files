def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    print ("You meet the requirements to graduate!")
 
  else:
    print ("You do not meet the requirement for graduation.")
graduation_reqs(3.0, 100)