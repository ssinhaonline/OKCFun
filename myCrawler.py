global_users = []

import Queue
import urllib2
import pdb
import re
from bs4 import BeautifulSoup

q = Queue.Queue()

def check_and_put(user):
    if user in global_users:
        return False
    else:
        q.put(user)
        return True

def spider():
    ch = 0
    count = 0
    while (q.empty() == False) and ch != 1:
        user = q.get()
        usr_url = "https://www.okcupid.com/profile/" + user + "/"
        try:
            count = count + 1
            req = urllib2.Request(usr_url)
            response = urllib2.urlopen(req)
            src = response.read()
            soup = BeautifulSoup(src)
            sim_usr_list_temp = soup.find('ul', {'id': 'similar_users_list'}).find_all('li')
            sex = str(soup.find('div', {'id': 'basic_info'}).find('div', {'id':'aso_loc'}).find('p', {'class' : 'infos'}).find('span', {'class':'notag_gender'}).find('span',{'class':'ajax_gender'}).text)
            age = str(soup.find('div', {'id': 'basic_info'}).find('div', {'id':'aso_loc'}).find('p', {'class' : 'infos'}).find('span', {'id':'ajax_age'}).text)
            page_monolith_section = soup.find('div',{'class':'monolith'})
            essays = page_monolith_section.find('div', {'id':'main_column'}).find_all('div', {'class':'essay'})
            details = page_monolith_section.find()
            print user + ' ' + sex + ' ' + age


            for item in sim_usr_list_temp:
                a_tag = item.find('a')
                href_string = a_tag.get('href')
                sim_user = re.search('profile/(.*)cf', href_string).group(1)
                q.put(sim_user[:-1])
            if count % 1000 == 0:
                ch = raw_input("Press X to exit, any other key to continue..")
                if ch == 'X':
                    ch = 1

        except(URLError, HTTPError):
            print "Could not open user: " + user
            pass

b_user_start = raw_input('Enter a male username:')
g_user_start = raw_input('Enter a female username:')
pdb.set_trace()
ret = check_and_put(b_user_start)
ret = check_and_put(g_user_start)

spider()
