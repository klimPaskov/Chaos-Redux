# ASSET-042 source notes

Source mode: built-in ImageGen on a flat `#00ff00` chroma-key background, followed by the installed `remove_chroma_key.py` helper with soft matte and despill.

All prompts requested a centered compact painterly HOI4-style navy-and-bronze charter medallion with no readable writing. State-specific prompt deltas were: rest (closed parchment and clasp), drafting (partially unrolled parchment and quill), vote (open parchment with three vote stars), and activated (sealed charter, joined pennants, cyan-gold halo).

The ImageGen output masters are retained in `source_frames/`; the final state sequence uses authored parchment, quill, vote-marker, pennant, and halo changes rather than local effects on one still.
