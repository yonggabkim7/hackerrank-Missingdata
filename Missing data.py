def calcMissing(readings):
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    for n in range(len(readings)):
        a = readings[n]
        a1 = a.split()[2]
        a2 = [char for char in a1]
        if 'M' in a2:
            k = []
            for n2 in range(4):
                if (n - 2 + n2) < len(readings) and isfloat(readings[n - 2 + n2].split()[2]):
                    k.append(float(readings[n - 2 + n2].split()[2]))
            print(sum(k) / len(k))


if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)
