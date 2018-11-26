import urllib2 as u
import time as t
#K-70
#J-71
#L-72
#M-73
#N-74
def fwd():
    u.urlopen("http://10.0.0.70/LED=ON")
    u.urlopen("http://10.0.0.71/LED=ON")
    u.urlopen("http://10.0.0.72/LED=ON")
    u.urlopen("http://10.0.0.73/LED=ON")
def right():
    u.urlopen("http://10.0.0.70/LED1=ON")
    u.urlopen("http://10.0.0.71/LED1=ON")
    u.urlopen("http://10.0.0.72/LED1=ON")
    u.urlopen("http://10.0.0.73/LED1=ON")
def left():
    u.urlopen("http://10.0.0.70/LED2=ON")
    u.urlopen("http://10.0.0.71/LED2=ON")
    u.urlopen("http://10.0.0.72/LED2=ON")
    u.urlopen("http://10.0.0.73/LED2=ON")
def stop():
    u.urlopen("http://10.0.0.70/LED=OFF")
    u.urlopen("http://10.0.0.71/LED=OFF")
    u.urlopen("http://10.0.0.72/LED=OFF")
    u.urlopen("http://10.0.0.73/LED=OFF")
if __name__ =="__main__":
    fwd()
    t.sleep(1)
    left()
    t.sleep(2)
    right()
    t.sleep(2)
    stop()



