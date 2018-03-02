f = open('yahoo.py', 'r')
print(f.read())
f.close()

with open('yahoo.py', 'r') as f:
    print(f.read())

class SampleClass:

    def __enter__(self):
        print('START')
        return self

    def myfunc(self):
        print('Do something...')

    def __exit__(self, exception_type, exception_value, traceback):
        print('END')

with SampleClass() as c:
    c.myfunc()
