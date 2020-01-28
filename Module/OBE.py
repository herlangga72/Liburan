import numpy as np
import warnings
warnings.filterwarnings("error")
class OBE():
    def Gauss_Jordan(self,matriks):
        ErrorCounter=0
        a=np.float64(matriks)
        icounter=0
        for i in a:
            print (a)
            for e in range (icounter+1,len(a)):
                bagi = a[e][icounter]/i[icounter]
                a[e]=a[e]-(bagi*i)
            if a[icounter][icounter]==0:
                print("The matriks have 0 number on desired position in row %s line %s" % (icounter , icounter))
                ErrorCounter=1
                break
            a[icounter]=a[icounter]/a[icounter][icounter]
            icounter=icounter+1
            print(a)
        if ErrorCounter !=1:
            for j in range (1,len(a)):
                p=a[len(a)-j]
                for i in range (len(a)-(j+1),-1,-1):
                    a[i]=a[i]-a[i][len(a)-j]/p[len(a)-j]*p
                print(a)
