import timeit
import matplotlib.pyplot as plt
import numpy
%matplotlib inline

def bench_mmm(startn,maxn,step,loops):
    count=0
    
    #Preallocate results lists
    avg_gflops = int((1+(maxn-startn)/step))*[0] 
    peak_gflops = int((1+(maxn-startn)/step))*[0]
    raw_times = [int(loops)*[0] for i in range(int(1+(maxn-startn)/step))]
    all_gflops = [int(loops)*[0] for i in  range(int(1+(maxn-startn)/step))]
    mat_size=int((1+(maxn-startn)/step))*[0] 

    for n in range(startn,maxn+step,step):
        setup_string = "from pylab import rand,dot;n=%d;a=rand(n,n);b=rand(n,n)" % n
        time_list = timeit.repeat("a.dot(b)", setup=setup_string, repeat=loops,number=1)
        raw_times[count] = time_list
        total_time = sum(time_list)
        avg_time = total_time / loops
        peak_time = min(time_list)
        num_ops = 2*n**3-n**2
        avg_gflops[count] = (num_ops/avg_time)/10**9
        peak_gflops[count] = (num_ops/peak_time)/10**9
        all_gflops[count] = [(num_ops/time)/10**9 for time in raw_times[count]]        
        mat_size[count] = n
        count=count+1
    
    plt.plot(mat_size,avg_gflops,'*-',label="Average over %d runs" %loops)
    plt.plot(mat_size,peak_gflops,'*-',label="Peak")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel('Matrix Size');
    plt.ylabel('GFlop/s');
    plt.show()
    
    return(max(peak_gflops),raw_times,all_gflops)

peak_flops = bench_mmm(50,200,50,50)

#CPU and host info. Most of this cell only works on Linux
import multiprocessing
!date
!uname -r
!test -d /etc/redhat-release && cat /etc/redhat-release !test -d /etc/debian_version && cat /etc/debian_version !test -d /etc/os-release && cat /etc/os-release
print('CPUS available = {0}'.format(multiprocessing.cpu_count()))
!hostname
!cat /proc/cpuinfo | grep 'model name' | uniq
!echo "OMP_NUM_THREADS=$OMP_NUM_THREADS"
print('Measured peak speed = {0} Gigaflops'.format(max(result1,result2)))

N=180000

maxprime = 18*N+1
prime = [1]*maxprime
prime[0] = prime[1] = 0
for i in range(maxprime):
  if prime[i]:
    for j in range(2*i,maxprime,i):prime[j]=0

for i in range(N):
  a=6*i+1
  b=12*i+1
  c=18*i+1
  if prime[a] and prime[b] and prime[c]:print(a*b*c)
  
  #!/usr/bin/env python
# -*- coding: cp1252 -*-
from math import sqrt

def diviseurs(n):
    D,racine=[1],int(sqrt(n))
    fin=racine+1
    for d in range(2,fin):
        if n%d==0 :
            D.extend([d,n//d])
    D=sorted(set(D))
    return D


print "           *****************************************************"
print "           *  Calcul de l'indicatrice d'Euler par différences  *"
print "           *****************************************************"
print

n=144457825
D=diviseurs(n)
print "D("+str(n)+") =",D
print
Phi,somme=[1],"1"

for i,div in enumerate(D):
    print "Phi("+str(div)+") =",
    ch=str(div)
    if div==1:
        print"1"
    else:
        D_i,q=[d for d in D if div%d==0 and d<div],0
        for d in D_i:
            q+=Phi[D.index(d)]
        ch+="-"+str(q)
        p=div-q
        Phi.append(p)
        somme+="+"+str(p)
        print str(div)+"-Somme des Phi des diviseurs<"+str(div)+" =",ch,"=",div-q
    ch=""
print
print "Somme :",somme,
print "=",sum(Phi)
print "          Phi("+str(n)+") =",str(n)+" - "+str(sum(Phi)),"=", n-sum(Phi)
