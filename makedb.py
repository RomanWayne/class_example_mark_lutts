from person import Person, Manager
import shelve

bob = Person('Bob Smith')
sue = Person('Sue Jones', 'dev', 100)

db = shelve.open('personsdb')
# for o in (bob, sue):
#     db[o.name] = o #запись в хранилище
# db.close()

import glob
print(glob.glob('person*'))
print(open('personsdb.dir').read())

print(db['Bob Smith'])