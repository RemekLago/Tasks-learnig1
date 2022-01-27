import requests

websites_list_check_correct = []
websites_list_check_wrong = []

def check_website_url(website_list):
    try:
        check = request.get(website_list)
        if respond.status.code == 200:
            return True
        else:
            return False
    except requests.exceptions.ConnectionError:
        return False

with open('aaa.txt', "r", encoding="UTF-8") as file:
    for line in 'aaa.txt':
        if check_website_url('aaa.txt') == True:
            websites_list_check_correct.append(line)
        else:
            websites_list_check_wrong.append(line)
    print(websites_list_check_correct(aaa.txt))