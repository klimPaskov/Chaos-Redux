# IW-010 Saar Willy Schmelcher trial-01 independent visual audit

Date: 2026-07-22  
Reviewer: independent generated-event-art audit subagent  
Decision: **FAIL-CLOSED**  
Runtime authorization: **no DDS conversion, no `.gfx` wiring, and no runtime
texture overwrite authorized**

## Audit scope and evidence

Inspected only the requested trial package, its source-authority package, and
the canonical leader-portrait family under
`.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`:

- Trial manifest:
  `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/saar_schmelcher_trial_01/manifest.md`
- Trial GFX handoff, prompt, unchanged source master, raw ImageGen master,
  processed native PNG, comparison sheet, and hash ledger in the same package.
- Source authority:
  `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/wallonia_saar_retry_01/manifest.md`
  and its recorded Schmelcher source/hash evidence.
- Canonical leader family README/CATALOG/contact sheet and the eight native
  `156x210` leader references.

The package contains one male identity only. It contains no DDS, `_small`
texture, advisor/dossier card, female asset, flag, focus, decision, or extra
identity. The contact sheet is review-only and is not a runtime asset.

## Exact file hashes and dimensions

| Artifact | Dimensions / mode | SHA-256 |
|---|---|---|
| `source_masters/AJX_willy_schmelcher_commander_1938.jpg` | 539x703 RGB | `a843a31c949b1128d857365f2e27c53e4897d7d2c62d6e2fd3b600c6823d2ad7` |
| `raw_masters/AJX_willy_schmelcher_hoi4_trial_01.png` | 1081x1455 RGB | `46bdcf6db2521ec019d31460a8b71833a41f92259515df462ba4b2a74081d70d` |
| `processed_png/AJX_saar_industrial_security_commissioner.png` | 156x210 RGBA, alpha 255/255 | `23e5b6317eba3602d907a6bd0a01a574c730f0a4c481e2b58e0fd21176666f7b` |
| `contact_sheets/source_result_style_comparison.png` | review sheet | `0899be676a31d8e22c3fc6afb28e184fbde6463389a6384e5b2805574e4e6c3e` |

The computed hashes match `hashes.sha256` exactly.

## Source mode, rights, and role

Saar is a grounded polity. The package correctly uses the unchanged attributed
real-person source path rather than a fictional or generated substitute. The
authority manifest identifies Willy Schmelcher (1894-1974), Polizeipräsident
of Saarbrücken from 1935, from E. Kienast (ed.), *Der Großdeutsche Reichstag
1938*, with image credit A. Gerspach, Neustadt. It records the Wikimedia
Commons file page and direct original, Commons public-domain metadata under
`PD-Germany-§134`, the local 539x703 master, and its hash. This is adequate
source traceability for the asset audit; the authority manifest correctly
retains a parent legal-territory caveat.

The Saar industrial/security role is historically defensible. The source
uniform and police context also provide stronger role evidence than the
candidate's neutral clothing.

## Visual comparison

### Same-person likeness

The raw master and native `156x210` PNG preserve the broad source structure:
single male, high rectangular forehead, short dark side-parted hair, narrow
long nose, horizontal moustache, closed lips, visible left ear, upright head
angle, and sober expression. The head-and-shoulders crop is complete and
readable at native size.

The strict grounded-identity gate does not pass, however. In direct source/raw
comparison the generated face is materially cleaned and reconstructed: the
brows are darker and more arched, the eyes are larger/brighter and less hooded,
the nose tip is fuller, the moustache is wider/denser, the lower jaw and chin
are broader, and the apparent age is somewhat younger/smoother. The gaze is
also more frontal. These are not just colour or brush-finish differences. They
leave a plausible resemblance, but not a defensible **exact same-person**
identity at the strict face-shape/forehead/hair/brows/eyes/gaze/nose/moustache/
lips/jaw/ears/age/ expression standard required for a grounded real person.
The native result remains identifiable as the same source concept at a glance,
but that broad resemblance cannot override the strict gate.

### HOI4 finish and crop

The candidate is a clean opaque `156x210` head-and-shoulders portrait with a
quiet warm-grey studio background, controlled contrast, restrained brush
texture, and a readable small-size silhouette. It fits the canonical leader
family's full portrait canvas and painted presentation. No frame, watermark,
text, UI, extra person, or modern prop is present. Style fit therefore passes;
style fit is not identity approval.

### Clothing substitution and role fit

The package openly discloses that the uniform-retaining attempt was moderation-
blocked and that the retained candidate replaces the source police/security
uniform with a plain 1930s civilian suit. The suit is period-plausible and
non-insignia-bearing, but it is an unauthorized simplifying departure for this
grounded portrait pipeline: it is not a source-backed depiction of Schmelcher,
and it removes the source's strongest Saar police/security role cue. The skill's
real-person gate permits an identity-preserving HOI4 finish of the unchanged
source master; it does not authorize inventing a new outfit merely to bypass a
blocked uniform edit. The role remains textually plausible, but visual role fit
is weakened and cannot be accepted as a silent substitute.

## Runtime and wiring disposition

`GFX_portrait_AJX_karl_becker` and
`gfx/leaders/006_independence_wave/portrait_AJX_saar_industrial_security_commissioner.dds`
remain reserved only. Do not convert the processed PNG, create a DDS, edit the
sprite, rename the stable token, or change the player-facing identity until a
replacement candidate passes an independent audit.

Required next step: obtain a new identity-preserving candidate that keeps
Schmelcher's facial geometry and source-backed clothing/role cues (or obtain an
explicit user-approved exception that changes the accepted design). If the
uniform cannot be retained under the image service, keep this package
fail-closed; do not use a fictional face, generic stand-in, or unapproved
civilian-suit substitute.

