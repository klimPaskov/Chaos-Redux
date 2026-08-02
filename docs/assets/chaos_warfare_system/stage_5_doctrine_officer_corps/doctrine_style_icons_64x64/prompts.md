# Doctrine-style icon generation prompts

Source mode for every row: built-in `$imagegen`, generated on a flat `#00ff00` chroma-key background, then processed with the official `remove_chroma_key.py` helper. The original generated PNG is retained in `source_png/`; the alpha master is retained in `alpha_master/`.

Shared constraints for every prompt: HOI4 doctrine-style gameplay icon, centered one-subject composition, black/charcoal, warm ivory, and restrained burnt-orange palette, crisp painted/pixel-readable silhouette at 64x64, no text, no watermark, no glossy 3D, no generic skull-only art, no opaque square backdrop, no fake checkerboard, no white halo, and a perfectly flat chroma-key background with no shadows or gradients.

| Asset | Prompt-specific subject |
|---|---|
| `doctrine_hazard_assault_formations` | Forward-facing sealed respirator helmet integrated with a compact breaching shield and two short pioneer stakes; disciplined masked assault formation. |
| `doctrine_toxic_armored_warfare` | Sealed period armored tank in three-quarter view with closed crew hatch and compact chemical delivery canister behind the turret; one strong vehicle silhouette. |
| `doctrine_contaminant_fire_support` | Large chemical artillery shell in a guarded loading cradle beside a compact projector tube and elevation wheel; dominant shell/projector symbol, no explosion. |
| `doctrine_integrated_cbrn_command` | Field command map case with weather vane and telephone handset, sealed sample canister and small signal mark as secondary props; one clear command silhouette. |
