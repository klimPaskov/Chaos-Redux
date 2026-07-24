# Event 006 Sicily portrait refinish — completed GFX/runtime handoff

The independent visual/provenance audit accepted all three real male identities, the separate Luigi Rizzo consumer audit accepted his current civilian-large political/security-director use with disclosure, and the approved DDS files are wired through `interface/006_independence_wave_mediterranean_portraits.gfx`.

## Runtime handoff

| Stable result | Proposed sprite name | Proposed target `.gfx` | Proposed runtime DDS path | HOI4 role/use | Package DDS |
|---|---|---|---|---|---|
| `ASX_luigi_sturzo.png` | `GFX_portrait_ASX_independence_wave_luigi_sturzo` | `interface/006_independence_wave_mediterranean_portraits.gfx` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_sturzo.dds` | Male country leader for the Sicilian provisional assembly | `final_dds/ASX_luigi_sturzo.dds` |
| `ASX_pietro_lanza_di_scalea.png` | `GFX_portrait_ASX_independence_wave_pietro_lanza_di_scalea` | `interface/006_independence_wave_mediterranean_portraits.gfx` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds` | Male country leader for the Sicilian crown council | `final_dds/ASX_pietro_lanza_di_scalea.dds` |
| `ASX_luigi_rizzo.png` | `GFX_portrait_ASX_independence_wave_luigi_rizzo` | `interface/006_independence_wave_mediterranean_portraits.gfx` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_rizzo.dds` | Male country leader for the Sicilian straits-security government; no corps-command consumer | `final_dds/ASX_luigi_rizzo.dds` |

## Wiring notes

- Use the stable result stems exactly as supplied; do not create `_small`,
  advisor, dossier, or alternate-gender derivatives.
- Register only the intended full `156x210` portrait texture after audit.
- Keep the three source masters and their exact crop previews in this evidence
  package for provenance; do not replace them with the painted results.
- Ensure the country/commander definitions use male metadata and do not pair any
  of these portraits with female names or `female = yes`.
- The parent owns all final `.gfx`, gameplay, localisation, and runtime-path edits.

## Completed audit gate

The package visual/provenance audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_sicily_trial01_portrait_visual_provenance_audit_2026_07_22.md`.
The current Luigi Rizzo civilian political-consumer audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_luigi_rizzo_political_consumer_independent_audit_2026_07_24.md`.
The runtime hashes are `4768E69316D2A03754BE052143C68A157902C6953D99CE9389472ED1ADA52E57` for Sturzo, `7D1201F05A7189001B88A9D7AA9B5E2ED565379CBD30F2FE170EF6AAA245475A` for Lanza di Scalea, and `659C819547559F50025FB3007CD5C60947A150CA4673238CC179DC2F0867D714` for Rizzo.
