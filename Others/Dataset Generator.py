import csv
import random


file = 'dataset_water_bahawalpur.csv'



with open(file,'w', newline='') as n:
    writer = csv.writer(n)
    writer.writerow(['Longitude','Latitude','Portability'])

    for x in range(10):
        longitude = random.choices((round(random.uniform(71.65, 71.67), 6), round(random.uniform(71.67, 71.71), 6),
                                    round(random.uniform(71.71, 71.76), 6)), (100, 0, 0))
        latitude = random.choices((round(random.uniform(29.35, 29.37), 6), round(random.uniform(29.37, 29.39), 6),
                                   round(random.uniform(29.39, 29.41), 6)), (100, 0, 0))

        portability = 1

        writer.writerow([str(longitude[0]), str(latitude[0]), str(portability)])

    for x in range(20):
        longitude = random.choices((round(random.uniform(71.65, 71.67), 6), round(random.uniform(71.67, 71.71), 6),
                                    round(random.uniform(71.71, 71.76), 6)), (100, 0, 0))
        latitude = random.choices((round(random.uniform(29.35, 29.37), 6), round(random.uniform(29.37, 29.39), 6),
                                   round(random.uniform(29.39, 29.41), 6)), (0, 100, 0))
        portability = 1
        writer.writerow([str(longitude[0]),str(latitude[0]),str(portability)])

    for x in range(15):
        longitude = random.choices((round(random.uniform(71.65, 71.67), 6), round(random.uniform(71.67, 71.71), 6),
                                    round(random.uniform(71.71, 71.76), 6)), (100, 0, 0))
        latitude = random.choices((round(random.uniform(29.35, 29.37), 6), round(random.uniform(29.37, 29.39), 6),
                                   round(random.uniform(29.39, 29.41), 6)), (0, 0, 100))
        portability = 0

        writer.writerow([str(longitude[0]), str(latitude[0]), str(portability)])

    for x in range(15):
        longitude = random.choices((round(random.uniform(71.65, 71.67), 6), round(random.uniform(71.67, 71.71), 6),
                                    round(random.uniform(71.71, 71.76), 6)), (0, 100, 0))
        latitude = random.choices((round(random.uniform(29.35, 29.37), 6), round(random.uniform(29.37, 29.39), 6),
                                   round(random.uniform(29.39, 29.41), 6)), (100, 0, 0))
        portability = 1

        writer.writerow([str(longitude[0]), str(latitude[0]), str(portability)])

    for x in range(30):
        longitude = random.choices((round(random.uniform(71.65, 71.67), 6), round(random.uniform(71.67, 71.71), 6),
                                    round(random.uniform(71.71, 71.76), 6)), (0, 100, 0))
        latitude = random.choices((round(random.uniform(29.35, 29.37), 6), round(random.uniform(29.37, 29.39), 6),
                                   round(random.uniform(29.39, 29.41), 6)), (0, 100, 0))
        portability = 0

        writer.writerow([str(longitude[0]), str(latitude[0]), str(portability)])

    for x in range(10):
        longitude = random.choices((round(random.uniform(71.65, 71.67), 6), round(random.uniform(71.67, 71.71), 6),
                                    round(random.uniform(71.71, 71.76), 6)), (0, 100, 0))
        latitude = random.choices((round(random.uniform(29.35, 29.37), 6), round(random.uniform(29.37, 29.39), 6),
                                   round(random.uniform(29.39, 29.41), 6)), (0, 0, 100))
        portability = 1

        writer.writerow([str(longitude[0]), str(latitude[0]), str(portability)])

    for x in range(10):
        longitude = random.choices((round(random.uniform(71.65, 71.67), 6), round(random.uniform(71.67, 71.71), 6),
                                    round(random.uniform(71.71, 71.76), 6)), (0, 0, 100))
        latitude = random.choices((round(random.uniform(29.35, 29.37), 6), round(random.uniform(29.37, 29.39), 6),
                                   round(random.uniform(29.39, 29.41), 6)), (100, 0, 0))
        portability = 1

        writer.writerow([str(longitude[0]), str(latitude[0]), str(portability)])

    for x in range(15):
        longitude = random.choices((round(random.uniform(71.65, 71.67), 6), round(random.uniform(71.67, 71.71), 6),
                                    round(random.uniform(71.71, 71.76), 6)), (0, 0, 100))
        latitude = random.choices((round(random.uniform(29.35, 29.37), 6), round(random.uniform(29.37, 29.39), 6),
                                   round(random.uniform(29.39, 29.41), 6)), (0, 100, 0))
        portability = 0

        writer.writerow([str(longitude[0]), str(latitude[0]), str(portability)])

    for x in range(10):
        longitude = random.choices((round(random.uniform(71.65, 71.67), 6), round(random.uniform(71.67, 71.71), 6),
                                    round(random.uniform(71.71, 71.76), 6)), (0, 0, 100))
        latitude = random.choices((round(random.uniform(29.35, 29.37), 6), round(random.uniform(29.37, 29.39), 6),
                                   round(random.uniform(29.39, 29.41), 6)), (0, 0, 100))
        portability = 0

        writer.writerow([str(longitude[0]), str(latitude[0]), str(portability)])







'''
with open(file,'w', newline='') as n:
    writer = csv.writer(n)
    writer.writerow(['Longitude','Latitude',"pH",'Hardness','Solids','Conductivity','Turbidity','Portability'])
    for x in range(5000):
        place = random.choices(('sea_water','ground_water','surface_water','waste_water'),(3,90,6,1))

        if place[0] == 'sea_water':
            latitude = round(random.uniform(29.26, 29.46), 6)
            longitude = round(random.uniform(71.60, 71.78), 6)
            pH = random.choices((round(random.uniform(6.51, 8), 5), round(random.uniform(8.00001, 10), 5),
                                 round(random.uniform(10.00001, 11), 5)),(20,70,10))
            Hardness = random.choices((round(random.uniform(0, 17), 5), round(random.uniform(17.1, 60), 5),
                                       round(random.uniform(60.1, 120), 5), round(random.uniform(120.1, 180), 5),
                                       round(random.uniform(180, 300), 5)), (3, 5, 28, 64, 10))
            solids = random.choices((round(random.uniform(10001, 40000), 5), round(random.uniform(1001, 10000), 5),
                                     round(random.uniform(0, 1000), 5)), (2, 78, 20))
            conductivity = random.choices((round(random.uniform(0.5, 3), 5), round(random.uniform(2, 42), 5),
                                           round(random.uniform(50, 800), 5), round(random.uniform(30, 1500), 5),
                                           round(random.uniform(100, 2000), 5), round(random.uniform(2000, 10000), 5),
                                           round(random.uniform(10000, 55000), 5)), (2, 2, 4, 2, 2, 8, 80))
            turbidity = random.choices((round(random.uniform(0, 10), 5), round(random.uniform(10, 25), 5),
                                        round(random.uniform(25, 50), 5), round(random.uniform(50, 100), 5),
                                        round(random.uniform(100, 250), 5)), (20, 70, 6, 3, 1))
            portability = random.choices((0,1),(90,10))
            writer.writerow(
                [str(longitude), str(latitude), str(pH[0]), str(Hardness[0]), str(solids[0]), str(conductivity[0]),
                 str(turbidity[0]),str(portability[0])])


        elif place[0] == 'ground_water':
            latitude = round(random.uniform(29.26, 29.46), 6)
            longitude = round(random.uniform(71.60, 71.78), 6)
            pH = random.choices((round(random.uniform(0, 4), 5), round(random.uniform(4.00001, 6.5), 5),
                                 round(random.uniform(6.51, 8), 5), round(random.uniform(8.00001, 10), 5),
                                 round(random.uniform(10.00001, 11), 5), round(random.uniform(11.00001, 14), 5)),
                                (0.2, 1, 7.6, 0.6, 0.5, 0.1))
            Hardness = random.choices((round(random.uniform(0, 17), 5), round(random.uniform(17.1, 60), 5),
                                       round(random.uniform(60.1, 120), 5), round(random.uniform(120.1, 180), 5),
                                       round(random.uniform(180, 300), 5)), (3, 5, 64, 25, 3))
            solids = random.choices((round(random.uniform(10001, 40000), 5), round(random.uniform(1001, 10000), 5),
                                     round(random.uniform(0, 1000), 5)), (5, 15, 80))
            conductivity = random.choices((round(random.uniform(0.5, 3), 5), round(random.uniform(2, 42), 5),
                                           round(random.uniform(50, 800), 5), round(random.uniform(30, 1500), 5),
                                           round(random.uniform(100, 2000), 5), round(random.uniform(2000, 10000), 5),
                                           round(random.uniform(10000, 55000), 5)), (10, 20, 30, 10, 2, 18, 10))
            turbidity = random.choices((round(random.uniform(0, 10), 5), round(random.uniform(10, 25), 5),
                                        round(random.uniform(25, 50), 5), round(random.uniform(50, 100), 5),
                                        round(random.uniform(100, 250), 5)), (70, 20, 6, 3, 1))
            portability = random.choices((0, 1), (40, 60))
            writer.writerow(
                [str(longitude), str(latitude), str(pH[0]), str(Hardness[0]), str(solids[0]), str(conductivity[0]),
                 str(turbidity[0]),str(portability[0])])


        elif place[0] == 'surface_water':
            latitude = round(random.uniform(29.26, 29.46), 6)
            longitude = round(random.uniform(71.60, 71.78), 6)
            pH = random.choices((round(random.uniform(0, 4), 5), round(random.uniform(4.00001, 6.5), 5),
                                 round(random.uniform(6.51, 8), 5), round(random.uniform(8.00001, 10), 5),
                                 round(random.uniform(10.00001, 11), 5), round(random.uniform(11.00001, 14), 5)),
                                (0.2, 1, 7.6, 0.6, 0.5, 0.1))
            Hardness = random.choices((round(random.uniform(0, 17), 5), round(random.uniform(17.1, 60), 5),
                                       round(random.uniform(60.1, 120), 5), round(random.uniform(120.1, 180), 5),
                                       round(random.uniform(180, 300), 5)), (3, 5, 40, 50, 2))
            solids = random.choices((round(random.uniform(10001, 40000), 5), round(random.uniform(1001, 10000), 5),
                                     round(random.uniform(0, 1000), 5)), (5, 15, 80))
            conductivity = random.choices((round(random.uniform(0.5, 3), 5), round(random.uniform(2, 42), 5),
                                           round(random.uniform(50, 800), 5), round(random.uniform(30, 1500), 5),
                                           round(random.uniform(100, 2000), 5), round(random.uniform(2000, 10000), 5),
                                           round(random.uniform(10000, 55000), 5)), (10, 10, 20, 10, 2, 8, 40))
            turbidity = random.choices((round(random.uniform(0, 10), 5), round(random.uniform(10, 25), 5),
                                        round(random.uniform(25, 50), 5), round(random.uniform(50, 100), 5),
                                        round(random.uniform(100, 250), 5)), (70, 20, 6, 3, 1))
            portability = random.choices((0, 1), (50, 50))
            writer.writerow(
                [str(longitude), str(latitude), str(pH[0]), str(Hardness[0]), str(solids[0]), str(conductivity[0]),
                 str(turbidity[0]),str(portability[0])])


        else:
            latitude = round(random.uniform(29.26, 29.46), 6)
            longitude = round(random.uniform(71.60, 71.78), 6)
            pH = random.choices((round(random.uniform(0, 4), 5), round(random.uniform(4.00001, 6.5), 5),
                                 round(random.uniform(6.51, 8), 5), round(random.uniform(8.00001, 10), 5),
                                 round(random.uniform(10.00001, 11), 5), round(random.uniform(11.00001, 14), 5)),
                                (4, 30, 2, 4, 30, 30))
            Hardness = random.choices((round(random.uniform(0, 17), 5), round(random.uniform(17.1, 60), 5),
                                       round(random.uniform(60.1, 120), 5), round(random.uniform(120.1, 180), 5),
                                       round(random.uniform(180, 300), 5)), (1, 2, 3, 5, 90))
            solids = random.choices((round(random.uniform(10001, 40000), 5), round(random.uniform(1001, 10000), 5),
                                     round(random.uniform(0, 1000), 5)), (5, 15, 80))
            conductivity = random.choices((round(random.uniform(0.5, 3), 5), round(random.uniform(2, 42), 5),
                                           round(random.uniform(50, 800), 5), round(random.uniform(30, 1500), 5),
                                           round(random.uniform(100, 2000), 5), round(random.uniform(2000, 10000), 5),
                                           round(random.uniform(10000, 55000), 5)), (2, 2, 2, 2, 5, 80, 8))
            turbidity = random.choices((round(random.uniform(0, 10), 5), round(random.uniform(10, 25), 5),
                                        round(random.uniform(25, 50), 5), round(random.uniform(50, 100), 5),
                                        round(random.uniform(100, 250), 5)), (1, 2, 3, 5, 90))

            portability = 0
            writer.writerow(
                [str(longitude), str(latitude), str(pH[0]), str(Hardness[0]), str(solids[0]), str(conductivity[0]),
                 str(turbidity[0]),str(portability)])

'''