import pandas as pd
cars = pd.read_csv('cars.csv')
a = cars.iloc[0:5:,range(0,11,2)]
b = cars.loc[cars['Model'] == 'Mazda RX4']
c = cars.loc[cars['Model'] == 'Camaro Z28', ['Model','cyl']]
d_1 = cars.loc[cars['Model'] == 'Mazda RX4 Wag', ['Model','cyl','gear']]
d_2 = cars.loc[cars['Model'] == 'Ford Pantera L', ['Model','cyl','gear']]
d_3 = cars.loc[cars['Model'] == 'Honda Civic', ['Model','cyl','gear']]
print("A.", a)
print(" ")
print("B.", b)
print(" ")
print("C.", c)
print(" ")
print("D.", d_1)
print(d_2)
print(d_3)