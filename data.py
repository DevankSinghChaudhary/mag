import json

def raw_json(raw_data):
    return json.dumps(raw_data)

def improved_json(ai_output):
    start = ai_output.find("{")
    end = ai_output.rfind("}")
    end_output = ai_output[start:end+1]
    return end_output

#def ask():
#    bio = input("Enter bio: ")
#    caption = []
#    nc = int(input("Enter number of captions: "))
#    for i in range(nc):
#        c = input(f"Enter caption {i+1}: ")
#        caption.append(c)
#    return {"bio": bio, "caption": caption}