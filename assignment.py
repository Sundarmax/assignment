

class Add:

    def __init__(self):
        pass

    def add(self):
        print(1+1)


class Sub:

    def __init__(self):
        pass

    def sub(self):
        print(1-1)

class process(Add,Sub):

    def __init__(self):
        self.add()
        self.sub()


def test_tuples():
    a = (1,2,3)
    b = [1,2,3] 
    # modifying an existing list
    b[1] = 4
    print("After changing an existing list",b)
    try:
        a[1] = 4
    except Exception as e:
        print(e)

def test():
    a = [1,2,3,4]
    if len(a) > 0:
        i = len(a) - 1
        while i >= 0:
            #if i % 
            print(a[i])
            i-=1

def check_palindrome():
    string_input = "redrumurder"
    print(len(string_input))
    first = 0 
    last =  len(string_input) -1 
    while first < last:
        #print(string_input[first],string_input[last])
        if not string_input[first] == string_input[last]:
            print("Given string is not palindrome")
        first+=1
        last-=1
    else:
        print("Given string is palindrome")

check_palindrome()
