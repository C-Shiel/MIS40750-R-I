import sqlite3
In [2]:
pwd
Out[2]:
u'C:\\Users\\Conor\\Documents\\python'
In [3]:
cd ..
C:\Users\Conor\Documents
In [4]:
cd Assignment-1-/
C:\Users\Conor\Documents\Assignment-1-
In [ ]:
 
In [5]:
import pandas as pd 
from math import radians, cos, sin, asin, sqrt
In [ ]:
 
In [ ]:
 
In [24]:
# Reads in the data and puts it into lists
list_location_production = []
list_location_lat = []
list_location_long = []
list_port_long = []
list_port_lat = []
    
def start():
    conn = sqlite3.connect('renewable.db')# creates connection 
    c = conn.cursor()
    
    
    h = c.execute("SELECT production FROM location")
    for i in h:
        list_location_production.append(i)
    for i in c.execute("SELECT lat FROM location;"):
        list_location_lat.append(i)
    for i in c.execute("SELECT long FROM location;"):
        list_location_long.append(i)
    
    for i in c.execute("SELECT long FROM ports"):
        list_port_long.append(i)
    for i in c.execute("SELECT lat FROM ports"):
        list_port_lat.append(i)
    
    
    print list_location_production
    print list_location_lat
    print list_location_long
    print list_port_long
    print list_port_lat
    
    
    
start()
    
    
[(259696.0,), (89499.0,), (271650.0,), (87606.0,), (298978.0,), (200068.0,), (60573.0,), (159794.0,), (163358.0,), (210817.0,)]
[(7.26,), (8.99,), (8.48,), (7.95,), (6.48,), (6.68,), (7.71,), (6.92,), (6.8,), (6.69,)]
[(52.66,), (52.86,), (54.28,), (53.42,), (52.34,), (53.22,), (52.36,), (52.84,), (53.18,), (53.66,)]
[(52.7,), (53.33,), (52.27,)]
[(8.63,), (6.25,), (6.39,)]

In [28]:
#Putting lists into float form.

list_location_production=[259696.0, 89499.0, 271650.0, 87606.0, 298978.0, 200068.0, 60573.0, 159794.0, 163358.0,210817.0]
list_location_long=[52.66,52.86, 54.28, 53.42, 52.34, 53.22, 52.36, 52.84, 53.18, 53.66]
list_location_lat=[7.26, 8.99, 8.48, 7.95, 6.48, 6.68, 7.71, 6.92, 6.8, 6.69]
list_port_long=[52.7,53.33,52.27]
list_port_lat=[8.63,6.25,6.39]

In [30]:
#Converts the production of the locations to number of trips that must be made by them.
#Then adds the number of trips to its key value in a dictionary

trips=[]
for i in list_location_production:
    result = i/40
    trips.append(result)
num = [0,1,2,3,4,5,6,7,8,9]
trips_1 = dict(zip(num,trips))
print trips_1
    
{0: 6492.4, 1: 2237.475, 2: 6791.25, 3: 2190.15, 4: 7474.45, 5: 5001.7, 6: 1514.325, 7: 3994.85, 8: 4083.95, 9: 5270.425}
In [32]:
#haversine formula to calculate the distance between to geographical points
#Taken from http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def length_km(lon1, lat1, lon2, lat2):  
    
     
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2]) #convert decimal degrees to radians 
    # haversine formula 
    dlon = lon2 - lon1 #difference in longitudes
    dlat = lat2 - lat1 #difference in latitude
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return "%0.2lf" % km

print "\n"

In [61]:
# The distance from a location to all of the ports. 

location_0_ports_dist=[] 
location_1_ports_dist=[]
location_2_ports_dist=[]
location_3_ports_dist=[]
location_4_ports_dist=[]
location_5_ports_dist=[]
location_6_ports_dist=[]
location_7_ports_dist=[]
location_8_ports_dist=[]
location_9_ports_dist=[]

for i in range(0,3):
        location_0_ports_dist.append(length_km(list_location_long[0],list_location_lat[0],list_port_long[i],list_port_lat[i]))

for i in range(0,3):
        location_1_ports_dist.append(length_km(list_location_long[1],list_location_lat[1],list_port_long[i],list_port_lat[i]))

for i in range(0,3):
        location_2_ports_dist.append(length_km(list_location_long[2],list_location_lat[2],list_port_long[i],list_port_lat[i]))

for i in range(0,3):
        location_3_ports_dist.append(length_km(list_location_long[3],list_location_lat[3],list_port_long[i],list_port_lat[i]))

for i in range(0,3):
        location_4_ports_dist.append(length_km(list_location_long[4],list_location_lat[4],list_port_long[i],list_port_lat[i]))

for i in range(0,3):
        location_5_ports_dist.append(length_km(list_location_long[5],list_location_lat[5],list_port_long[i],list_port_lat[i]))

for i in range(0,3):
        location_6_ports_dist.append(length_km(list_location_long[6],list_location_lat[6],list_port_long[i],list_port_lat[i]))

for i in range(0,3):
        location_7_ports_dist.append(length_km(list_location_long[7],list_location_lat[7],list_port_long[i],list_port_lat[i]))

for i in range(0,3):
        location_8_ports_dist.append(length_km(list_location_long[8],list_location_lat[8],list_port_long[i],list_port_lat[i]))

for i in range(0,3):
        location_9_ports_dist.append(length_km(list_location_long[9],list_location_lat[9],list_port_long[i],list_port_lat[i]))



print "0: ",location_0_ports_dist 
print "1:",location_1_ports_dist
print "2: ", location_2_ports_dist
print "3:", location_3_ports_dist
print "4: ", location_4_ports_dist
print "5:" , location_5_ports_dist
print "6:" , location_6_ports_dist
print "7:" , location_7_ports_dist
print "8:" , location_8_ports_dist
print "9:" , location_9_ports_dist
0:  ['152.31', '134.40', '105.82']
1: ['43.69', '308.85', '296.14']
2:  ['174.42', '269.02', '320.92']
3: ['109.45', '189.17', '214.77']
4:  ['242.19', '112.28', '12.64']
5: ['224.13', '49.30', '109.72']
6: ['108.86', '194.34', '147.02']
7: ['190.65', '92.03', '86.18']
8: ['210.12', '63.32', '110.30']
9: ['240.11', '60.98', '157.04']

In [53]:
# The distance from the locations to the other loactions.
# Then each one added to a dictionary 

location_0_location= []
location_1_location= []
location_2_location= []
location_3_location= []
location_4_location= []
location_5_location= []
location_6_location= []
location_7_location= []
location_8_location= []
location_9_location= []

zero= [1,2,3,4,5,6,7,8,9]
one = [0,2,3,4,5,6,7,8,9]
two = [0,1,3,4,5,6,7,8,9]
three = [0,1,2,4,5,6,7,8,9]
four = [0,1,2,3,5,6,7,8,9]
five = [0,1,2,3,4,6,7,8,9]
six = [0,1,2,3,4,5,7,8,9]
seven = [0,1,2,3,4,5,6,8,9]
eight = [0,1,2,3,4,5,6,7,9]
nine = [0,1,2,3,4,5,6,7,8]



for i in range(0,10):
    if i !=0:
        location_0_location.append(length_km(list_location_long[0],list_location_lat[0],list_location_long[i],list_location_lat[i]))


for i in range(0,10):
    if i !=1:
        location_1_location.append(length_km(list_location_long[1],list_location_lat[1],list_location_long[i],list_location_lat[i]))


                       

for i in range(0,10):
    if i !=2:
        location_2_location.append(length_km(list_location_long[2],list_location_lat[2],list_location_long[i],list_location_lat[i]))
        
                       
                       

for i in range(0,10):
    if i !=3:
        location_3_location.append(length_km(list_location_long[3],list_location_lat[3],list_location_long[i],list_location_lat[i]))



location_4_location=[]
for i in range(0,10):
    if i !=4:
        location_4_location.append(length_km(list_location_long[4],list_location_lat[4],list_location_long[i],list_location_lat[i]))



                       

for i in range(0,10):
    if i !=5:
        location_5_location.append(length_km(list_location_long[5],list_location_lat[5],list_location_long[i],list_location_lat[i]))




for i in range(0,10):
    if i !=6:
        location_6_location.append(length_km(list_location_long[6],list_location_lat[6],list_location_long[i],list_location_lat[i]))



                       

for i in range(0,10):
    if i !=7:
        location_7_location.append(length_km(list_location_long[7],list_location_lat[7],list_location_long[i],list_location_lat[i]))

                       

for i in range(0,10):
    if i !=8:
        location_8_location.append(length_km(list_location_long[8],list_location_lat[8],list_location_long[i],list_location_lat[i]))
                       

for i in range(0,10):
    if i !=9:
        location_9_location.append(length_km(list_location_long[9],list_location_lat[9],list_location_long[i],list_location_lat[i]))


location_0_location = dict(zip(zero,location_0_location))
location_1_location = dict(zip(one,location_1_location))
location_2_location = dict(zip(two,location_2_location))
location_3_location = dict(zip(three,location_3_location))
location_4_location = dict(zip(four,location_4_location))
location_5_location = dict(zip(five,location_5_location))
location_6_location = dict(zip(six,location_6_location))
location_7_location = dict(zip(seven,location_7_location))
location_8_location = dict(zip(eight,location_8_location))
location_9_location = dict(zip(nine,location_9_location))

print "dist to 0" ,location_0_location
print "dist to 1" ,location_1_location
print "dist to 2" , location_2_location
print "dist to 3" , location_3_location
print "dist to 4" ,location_4_location
print "dist to 5" , location_5_location
print "dist to 6" , location_6_location 
print " dist to 7" , location_7_location
print "dist to 8 " , location_8_location
print " dist to 9" , location_9_location
dist to 0 {1: '193.50', 2: '224.01', 3: '113.52', 4: '93.59', 5: '89.27', 6: '59.94', 7: '42.68', 8: '76.83', 9: '127.20'}
dist to 1 {0: '193.50', 2: '165.94', 3: '130.94', 4: '284.74', 5: '259.74', 6: '152.49', 7: '230.04', 8: '245.90', 9: '270.33'}
dist to 2 {0: '224.01', 1: '165.94', 3: '111.42', 4: '308.35', 5: '231.61', 6: '227.91', 7: '234.94', 8: '222.55', 9: '210.31'}
dist to 3 {0: '113.52', 1: '130.94', 2: '111.42', 4: '202.14', 5: '142.84', 6: '119.70', 7: '131.09', 8: '130.50', 9: '142.49'}
dist to 4 {0: '93.59', 1: '284.74', 2: '308.35', 3: '202.14', 5: '99.66', 6: '136.70', 7: '73.73', 8: '99.30', 9: '147.57'}
dist to 5 {0: '89.27', 1: '259.74', 2: '231.61', 3: '142.84', 4: '99.66', 6: '148.63', 7: '49.69', 8: '14.05', 9: '48.58'}
dist to 6 {0: '59.94', 1: '152.49', 2: '227.91', 3: '119.70', 4: '136.70', 5: '148.63', 7: '102.50', 8: '135.63', 9: '182.73'}
 dist to 7 {0: '42.68', 1: '230.04', 2: '234.94', 3: '131.09', 4: '73.73', 5: '49.69', 6: '102.50', 8: '39.81', 9: '94.02'}
dist to 8  {0: '76.83', 1: '245.90', 2: '222.55', 3: '130.50', 4: '99.30', 5: '14.05', 6: '135.63', 7: '39.81', 9: '54.36'}
 dist to 9 {0: '127.20', 1: '270.33', 2: '210.31', 3: '142.49', 4: '147.57', 5: '48.58', 6: '182.73', 7: '94.02', 8: '54.36'}
 
In [54]:
# This function multiplies the numnber of trips that will have to be made from a plant
# by the distance they will have to travel to the other.

def mult_dicts(dict1, dict2):
  result_dict = {} 
  for word in dict1:
    if word in dict2:
      result_dict[word] = dict1[word] * dict2[word]
  return result_dict
  
In [55]:
# This function sums the transport distances to a location.

def sum_dict(x): 
    result = 0.0
    for i in x: 
        result+=x[i]
    return result 
	
In [62]:
location_0_location = {1: 193.50, 2: 224.01, 3: 113.52, 4: 93.59, 5: 89.27, 6: 59.94, 7: 42.68, 8: 76.83, 9: 127.20}
location_1_location = {0: 193.50, 2: 165.94, 3: 130.94, 4: 284.74, 5: 259.74, 6: 152.49, 7: 230.04, 8: 245.90, 9: 270.33}
location_2_location = {0: 224.01, 1: 165.94, 3: 111.42, 4: 308.35, 5: 231.61, 6: 227.91, 7: 234.94, 8: 222.55, 9: 210.31}
location_3_location = {0: 113.52, 1: 130.94, 2: 111.42, 4: 202.14, 5: 142.84, 6: 119.70, 7: 131.09, 8: 130.50, 9: 142.49}
location_4_location = {0: 93.59, 1: 284.74, 2: 308.35, 3: 202.14, 5: 99.66, 6: 136.70, 7: 73.73, 8: 99.30, 9: 147.57}
location_5_location = {0: 89.27, 1: 259.74, 2: 231.61, 3: 142.84, 4: 99.66, 6: 148.63, 7: 49.69, 8: 14.05, 9: 48.58}
location_6_location = {0: 59.94, 1: 152.49, 2: 227.91, 3: 119.70, 4: 136.70, 5: 148.63, 7: 102.50, 8: 135.63, 9: 182.73}
location_7_location = {0: 42.68, 1: 230.04, 2: 234.94, 3: 131.09, 4: 73.73, 5: 49.69, 6: 102.50, 8: 39.81, 9: 94.02}
location_8_location = {0: 76.83, 1: 245.90, 2: 222.55, 3: 130.50, 4: 99.30, 5: 14.05, 6: 135.63, 7: 39.81, 9: 54.36}
location_9_location = {0: 127.20, 1: 270.33, 2: 210.31, 3: 142.49, 4: 147.57, 5: 48.58, 6: 182.73, 7: 94.02, 8: 54.36}

In [63]:
# Here I use the mult_dicts function and the sum_dict function to give me a distance value for a port.
#I then add the closet port to give me a total distance value for a location.

#location 0
distance_traveled_to_location_0= mult_dicts(trips_1,location_0_location)
total_distance_tavelled_to_0= sum_dict(distance_traveled_to_location_0)
km_total_0 =  total_distance_tavelled_to_0 + float(location_0_ports_dist[2])

#location 1
distance_traveled_to_location_1= mult_dicts(trips_1,location_1_location)
total_distance_tavelled_to_1= sum_dict(distance_traveled_to_location_1)
km_total_1 =  total_distance_tavelled_to_1 + float(location_1_ports_dist[0])

#location 2
distance_traveled_to_location_2= mult_dicts(trips_1,location_2_location)
total_distance_tavelled_to_2= sum_dict(distance_traveled_to_location_2)
km_total_2 =  total_distance_tavelled_to_2 + float(location_2_ports_dist[0])

#location 3 
distance_traveled_to_location_3= mult_dicts(trips_1,location_3_location)
total_distance_tavelled_to_3= sum_dict(distance_traveled_to_location_3)
km_total_3 =  total_distance_tavelled_to_3 + float(location_3_ports_dist[0])

#location 4
distance_traveled_to_location_4= mult_dicts(trips_1,location_4_location)
total_distance_tavelled_to_4= sum_dict(distance_traveled_to_location_4)
km_total_4 =  total_distance_tavelled_to_4 + float(location_4_ports_dist[2])

#loacation 5
distance_traveled_to_location_5= mult_dicts(trips_1,location_5_location)
total_distance_tavelled_to_5= sum_dict(distance_traveled_to_location_5)
km_total_5 =  total_distance_tavelled_to_5 + float(location_5_ports_dist[1])

#location 6
distance_traveled_to_location_6= mult_dicts(trips_1,location_6_location)
total_distance_tavelled_to_6= sum_dict(distance_traveled_to_location_6)
km_total_6 =  total_distance_tavelled_to_6 + float(location_6_ports_dist[0])

#location 7
distance_traveled_to_location_7= mult_dicts(trips_1,location_7_location)
total_distance_tavelled_to_7= sum_dict(distance_traveled_to_location_7)
km_total_7 =  total_distance_tavelled_to_7 + float(location_7_ports_dist[2])

#location 8
distance_traveled_to_location_8= mult_dicts(trips_1,location_8_location)
total_distance_tavelled_to_8= sum_dict(distance_traveled_to_location_8)
km_total_8 =  total_distance_tavelled_to_8 + float(location_8_ports_dist[1])

#location 9
distance_traveled_to_location_9= mult_dicts(trips_1,location_9_location)
total_distance_tavelled_to_9= sum_dict(distance_traveled_to_location_9)
km_total_9 =  total_distance_tavelled_to_9 + float(location_9_ports_dist[1])

print km_total_0
print km_total_1
print km_total_2
print km_total_3
print km_total_4
print km_total_5
print km_total_6
print km_total_7
print km_total_8
print km_total_9
4594463.2845
9676349.8155
8834026.477
6000998.82275
5964844.63825
4528448.69525
6232013.631
4287484.9915
4309686.72825
5391392.2365

In [64]:
H = [km_total_0,km_total_1,km_total_2,km_total_3,km_total_4,km_total_5,km_total_6,km_total_7,km_total_8,km_total_9]
smallest = None 
for item in H:
    print item
    if (smallest == None) or (item < smallest):
        smallest = item
print "smallest = ", smallest

#There for the cheapest area to produce would be km_total_7 which has:
# a longitude of 52.84 and a latitude of 6.92 and a total production of 159,794tonnes.
4594463.2845
9676349.8155
8834026.477
6000998.82275
5964844.63825
4528448.69525
6232013.631
4287484.9915
4309686.72825
5391392.2365
smallest =  4287484.9915