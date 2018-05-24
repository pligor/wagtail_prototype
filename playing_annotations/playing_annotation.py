
def myanno(func):
    def mywrapper(param):
        print("this is the param: {}".format(param))
        resp = func(param)
        print("this is the response: {}".format(resp))
        return resp + 10

    return mywrapper

@myanno
def myfunc(the_param):
    print("this is the parameter inside func: {}".format(the_param))
    return the_param * 2



if __name__ == '__main__':
    print(myfunc(33))