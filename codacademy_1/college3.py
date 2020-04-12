def grade_converter(gpa):
  if gpa >= 4.0:
    print("A")
  elif gpa >= 3.0:
    print("B")
  elif gpa >= 2.0:
    print("C")
  elif gpa >= 1.0:
    print("D")
  else:
    print("F")
    
grade_converter(0.9)

#to return the function, substitute return in place of print