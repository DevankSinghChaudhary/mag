

def main(niche):
    chunks = []
    fixed = {}
    dynamic = {}
    for key, value in niche.items():
        if isinstance(value, list):
            dynamic[key]=value
        else:
            fixed[key]=value

    for key, value in dynamic.items():
        for items in value:
            chunk = fixed.copy()
            chunk[key]=items
            chunks.append(chunk)
    return chunks


