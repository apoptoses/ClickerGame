import shelve

d = shelve.open('savefile')

d[key] = data

data = d[key]

del d[key]

flag = key in d

d.close()
