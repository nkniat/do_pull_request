def usun_puste(content):
    content = str(content[0])
    x = content.replace(" ", "")
    return x

def ile_a(content):
    char = str('a')
    content = str(content[0])
    count = 0
    for c in content:
        if char == c:
            count += 1
    return count

def ile(content, x):
    char = str(x)
    content = str(content[0])
    count = 0
    for c in content:
        if char == c:
            count += 1
    return count