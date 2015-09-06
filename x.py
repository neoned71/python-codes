def maxset(A):
        size=len(A)
        pmax=0
        plist=[]
        cmax=0
        done=False
        clist=[]
        i=0
        while i < size:
            while i < size and A[i]>=0:
                cmax=cmax+A[i]
                print i
                clist.append(A[i])
                i=i+1
            if i < size:
                if cmax>pmax or (cmax==pmax and len(clist)>len(plist)):
                    plist=clist
                    pmax=cmax
                    done=True
                    clist=[]
                    cmax=0
            i=i+1
        if pmax>=cmax:
            print plist
        else:
            print clist


maxset([ 0,0,-1,0])
