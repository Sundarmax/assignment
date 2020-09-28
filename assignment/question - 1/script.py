

class QueryString:
    
    input_string = None  # Member variable with public access

    def __init__(self,input_string):
        '''constructor'''
        self.input_string = input_string
        self.result = {}
        self.stack = [] # stack

    def query_string_validation(self):
        '''A function which performs string validation with the help of stack and return the result'''
        if len(self.input_string) > 0 :
            for char in self.input_string:
                if char == '(':
                    self.stack.append(char)
                if char == ')':
                    try:
                        stack_top = self.stack[-1]
                    except IndexError:
                        return False
                    if stack_top == '(':
                        #print('Stack--> ',self.stack)
                        #print('Inc : ' ,char,'Stop :',stack_top)
                        self.stack.remove(stack_top)
            if len(self.stack) > 0:
                return False
            else:
                return True

    def design_json_output(self,start,end):
        _parent = {}
        _child  = {}
        _parentKey = ""
        while start < end:
            if self.input_string[start] == "=":
                _child.update({ self.input_string[start-1] : self.input_string[start+1] })
                if self.input_string[start+2] == '&' and self.input_string[start+3] == '&':
                    _parentKey = "and"
                if self.input_string[start+2] == '|' and self.input_string[start+3] == '|':
                    _parentKey = "or"
            start+=1
        if _parentKey == "":
            return "Syntax invalid"
        _parent[_parentKey] = _child
        return _parent

    def query_string_conversion(self):
        '''A function which accepts valid Q string and convert to Q json'''
        terms_count = 0
        # Remove whitespaces in the string .
        new_string = self.input_string.replace(" ", "") 
        self.input_string = new_string 
        _parentkey = ""
        _parentList = []
        _resultDict = {}
        for i,char in enumerate(self.input_string):
            # Get the term count by checking their ascii values.
            # Alphabets in the given expression must be uppercase.  
            if ord(char) >= 65 and ord(char) <= 90:
                terms_count+=1
                if terms_count == 1:
                    start_point = i
            if char == ')' and terms_count == 2: # Case-3 Fail which was mentioned below        
                try:
                    if self.input_string[i+1] == '|' and self.input_string[i+2] == '|':
                        _parentkey = "or"
                    if self.input_string[i+1] == '&' and self.input_string[i+2] == '&':
                        _parentkey = "and"
                except Exception as e:
                    return "Syntax invalid" 
                end_point   = i
                terms_count = 0
                term_output = self.design_json_output(start_point,end_point)
                if term_output == "Syntax invalid":
                    return "Syntax invalid"
                _parentList.append(term_output)
        # design a json
        _resultDict.update({_parentkey: _parentList})
        self.result["query"] = _resultDict
        if terms_count > 0 or _parentkey == "":
            return "Syntax invalid"
        return self.result

    def process(self):
        is_valid = self.query_string_validation()
        if is_valid is not True:
            return "Syntax invalid"
        else:
            return self.query_string_conversion()

print("# ------ Test Cases for valid Result --------------#")
String = "((A=2 || B=3) || (C=4 && D=5))"
print("Valid-->  ((A=2 || B=3) || (C=4 && D=5))")
print("# ------ Test Cases for Invalid Result ------------#")
print("Invalid --> ((A=2 && B=3)) || (C=4 && D=5))")
#String = "((A=2 && B=3 || (C=4 && D=5))"
#String = "((A=2 && B=3 || C=4 && D=5))"
obj     = QueryString(String)
output  = obj.process()
print("# -----------------------------------------------#")
print("Input : ",String)
print("Output  : ",output)
