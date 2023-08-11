dic = {'m':'t',
        'e':'h',
        'y':'e',
        'f':'p',
        'p':'a',
        'a':'s',
        'v':'w',
        'g':'o',
        's':'r',
        'u':'d',
        'w':'i',
        't':'f',
        'i':'c',
        'j':'m',
        'o':'b',
        'b':'v',
        'h':'n',
        'r':'g',
        'n':'u',
        'k':'l',
        'd':'q',
        'x':'y'
        }

s = str(input())
s = s.lower()
ans = ""
for i in range(len(s)):
    if s[i] in dic:
        ans += dic[s[i]]
    else:
        if(s[i].isalpha()):
            ans += '_'
        else:
            ans += s[i]
print(ans)