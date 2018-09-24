liste1 = ['a','b','c','d','j','g','e']
liste2 = ['b','d']
liste3 = []
print(liste1)
print(liste2)
for i in range(0,7):
#    print (liste1[i])
 #   print(i)
    for j in range(0,2):

        if liste2[j] < liste1[i]:
            liste3.append(liste1[i])
            print (liste1[i])
print ((sorted(liste3)))
