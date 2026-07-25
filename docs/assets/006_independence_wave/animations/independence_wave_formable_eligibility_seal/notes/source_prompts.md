# ASSET-043 source notes

Source mode: built-in ImageGen on a flat `#00ff00` chroma-key background, followed by the installed `remove_chroma_key.py` helper with soft matte and despill.

All prompts requested a centered compact painterly HOI4-style heraldic seal with no readable writing or watermark. State-specific prompt deltas were: hidden (blank shield and closed clasp), discovered (visible shield, compass star and opened clasp), eligible (joined stars, green-gold inset and lit rim segments), and proclaimed (civic crown, ribbon tabs and cyan-gold halo).

The ImageGen output masters are retained in `source_frames/`; the final state sequence uses authored heraldic state changes rather than local glow, opacity, color, or transform processing.
