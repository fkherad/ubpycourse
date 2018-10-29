
import time
c = []
d = []
i = 1
with open("C:\\Users\\Milad\\Downloads\\Compressed\\instacart_online_grocery_shopping_2017_05_01\\instacart_2017_05_01\\orders.csv","r") as orders:
#with open("C:\\Users\\Lenovo\\Desktop\\Misc\\instacart_online_grocery_shopping_2017_05_01\\instacart_2017_05_01\\orders.csv" ,"r")as orders:
    for line in orders:
        a = line.split(',')
        b = a[5:6]
        c.append(b[0])
        # print(c)
    while i<=24:
      c.count(str(i))
      d.append(c.count(str(i)))
    result = sum(d)
    avg=result/24
    print(avg)
    time.time()