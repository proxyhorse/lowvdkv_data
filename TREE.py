import pickle

chasti = {
            'zhidkost' :
                    {
                        'blood' : 10
                        ,'pee' : 5
                    }
            ,'body' :
                    {
                        'head' : 10
                        ,'body' : 35
                        ,'hands' : 5
                        ,'foots' : 10
                        ,'fingers' : 3
                        ,'nipples' : 1
                        ,'hair' : 2
                        ,'tooth' : 1
                        ,'eyes' : 1
                        ,
                    }
        }
n1 = 0
n2 = 0
n3 = 0

for i in chasti:
    z = chasti['zhidkost']
    b = chasti['body']

for x in z:
    n1 += z[x]
for q in b:
    n2 += b[q]
n3 = n1 + n2

print (n3)