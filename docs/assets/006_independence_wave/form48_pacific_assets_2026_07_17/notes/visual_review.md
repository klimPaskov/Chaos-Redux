# FORM-48 native-size visual review

Date: 2026-07-18

## Flags

- `HBX` 82x52: red star, left-facing bear, green ground, white field, red lower
  stripe, and the dark `CALIFORNIA REPUBLIC` legend remain distinct. The
  legend is recognizable at native normal size and uses no generated extra
  wording.
- `HBX` 41x26: bear direction and the star/ground/stripe hierarchy remain
  readable; the legend compresses into a dark but still visibly lettered band.
  Fixed brown tones preserve bear articulation without gradient or texture.
- `HBX` 10x7: the bear resolves as a deliberate brown civic charge; red star,
  green ground, and red stripe remain separately visible. The historical legend
  necessarily collapses into a dark lower text band at this engine size and is
  not individually legible; it remains retained in the master/normal/medium
  ladders rather than being removed from the historical design.
- `PFX` 82x52: the rope ring, three ivory currents, compact compass, turquoise
  corridor, and gold edging are distinct.
- `PFX` 41x26: the ring, currents, compass center, and corridor retain their
  visual hierarchy without merging into a solid disk.
- `PFX` 10x7: the federal charge resolves as a gold-and-ivory navigational mark
  on the turquoise corridor; the navy field and gold edges remain distinct.
- Every runtime flag is fully opaque and uses only its declared spot palette.
  No gradient, fabric texture, lighting, perspective, or watermark is present.

## Emblem

- The raw chroma source, transparent alpha master, 128x128 processed PNG, and
  decoded DDS were compared in
  `contact_sheets/006_form48_emblem_source_and_runtime.png`.
- The open charter, eight-point compass, rising sun, three linked wave
  medallions, and rope arc remain distinct at native size.
- The decoded DDS is pixel-identical to the processed PNG. Alpha spans 0-255,
  and no visible magenta chroma pixels remain.

## Scope review

The contact sheets and package paths contain no portrait, commander, advisor,
BAY, or RHI asset. No gameplay, localisation, `.gfx`, `.gui`, or registry file
is part of the build output.

## Independent parent review

Date: 2026-07-18
Reviewer: parent implementation agent (`/root`)
Verdict: PASS

The parent reviewed the retained ImageGen source, flat master, contact sheet,
and decoded runtime ladder. The 1911 Bear Flag arrangement is faithful and the
exact `CALIFORNIA REPUBLIC` legend is readable at 82x52; medium retains
recognizable lettering, while small correctly abstracts the legend and keeps
the star, bear, grass, and stripe hierarchy. Protected BAY/RHI portrait hashes
and the zero Event 006 advisor-DDS boundary were reconfirmed unchanged.
