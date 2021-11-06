def ts(x) :
    try:
        x = int(x)
    except ValueError:
        try:
            x = float(x)
        except:
            pass
        else:
            return(x)
    else:
        return(x)

a, b = map(str, input().split())
try:
    a = ts(a)
    b = ts(b)
    a % b
except Exception as e: print(e)
#except NameError as px:
#    print (px)
#except TypeError as px:
#    print (px)
#except ValueError as px:
#    print (px)
#except ZeroDivisionError as px:
#    print (px)
else:
    print(a % b)
