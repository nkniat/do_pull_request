#funkcja biorąca "content" i zapisująca wszystkie linie w jednej liście     "razem"
def listToString(new_content_string):
    new_content_string = ''
        for line in new_content:
        new_content_string+=line
    return new_content_string