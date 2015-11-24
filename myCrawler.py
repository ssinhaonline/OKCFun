global_users = []

import Queue
import urllib2
import pdb
import re
from bs4 import BeautifulSoup
from select import select
import sys

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
    data = open('OKCDump.csv', 'w')
    data.write('username|sex|age|orientation|ethnic|status|rel_type|height|body_type|diet|smoking|drinking|drugs|religion|sunsign|education|offspring|pets|language|self_summary|doing_in_life|really_good_at|favorites|six_things|thinking_about|friday_nights|message_me_if\n')
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
            essay0 = essay1 = essay2 = essay3 = essay4 = essay5 = essay6 = essay7 = 'Null'
            #pdb.set_trace()
            for tag in page_monolith_section.find('div', {'id':'main_column'}):
                try:
                    if re.search('essay_', tag['id']):
                        if tag['id'] == 'essay_0':
                            essay0 = tag.find('div', {'class': 'text'}).text.replace('"', '').replace('\n','')
                        elif tag['id'] == 'essay_1':
                            essay1 = tag.find('div', {'class': 'text'}).text.replace('"', '').replace('\n','')
                        elif tag['id'] == 'essay_2':
                            essay2 = tag.find('div', {'class': 'text'}).text.replace('"', '').replace('\n','')
                        elif tag['id'] == 'essay_3':
                            essay3 = tag.find('div', {'class': 'text'}).text.replace('"', '').replace('\n','')
                        elif tag['id'] == 'essay_4':
                            essay4 = tag.find('div', {'class': 'text'}).text.replace('"', '').replace('\n','')
                        elif tag['id'] == 'essay_5':
                            essay5 = tag.find('div', {'class': 'text'}).text.replace('"', '').replace('\n','')
                        elif tag['id'] == 'essay_6':
                            essay6 = tag.find('div', {'class': 'text'}).text.replace('"', '').replace('\n','')
                        elif tag['id'] == 'essay_7':
                            essay7 = tag.find('div', {'class': 'text'}).text.replace('"', '').replace('\n','')
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
            #print essay0 + ' ' + essay1 + ' ' + essay2
            details = page_monolith_section.find('div', {'id':'right_column'}).find('div', {'id':'profile_details'}).find_all('dl')
	    orientation = eth = status = rel_type = h = body_type = diet = smok = drnk = drugs = relg = edu = sunsign = offspring = pets = lang = 'Null'
	    for dl in details:
		if re.search('Last online', str(dl.find('dt').text)):
		    pass
		elif re.search('Orientation', str(dl.find('dt').text)):
		    try:
			orientation = dl.find('dd').text.replace('"', '')

		    except:
			orientation = 'Data_ERR'
		elif re.search('Ethnicity', str(dl.find('dt').text)):
		    try:
			eth = dl.find('dd').text.replace('"', '')

		    except:
		        eth = 'Data_ERR'
		elif re.search('Status', str(dl.find('dt').text)):
		    try:
			status = dl.find('dd').text.replace('"', '')

		    except:
		        status = 'Data_ERR'
		elif re.search('Relationship', str(dl.find('dt').text)):
		    try:
			rel_type = dl.find('dd').text.replace('"', '')

		    except:
		        rel_type = 'Data_ERR'
		elif re.search('Height', str(dl.find('dt').text)):
		    try:
			h = dl.find('dd').text.replace('"', '')

		    except:
		        h = 'Data_ERR'
		elif re.search('Body Type', str(dl.find('dt').text)):
		    try:
			body_type = dl.find('dd').text.replace('"', '')

		    except:
		        body_type = 'Data_ERR'
		elif re.search('Diet', str(dl.find('dt').text)):
		    try:
			diet = dl.find('dd').text.replace('"', '')

		    except:
		        diet = 'Data_ERR'
		elif re.search('Smoking', str(dl.find('dt').text)):
		    try:
			smok = dl.find('dd').text.replace('"', '')

		    except:
		        smok = 'Data_ERR'
		elif re.search('Drinking', str(dl.find('dt').text)):
		    try:
			drnk = dl.find('dd').text.replace('"', '')

		    except:
		        drnk = 'Data_ERR'
		elif re.search('Drugs', str(dl.find('dt').text)):
		    try:
			drugs = dl.find('dd').text.replace('"', '')

		    except:
		        drugs = 'Data_ERR'
		elif re.search('Religion', str(dl.find('dt').text)):
		    try:
			relg = dl.find('dd').text.replace('"', '')

		    except:
		        relg = 'Data_ERR'
		elif re.search('Sign', str(dl.find('dt').text)):
		    try:
			sunsign = dl.find('dd').text.replace('"', '')

		    except:
		        sunsign = 'Data_ERR'
		elif re.search('Education', str(dl.find('dt').text)):
		    try:
			edu = dl.find('dd').text.replace('"', '')

		    except:
		        edu = 'Data_ERR'
		elif re.search('Offspring', str(dl.find('dt').text)):
		    try:
			offspring = dl.find('dd').text.replace('"', '')

		    except:
		        offspring = 'Data_ERR'
		elif re.search('Pets', str(dl.find('dt').text)):
		    try:
			pets = dl.find('dd').text.replace('"', '')

		    except:
		        pets = 'Data_ERR'
		elif re.search('Speaks', str(dl.find('dt').text)):
		    try:
			lang = dl.find('dd').text.replace('"', '')

		    except:
		        lang = 'Data_ERR'
		else:
		    pass
		 
            #print user + ' ' + sex + ' ' + age
	    #print orientation + ' ' + eth + ' ' + status + ' ' + rel_type + ' ' + h + ' ' + body_type + ' ' + diet + ' ' + smok + ' ' + drnk + ' ' + drugs + ' ' + relg + ' ' + sunsign + ' ' + edu + ' ' + offspring + ' ' + pets + ' ' + lang            
            #pdb.set_trace()
            try:
                data.write((user + '|' + sex + '|' + age + '|' + orientation + '|' + eth + '|' + status + '|' + rel_type + '|' + h + '|' + body_type + '|' + diet + '|' + smok + '|' + drnk + '|' + drugs  + '|' + relg + '|' + sunsign + '|' + edu  + '|' + offspring + '|' + pets + '|' + lang + '|' +essay0 + '|' + essay1 + '|' + essay2 + '|' + essay3 + '|' + essay4 + '|' + essay5 + '|' + essay6 + '|' + essay7 + '\n').encode('utf8'))
            except:
                print "Data write failed for user:" + user

            for item in sim_usr_list_temp:
                a_tag = item.find('a')
                href_string = a_tag.get('href')
                sim_user = re.search('profile/(.*)cf', href_string).group(1)
                ret = check_and_put(sim_user[:-1])
		if ret == False:
		    pass
            '''if count % 1000 == 0:
                ch = raw_input("Press X to exit, any other key to continue..")
                if ch == 'X':
                    ch = 1
                else:
                    ch = 0'''

        except (urllib2.URLError, urllib2.HTTPError):
            print "Could not open user: " + user
            pass
        except KeyboardInterrupt:
            data.close()
            sys.exit()
	except:
	    print "Skipping user for data error: " + user
	    pass
    data.close()

b_user_start = raw_input('Enter a male username: ')
g_user_start = raw_input('Enter a female username: ')
#pdb.set_trace()
ret = check_and_put(b_user_start)
ret = check_and_put(g_user_start)

spider()
