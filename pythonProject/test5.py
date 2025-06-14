import math
from operator import *

# dicc={'A':('a','b','d'),'B':('a','c'),'C':('b','e'),'D':('c','d','e')}
dicc={}
with open('ratings.dat','r') as f:
    for i in range(1000000):
        line = f.readline().strip().split("::")
        # print(type(line[0]))
        if line[2]!='5':
            continue
        if line[0] not in dicc.keys():
            dicc[line[0]]=set()
        dicc[line[0]].add(line[3])
# print(dicc)

def Usersim(dicc):
    item_user=dict()
    # print(item_user)
    for u,items in dicc.items():
        # print(u,items)
        for i in items:
            if i not in item_user.keys():
                item_user[i]=set()
            item_user[i].add(u)
    # print(item_user)
    # return
    C=dict()
    N=dict()
    for item,users in item_user.items():
        # print(item,users)
        for u in users:
            if u not in N.keys():
               N[u]=0
            N[u]+=1
            # print(u,N[u])

            for v in users:
                # print(u,v)
                if u==v:
                    continue
                if (u,v) not in C.keys():
                    C[u,v]=0
                C[u,v]+=1
    W=dict()
    for co_user,cuv in C.items():
    # print(co_user,cuv)
        W[co_user]=cuv / math.sqrt(N[co_user[0]]*N[co_user[1]])
    # print(W)
    return W

def Recommend(user,dicc,W2,K):
    rvi=1
    rank=dict()
    related_user=[]
    interacted_items=dicc[user]
    for co_user,item in W2.items():
        # print(co_user,item)
        if co_user[0]==user:
            related_user.append((co_user[1],item))
    # print(related_user)
    for v, wuv in sorted(related_user, key=itemgetter(1), reverse=True)[0:K]:
        # print(v,wuv)
        for i in dicc[v]:
            # print(i)
            if i in interacted_items:
                continue
            if i not in rank.keys():
                rank[i]=0
            rank[i]+=wuv*rvi
    return rank

W3 = Usersim(dicc)
Last_Rank=Recommend('10',dicc,W3,1)
print(Last_Rank)