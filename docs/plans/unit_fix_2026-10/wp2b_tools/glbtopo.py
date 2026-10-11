import struct, json, sys
import numpy as np
def load(p):
    b=open(p,"rb").read()
    n=struct.unpack("<I",b[12:16])[0]
    j=json.loads(b[20:20+n])
    off=20+n; 
    bl=struct.unpack("<I",b[off:off+4])[0]; bin_=b[off+8:off+8+bl]
    out=[]
    for m in j['meshes']:
        for pr in m['primitives']:
            def acc(i):
                a=j['accessors'][i]; bv=j['bufferViews'][a['bufferView']]
                ct={5126:np.float32,5125:np.uint32,5123:np.uint16,5121:np.uint8}[a['componentType']]
                nc={'SCALAR':1,'VEC2':2,'VEC3':3,'VEC4':4}[a['type']]
                o=bv.get('byteOffset',0)+a.get('byteOffset',0)
                arr=np.frombuffer(bin_,dtype=ct,count=a['count']*nc,offset=o)
                return arr.reshape(-1,nc) if nc>1 else arr
            pos=acc(pr['attributes']['POSITION']); idx=acc(pr['indices']).reshape(-1,3)
            out.append((pos,idx))
    return out
def topo(pos,idx,tol):
    q=np.round(pos/tol).astype(np.int64)
    _,inv=np.unique(q,axis=0,return_inverse=True)
    inv=inv.reshape(-1)
    f=inv[idx]
    f=f[(f[:,0]!=f[:,1])&(f[:,1]!=f[:,2])&(f[:,0]!=f[:,2])]
    e=np.concatenate([f[:,[0,1]],f[:,[1,2]],f[:,[2,0]]])
    e=np.sort(e,axis=1)
    key=e[:,0].astype(np.int64)*(inv.max()+1)+e[:,1]
    u,c=np.unique(key,return_counts=True)
    bnd=(c==1).sum(); nm=(c>2).sum()
    # components
    par=np.arange(inv.max()+1)
    def find(x):
        while par[x]!=x:
            par[x]=par[par[x]]; x=par[x]
        return x
    for a,b in zip(f[:,0],f[:,1]):
        ra,rb=find(a),find(b)
        if ra!=rb: par[ra]=rb
    for a,b in zip(f[:,1],f[:,2]):
        ra,rb=find(a),find(b)
        if ra!=rb: par[ra]=rb
    used=np.unique(f)
    comps=len({find(x) for x in used})
    return dict(verts=int(len(pos)),tris=int(len(idx)),welded=int(len(np.unique(f))),boundary=int(bnd),nonmanifold=int(nm),components=comps)
if __name__=="__main__":
    for p in sys.argv[1:]:
        for pos,idx in load(p):
            print(p.split("/")[-1], "bbox", pos.min(0).round(3), pos.max(0).round(3))
            for tol in (0.0005,0.002):
                print(" tol",tol,topo(pos,idx,tol))
