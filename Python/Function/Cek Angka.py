x = input()

try:
    x = int(x)
except ValueError:
    try:
        x = float(x)
    except ValueError:
        print('Nilai tidak valid')
        pass
    else:
        fungsi()
else:
    fungsi()