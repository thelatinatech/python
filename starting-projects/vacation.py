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

def trip_cost(city,days):
  sum = rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city)
  return sum
