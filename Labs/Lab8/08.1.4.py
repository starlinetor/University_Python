def print_table(table : list[list[int]]) -> None:
    for i in range(len(table)):
        print(table[i])
    print()

n = 10
#colums
m = 9
#rows

#init a table with only 0
table = [[0 for _ in range(n)] for _ in range(m)] 
print_table(table)

#fill the table with values of 1
for i in range(m):
    for j in range(n):
        table[i][j] = 1
print_table(table)

#fill the table with an alternating 01 pattern
m_value : bool = False
n_value : bool = False
for i in range(m):
    m_value = not m_value
    n_value = m_value
    for j in range(n):
        n_value = not n_value
        table[i][j] = 1 if n_value else 0
print_table(table)

#fill with 0 the top and lower row
table[0] = [0 for _ in range(n)]
table[m-1] = [0 for _ in range(n)]
print_table(table)

#fill with 1 the left and right collumn
for i in range(m):
    for j in range(n):
        if j == 0 or j == n-1:
            table[i][j] = 1
print_table(table)

#sum all elements
total : int = 0

for i in range(m):
    for j in range(n):
        if j == 0 or j == n-1:
            total += table[i][j]
print(total)