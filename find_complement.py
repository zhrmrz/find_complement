class Sol:
    def find_complement(self,num):
        i=1
        while i<=num:
            i<<=1
        return (i-1)^num
