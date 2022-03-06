#funkcja usuwająca puste linie   "usun_puste"
def usun_puste(content):
    new_content = []
    for line in content:
        if line != '\n':
            new_content.append(line)
    return new_content

