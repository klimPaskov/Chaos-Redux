# Event 006 Sicily portrait refinish — deferred GFX/runtime handoff

This handoff is a proposal only. Parent conversion/wiring is **unauthorized**
until an independent visual/provenance audit accepts each subject. The package
contains no runtime files and does not edit any `.gfx` definition.

## Proposed runtime handoff

| Stable result | Proposed sprite name | Proposed target `.gfx` | Proposed runtime DDS path | HOI4 role/use | Package DDS |
|---|---|---|---|---|---|
| `ASX_luigi_sturzo.png` | `GFX_portrait_ASX_luigi_sturzo` | A Sicily/Event 006 leader portrait `.gfx` block owned by the parent | `gfx/leaders/006_independence_wave/ASX_luigi_sturzo.dds` | Male country leader for the Sicilian provisional assembly | `final_dds/ASX_luigi_sturzo.dds` |
| `ASX_pietro_lanza_di_scalea.png` | `GFX_portrait_ASX_pietro_lanza_di_scalea` | A Sicily/Event 006 leader portrait `.gfx` block owned by the parent | `gfx/leaders/006_independence_wave/ASX_pietro_lanza_di_scalea.dds` | Male country leader for the Sicilian crown council | `final_dds/ASX_pietro_lanza_di_scalea.dds` |
| `ASX_luigi_rizzo.png` | `GFX_portrait_ASX_luigi_rizzo` | A Sicily/Event 006 commander portrait `.gfx` block owned by the parent | `gfx/leaders/006_independence_wave/ASX_luigi_rizzo.dds` | Male Regia Marina/navy commander for Sicilian emergency command | `final_dds/ASX_luigi_rizzo.dds` |

## Wiring notes after audit only

- Use the stable result stems exactly as supplied; do not create `_small`,
  advisor, dossier, or alternate-gender derivatives.
- Register only the intended full `156x210` portrait texture after audit.
- Keep the three source masters and their exact crop previews in this evidence
  package for provenance; do not replace them with the painted results.
- Ensure the country/commander definitions use male metadata and do not pair any
  of these portraits with female names or `female = yes`.
- The parent owns all final `.gfx`, gameplay, localisation, and runtime-path
  edits; this subpackage intentionally does not perform them.

## Audit gate

Required before any promotion from `needs_user_review`:

1. Independent reviewer compares source master -> exact crop -> ImageGen master
   -> processed 156x210 portrait for identity, age, hair, facial hair,
   expression, pose, clothing/regalia, and distinctive structure.
2. Independent reviewer checks source links, author/archive, date, rights note,
   and source hashes against the current source/provenance ledgers.
3. Auditor records accepted/blocked disposition per subject. Any identity drift
   or unresolved rights concern fails closed; do not substitute a generated or
   generic person.

Until all three rows pass those gates, no parent conversion, GFX registration,
runtime copy, or gameplay/localisation wiring is authorized.
