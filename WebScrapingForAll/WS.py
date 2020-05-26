import requests
import sys

def obj(source_cod, pos_ini, start, end):
    pos_ini = source_cod.find(str(start),pos_ini)
    pos_fini = source_cod.find(str(end), pos_ini)
    output=source_cod[pos_ini+len(start):pos_fini]
    return [output, pos_fini]



def FindKey(address,training):
    source=requests.get(str(address)).text
    numkw=[]
    for i in training:
        nkw=source.count(str(i))
        numkw.append(nkw)
    if max(numkw)>1:    
        print('One or more kewyords have more than one appearance, wil go with\
              first. Check source code (crtl+u) for a more specific key')
    keysst=[]
    for i in training:
        nkey=2
        lnky=1
        posi=source.find(str(i))
        while nkey>1:
            key=source[posi-lnky:posi+len(i)]
            nkey=source.count(str(key))
            lnky=lnky+1
        key=key[0:len(key)-len(i)]
        keysst.append(key)
    keysnd=[]
    for i in training:
        nkey=2
        lnky=1
        posi=source.find(str(i))
        while nkey>1:
            key=source[posi:posi+len(i)+lnky]
            nkey=source.count(str(key))
            lnky=lnky+1
        key=key[len(i):len(key)]
        keysnd.append(key)
    keyst=list(set(keysst))    
    keynd=list(set(keysnd))
    if len(keyst)>1 or len(keynd)>1:
        sys.exit('No one key found, to many diffrent patherns in sourcecode')
    keyst=str(keyst[0])   
    keynd=str(keynd[0])
    print('Key start:'+str(keyst)+' and key end:'+str(keynd))
    return [keyst,keynd]



def ManyInOne(address,keyst,keynd):
    results=[]
    source=requests.get(str(address)).text
    nky=source.count(keyst)
    i=1
    pos0=1
    results=[]
    while i <=nky:
        result=obj(source_cod=source,pos_ini=pos0,start=keyst,end=keynd)
        results.append(result[0])
        pos0=result[1]+1
        i=i+1
    return results


def OneInMany(address,keyst,keynd):
    results=[]
    if not type(address) is list:
        address=[address]
    for i in address:
        source=requests.get(str(i)).text
        nky=source.count(keyst)
        j=1
        pos0=1
        results=[]
        while j <=nky:
            result=obj(source_cod=source,pos_ini=pos0,start=keyst,end=keynd)
            results.append(result[0])
            pos0=result[1]+1
            j=j+1
        return results
