def duplicate_count(text):
    text = text.lower()
    lst = [(el,text.count(el)) for el in text]
    s = set(lst)
    l = [el for el in s if el[1]>1]
    return len(l)