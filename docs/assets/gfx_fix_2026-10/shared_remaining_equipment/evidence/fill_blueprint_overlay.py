from pathlib import Path
from PIL import Image, ImageFilter
import cv2, hashlib, json, numpy as np
ROOT=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
source=ROOT/'source_png/livens_projector_chassis_blueprint_v2.png'
mask_source=ROOT/'source_png/projectile_slot_source_mask_v2.png'
source_overlay=ROOT/'source_png/projectile_slot_source_overlay_v2.png'
processed=ROOT/'processed_png/projectile_slot_v2_508x248.png'
staged=ROOT/'staged_dds/projectile_slot_v2.dds'
composite=ROOT/'evidence/projectile_slot_overlay_on_blueprint_v2.png'
composite4x=ROOT/'evidence/projectile_slot_overlay_on_blueprint_v2_4x.png'
overlay4x=ROOT/'evidence/projectile_slot_overlay_v2_4x.png'
for p in (mask_source,source_overlay,processed,staged,composite,composite4x,overlay4x):
    if p.exists(): raise FileExistsError(p)
raw=Image.open(source).convert('RGBA')
if raw.size!=(1796,876) or raw.getchannel('A').getextrema()!=(255,255):raise ValueError('Accepted full-canvas source dimensions/opacity changed')
rgb=np.asarray(raw.convert('RGB'));gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
roi=(900,280,1400,720);x0,y0,x1,y1=roi;region=gray[y0:y1,x0:x1];threshold=70
binary=(region>=threshold).astype(np.uint8);count,labels,stats,centroids=cv2.connectedComponentsWithStats(binary,connectivity=8)
selected=[]
for idx in range(1,count):
    x,y,w,h,area=map(int,stats[idx]);box=(x0+x,y0+y,w,h)
    if area>20000 and w>300 and 95<=h<=130 and 930<=box[0]<=960 and 300<=box[1]<=690:
        selected.append({'label':idx,'bbox':list(box),'area_before_fill':area,'centroid':[float(centroids[idx][0]+x0),float(centroids[idx][1]+y0)]})
selected=sorted(selected,key=lambda item:item['bbox'][1])
if len(selected)!=3:raise ValueError(f'Expected three actual canister silhouettes, found {selected}')
mask=np.zeros(gray.shape,dtype=np.uint8)
for item in selected:
    local=(labels==item['label']).astype(np.uint8)
    contours,_=cv2.findContours(local,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    if not contours:raise ValueError('Missing cylinder outer contour')
    outer=max(contours,key=cv2.contourArea)
    filled=np.zeros_like(local)
    cv2.drawContours(filled,[outer],-1,255,thickness=cv2.FILLED)
    # Include a narrow source-resolution contour allowance; final resampling turns it into a subpixel edge.
    filled=cv2.dilate(filled,np.ones((5,5),np.uint8),iterations=1)
    mask[y0:y1,x0:x1]=np.maximum(mask[y0:y1,x0:x1],filled)
mask_source.parent.mkdir(parents=True,exist_ok=True)
Image.fromarray(mask,'L').save(mask_source,format='PNG',optimize=True)
alpha_raw=np.rint(mask.astype(np.float32)*128/255).astype(np.uint8)
source_rgba=np.zeros((raw.height,raw.width,4),dtype=np.uint8);source_rgba[:,:,:3]=[149,157,240];source_rgba[:,:,3]=alpha_raw
Image.fromarray(source_rgba,'RGBA').save(source_overlay,format='PNG',optimize=True)
mask_native=Image.fromarray(mask,'L').resize((508,248),Image.Resampling.LANCZOS)
mask_native=mask_native.filter(ImageFilter.GaussianBlur(radius=0.45))
mask_values=np.asarray(mask_native).astype(np.uint16);alpha=np.rint(mask_values*128/255).astype(np.uint8)
rgba=np.zeros((248,508,4),dtype=np.uint8);rgba[:,:,:3]=[149,157,240];rgba[:,:,3]=alpha
Image.fromarray(rgba,'RGBA').save(processed,format='PNG',optimize=True)
board=Image.open(ROOT/'processed_png/livens_projector_chassis_blueprint_v2_508x248.png').convert('RGBA')
layer=Image.open(processed).convert('RGBA')
Image.alpha_composite(board,layer).save(composite,format='PNG',optimize=True)
Image.open(composite).convert('RGBA').resize((2032,992),Image.Resampling.BICUBIC).save(composite4x,format='PNG',optimize=True)
Image.open(processed).convert('RGBA').resize((2032,992),Image.Resampling.BICUBIC).save(overlay4x,format='PNG',optimize=True)
# Confirm exactly three separate filled silhouettes and no internal holes at the final alpha body level.
final_alpha=np.asarray(Image.open(processed).getchannel('A'))
solid=(final_alpha>=64).astype(np.uint8)
nlabels,final_labels,final_stats,_=cv2.connectedComponentsWithStats(solid,connectivity=8)
components=[]
for i in range(1,nlabels):
    x,y,w,h,area=map(int,final_stats[i])
    if area>100:components.append({'bbox':[x,y,w,h],'area':area})
components=sorted(components,key=lambda c:c['bbox'][1])
if len(components)!=3:raise ValueError(f'Expected exactly three final filled silhouettes, got {components}')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def astats(a):
 v=list(a.getdata());return {'min':min(v),'max':max(v),'zero':sum(x==0 for x in v),'partial':sum(0<x<255 for x in v),'bbox_gt_0':a.getbbox(),'bbox_ge_16':a.point(lambda x:255 if x>=16 else 0).getbbox()}
report={'candidate_id':'projectile_slot_v2','parent_source':{'path':source.as_posix(),'sha256':sha(source),'size':list(raw.size)},'previous_mask_candidate':'projectile_slot_v1 rejected: thresholded interiors left dark texture gaps', 'delineation':{'roi_xyxy':list(roi),'grayscale_threshold_inclusive':threshold,'connectivity':8,'method':'extract the three source-connected canister regions, take each actual external contour and fill that contour; internal threshold holes are discarded; a 5x5 source-resolution dilation adds a narrow subpixel contour allowance before exact shared-resize mapping','source_components':selected,'filled_source_mask_path':mask_source.as_posix(),'filled_source_mask_sha256':sha(mask_source)},'source_overlay_png':{'path':source_overlay.as_posix(),'sha256':sha(source_overlay),'size':list(raw.size),'rgb':[149,157,240],'alpha_max':128,'alpha_stats':astats(Image.open(source_overlay).getchannel('A'))},'processed_overlay_png':{'path':processed.as_posix(),'sha256':sha(processed),'size':[508,248],'rgb':[149,157,240],'alpha_max':128,'alpha_stats':astats(Image.open(processed).getchannel('A')),'source_to_target':'same direct 1796x876 to 508x248 Lanczos resize used by blueprint; no translation, rotation, or separate layout transform','final_filled_components':components,'antialias':'Lanczos downsample plus 0.45px Gaussian edge smoothing; final full-alpha edge is at most 128'},'composite_native':{'path':composite.as_posix(),'sha256':sha(composite)},'composite_smooth_4x':{'path':composite4x.as_posix(),'sha256':sha(composite4x)},'overlay_only_smooth_4x':{'path':overlay4x.as_posix(),'sha256':sha(overlay4x)},'fallback_used':False}
(ROOT/'evidence/blueprint_overlay_lineage_v2.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
