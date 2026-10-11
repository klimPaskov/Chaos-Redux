"""Software preview of a Meshy GLB (flat-shaded, base colour sampled at triangle centroid). Read-only review aid."""
import struct, json, sys, os
import numpy as np
from PIL import Image, ImageDraw
def load(p):
    b=open(p,"rb").read()
    n=struct.unpack("<I",b[12:16])[0]
    j=json.loads(b[20:20+n]); off=20+n
    bl=struct.unpack("<I",b[off:off+4])[0]; bin_=b[off+8:off+8+bl]
    pr=j['meshes'][0]['primitives'][0]
    def acc(i):
        a=j['accessors'][i]; bv=j['bufferViews'][a['bufferView']]
        ct={5126:np.float32,5125:np.uint32,5123:np.uint16}[a['componentType']]
        nc={'SCALAR':1,'VEC2':2,'VEC3':3}[a['type']]
        o=bv.get('byteOffset',0)+a.get('byteOffset',0)
        arr=np.frombuffer(bin_,dtype=ct,count=a['count']*nc,offset=o)
        return arr.reshape(-1,nc) if nc>1 else arr
    return acc(pr['attributes']['POSITION']),acc(pr['attributes']['TEXCOORD_0']),acc(pr['indices']).reshape(-1,3)
def render(p, tex, out, views=("front","side","back","three"), size=900):
    pos,uv,idx=load(p)
    T=np.asarray(Image.open(tex).convert("RGB"))
    th,tw=T.shape[:2]
    imgs=[]
    lo=pos.min(0); hi=pos.max(0); c=(lo+hi)/2; ext=(hi-lo).max()
    for v in views:
        ang={"front":0,"side":90,"back":180,"three":35}[v]
        a=np.radians(ang)
        R=np.array([[np.cos(a),0,np.sin(a)],[0,1,0],[-np.sin(a),0,np.cos(a)]])
        P=(pos-c)@R.T
        # camera looks along -z (front view: viewer at +z)
        t=idx
        tri=P[t]; z=tri[:,:,2].mean(1)
        order=np.argsort(z)
        n=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]); n/= (np.linalg.norm(n,axis=1,keepdims=True)+1e-12)
        light=np.clip(n@np.array([0.3,0.4,0.85]),0.15,1)
        cuv=uv[t].mean(1)
        cx=np.clip((cuv[:,0]*tw).astype(int),0,tw-1); cy=np.clip(((cuv[:,1])*th).astype(int),0,th-1)
        col=T[cy,cx]*light[:,None]
        im=Image.new("RGB",(size,size),(70,70,75)); d=ImageDraw.Draw(im)
        sc=size*0.92/ext
        X=P[:,0]*sc+size/2; Y=size/2-P[:,1]*sc
        for i in order:
            if n[i,2]<-0.05: continue
            tt=t[i]
            d.polygon([(X[tt[0]],Y[tt[0]]),(X[tt[1]],Y[tt[1]]),(X[tt[2]],Y[tt[2]])],fill=tuple(int(x) for x in col[i]))
        imgs.append(im)
    sheet=Image.new("RGB",(size*len(imgs)//2,size//2))
    for k,im in enumerate(imgs): sheet.paste(im.resize((size//2,size//2)),(k*size//2,0))
    sheet.save(out)
if __name__=="__main__":
    render(sys.argv[1],sys.argv[2],sys.argv[3])
