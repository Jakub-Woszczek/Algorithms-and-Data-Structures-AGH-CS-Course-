import random
n = 20
T = [[i,random.randint(i,i+100),random.randint(1000,1000000)] for i in range(n)]
T_2 = [[0,10,60],[1,20,100],[2,30,120]]
def Knapsack_requrzyjnie(L,waga):

    def req(L,weight_left,price,i):

        if weight_left == 0 or i == len(L):
            return price

        r_1 = req(L,weight_left,price,i+1)
        r_2 = 0
        if weight_left - L[i][1] >= 0:
            r_2 = req(L,weight_left-L[i][1],price+L[i][2],i+1)

        return max(r_1,r_2)
        # return max(req(L,weight_left,price,i+1),req(L,weight_left-L[i][1],price+L[i][2],i+1))

    return req(L,waga,0,0)

def Knapsack_dynamiq(Weights,Prices,B):

    n = len(Weights)
    F = [[0 for b in range(B+1)] for i in range(n)]

    # My tutaj
    for b in range(Weights[0],B+1):
        F[0][b] = Prices[0]

    for bruh in F:
        print(bruh)

    for b in range(B + 1):
        for i in range(1,n):
            F[i][b] = F[i-1][b]

            if b - Weights[i] >= 0:
                F[i][b] = max(F[i][b],F[i-1][b-Weights[i]] + Prices[i])

        for bruh in F:
            print(bruh)
        print('')

    return F[n-1][B]

# print(Knapsack_requrzyjnie(T_2,50))
W = [random.randint(1,10) for _ in range(10)]
P = [random.randint(100,10000) for _ in range(10)]
# Knapsack_dynamiq(W,P,40)
print(Knapsack_dynamiq([10,20,30],[60,100,120],50))