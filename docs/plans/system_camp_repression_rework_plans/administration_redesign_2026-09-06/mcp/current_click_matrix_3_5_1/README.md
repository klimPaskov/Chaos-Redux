# GUI render and click-region qualification

Disposition: source-render review implemented; native interaction and engine acceptance remain incomplete.
The review implements the user's request for fresh MCP renders and a documented hover/click/edge matrix without inventing campaign evidence.

Installed MCP 3.5.1 rendered all 45 declared cases, and both replay workers exited successfully.
The archive preserves 270 original artifacts: full PNG, cropped PNG, click-region PNG, layout JSON, fidelity JSON and validation JSON for every case.
Every artifact's size and SHA-256 matched the MCP result before and after archival.
Each native image was inspected directly or matched byte-for-byte to an inspected image; control geometry was compared separately, and differing click overlays were inspected.
The [case-by-case review](review.md) records which method was used.

## Coverage and results

The cases cover Administration, active and paused shortage states, long-name/large-number Locations, empty lists, filter hover, empty custody, closed sites, role-picker normal/hover/locked states, and Records.
Display configurations are 1280×720 at 100%, 1920×1080 at 100%, and 1920×1080 at 125% UI scale.
All 45 cases satisfied their declared visibility expectations, and no visible text overflow, clipped active control, active-region intersection or active control outside the window was found.
The original diagnostic and fidelity files retain their nonblocking findings; this is not a claim that every diagnostic is resolved.

Nine of 15 targeted hover requests produced the requested visible hover state.
The other six resolved to disabled states:

- Cases [16](16/crop.png), [22](22/crop.png) and [28](28/crop.png) force the purpose control visible but omit the selected-state binding required by its enable trigger.
- Cases [20](20/crop.png), [26](26/crop.png) and [32](32/crop.png) target a control whose source deliberately sets click enablement to false.

Those six cases establish disabled presentation, not active hover or tooltip coverage.
The legacy shortage cases [04](04/crop.png), [09](09/crop.png) and [14](14/crop.png) retain a declared “Projects Deferred” label with an active region, while the explicit paused cases suppress that region.
Closed-site cases retain legacy declared support and capacity numbers and are not accepted as engine-consistent campaign states.
Locked picker fixtures disable all three choices; they do not establish availability of the other choices.

## Evidence

The [manifest](manifest.json) contains every original artifact URI, saved path, size, hash, scenario identity, source revision and source-file identity.
The [exact input set](matrix-inputs.json) preserves the previous declared fixtures; only replay scenario identifiers were changed.
The [geometry and integrity report](geometry-and-integrity.json) retains visibility checks, state outcomes, active regions and image/control equivalence.
Each numbered directory contains `request.json`, `result.json`, `full.png`, `crop.png`, `click.png`, `layout.json`, `fidelity.json` and `validation.json`.
Its `click-crop.png` is a derived viewing aid; the original MCP click image remains unchanged.

| Surface | Native crop | Click regions |
| --- | --- | --- |
| Administration | [02](02/crop.png) | [02](02/click-crop.png) |
| Shortage active | [01](01/crop.png) | [01](01/click-crop.png) |
| Shortage paused | [05](05/crop.png) | [05](05/click-crop.png) |
| Locations stress at 125% | [22](22/crop.png) | [22](22/click-crop.png) |
| Empty filter hover at 125% | [24](24/crop.png) | [24](24/click-crop.png) |
| Locked picker at 125% | [38](38/crop.png) | [38](38/click-crop.png) |
| Active picker at 125% | [39](39/crop.png) | [39](39/click-crop.png) |
| Picker hover at 125% | [37](37/crop.png) | [37](37/click-crop.png) |
| Records at 125% | [44](44/crop.png) | [44](44/click-crop.png) |

The three recorded GUI, scripted-GUI and localisation files retained one hash set throughout the replay and remained unchanged within every call.
Fifteen aggregate source revisions were recorded, so this is not one frozen-workspace acceptance claim.
Render-call times on this shared machine ranged from 166.260 to 511.722 seconds, with a median of 221.354 seconds; artifact retrieval followed each call immediately.

## Unproved behavior

These are declared scenarios over real source, not in-game captures or save-derived state.
Numeric values are test inputs and establish neither campaign nor historical measurements.
Native tooltip popups, window raising, scrollbar interaction, actual clicks, payments, transfers, delayed callbacks and timer receipts remain unproved.
No new selected-state, controller or engine facts were invented to make a case pass.
The user reported no saves available; no game launch, save search or game-log request was performed.
This matrix does not establish 99% or 99.9% whole-image accuracy and is not exhaustive coverage of later source features outside its declared cases.

## Release and workflow boundary

The [public repository recheck](public-repository-audit.json) confirms one canonical checkout, local and remote `main`, one Git tag and GitHub release `v3.5.1`, zero open pull requests, public visibility and npm latest `3.5.1` at the recorded time.
The [retired-runtime check](retired-native-runtime-check.json) confirms its native DLL was still in use; it was preserved.
Two separate ignored installation-test prefixes remain because automatic approval review rejected their deletion as “blocked by policy.”
The originally named temporary project checkouts are gone.

The review used the scripted-GUI, documentation-curator and shared-Git workflows.
It changed evidence and documentation only; no renderer or gameplay patch was justified by the observed image and geometry results.
