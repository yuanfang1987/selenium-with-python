__author__ = 'Administrator'

def add(parameter1):
    print("execute add function.",parameter1)

def delete(parameter1):
    print("execute delete function.",parameter1)

def multi(parameter1):
    print("execute multi function.",parameter1)

functions = dict(a=add,d=delete,m=multi)

functions['m']("haha")
