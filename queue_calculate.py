from numpy import *

# 计算阶乘
def fact(n):
    if type(n) is not int:
        raise Exception("输入不能为整数")
    if n <0:
        raise Exception("输入不能为负数")
    if n == 0:
        answer = 1
    else:
        answer = 1
        for i in range(1,n+1):
            answer *= i
    return answer


###########################################
# 计算整个通道系统处于空闲的概率
# 输入：n为通道数量，r为平均达到率 ,u为服务率
# 输出：prob为空闲概率
def prob_free(n,r,u):
    p =r/u
    s=0 ; sum=0
    while s <= n-1:
        sum += p**s/fact(s)
        s +=1
    prob = sum + p**n/(fact(n)*(1-p/n))
    prob = prob**(-1)
    return prob



###########################################
# 计算平均排队长
# 输入：n为通道数量，r为平均达到率 ,u为服务率
# 输出：Lq为平均排队长
def average_lenth_list(n,r,u):  # Lq
    p =r/u
    Lq = (Prob_free(n,r,u)*p**n*p/3)/(fact(3)*(1-p/3)**2)
    return Lq


###########################################
# 计算平均队长
# 输入：n为通道数量，r为平均达到率 ,u为服务率
# 输出：L为平均队长
def lenth_list(n,r,u):
    p =r/u
    Ls = average_lenth_list(n,r,u) + p
    return Ls


###########################################
# 计算平均等待时间
# 输入：n为通道数量，r为平均达到率 ,u为服务率
# 输出：Wq为平均等待时间
def average_wait(n,r,u):  #Wq
    Wq = average_lenth_list(n,r,u)/r
    return Wq


###########################################
# 计算平均逗留时间
# 输入：n为通道数量，r为平均达到率 ,u为服务率
# 输出：Ws为平均等待时间
def average_stay(n,r,u):
    Ws = lenth_list(n,r,u)/r
    return Ws

###########################################
# 计算顾客到达时必须排队等待的概率
# 输入：n为通道数量，r为平均达到率 ,u为服务率
# 输出：prob为等待的概率
def prob_stay(n,r,u):
    p = r/u
    prob = p**n/(fact(n)*(1-p/n))*prob_free(n,r,u)
    return prob

