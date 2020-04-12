def cost_ground_shipping(weight):
  if weight>10:
    return (4.75*weight+20)
  elif 6<weight<=10:
    return (4.00*weight+20)
  elif 2<weight<=6:
    return(3.00*weight+20)
  else:
    return(1.5*weight+20)
  print(cost_ground_shipping(8.4))
  
  def cost_ground_shipping(weight):
      if weight>10:
          return (4.75*weight+20)
      elif 6<weight<=10:
          return (4.00*weight+20)
      elif 2<weight<=6:
          return(3.00*weight+20)
      else:
          return(1.5*weight+20) 

print(cost_ground_shipping(8.4))

def cost_drone_shipping(weight):
  if weight>10:
    return (14.25*weight)
  elif 6<weight<=10:
    return (12*weight)
  elif 2<weight<=6:
    return(9*weight)
  else:
    return(4.5*weight)

print(cost_drone_shipping(1.5))

def cheapest_method(weight):
  if cost_ground_shipping(weight)>cost_drone_shipping(weight):
    return "ground shipping"
  else:
    return "drone shipping"

print cheapest_method(4.8)
  

  
  
