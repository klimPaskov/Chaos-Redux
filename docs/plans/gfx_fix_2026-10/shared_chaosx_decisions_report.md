# Shared decision icon repairs

Disposition: both assigned finding rows implemented.
Acceptance basis: the graphics-fix task requests the rocket category margin and flat skull decision icon.

| Finding | Result | Runtime |
|---|---|---|
| Space Race category, severity 3 | Rocket and exhaust fit completely inside the original blue/brass roundel; the complete badge has a 3px vertical margin | `gfx/interface/decisions/044_space_race/decision_category_space_race.dds` |
| Chaos Doom decision, severity 3 | Flat frontal beige skull with readable dark sockets replaces the shaded side-view skull | `gfx/interface/decisions/decision_chaos_doom.dds` |

The category canvas remains 52×40; its visible bounds are x=9–42, y=3–36.
The action icon uses the task's explicit 34×34 decision contract instead of the previous 33×32 texture; its visible bounds are x=5–28, y=2–31.
Both existing sprite names and texture paths remain valid; their `spriteType` registrations have no explicit size field to update.
No GUI, decision cost, effect, timing, eligibility or AI changes were made.

## Sources and verification

Before images and native ImageGen source art are retained under `docs/assets/gfx_fix_shared_decisions/`.
The rocket edit source basename is `exec-7daebefc-c089-4eb2-88cf-fd1e3271ba19.png`; the prompt preserves the blue/brass roundel while reducing and centring the rocket/flame inside it, with native transparency.
The skull source basename is `exec-e5715388-da5f-4c51-801a-0467a838cc0e.png`; the prompt requests an original flat beige skull pictogram with dark sockets, no three-dimensional rendering, glow, text or background.
The canonical decisions contact sheet and installed `interface/decisions.gfx` generic-decision definitions establish the action-icon family; the original Space Race badge establishes the category's roundel treatment.
The native-alpha subjects were proportionally fitted to their own canvases, with transparent unused canvas and no background-removal fallback.
The standard asset-skill converter produced both final DDS files, which decode pixel-for-pixel to the approved processed PNGs.
`processing.json` and `validation.json` record the source hashes, crop bounds, final dimensions and runtime hashes.
`before_after.png` contains native and 3× nearest-neighbour comparisons.
The complete current group was rendered with the narrowed `.tools/gfx/gfx.py sheet` route into `contact_sheets/`; the two repaired entries are on `shared_chaosx_decisions_review_1.png`.
The unchanged cure-state and airship entries in the rest of that group are outside the two assigned findings.

Final SHA-256 values are `572786480f4ae61fd2ba73843227909450c4a62f1c957444d02716b125564cf0` for the category badge and `45c23907d04b99c1c3c94070f59033dc883998a277424b2e685720709c39b44a` for the skull.

## Orchestrator live checks

For the badge, use paused 1936 USA, run `event chaosx.nr44.2 USA`, accept its sole option and open Decisions.
The Space Race category must show its complete blue/brass badge with the exhaust inside the ring and no overlap with the category border.
For the skull, use the camp-repression owner's Germany fixture with a controlled state eligible for `genocide_restricted_chemical_site_escalation`.
Inspect that decision without executing it; its row and map icon must display the flat beige skull at native scale without clipping or a dark square backdrop.
The existing target and cost requirements still apply; this graphics pass does not establish gameplay eligibility.

No finding rows, subjects or required icon families were omitted or substituted.
