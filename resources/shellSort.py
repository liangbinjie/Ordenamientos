def ordenShell(lista):
     inc=int(len(lista)/2 )
     while  inc>0:
          for  i in range(inc,len(lista)):
               j=i
               temp=lista[i]
               while j>=inc and lista[j-inc]>temp:
                    lista[j]=lista[j-inc]
                    j=j-inc 
               lista[j]=temp
          if (inc==2) :
               inc=1
          else :
               inc=int(inc/2.5)
     print(lista)
