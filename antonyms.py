list= ['hot','night','black','small','fat','old']
print (list)
list2= ['cold','day','white','big','thin','young']
print (list2)
k=input("enter")
dicant=dict(zip(list,list2))
dicant1=dict(zip(list2,list))
if k in dicant.keys():
    print(dicant[k])
elif k in dicant1.keys():
    print(dicant1[k])
else:
    print("I dont know the antonym of %s",(k))
    x=input("Do you know?")
    if x=="y":
        print("what is it?")
        dicant2=dict()
        a=input()
        dicant2[k]=a
        dicant.update(dicant2)
        dicant2[a]=k
        dicant1.update(dicant2)
        print(dicant)
        print(dicant1)
    else:
        print("I dont know")
