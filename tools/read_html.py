
#  encoding="cp1251"

def read_html(offline_html):
    with open(offline_html) as input_file:
        return input_file.read()
