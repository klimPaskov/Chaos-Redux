# Ledger District Native-Size Visual Review

Date: `2026-07-16`

Review surfaces:

- `contact_sheets/district_roles_native_1x.png` shows every role final at the exact runtime size, `300x96`.
- `contact_sheets/district_states_native_1x.png` shows every state final at the exact runtime size, `48x48`.
- `contact_sheets/district_states_nearest_4x.png` enlarges the exact state pixels with nearest-neighbour scaling solely to inspect keyed edges and geometry.
- The source/runtime sheets compare each accepted independent built-in ImageGen master with its final.

## Role review

| Role | Native-size identity | Quiet-card and exclusion review | Result |
| --- | --- | --- | --- |
| Market garden | Allotment beds, cold frames, cottages, pump, and produce shed remain immediately legible. | Subdued left field remains available for live UI text. No person, human shadow, readable text, number, sign, or malformed structure is visible. | PASS |
| Industrial housing | Dense brick rows, common court, sawtooth workshop, boiler stack, and material yard distinguish the role from every settlement card. | Subdued left field remains available. The card is not a generic factory photograph and has no people, readable text, or signs. | PASS |
| Rail junction | Crossing rails, switches, sidings, semaphore posts, depot, signal cabin, and water tower remain the dominant silhouette. | Subdued left field remains available. Track geometry is coherent at runtime size; there is no station name, number, person, or train clutter. | PASS |
| Port town | Quay basin, breakwater, warehouses, crane, rail spur, workboats, cargo coaster, and town read as one port municipality. | Subdued left field remains available. No boat name, shipping-container anachronism, person, sign, or readable text is visible. | PASS |
| Research town | Interwar laboratories, greenhouse, observatory dome, test garden, weather mast, and modest housing remain distinct without science-fiction cues. | The rejected draft's roof number is absent from the accepted ImageGen edit. Subdued left field remains available; no other readable or pseudo-readable text is visible. | PASS |
| Refugee municipality | Timber cottages, retained reception shelters, clinic/municipal hall, water tower, gardens, and service buildings communicate a settlement becoming permanent. | Subdued left field remains available. The scene is humane, people-free, and free of prison, guard-tower, barbed-wire, sign, or text imagery. | PASS |
| Inland Island ring | Concentric ring railway, green belt, gatehouses, gardens, housing arcs, and central civic works remain unmistakable. | Subdued left field remains available. The ring is a physical district model rather than a flat map, logo, fort, or literal island; circles remain undistorted. | PASS |

The seven role source hashes and final hashes are all unique. No card is a palette swap, filtered duplicate, recycled decision/focus icon, or programmatic reconstruction.

## State review

| State | Native-size identity | Geometry and exclusion review | Result |
| --- | --- | --- | --- |
| Surveyed | Brass theodolite, tripod, stakes, chain, and red seal read as field survey. | Instrument and badge outline remain proportional; no dial number, text, person, or magenta fringe is visible. | PASS |
| Planned | Blank rolled plan, drafting frame/dividers, set square, and wax seal read as an approved design stage. | Paper remains blank; frame and seal remain proportional; no pseudo-writing or magenta fringe is visible. | PASS |
| Building | Half-built civic hall, roof truss, scaffold, masonry, and hammer read as active construction. | Scaffolding and building remain coherent; no worker, text, or magenta fringe is visible. | PASS |
| Blocked | Broken rail bridge, snapped structure, crossed heavy timbers, and red lantern read as a halted project. | The badge does not rely on a generic X or stop sign; structural silhouette remains proportional and the key edge is clean. | PASS |
| Complete | Finished civic hall, ceremonial key, bound grain, and green enamel read as a settled public project. | The badge does not rely on a checkmark or trophy; circular frame and key remain proportional and the key edge is clean. | PASS |
| Disputed | Split blank charter, opposed cords, and different wax seals read as unresolved competing claims. | The asymmetrical split remains distinct from Blocked; no hands, scales, swords, pseudo-writing, or magenta fringe is visible. | PASS |

All six state source, processed, and runtime hashes are unique. At native size the weakest pairwise dHash separation is still `10` bits, and the weakest normalized pairwise pixel difference is greater than `0.069`. Each overlay retains transparent corners and an undistorted, aspect-preserved emblem.

## Rejection record

The first independent research-town generation contained a pale roof marking resembling the number `500`. It is retained only under `source_png/rejected/` and is not processed or shipped. A targeted built-in ImageGen edit removed that marking without changing the camera, settlement, frame, palette, or role identity; the edited result is the accepted research-town master.

## Verdict

**PASS.** All thirteen accepted finals are people-free, text-free, role/state-distinct, proportionally fitted, and usable at their native Ledger sizes. No fallback, recycled gameplay icon, local drawing, or transform-derived substitute is present.
