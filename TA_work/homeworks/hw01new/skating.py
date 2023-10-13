#10 min
from math import ceil
students=int(input("How many students are going? "))
teachers=int(input("How many teachers are going? "))
skates=int(input("How many students brought their own skates? "))
print(f'Bus cost: {ceil((students+teachers)/50)*200}')
print(f'Lunch cost: {(students*5)+(teachers*7)}')
print(f'Rental cost: {(students-skates)*4}')
print(f'Total cost: {(ceil((students+teachers)/50)*200)+((students*5)+(teachers*7))+((students-skates)*4)}')