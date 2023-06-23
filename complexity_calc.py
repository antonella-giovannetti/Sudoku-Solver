from timeit import default_timer as timer 

start = timer()
# tâches dont on veut mesurer le temps d'exécution.
end = timer()
print(end - start) # affichage du temps écoulé   

def conversion(n:float)->tuple:
    h = n // 3600 
    m = (n-3600*h) // 60 
    s = n % 60
    return h,m,s 
#  Coût en temps (constant) 0(1)
# T(n) = 3 + 6 + 3 = 12

def puissanceMoinsUn(n:int)->int:
	if n%2==0:
		res = 1
	else:
		res = -1
	return res
#  Coût en temps (constant) 0(1)
# T(n) = 3 + 1 = 4

def sommeEntiers1(n:int)->int:
	somme = 0
	for i in range(n+1):
		somme += i
	return somme
#  Coût en temps (linéaire) 0(n)
# T(n) = 1 + 6n

def Somme_amis(Tab2)->int:
	somme = 0
	for i in range(n):
		for j in range(i+1,n):
			somme = somme + Tab2[i][j]
	return somme
#  Coût en temps (quadratique) 0(n²)
# T(n) = (6n + 2)n = 6n² + 2n + 1 