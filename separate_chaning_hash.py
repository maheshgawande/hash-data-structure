class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Separate_chaning_hash:
    def __init__(self):
        self.tl = [None] * 7


    def check_tl(self):
        is_empty = True
        tl = self.tl
        for n in tl:
            if n != None:
                is_empty = False
                return is_empty

        return is_empty


    def _hash(self, key):
        return key % 7


    def table(self, i, new_node):
        insert_status = False
        tl = self.tl
        if tl[i] == None:
            tl[i] = new_node
            insert_status = True
        else:
            cur_node = tl[i]
            while True:
                new_data = new_node.data
                cur_data = cur_node.data
                if new_data['eid'] == cur_data['eid']:
                    return insert_status

                if cur_node.next == None:
                    break

                cur_node = cur_node.next

            cur_node.next = new_node
            insert_status = True

        return insert_status


    def insert(self, eid, name, dept):
        hash_value = self._hash(eid)
        data = {
            'eid': eid,
            'name': name,
            'dept': dept
        }
        node = Node(data)
        data_inserted = self.table(hash_value, node)
        if data_inserted:
            print('-----Data inserted.-----')
        else:
            print('-----Duplicate data not allowed.-----')


    def delete(self, key):
        is_tl_empty = self.check_tl()
        if is_tl_empty:
            print('Table is empty.')
            return

        tl = self.tl
        data_deleted = False
        i = self._hash(key)
        if tl[i] != None:
            cur_node = tl[i]
            cur_data = cur_node.data
            if cur_data['eid'] == key:
                tl[i] = cur_node.next
                data_deleted = True
            else:
                while True:
                    prev_node = cur_node
                    cur_node = cur_node.next
                    cur_data = cur_node.data
                    if cur_data['eid'] == key:
                        prev_node.next = cur_node.next
                        data_deleted = True
                        break

                    if cur_node.next == None:
                        break
                    else:
                        cur_node = cur_node.next

        if data_deleted:
            print('-----Data has been deleted.-----')
        else:
            print('-----Given entry not found.-----')


    def display(self):
        is_tl_empty = self.check_tl()
        if is_tl_empty:
            print('Table is empty.')
            return

        tl = self.tl
        for node in tl:
            if node != None:
                while True:
                    if node.data != None:
                        print(node.data)

                    if node.next == None:
                        break

                    node = node.next


if __name__ == '__main__':
    sch = Separate_chaning_hash()
    while True:
        try:
            choice = int(input('''1. Insert
2. Display
3. Delete
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

                sch.insert(eid, name, dept)
                print('----------------------------------------\n')
            elif choice == 2:
                print('\n----------------------------------------')
                sch.display()
                print('----------------------------------------\n')
            elif choice == 3:
                print('\n----------------------------------------')
                while True:
                    try:
                        eid = int(input('Enter emply id: '))
                    except ValueError:
                        print('Enter only number.')
                    else:
                        break

                sch.delete(eid)
                print('----------------------------------------\n')
            elif choice == 4:
                break
            else:
                print('\nWrong choice.\n')