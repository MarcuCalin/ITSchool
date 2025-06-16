
while True:
    try:
        age = input("Varsta ? ")
        age = int(age)
        if age > 120:
            raise ValueError("Varsta prea mare ")
        
            break
    except ValueError as exceptie_value_error:
        print(f"Eroarea este{exceptie_value_error}")
        print("Varsta invalida ")

    except Exception as exceptie:
        print(f"Eroarea este{exceptie}")
        print("Varsta invalida ")
    finally:
        print(" Finally se executa mereu! ")
    
print (type(age))