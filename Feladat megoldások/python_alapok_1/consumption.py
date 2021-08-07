consumption_highway = float(input('consuption on highway> '))
consumption_city = float(input('consuption in the city> '))
city_distance = float(input('distance traveled in the city> '))
highway_distance = float(input('distance traveled on the highway> '))


gass_price = 350
one_way_fuel_consumption = (highway_distance/100 * consumption_highway) + (city_distance/100 * consumption_city)
one_way_cost = one_way_fuel_consumption * gass_price
print('One way fuel consumption', one_way_fuel_consumption)
print('One way cost:', one_way_cost)
print('Retour cost:', one_way_cost * 2)
