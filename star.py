#!usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
from optparse import OptionParser
import sys
from termcolor import colored
if sys.version_info[0] >= 3:
    from urllib.parse import urljoin
else:
    from urlparse import urljoin

class Crawler:
    def __init__(self):
        self.about()
        self.script_desc()
        self.target_links = []


    def arguman_al(self):
        parse = OptionParser(description=self.description,epilog=self.use,prog=self.program)
        parse.add_option("-u", "--url", dest="url", help="Hedef url")
        (options, arguments) = parse.parse_args()
        if not options.url:
            parse.error("[-] Please specify a url, use --help for more information .")
        return options

    def get_links(self,url):
        try:
            if "http://" in url   or "https://" in url:
                response=requests.get(url)
                return re.findall('(?:href=")(.*?)"', str(response.content))
            else:
                response=requests.get("http://"+url)
                return re.findall('(?:href=")(.*?)"',str(response.content))
        except requests.exceptions.ConnectionError:
            pass
        except requests.exceptions.InvalidURL:
            pass
        except UnicodeError:
            pass


    def crawl(self,url):
        href_links=self.get_links(url)
        if href_links:
            for link in href_links:
                link=urljoin(url,link)
                if "#" in link:
                    link=link.split("#")[0]
                if options.url in link and link not in self.target_links:
                    self.target_links.append(link)
                    print(link)
                    self.crawl(link)


    def result_count(self):
        print(colored("[+] in total "+ str(len(self.target_links))+" one link found ","green"));

    def script_desc(self):
        self.program="spider"
        self.use="""Example Usage1 : python spider.py --url http://example/etc
        \n\n\n\n\n 
      Example Usage2 : python spider.py -u  http://example/etc """
        if sys.version_info[0] >= 3:
            self.description = "A web crawler script that crawls the target website and lists its links. "
        else:
            self.description = unicode("A web crawler script that crawls the target website and lists its links. ", "utf8")
            self.use = unicode(self.use,"utf8")


    def about(self):
      print(colored("        _, ", "green"))                    
    print(colored("             _       .'` | ", "green"))
    print(colored("             \`'-.  / .' ; ", "green"))
    print(colored("              '.  \/ :' / ", "green"))
    print(colored("                \ | :' / ", "green"))
    print(colored("                _)\ '_/ ", "green"))
    print(colored("             .'`     `\ ", "green"))
    print(colored("            /e         | ", "green"))
    print(colored("           o-'   e     | ", "green"))
    print(colored("          =\__=       / ", "green"))
    print(colored("            '--,--'   \ ", "green"))
    print(colored("             .'        | ", "green"))
    print(colored("          .-/  _,      | ", "green"))
    print(colored("         /  ;/`       / ", "green"))
    print(colored("         \  |    __.'( ", "green"))
    print(colored("          '-\   /     '. ", "green"))
    print(colored("            |;-'        \.--. ", "green"))
    print(colored("             \   /       \   } ", "green"))
    print(colored("             _'. |        |_.' ", "green"))
    print(colored("          .-'   ` \      / ", "green"))
    print(colored("         /       .-'    ( ", "green"))
    print(colored("         \,,__.-/       / ", "green"))
    print(colored("# author      :","green")+"Ashutosh Raval")
    print(colored("# linkedin    :","green")+"https://www.linkedin.com/in/ashutosh-raval-b58b89137")
    print(colored("# title       :","green")+"Star.py")
    print(colored("# description :","green")+"A web crawler script that crawls the target website and lists its links. ")
    print(colored("# date        :","green")+"7.10.2021")
    print(colored("# version     :","green")+"1.0")
    print(colored("# ==============================================================================","green"))

    def keyboardinterrupt_message(self):
        print("[-] CTRL+C printed. Exiting the application. ...")
        print("[-] Signed out of the app !")


try:
    crawl=Crawler()
    options=crawl.arguman_al()
    print(colored("[+] Scanned Web Address :","green")+options.url+"\n")
    crawl.crawl(options.url)
    crawl.result_count()
except KeyboardInterrupt:
    crawl.keyboardinterrupt_message()


