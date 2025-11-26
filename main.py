import random


class Vinyl:
    def __init__(self, title, artist, ts):
        self.title = title
        self.artist = artist
        self.ts = ts


def start(name):
    # Use a breakpoint in the code line below to debug your script.
    v1 = Vinyl("(What's the Story) Morning Glory?", 'Oasis', 40)
    v2 = Vinyl("Be here now", 'Oasis', 2 )
    v3 = Vinyl("Definitely Maybe", 'Oasis', 3)
    v4 = Vinyl("Left of the Middle", 'Natalie Imbruglia', 20)
    v5 = Vinyl("Distance", 'Utada Hikaru', 5)
    v6 = Vinyl("First Love", 'Utada Hikaru', 4)
    v7 = Vinyl("Fantôme", 'Utada Hikaru', 1)
    v8 = Vinyl("Ultra Blue", 'Utada Hikaru', 10)

    records = [v1, v2, v3, v4, v5, v6, v7, v8]
    random.shuffle(records) # Change this line

    max_ts = 0

    for v in records:
        if max_ts < v.ts:
            max_ts = v.ts

    pool = []
    for v in records:
        for i in range(max_ts - v.ts + 1):
            pool.append(v)

    #Select from pool

    records2 = []
    old_records = list(records)

    size = len(records)
    i = 0

    current_item = Vinyl('','',10)

    while i < size:
        list_size = len(records)
        if i == 0:
            random_integer = random.randint(1, list_size) - 1
            item = records[random_integer]
            current_item = item

            records.remove(item)
            records2.append(item)
        else:
            random_integer = random.randint(1, list_size) - 1
            item = records[random_integer]

            # check whether the list have only one artist left or not
            if is_one_artist(records):
                current_item = item
                records.remove(item)
                records2.append(item)
            else:
                dup = True
                while dup:
                    if current_item.artist == item.artist:
                        dup = True
                        random_integer = random.randint(1, list_size) - 1
                        item = records[random_integer]
                    else:
                        dup = False
                        current_item = item
                        records.remove(item)
                        records2.append(item)

        i = i + 1

    records3 = []
    current_item2 = Vinyl('', '', 10)

    j = 0
    while len(records3) < size:
        pool_size = len(pool)
        print('pool size:' + str(pool_size))
        if j == 0:
            random_integer = random.randint(1, pool_size) - 1
            item = pool[random_integer]

            records3.append(item)
            pool = remove_all(pool, item)

            current_item2 = item
        else:
            random_integer = random.randint(1, pool_size) - 1
            item = pool[random_integer]

            if is_one_artist(pool):
                records3.append(item)
                pool = remove_all(pool, item)

                current_item2 = item
            else:
                dup = True
                while dup:
                    if current_item2.artist == item.artist:
                        dup = True
                        random_integer = random.randint(1, pool_size) - 1
                        item = pool[random_integer]
                    else:
                        dup = False
                        current_item2 = item

                        records3.append(item)
                        pool = remove_all(pool, item)
        j = j + 1

    print('input:')
    for v in old_records:
        print(v.artist,'-', v.title)

    print('output:')
    for v in records2:
        print(v.artist,'-', v.title)

    #print('pool:')
    #for v in pool:
    #    print(v.artist,'-', v.title)

    print('records3:')
    for v in records3:
        print(v.artist,'-', v.title)

def is_one_artist(vinyls):
    artist_list = []
    for v in vinyls:
        artist_list.append(v.artist)

    if len(artist_list) == 0:
        return False
    else:
        if len(list(set(artist_list))) <= 1:
            return True
        else:
            return False


def remove_all(my_list, element):
    new_list = []
    for e in my_list:
        if e != element:
            new_list.append(e)

    return new_list

def remove_items(test_list, item):

    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
    return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start('PyCharm')