# ASSET-040 source notes

Source mode: built-in ImageGen on a flat `#00ff00` chroma-key background, followed by the installed `remove_chroma_key.py` helper with soft matte and despill.

All prompts requested a centered compact painterly HOI4-style recognition seal with a dark navy enamel disk, bronze ring, white star, no text, no watermark, and stable camera/anchor. State-specific prompt deltas were: hidden (unlit star and ticks), weak (smaller dim star and cool-blue rim), rising (medium bright star and growing cyan rim), strong (large star and complete cyan halo), and entrenched (gold wreath, full halo, settled notch).

The ImageGen output masters are retained in `source_frames/`; generated source frames are not treated as final runtime art until the mechanical chroma-key, normalization, DDS conversion, and validation steps complete.
