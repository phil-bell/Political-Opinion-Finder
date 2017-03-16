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
            out = (str(inp).replace("{","").replace("}",""))
        if str(inp)[0] == "[":
            out = (str(inp).replace("[", "").replace("]", ""))
        if "'" in out:
            out = (out.replace("'", ""))
        if '"' in out:
            out = (out.replace('"', ""))
        return out
