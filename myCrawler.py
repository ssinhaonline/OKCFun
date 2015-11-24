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
	global_users.append(user)
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
            details = page_monolith_section.find('div', {'id':'right_column'}).find('div', {'id':'profile_details'}).find_all('dl')
	    orientation = eth = status = rel_type = h = body_type = diet = smok = drnk = drugs = relg = edu = sunsign = offspring = pets = lang = 'Null'
	    for dl in details:
		if re.search('Last online', str(dl.find('dt').text)):
		    pass
		elif re.search('Orientation', str(dl.find('dt').text)):
		    try:
			orientation = dl.find('dd').text
		    except:
			orientation = 'Data_ERR'
		elif re.search('Ethnicity', str(dl.find('dt').text)):
		    try:
			eth = dl.find('dd').text
		    except:
		        eth = 'Data_ERR'
		elif re.search('Status', str(dl.find('dt').text)):
		    try:
			status = dl.find('dd').text
		    except:
		        status = 'Data_ERR'
		elif re.search('Relationship', str(dl.find('dt').text)):
		    try:
			rel_type = dl.find('dd').text
		    except:
		        rel_type = 'Data_ERR'
		elif re.search('Height', str(dl.find('dt').text)):
		    try:
			h = dl.find('dd').text
		    except:
		        h = 'Data_ERR'
		elif re.search('Body Type', str(dl.find('dt').text)):
		    try:
			body_type = dl.find('dd').text
		    except:
		        body_type = 'Data_ERR'
		elif re.search('Diet', str(dl.find('dt').text)):
		    try:
			diet = dl.find('dd').text
		    except:
		        diet = 'Data_ERR'
		elif re.search('Smoking', str(dl.find('dt').text)):
		    try:
			smok = dl.find('dd').text
		    except:
		        smok = 'Data_ERR'
		elif re.search('Drinking', str(dl.find('dt').text)):
		    try:
			drnk = dl.find('dd').text
		    except:
		        drnk = 'Data_ERR'
		elif re.search('Drugs', str(dl.find('dt').text)):
		    try:
			drugs = dl.find('dd').text
		    except:
		        drugs = 'Data_ERR'
		elif re.search('Religion', str(dl.find('dt').text)):
		    try:
			relg = dl.find('dd').text
		    except:
		        relg = 'Data_ERR'
		elif re.search('Sign', str(dl.find('dt').text)):
		    try:
			sunsign = dl.find('dd').text
		    except:
		        sunsign = 'Data_ERR'
		elif re.search('Education', str(dl.find('dt').text)):
		    try:
			edu = dl.find('dd').text
		    except:
		        edu = 'Data_ERR'
		elif re.search('Offspring', str(dl.find('dt').text)):
		    try:
			offspring = dl.find('dd').text
		    except:
		        offspring = 'Data_ERR'
		elif re.search('Pets', str(dl.find('dt').text)):
		    try:
			pets = dl.find('dd').text
		    except:
		        pets = 'Data_ERR'
		elif re.search('Speaks', str(dl.find('dt').text)):
		    try:
			lang = dl.find('dd').text
		    except:
		        lang = 'Data_ERR'
		else:
		    pass
		 
            print user + ' ' + sex + ' ' + age
	    print orientation + ' ' + eth + ' ' + status + ' ' + rel_type + ' ' + h + ' ' + body_type + ' ' + diet + ' ' + smok + ' ' + drnk + ' ' + drugs + ' ' + relg + ' ' + sunsign + ' ' + edu + ' ' + offspring + ' ' + pets + ' ' + lang            


            for item in sim_usr_list_temp:
                a_tag = item.find('a')
                href_string = a_tag.get('href')
                sim_user = re.search('profile/(.*)cf', href_string).group(1)
                ret = check_and_put(sim_user[:-1])
		if ret == False:
		    pass
            if count % 1000 == 0:
                ch = raw_input("Press X to exit, any other key to continue..")
                if ch == 'X':
                    ch = 1

        except (urllib2.URLError, urllib2.HTTPError):
            print "Could not open user: " + user
            pass
	except:
	    print "Skipping user for data error: " + user
	    pass

b_user_start = raw_input('Enter a male username: ')
g_user_start = raw_input('Enter a female username: ')
#pdb.set_trace()
ret = check_and_put(b_user_start)
ret = check_and_put(g_user_start)

spider()
