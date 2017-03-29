#The display class include methods that display things to
#the screen for the user.

class display:
    #This creates a dividers must be passed:
    #   * length of the divider
    #   * what the divider is made of, "=" for example
    def divider(self, length, string):
        for self.i in range(0, length):
            string = string + "="
        print(string)

    #The joiner removes and brackets and quotation marks from
    #a string handed to it and then returns it.
    def joiner(self,inp):
        if str(inp)[0] == "{":
            self.out = (str(inp).replace("{","").replace("}",""))
        if str(inp)[0] == "[":
            self.out = (str(inp).replace("[", "").replace("]", ""))
        if "'" in self.out:
            self.out = (self.out.replace("'", ""))
        if '"' in self.out:
            self.out = (self.out.replace('"', ""))
        return self.out

    # This formats a dictionary for printing in a more readble 
    # fashion
    def format(self,d, tab=1):
        self.s = ['{\n']
        for self.k, self.v in d.items():
            if isinstance(self.v, dict):
                self.v = format(self.v, tab + 1)
            else:
                self.v = repr(self.v)

            self.s.append('%s%r: %s,\n' % ('  ' * tab, self.k, self.v))
        self.s.append('%s}' % ('  ' * tab))
        return ''.join(self.s)

