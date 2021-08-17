import in_place


with in_place.InPlace("my.txt") as f:
    for line in f.readlines():
        b = line.replace('a', 'XX')
        f.writelines(b)
