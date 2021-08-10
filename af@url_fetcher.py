from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import requests
import re
import tldextract
import sys
import os
import threading
import time

urls = []

try:
    if sys.argv[1] == '-l':
        try:
            userlist = open(sys.argv[2], "r")
        except:
            print("[ERROR] file not found")
        try:
            for i in userlist:
                i = i.rstrip('\n"')
                url = ''.join(i.split('"'))
                ua = UserAgent()
                header = {'User-Agent': str(ua.random)}
                reqs = requests.get(url, headers=header)
                content = reqs.text
                soup = BeautifulSoup(content, 'html.parser')
                

                def li():
                    for h in soup.findAll('li'):
                        a = h.find('a')
                        try:
                            if 'href' in a.attrs:
                                url1 = a.get('href')
                                if url.split('www')[2] not in url1:
                                    pass
                                else:
                                    urls.append(url1)
                        except:
                            pass

                def meta():
                    for h in soup.findAll('link'):
                        try:
                            if 'href' in h.attrs:
                                url1 = h.get('href')
                                if str(url.split('www.')[1]) in url1:
                                    urls.append(url1)
                                else:
                                    pass

                        except:
                            pass

                def p():
                    for h in soup.findAll('p'):
                        a = h.find('a')
                        try:
                            if 'href' in a.attrs:
                                url1 = a.get('href')
                                if url.split('www')[1] not in url1:
                                    pass
                                else:
                                    urls.append(url1)

                        except:
                            pass

                def a():
                    for h in soup.findAll('a'):
                        try:
                            if h is not None and 'href' in h.attrs:
                                url1 = h.get('href')
                                if url.split('www')[1] not in url1:
                                    pass
                                else:
                                    urls.append(url1)

                        except:
                            pass

                def script():
                    for h in soup.findAll('script'):
                        try:
                            if 'src' in a.attrs:
                                url1 = a.get('src')
                                if url.split('www')[1] not in url1:
                                    pass
                                else:
                                    urls.append(url1)

                        except:
                            pass

                def div():
                    for h in soup.findAll('div'):
                        a = h.find('a')
                        try:
                            if 'href' in a.attrs:
                                url1 = a.get('href')
                                if url.split('www')[1] not in url1:
                                    pass
                                else:
                                    urls.append(url1)

                        except:
                            pass

                final_urls = []

                def protocol():
                    for i in urls:
                        try:
                            if 'https' not in i:
                                final_urls.append(
                                    'https://'+url.split('/')[2]+i)
                            else:
                                final_urls.append(i)
                        except:
                            pass

                thread1 = threading.Thread(target=li)
                thread2 = threading.Thread(target=p)
                thread3 = threading.Thread(target=a)
                thread4 = threading.Thread(target=script)
                thread5 = threading.Thread(target=div)
                thread6 = threading.Thread(target=meta)
                thread7 = threading.Thread(target=protocol)

                thread1.start()
                thread2.start()
                thread3.start()
                thread4.start()
                thread5.start()
                thread6.start()
                thread7.start()

                thread1.join()
                thread2.join()
                thread3.join()
                thread4.join()
                thread5.join()
                thread6.join()
                thread7.join()

                for i in list(set(final_urls)):
                    print(i)
        
        except:
            print("\n[ERROR] Incase IP Blocked this error occured!\n")
    elif sys.argv[1] == '-u':
        url = sys.argv[2]
        if url[-1] == '/':
            pass
        else:
            url = sys.argv[2]+'/'
        ua = UserAgent()
        header = {'User-Agent': str(ua.random)}
        reqs = requests.get(url, headers=header)
        content = reqs.text
        soup = BeautifulSoup(content, 'html.parser')
        time.sleep(5)

        def li_u():
            for h in soup.findAll('li'):
                a = h.find('a')
                try:
                    if 'href' in a.attrs:
                        url1 = a.get('href')
                        # if url.split('www.')[1] not in url1:
                        ext = tldextract.extract(url1)
                        domain = ''.join(ext.domain+'.'+ext.suffix)
                        URL = str(re.findall(r'//.+?/',str(url))[0])
                        if str(domain) in str(URL):
                            if 'https' not in url1:
                                print('https://'+sys.argv[1].split('/')[2]+i)
                                urls.append(url1)
                            else:
                                print(url1)
                        else:
                            pass 
       
                except:
                    pass
        def meta():
            for h in soup.findAll('link'):
                try:
                    if 'href' in h.attrs:
                        url1 = h.get('href')
                        ext = tldextract.extract(url1)
                        domain = ''.join(ext.domain+'.'+ext.suffix)
                        URL = str(re.findall(r'//.+?/',str(url))[0])
                        if str(domain) in str(URL):
                            if 'https' not in url1:
                                print('https://'+sys.argv[1].split('/')[2]+i)
                                urls.append(url1)
                            else:
                                print(url1)

                except:
                    pass

        def p():
            for h in soup.findAll('p'):
                a = h.find('a')
                try:
                    if 'href' in a.attrs:
                        url1 = a.get('href')
                        ext = tldextract.extract(url1)
                        domain = ''.join(ext.domain+'.'+ext.suffix)
                        URL = str(re.findall(r'//.+?/',str(url))[0])
                        if str(domain) in str(URL):
                            if 'https' not in url1:
                                print('https://'+sys.argv[1].split('/')[2]+i)
                                urls.append(url1)
                            else:
                                print(url1)

                except:
                    pass

        def a():
            for h in soup.findAll('a'):
                try:
                    if h is not None and 'href' in h.attrs:
                        url1 = h.get('href')
                        ext = tldextract.extract(url1)
                        domain = ''.join(ext.domain+'.'+ext.suffix)
                        URL = str(re.findall(r'//.+?/',str(url))[0])
                        if str(domain) in str(URL):
                            if 'https' not in url1:
                                print('https://'+sys.argv[1].split('/')[2]+i)
                                urls.append(url1)
                            else:
                                print(url1)

                except:
                    pass

        def script():
            script_urls = soup.findAll("script")
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(script_urls))
            for i in urls:
                ext = tldextract.extract(i)
                domain = ''.join(ext.domain+'.'+ext.suffix)
                URL = str(re.findall(r'//.+?/',str(url))[0])
                
                if str(domain) in str(URL):
                    print(i)
                else:
                    pass
        def div():
            for h in soup.findAll('div'):
                a = h.find('a')

                try:
                    if 'href' in a.attrs:
                        url1 = a.get('href')
                        ext = tldextract.extract(url1)
                        domain = ''.join(ext.domain+'.'+ext.suffix)
                        URL = str(re.findall(r'//.+?/',str(url))[0])
                        if str(domain) in str(URL):
                            if 'https' not in url1:
                                print('https://'+sys.argv[1].split('/')[2]+i)
                                urls.append(url1)
                            else:
                                print(url1)
                except:
                    pass

        thread1 = threading.Thread(target=li_u)
        thread2 = threading.Thread(target=p)
        thread3 = threading.Thread(target=a)
        thread4 = threading.Thread(target=script)
        thread5 = threading.Thread(target=div)
        thread6 = threading.Thread(target=meta)

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()

        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
    elif sys.argv[1] == '-h':
        print("[USAGE] python3 af@url_fetcher.py -l <url-list>\n[USAGE] python3 af@url_fetcher.py -u single-url")
    else:
        print("[*] Invalid flag")
        print("[HELP] python3 af@url_fetcher.py -h")

except:
    print("[*] Url not found")
