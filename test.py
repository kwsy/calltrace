from pycalltrace import CallTrace

def func1():
    print('ok')

def func2():
    func1()

def func3():
    func2()

def func4():
    func3()

def file_filter(filename):
    if filename.find('calc') != -1:
        return True
    return False


with CallTrace(filter_func=lambda x: x.find('calc') == -1):
    func4()

# call_trace = CallTrace(filter_func=lambda x: x.find('calc') == -1)
# call_trace.start()
# func4()
# call_trace.stop()
# call_trace.output()