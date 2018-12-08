import time as t
import urllib2 as url


url.urlopen("http://10.0.0.20/LED=ON")
t.sleep(3)
url.urlopen("http://10.0.0.20/LED=OFF")
url.urlopen("http://10.0.0.20/LED2=ON")
t.sleep(2)
url.urlopen("http://10.0.0.20/LED=OFF")
url.urlopen("http://10.0.0.20/LED=ON")
t.sleep(4)
url.urlopen("http://10.0.0.20/LED=OFF")
url.urlopen("http://10.0.0.20/LED1=ON")
t.sleep(2)
url.urlopen("http://10.0.0.20/LED=OFF")
url.urlopen("http://10.0.0.20/LED1=ON")
t.sleep(3)
url.urlopen("http://10.0.0.20/LED=OFF")
url.urlopen("http://10.0.0.20/LED=ON")
t.sleep(3)
url.urlopen("http://10.0.0.20/LED=OFF")

