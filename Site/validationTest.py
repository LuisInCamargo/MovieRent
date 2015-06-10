__author__ = 'oem'
import cgi

def check_letras(arg):
    resp=True
    arg=arg.upper()
    for i in range(0,len(arg)):
        if(ord(arg[i])>90 or ord(arg[i])<65):
            resp=False
            return resp
    return resp
def check_mail(arg):
    resp=True
    arg=arg.upper()
    for i in range(0,len(arg)):
        if not((ord(arg[i])<90 and ord(arg[i])>64) or(ord(arg[i])<58 and ord(arg[i])>47) or ord(arg[i])==46 or ord(arg[i])==95 or ord(arg[i])==45):
            resp=False
            return resp
    return resp

def escape_html(s):
    ns = ''
    for i in range(len(s)):
        letra = s[i]
        if( letra =='&'):
            ns = ns+'&amp;'
        elif ( letra =='<'):
            ns = ns+'&lt;'
        elif ( letra =='>'):
            ns = ns+'&gt;'
        elif ( letra =='"'):
            ns = ns+'&quot;'
        else:
            ns = ns+letra
    return ns

def check_num(arg):
    resp=True
    for i in range(0,len(arg)):
        if(ord(arg[i])<48 or ord(arg[i]>57)):
            resp=False
            return resp
    return resp

def check_password(arg):
    resp=True
    arg=arg.upper()
    for i in range(0,len(arg)):
        if not((ord(arg[i])<90 and ord(arg[i])>64) or(ord(arg[i])<58 and ord(arg[i])>47)):
            if not(ord(arg[i])==46 or ord(arg[i])==95 or ord(arg[i])==45):
                resp=False
                return resp
    return resp
