code = input("ulang>")
while True:
    try:
        exec(code)
    except:
        print("Error!")
        break