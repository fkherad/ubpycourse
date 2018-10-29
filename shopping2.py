import time
c = []
d = []
with open("C:\\Users\\Lenovo\\Desktop\\Misc\\instacart_online_grocery_shopping_2017_05_01\\instacart_2017_05_01\\order_products__prior.csv", "r")as order_products__prior:
        for line in order_products__prior:
            a = line.split(',')
            b=a[1:2]
            c.append(b[0])
        for i in range(1,10000):
            d.append(c.count(str(i)))
        goal = d.index(max(d))
with open("C:\\Users\\Lenovo\\Desktop\\Misc\\instacart_online_grocery_shopping_2017_05_01\\instacart_2017_05_01\\products.csv","r")as products:
    w=time.time()
    for line in products:
        e=line.split(',')
        if e[0] == str(goal):
            print(e[1])
    q=time.time()
    x=q-w
    print("time: "+str(x))