import json

def ask(): #INPUT ASKING
    while True:
        asking = input("Enter Bio: ").strip()
        if asking:
            break
        print("Cannot be empty!")
    while True:
        try:
            c = int(input("Enter number of captions: "))
            if c<0:
                print("Enter positive value!")
            elif c:
                break
        except ValueError:
            print("Cannot be empty!")
    caption = []
    for i in range(c):
        while True:
            acaption = input(f"Enter Caption {i+1}: ")
            if not acaption:
                print("Cannot be empty!")
                continue
            caption.append(acaption)
            break
    return {
            "bio": asking, 
            "caption": caption
            }

def improved_json(ai_output): #FILTERING JSON
    start = ai_output.find("{")
    end = ai_output.rfind("}")
    end_output = ai_output[start:end+1]
    return end_output

def json_making(chunks_data): #JSON MAKING FOR DATA CHUNKS
    json.dumps(chunks_data)