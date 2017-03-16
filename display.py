class display:
    def divider(self, length, string):
        for self.i in range(0, length):
            string = string + "="

        print(string)

    def joiner(self,inp):
        if str(inp)[0] == "{":
            out = (str(inp).replace("{","").replace("}",""))
            print (out)
        elif str(inp)[0] == "[":
            out = (str(inp).replace("[", "").replace("]", ""))
        return out
