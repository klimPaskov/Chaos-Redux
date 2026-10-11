import sys, os
sys.path.insert(0,"<mod root>/.tools/3d_pipeline/runtime")
import pdx_reader, numpy as np
from PIL import Image, ImageDraw
def view(mesh, diffuse, out, angles=(180,90,0,215), size=900, flipv=True):
    t,ev=pdx_reader.read(mesh)
    Ps=[];Us=[];Is=[];off=0
    for m in t.iter("mesh"):
        P=np.array(m.attrib['p'],dtype=np.float32).reshape(-1,3)
        U=np.array(m.attrib['u0'],dtype=np.float32).reshape(-1,2)
        I=np.array(m.attrib['tri'],dtype=np.int64).reshape(-1,3)+off
        Ps.append(P);Us.append(U);Is.append(I);off+=len(P)
    P=np.concatenate(Ps);U=np.concatenate(Us);I=np.concatenate(Is)
    T=np.asarray(Image.open(diffuse).convert("RGB")); th,tw=T.shape[:2]
    lo=P.min(0); hi=P.max(0); c=(lo+hi)/2; ext=(hi-lo).max()
    ims=[]
    for ang in angles:
        a=np.radians(ang); R=np.array([[np.cos(a),0,np.sin(a)],[0,1,0],[-np.sin(a),0,np.cos(a)]])
        Q=(P-c)@R.T; tri=Q[I]; z=tri[:,:,2].mean(1); order=np.argsort(z)
        n=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]); n/=np.linalg.norm(n,axis=1,keepdims=True)+1e-12
        light=np.clip(n@np.array([0.3,0.4,0.85]),0.2,1)
        cuv=U[I].mean(1); cx=np.clip((cuv[:,0]*tw).astype(int),0,tw-1)
        cy=np.clip((((1-cuv[:,1]) if flipv else cuv[:,1])*th).astype(int),0,th-1)
        col=T[cy,cx]*light[:,None]
        im=Image.new("RGB",(size,size),(70,70,75)); d=ImageDraw.Draw(im); sc=size*0.92/ext
        X=Q[:,0]*sc+size/2; Y=size/2-Q[:,1]*sc
        for i in order:
            tt=I[i]; d.polygon([(X[tt[0]],Y[tt[0]]),(X[tt[1]],Y[tt[1]]),(X[tt[2]],Y[tt[2]])],fill=tuple(int(v) for v in col[i]))
        ims.append(im.resize((size//2,size//2)))
    s=Image.new("RGB",(size//2*len(ims),size//2))
    for k,im in enumerate(ims): s.paste(im,(k*size//2,0))
    s.save(out)
if __name__=="__main__":
    view(sys.argv[1],sys.argv[2],sys.argv[3])
