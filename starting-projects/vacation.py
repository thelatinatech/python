#This exercise calculates three costs of a trip: hotel, plane, rental car. 

def hotel_cost(nights):
 return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475 

def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    return cost - 50
  elif days >=3:
    return cost - 20
  else:
    return cost

def trip_cost(city,days,spending_money):
  sum = rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)+ spending_money
  return sum

#example: 5-day trip to Los Angeles with an extra $600 for spending money
print trip_cost("Los Angeles", 5, 600)
