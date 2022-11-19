n=1
a=0
while n !=0:

   if n > a:
     a = n
   n = int(input("Masukkan bilangan: "))
   
   if n == 0:
     break
print("Nilai terbesarnya adalah:", a)
