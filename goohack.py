#!/usr/bin/env python3

import subprocess
import time
import sys

def open_urls_with_firefox(urls, delay=5):
    for url in urls:
        subprocess.Popen(['firefox', url])
        time.sleep(delay)

def main(target):
    if not target:
        print("\033[93m + -- --=[google hacking python\033[0m")
        print("\033[93m + -- --=[GooHack.py jeanoliveirafs v1.0 \033[0m")
        print("\033[93m + -- --=[Usar:./goohak.py <domain>\033[0m")
        sys.exit()

    urls = [
        f"http://{target}",
        f"https://{target}",
        f"https://search.dnslytics.com/search?d=%3Call%3E&utm_source=website&utm_medium=search&utm_campaign=homepage&q={target}",
        f"http://toolbar.netcraft.com/site_report?url={target}",
        f"https://www.shodan.io/search?query={target}",
        f"https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q={target}",
        f"https://crt.sh/?q=%25.{target}",
        f"https://www.google.ca/search?q=site:zone-h.org+{target}",
        f"https://www.xssposed.org/search/?search={target}&type=host",
        f"https://securityheaders.io/?q={target}",
        f"https://www.ssllabs.com/ssltest/analyze.html?d={target}",
        f"https://securityheaders.io/?q={target}",
        f"https://www.zoomeye.org/searchResult/bugs?q={target}",
        f"https://securitytrails.com/search/domain/{target}/dns",
        f"https://web.archive.org/web/*/{target}",
        f"http://viewdns.info/reversewhois/?q={target}",
        f"https://www.google.ca/search?q=site:*.{target}",
        f"https://www.google.ca/search?q=site:*.*.{target}",
        f"https://www.google.ca/search?q=site:{target}+username+OR+password+OR+login+OR+root+OR+admin",
        f"https://www.google.ca/search?q=site:{target}+inurl:shell+OR+inurl:backdoor+OR+inurl:wso+OR+inurl:cmd+OR+shadow+OR+passwd+OR+boot.ini+OR+inurl:backdoor",
        f"https://www.google.ca/search?q=site:{target}+inurl:readme+OR+inurl:license+OR+inurl:install+OR+inurl:setup+OR+inurl:config",
        f"https://www.google.ca/search?q=site:{target}+inurl:wp-+OR+inurl:plugin+OR+inurl:upload+OR+inurl:download",
        f"https://www.google.ca/search?q=site:{target}+inurl:redir+OR+inurl:url+OR+inurl:redirect+OR+inurl:return+OR+inurl:src=http+OR+inurl:r=http",
        f"https://www.google.ca/search?q=site:{target}+ext:cgi+OR+ext:php+OR+ext:asp+OR+ext:aspx+OR+ext:jsp+OR+ext:jspx+OR+ext:swf+OR+ext:fla+OR+ext:xml",
        f"https://www.google.ca/search?q=site:{target}+ext:doc+OR+ext:docx+OR+ext:csv+OR+ext:pdf+OR+ext:txt+OR+ext:log+OR+ext:bak",
        f"https://www.google.ca/search?q=site:{target}+ext:action+OR+struts",
        f"https://www.google.ca/search?q=site:pastebin.com+{target}",
        f"https://www.google.ca/search?q=site:linkedin.com+employees+{target}"
    ]

    open_urls_with_firefox(urls)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("\033[93m + -- --=[google hacking python\033[0m")
        print("\033[93m + -- --=[GooHack.py jeanoliveirafs v1.0 \033[0m")
        print("\033[93m + -- --=[Usar:./goohak.py <domain>\033[0m")
        sys.exit()

    target = sys.argv[1]
    main(target)
