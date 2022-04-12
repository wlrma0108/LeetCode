from sqlite3 import Cursor


class Solution(object):
    def romaToInt(self,s):
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value=0
        temp=''
        cursor=0
        while cursor<len(s):
            if(cursor+1)!=len(s) and s[cursor] +s[cursor+1] in roman:
                value+=roman[s[cursor]+s[cursor+1]]
                cursor+=2
            else:
                value+=roman[s[cursor]]
                cursor+=1
                
                
        return value

            
            