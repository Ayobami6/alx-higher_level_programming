tup = (('San Francisco'),
       ('San Jose'),
       ('Los Angeles'),
       ('Fremont'),
       ('Livermore'))

new = []
for item in tup:
    new.append(item)

print(*new, sep=", ")
# print(new_tup)
