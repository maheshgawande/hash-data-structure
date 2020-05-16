class Liniar_hashing:
    def __init__(self):
        self.tl = [None] * 11


    def _hash(self, key, c):
        return ((key + c) % 11)


    def search(self, key):
        key_i = None
        tl = self.tl
        for i in range(len(tl)):
            if tl[i] != None:
                if tl[i]['eid'] == key:
                    key_i = i

        return key_i


    def insert(self, eid, name, dept):
        data_added = False
        key_i = self.search(eid)
        if key_i == None:
            data = {
                'eid': eid,
                'name': name,
                'dept': dept
                }
            tl = self.tl
            c = 0
            while c != 11:
                i = self._hash(eid, c)
                if tl[i] == None:
                    tl[i] = data
                    data_added = True
                    break
    
                c += 1

        if data_added:
            print('\nData successfully added.')
        else:
            print('\nData can not be added.')


    def delete(self, key):
        data_deleted = False
        tl = self.tl
        c = 0
        while c != 11:
            i = self._hash(key, c)
            if tl[i] != None:
                data = tl[i]
                if data['eid'] == key:
                    tl[i] = None
                    data_deleted = True
                    break

            c += 1

        if data_deleted:
            print('\nData deleted successfully.')
        else:
            print(f'\nGiven epmly id {key} not found.')


    def display(self):
        tl = self.tl
        for i in range(len(tl)):
            print(f'{i} --> {tl[i]}')


class Double_hashing:
    def __init__(self):
        self.tl = [None] * 13


    def hash1(self, key):
        return key % 13


    def hash2(self, key):
        return 7 - (key % 7)


    def double_hash(self, key, c):
        return (self.hash1(key) + c * self.hash2(key)) % 13


    def search(self, key):
        key_i = None
        tl = self.tl
        for i in range(len(tl)):
            if tl[i] != None:
                if tl[i]['eid'] == key:
                    key_i = i
                    return

        return key_i


    def insert(self, eid, name, dept):
        data_added = False
        key_i = self.search(eid)
        if key_i == None:
            data = {
                'eid': eid,
                'name': name,
                'dept': dept
                }
            tl = self.tl
            i = self.hash1(eid)
            if tl[i] == None:
                tl[i] = data
                data_added = True
            else:
                c = 1
                while c != 13:
                    i = self.double_hash(eid, c)
                    if tl[i] == None:
                        tl[i] = data
                        data_added = True
                        break

                    c += 1

        if data_added:
            print('\nData successfully added.')
        else:
            print('\nData can not be added.')


    def delete(self, key):
        data_deleted = False
        tl = self.tl
        i = self.hash1(key)
        if tl[i] != None and tl[i]['eid'] == key:
            tl[i] = None
            data_deleted = True
        else:
            c = 1
            while c != 13:
                i = self.double_hash(key, c)
                if tl[i] != None and tl[i]['eid'] == key:
                    tl[i] = None
                    data_deleted = True
                    break

                c += 1
                

        if data_deleted:
            print('\nData deleted successfully.')
        else:
            print(f'\nGiven epmly id {key} not found.')


    def display(self):
        tl = self.tl
        for i in range(len(tl)):
            print(f'{i} --> {tl[i]}')


if __name__ == '__main__':
    while True:
        try:
            method = int(input('''1. Linear hashing
2. Double hashing
Method of handling collision: '''))
        except ValueError:
            print('\nEnter only number.\n')
        else:
            if method == 1:
                oah = Liniar_hashing()
                break
            elif method == 2:
                oah = Double_hashing()
                break
            else:
                print('\nWrong choice.\n')

    while True:
        try:
            choice = int(input('''1. Insert
2. Delete
3. Display
4. Exit
Enter your choice: '''))
        except ValueError:
            print('\nEnter only number.\n')
        else:
            if choice == 1:
                print('\n----------------------------------------')
                while True:
                    try:
                        eid = int(input('Enter emply id: '))
                    except ValueError:
                        print('Enter only number.')
                    else:
                        break

                while True:
                    name = input('Enter emply name: ')
                    name = name.strip()
                    if name:
                        break
                    else:
                        print('Empty input not allowed.')

                while True:
                    dept = input('Enter emply dept: ')
                    dept = dept.strip()
                    if dept:
                        break
                    else:
                        print('Empty input not allowed.')

                oah.insert(eid, name, dept)
                print('----------------------------------------\n')
            elif choice == 2:
                print('\n----------------------------------------')
                while True:
                    try:
                        eid = int(input('Enter emply id: '))
                    except ValueError:
                        print('Enter only number.')
                    else:
                        break

                oah.delete(eid)
                print('----------------------------------------\n')
            elif choice == 3:
                print('\n----------------------------------------')
                oah.display()
                print('----------------------------------------\n')
            elif choice == 4:
                break
            else:
                print('\nWrong choice.\n')