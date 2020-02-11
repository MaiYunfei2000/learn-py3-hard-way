def super_int_input(prompt):
    try:
        i = int(input(prompt))
        return i
    except ValueError:
        print("Bad Input")
    except KeyboardInterrupt:
        print("Aborted")
    except:
        print("Unkown Error")
    
    return None