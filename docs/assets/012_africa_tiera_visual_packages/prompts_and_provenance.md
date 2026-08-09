# Event 012 promoted Tier A visual prompts and provenance

This package is generated symbolic art for six fictional high-chaos cosmetic identities. The source files are retained under `source_flags/` and `source_emblems/`; no real people, historical flags, readable text, or new country tags are represented.

## Source-mode audit

The five existing flag/emblem masters were present in the ignored partial package before this tranche. They are valid generated flat designs or chroma-key emblem masters and were retained after visual review. Their PNG files contain no embedded prompt metadata, so the original generation call is unavailable. The normalized acceptance prompts below record the exact visual constraints used to accept each retained source; this uncertainty is carried in `manifest.json` as `generated_imagegen_partial`.

Ancient Hosts emblem is the only newly generated source in this tranche. It was produced through the official ImageGen tool with the exact prompt recorded below and saved as `source_emblems/ancient_hosts_dhx_emblem_imagegen_source.png`.

## Normalized acceptance prompts for retained flag masters

### Pan (EBX)

`Use a flat orthographic alternate-history flag for a fictional lean great-ape engineer polity: dark forest green field, a readable ochre great-ape profile, crossed workshop tool and leaf motif, crisp heraldic outline, no fabric, folds, pole, perspective, shadows, text, watermark, modern props, or people beyond the symbolic ape mark.`

### Gorilla Kingdom (EHX)

`Use a flat orthographic alternate-history flag for a fictional gorilla kingdom: deep navy field, broad silverback gorilla centered before a mountain crown, restrained gold border and crown, crisp heraldic construction, no fabric, folds, pole, perspective, shadows, text, watermark, or modern props.`

### The Green (DPX)

`Use a flat orthographic alternate-history flag for a living forest and ritual ecology: deep teal field, luminous green tree canopy with root-and-eye ecological seal, crisp heraldic construction, no fabric, folds, pole, perspective, shadows, text, watermark, or modern props.`

### Living Rivers (EEX)

`Use a flat orthographic alternate-history flag for a river-braid civilization: deep blue field, four turquoise river branches converging into an ivory central knot beneath a small flood crown, crisp readable geometry, no fabric, folds, pole, perspective, shadows, text, watermark, or modern props.`

### Stoneborn (DFX)

`Use a flat orthographic alternate-history flag for volcanic highland monoliths: charcoal field, centered basalt monolith/stoneborn silhouette with a pale stone core and rust volcanic lower band, thin corner marks, crisp heraldic construction, no fabric, folds, pole, perspective, shadows, text, watermark, or modern props.`

### Ancient Hosts (DHX)

`Use a flat orthographic alternate-history flag for an antique host and ruin standard: oxblood upper band, ochre lower field, centered antique bronze spear-standard and ivory sun disk in a dark circular mount, crisp heraldic construction, no fabric, folds, pole, perspective, shadows, text, watermark, or modern props.`

## Exact ImageGen prompt for Ancient Hosts emblem

`Use case: logo-brand. Asset type: fictional alternate-history country emblem/seal for Hearts of Iron IV, 64x64 runtime icon. Primary request: a distinctive antique host seal for the fictional AFRICA_PROMOTED_ANCIENT identity: an ancient stone-and-bronze ceremonial standard rising from a broken archaeological ruin, a geometric sun disk behind it, two small crossed spear standards, restrained archaeological motifs, no people or faces. Scene/backdrop: perfectly flat solid chroma-key #00ff00 background for local removal; no floor, no shadow, no gradient. Subject: centered compact heraldic emblem with clear silhouette at 64x64, antique ruin standard and sun disk. Style/medium: crisp flat heraldic graphic with limited textured stone/bronze accents, readable game icon, orthographic front view. Composition/framing: centered, symmetrical, generous padding, thick dark outline, no circular badge border unless naturally part of the emblem. Lighting/mood: even graphic lighting, solemn ancient authority. Color palette: charcoal basalt, aged bronze, muted sandstone, ivory sun, deep brown outline; do not use chroma green in the emblem. Materials/textures: simplified carved stone and hammered bronze, crisp edges, no photoreal scene. Text (verbatim): "". Constraints: no text, no letters, no watermark, no UI, no modern objects, no fabric flag, no people, no perspective, no cast shadow, no halo; background must be one perfectly uniform #00ff00 color.`

## Processing

Flags were center-cropped to the vanilla 82:52 ratio and resized to 82x52, 41x26, and 10x7 with Lanczos resampling. All flag alpha was normalized opaque. Normal/medium TGA files use the vanilla 32-bit bottom-left origin convention with the TGA footer; small TGA files use the vanilla 18-byte header, 32-bit pixels, bottom-left origin, no footer convention. Emblems were chroma-keyed with the official `remove_chroma_key.py` helper, cropped to the subject bounds with padding, resized to 64x64 RGBA, and converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` to uncompressed BGRA DDS.
