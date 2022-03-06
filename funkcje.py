def usun_puste(content):
    content = str(content[0])
    x = content.replace(" ", "")
    return x
def ile_a(content):
    char = "a"
    content = str(content[0])
    count = 0
    while count <= len(content):
        for char in content:
            if content[count] == char:
                count += 1
                return count



