class StringUtility:

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string
        
    def vowels(self):
        count = 0
        for i in range(0, len(self.string)):
            if self.string[i] in "aeiouAEIOU":
                count += 1
          
        return count

    def bothEnds(self):
        self.string = self.string[0] + self.string[1] + self.string[len(self.string-1)] + self.string[-1]
        if len(self.string) <= 2:
            self.string = " "
        return self.string

    def fixStart(self):
        char = self.string[0]
        self.string = self.string.replace(char, '*')
        self.string = char + self.string[1:]
        return self.string

    def asciiSum(self):
        sum = None
        for i in range(0, len(self.string)):
            sum += ord.self.string[i]
        return sum

    def cipher(self):
        for i in range(0, len(self.string)):
            self.string[i] = chr(ord(self.string[0]) + len(self.string))
        return self.string
