__author__ = 'Administrator'
a='12=34,34=67,567=a,545=y'
q=[i.split('=') for i in a.split(',')]
print(q)
