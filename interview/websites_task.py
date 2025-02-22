from websites.resources.data import WEBSITES

def find_greater(number: int) -> list:

    new_dict = []

    for website in WEBSITES:
        if website['value'] > number:
            new_dict.append(website)

    return new_dict


def amend_data():

    for website in WEBSITES:
        website['domain'] = 'www.' + website['domain']

def cleanse_data():

    for website in WEBSITES:
        if website['url'].startswith('https://'):
            website['secure'] = True
        else:
            website['secure'] = False

def addup_values() -> int:
    res = 0
    for website in WEBSITES:
       res += website['value'] if 'value' in website else 0

    return res

if __name__ == '__main__':

    # print(find_greater(4))
    # amend_data()
    # cleanse_data()
    print(addup_values())

