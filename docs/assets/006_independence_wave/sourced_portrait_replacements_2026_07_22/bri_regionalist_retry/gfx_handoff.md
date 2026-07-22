# Event 006 BRI regionalist portrait source retry - GFX handoff

Date: 2026-07-22  
Scope: source provenance and sprite handoff only. No `.gfx` file was edited.

The existing runtime declaration is already the correct target and must not be
duplicated. The parent agent owns final crop, native HOI4 leader-portrait
finishing, visual comparison against the canonical vanilla reference family,
DDS conversion, and any wiring decision.

## Existing sprite to preserve

```text
spriteType = {
	name = "GFX_portrait_BRI_independence_wave_civic_commission"
	texturefile = "gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds"
}
```

The definition is in `interface/006_independence_wave_brittany_portraits.gfx`.
This snippet is a verification target, not a request to add another entry.

| Sprite | Character token | Role branches | Source status | Deferred runtime DDS |
|---|---|---|---|---|
| `GFX_portrait_BRI_independence_wave_civic_commission` | `BRI_independence_wave_civic_delegate` | traditional regionalist compact; protected-ports patron | Régis de l'Estourbeillon, 1904 photograph: `source_ready` pending parent visual processing | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds` |

## Source paths and parent actions

Primary source master:

`source_masters/BRI/BRI_regis_de_l_estourbeillon_john_wickens_1904.jpg`

The parent should perform an explicit head-and-shoulders crop from the unchanged
master, preserve the identity and Breton-period clothing, finish to the
repository's full `156x210` leader portrait target, compare independently with
the canonical references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders`,
and then run the repository-standard DDS converter. The 1904 source's halftone
texture and age difference from 1936 must be considered in that review.

Review-gated alternative:

`source_masters/BRI/BRI_regis_de_l_estourbeillon_maurice_dulac_1898.jpg`

This is an archival line illustration. Do not process or wire it unless the
parent explicitly approves an illustration for this grounded real-person token
and records the unresolved rights/format decision.

## Explicit non-wiring rules

- Do not point the live sprite at either source JPEG.
- Do not use a generated, generic, female, advisor, or operative portrait as a
  substitute for this grounded BRI civic identity.
- Do not create a second sprite declaration under another name; preserve the
  existing `GFX_portrait_BRI_independence_wave_civic_commission` mapping.
- No processed PNG, runtime DDS, or GFX change is included in this package.
- If the parent rejects the primary after visual review and does not approve
  the illustration, leave the civic slot blocked and commission a new sourced
  retry; do not silently fall back.
