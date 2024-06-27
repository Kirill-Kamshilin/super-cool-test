clients_data = [('Brendan Novak', 17), ('Jenny Fisher', 13), 
                ('Michael Carpenter', 2), ('Amber Newton', 14), ('Cynthia Stark', 2), 
                ('Julia Morgan', 6), ('Seth Fox', 2), ('Kristen Gonzalez', 16), 
                ('Michael Carpenter', 3), ('Cynthia Stark', 7), ('Seth Fox', 16), 
                ('Michael Carpenter', 9), ('Victoria Hayes', 20), ('Julia Morgan', 14), 
                ('Julia Morgan', 21), ('Jenny Fisher', 23), ('Victoria Hayes', 11), 
                ('Victoria Hayes', 20), ('Julia Morgan', 6), ('Kristen Gonzalez', 20), 
                ('Cynthia Stark', 14), ('Seth Fox', 6), ('Jenny Fisher', 7), 
                ('Seth Fox', 23), ('Julia Morgan', 15), ('Seth Fox', 22), 
                ('Victoria Hayes', 5), ('Seth Fox', 20), ('Julia Morgan', 19), 
                ('Cynthia Stark', 21)]
a = len(set([a[0] for a in clients_data if 6 <= a[1] < 12]))
b = len(set([a[0] for a in clients_data if 12 <= a[1] < 18]))
c = len(set([a[0] for a in clients_data if 18 <= a[1] <= 24]))
d = len(set([a[0] for a in clients_data if 0 <= a[1] < 6]))
print(f'{a}, {b}, {c}, {d}')