from pathlib import Path
from PIL import Image, ImageChops, ImageFilter
import cv2, hashlib, json, numpy as np
ROOT=Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
source=ROOT/'source_png/livens_projector_chassis_blueprint_v2.png'
blueprint=ROOT/'processed_png/livens_projector_chassis_blueprint_v2_508x248.png'
mask_source=ROOT/'source_png/projectile_slot_source_mask_v1.png'
overlay=ROOT/'processed_png/projectile_slot_v1_508x248.png'
composite=ROOT/'evidence/projectile_slot_overlay_on_blueprint_v1.png'
if not source.is_file(): raise FileNotFoundError(source)
for path in (blueprint,mask_source,overlay,composite):
    if path.exists(): raise FileExistsError(path)
raw=Image.open(source).convert('RGBA')
if raw.getchannel('A').getextrema()!=(255,255): raise ValueError('Blueprint source must remain fully opaque for this consumer')
source_size=raw.size
# Source is 1796x876 (~2.0502:1); scale directly to the exact 508x248 GUI texture without cropping.
board=raw.resize((508,248),Image.Resampling.LANCZOS).convert('RGBA')
blueprint.parent.mkdir(parents=True,exist_ok=True)
board.save(blueprint,format='PNG',optimize=True)
# Delineate the three bright closed canister footprints from their actual line-art fill in the ImageGen source.
rgb=np.asarray(raw.convert('RGB'))
gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
roi=(900,280,1400,720)
x0,y0,x1,y1=roi
region=gray[y0:y1,x0:x1]
threshold=70
binary=(region>=threshold).astype(np.uint8)
count,labels,stats,centroids=cv2.connectedComponentsWithStats(binary,connectivity=8)
selected=[]
for idx in range(1,count):
    x,y,w,h,area=map(int,stats[idx])
    global_box=(x0+x,y0+y,w,h)
    if area>20000 and w>300 and 95<=h<=130 and 930<=global_box[0]<=960 and 300<=global_box[1]<=690:
        selected.append({'label':idx,'bbox':global_box,'area':area,'centroid':[float(centroids[idx][0]+x0),float(centroids[idx][1]+y0)]})
selected=sorted(selected,key=lambda item:item['bbox'][1])
if len(selected)!=3: raise ValueError(f'Expected exactly three source-matched cylinder components; found {selected}')
mask=np.zeros(gray.shape,dtype=np.uint8)
for item in selected:
    idx=item['label']
    local=labels==idx
    mask[y0:y1,x0:x1][local]=255
mask_source.parent.mkdir(parents=True,exist_ok=True)
Image.fromarray(mask,mode='L').save(mask_source,format='PNG',optimize=True)
mask_native=Image.fromarray(mask,mode='L').resize((508,248),Image.Resampling.LANCZOS)
mask_values=np.asarray(mask_native).astype(np.uint16)
alpha=np.rint(mask_values*128/255).astype(np.uint8)
rgba=np.zeros((248,508,4),dtype=np.uint8)
rgba[:,:,:3]=np.array([149,157,240],dtype=np.uint8)
rgba[:,:,3]=alpha
Image.fromarray(rgba,'RGBA').save(overlay,format='PNG',optimize=True)
blueprint_rgba=Image.open(blueprint).convert('RGBA')
overlay_rgba=Image.open(overlay).convert('RGBA')
Image.alpha_composite(blueprint_rgba,overlay_rgba).save(composite,format='PNG',optimize=True)

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def alpha_stats(im):
 a=im.getchannel('A');vals=list(a.getdata());return {'min':min(vals),'max':max(vals),'transparent':sum(v==0 for v in vals),'partial':sum(0<v<255 for v in vals),'opaque':sum(v==255 for v in vals),'bbox_alpha_gt_0':a.getbbox(),'bbox_alpha_ge_16':a.point(lambda v:255 if v>=16 else 0).getbbox()}
report={
 'source_blueprint':{'path':source.as_posix(),'sha256':sha(source),'size':list(source_size),'alpha_extrema':list(raw.getchannel('A').getextrema())},
 'processed_blueprint':{'path':blueprint.as_posix(),'sha256':sha(blueprint),'size':[508,248],'alpha_extrema':list(Image.open(blueprint).getchannel('A').getextrema()),'resize':'direct Lanczos to exact 508x248; no crop'},
 'source_delineation':{'path':mask_source.as_posix(),'sha256':sha(mask_source),'source_roi_xyxy':list(roi),'grayscale_threshold_inclusive':threshold,'connectivity':8,'selected_component_count':len(selected),'components_top_to_bottom':selected,'method':'connected components of the actual pale filled cylinder silhouettes in the supplied ImageGen blueprint source; no guessed or unrelated shape'},
 'processed_overlay':{'path':overlay.as_posix(),'sha256':sha(overlay),'size':[508,248],'rgb':[149,157,240],'alpha_max':128,'alpha_stats':alpha_stats(Image.open(overlay).convert('RGBA')),'source_mask_resize':'Lanczos from the exact blueprint source canvas to 508x248; mask pixels carry no translation or rotation'},
 'native_overlay_composite':{'path':composite.as_posix(),'sha256':sha(composite),'size':[508,248]},
 'background_mode':'native transparent overlay derived from exact source silhouette; opaque blueprint panel required by the full-canvas GUI consumer',
 'fallback_used':False
}
(ROOT/'evidence/blueprint_overlay_lineage.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
