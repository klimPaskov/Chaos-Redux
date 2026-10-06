from pathlib import Path
from PIL import Image
import hashlib, json, math

ROOT = Path('docs/assets/gfx_fix_2026-10/shared_remaining_equipment')
ASSETS = [
    {'id': 'coal_golem_equipment_v5', 'source': ROOT / 'source_png/coal_golem_equipment_v5.png', 'target': [131, 52], 'output': ROOT / 'processed_png/coal_golem_equipment_v5_131x52.png', 'margin': 2},
    {'id': 'tabun_projectile_v1', 'source': ROOT / 'source_png/tabun_projectile_v1.png', 'target': [56, 42], 'output': ROOT / 'processed_png/tabun_projectile_v1_56x42.png', 'margin': 2},
    {'id': 'archetype_livens_projector_v1', 'source': ROOT / 'source_png/archetype_livens_projector_v1.png', 'target': [58, 40], 'output': ROOT / 'processed_png/archetype_livens_projector_v1_58x40.png', 'margin': 2},
]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def bbox_above(alpha, threshold):
    return alpha.point(lambda a: 255 if a >= threshold else 0).getbbox()

def alpha_report(image):
    a = image.getchannel('A')
    vals = list(a.getdata())
    return {'min': min(vals), 'max': max(vals), 'transparent': sum(v == 0 for v in vals), 'partial': sum(0 < v < 255 for v in vals), 'opaque': sum(v == 255 for v in vals), 'bbox_alpha_gt_0': a.getbbox(), 'bbox_alpha_ge_16': bbox_above(a, 16)}

reports = []
for spec in ASSETS:
    src_path = spec['source']
    out_path = spec['output']
    if not src_path.is_file():
        raise FileNotFoundError(src_path)
    if out_path.exists():
        raise FileExistsError(f'Refusing to overwrite candidate {out_path}')
    raw = Image.open(src_path).convert('RGBA')
    alpha = raw.getchannel('A')
    source_bbox = bbox_above(alpha, 8)
    if source_bbox is None:
        raise ValueError(f'No native-alpha subject in {src_path}')
    pad = max(8, round(max(raw.size) * 0.008))
    x0, y0, x1, y1 = source_bbox
    crop_box = (max(0, x0-pad), max(0, y0-pad), min(raw.width, x1+pad), min(raw.height, y1+pad))
    cropped = raw.crop(crop_box)
    target_w, target_h = spec['target']
    margin = spec['margin']
    max_w, max_h = target_w - 2*margin, target_h - 2*margin
    scale = min(max_w / cropped.width, max_h / cropped.height)
    new_size = (max(1, round(cropped.width * scale)), max(1, round(cropped.height * scale)))
    # Resize in premultiplied-alpha space to avoid colored fringes around transparent edges.
    premultiplied = cropped.convert('RGBa')
    resized = premultiplied.resize(new_size, Image.Resampling.LANCZOS).convert('RGBA')
    canvas = Image.new('RGBA', (target_w, target_h), (0, 0, 0, 0))
    offset = ((target_w-new_size[0])//2, (target_h-new_size[1])//2)
    canvas.alpha_composite(resized, offset)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path, format='PNG', optimize=True)
    final = Image.open(out_path).convert('RGBA')
    reports.append({
        'candidate_id': spec['id'], 'source_path': src_path.as_posix(), 'source_sha256': sha(src_path),
        'source_size': list(raw.size), 'source_alpha': alpha_report(raw), 'source_bbox_alpha_ge_8': source_bbox,
        'source_crop_padding_pixels': pad, 'source_crop_box': crop_box,
        'target_size': spec['target'], 'resized_subject_size': list(new_size), 'target_offset': offset,
        'processed_path': out_path.as_posix(), 'processed_sha256': sha(out_path), 'processed_alpha': alpha_report(final),
        'background_mode': 'native_transparent', 'fallback_used': False,
        'processing': 'threshold-8 subject crop with transparent margin, premultiplied-alpha Lanczos downsample, centered on exact target canvas'
    })
report_path = ROOT / 'evidence/first_tranche_processing.json'
report_path.write_text(json.dumps(reports, indent=2), encoding='utf-8')
print(json.dumps(reports, indent=2))
