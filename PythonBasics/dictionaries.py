dict = {'David': 22, 'Rosa': 48, 'Juan': 49, 'Brenda': 19, 'Bere': 18,
        'Some': [['Pepe', 23, 'Pedro', 45], ['Jose', 34, 'Araceli', 78]]}

dict['Emilia'] = 68

print(dict)
print(dict['Some'][0][2])

del dict['Emilia']
print(dict)

#-----------------------------------------------------------------------------------

locations = {'North America': {'USA': ['Mountain View']}}

locations['Asia'] = {'India': ['Bangalore']}
locations['North America']['USA'].append('Atlanta')
locations['Africa'] = {'Egypt': ['Cairo']}
locations['Asia']['China'] = ['Shanghai', 'Beijing']

loc = sorted(locations['North America']['USA'])

print(1)
for x in loc:
    print(x)

print(2)
asia_cities = []
for countries, cities in locations['Asia'].items():
    for c in cities:
        temp = c + " - " + countries
        asia_cities.append(temp)

for i in sorted(asia_cities):
    print(i)