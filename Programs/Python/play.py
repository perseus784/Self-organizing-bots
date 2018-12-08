import time as t
import urllib2 as url
speed=5
angular_speed=43
def forward(distance):
    time=distance/speed
    url.urlopen("http://10.0.0.20/LED=ON")
    t.sleep(time)
    url.urlopen("http://10.0.0.20/LED=OFF")
    pass
def left(angle):
    time=angle/angular_speed
    url.urlopen("http://10.0.0.20/LED1=ON")
    t.sleep(time)
    url.urlopen("http://10.0.0.20/LED=OFF")
    pass
def right(angle):
    time = angle / angular_speed
    url.urlopen("http://10.0.0.20/LED2=ON")
    t.sleep(time)
    url.urlopen("http://10.0.0.20/LED=OFF")
    pass

def overall():
    url.urlopen("http://192.168.43.70/LED=ON")
    t.sleep(0.9)
    url.urlopen("http://192.168.43.70/LED=OFF")
    url.urlopen("http://192.168.43.72/LED2=ON")
    t.sleep(0.4)
    url.urlopen("http://192.168.43.72/LED=OFF")
    url.urlopen("http://192.168.43.73/LED=ON")
    t.sleep(0.8)
    url.urlopen("http://192.168.43.73/LED=OFF")
    url.urlopen("http://192.168.43.73/LED1=ON")
    t.sleep(0.7)
    url.urlopen("http://192.168.43.73/LED=OFF")
    url.urlopen("http://192.168.43.71/LED1=ON")
    t.sleep(0.8)
    url.urlopen("http://192.168.43.71/LED=OFF")
    url.urlopen("http://192.168.43.72/LED=ON")
    t.sleep(0.8)
    url.urlopen("http://192.168.43.72/LED=OFF")
    url.urlopen("http://192.168.43.70/LED1=ON")
    t.sleep(0.8)
    url.urlopen("http://192.168.43.70/LED=OFF")
    url.urlopen("http://192.168.43.72/LED1=ON")
    t.sleep(0.3)
    url.urlopen("http://192.168.43.72/LED=OFF")
    url.urlopen("http://192.168.43.71/LED=ON")
    t.sleep(0.7)
    url.urlopen("http://192.168.43.71/LED=OFF")
    url.urlopen("http://192.168.43.73/LED2=ON")
    t.sleep(0.6)
    url.urlopen("http://192.168.43.73/LED=OFF")
    url.urlopen("http://192.168.43.71/LED2=ON")
    t.sleep(0.7)
    url.urlopen("http://192.168.43.71/LED=OFF")
    url.urlopen("http://192.168.43.70/LED2=ON")
    t.sleep(0.8)
    url.urlopen("http://192.168.43.70/LED=OFF")
def bot70():
    url.urlopen("http://192.168.43.70/LED=ON")
    t.sleep(0.1)
    url.urlopen("http://192.168.43.70/LED=OFF")
    '''url.urlopen("http://192.168.43.70/LED1=ON")
    t.sleep(0.3)
    url.urlopen("http://192.168.43.70/LED=OFF")'''
def bot73():
    url.urlopen("http://192.168.43.73/LED=ON")
    t.sleep(0.1)
    url.urlopen("http://192.168.43.73/LED=OFF")
    url.urlopen("http://192.168.43.73/LED1=ON")
    t.sleep(0.1)
    url.urlopen("http://192.168.43.73/LED=OFF")
def bot72():
    url.urlopen("http://192.168.43.72/LED=ON")
    t.sleep(0.5)
    url.urlopen("http://192.168.43.72/LED=OFF")
    url.urlopen("http://192.168.43.72/LED1=ON")
    t.sleep(0.1)
    url.urlopen("http://192.168.43.72/LED=OFF")
def bot71():
    url.urlopen("http://192.168.43.71/LED=ON")
    t.sleep(1)
    url.urlopen("http://192.168.43.71/LED=OFF")
    url.urlopen("http://192.168.43.71/LED2=ON")
    t.sleep(0.1)
    url.urlopen("http://192.168.43.71/LED=OFF")
for i in range(5):
    forward(10)
    left(90)


