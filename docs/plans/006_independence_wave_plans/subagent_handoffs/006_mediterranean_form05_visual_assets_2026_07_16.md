# Event 006 FORM-05 Mediterranean visual-asset handoff

Date: 2026-07-16
Subagent scope: `ARX`, `ASX`, `MIX`, seven FORM-05 decisions, three FORM-05
lifecycle ideas, league emblem, charter-congress report art, dedicated sprite
registration, package evidence, and runtime QA

## Result

The bounded FORM-05 visual tranche is ready for parent integration:

- `ARX`, `ASX`, and `MIX` each have a complete 15-file TGA ladder: base,
  democratic, communism, fascism, and neutrality at 82x52, 41x26, and 10x7.
- Every flag is strictly fixed-palette, fully opaque, uncompressed 32-bit true
  color, bottom-left origin, and decode-identical to its target PNG. The five
  ideology filenames at each size are intentionally byte-identical civic
  designs with no ideological overlay.
- Sardinia uses the Italian Ministry of Culture's attested 1766-1815
  disposition: red cross on white, four Moor profiles, every profile turned
  left, white bands on the forehead above visible eyes. Savoy, crown, eagle,
  border, and regimental additions are absent.
- Sicily uses the cataloged 1848 S.015 disposition: vertical green/ecru/red
  with green at the hoist and one central all-gold Trinacria. The 3:2 flat
  field is a disclosed normalization; ceremonial attachments are absent.
- `MIX` has an original navy/sea-green/gold/ivory league flag and a distinct
  charter-and-anchor league emblem.
- The seven exact decision icons, three exact idea icons, one report card, and
  one emblem are legacy uncompressed BGRA DDS at their requested sizes.
- `interface/006_independence_wave_form05.gfx` registers the exact sprite names
  and runtime paths. It creates no extra post-formation decision sprite; the
  later actions reuse the requested seven.

## Exact bounded paths

### Package and evidence

- `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/`
  - 14 current official ImageGen raw files plus the retained ASX raw/master
  - 11 transparent alpha masters
  - 3 fixed-palette flag masters
  - 20 processed target PNGs
  - 3 contact sheets
  - exact prompt log, source/license/consumer manifest, build tool, SHA-256
    ledger, and machine-readable validation report
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_mediterranean_form05_visual_assets_2026_07_16.md`

### Runtime flags

For each `TAG` in `ARX`, `ASX`, and `MIX`, the following exact patterns are
owned by this handoff:

- `gfx/flags/TAG.tga`
- `gfx/flags/TAG_democratic.tga`
- `gfx/flags/TAG_communism.tga`
- `gfx/flags/TAG_fascism.tga`
- `gfx/flags/TAG_neutrality.tga`
- the same five names under `gfx/flags/medium/`
- the same five names under `gfx/flags/small/`

No other flag tag or filename is owned by this handoff.

### Runtime UI/report finals

- `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_charter.dds`
- `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_delegation.dds`
- `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_shipping.dds`
- `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_defense.dds`
- `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_customs.dds`
- `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_capital.dds`
- `gfx/interface/decisions/006_independence_wave/mediterranean/decision_independence_wave_form05_proclamation.dds`
- `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_form05_provisional_charter.dds`
- `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_form05_ratified_union.dds`
- `gfx/interface/ideas/006_independence_wave/mediterranean/idea_independence_wave_form05_charter_breakdown.dds`
- `gfx/interface/006_independence_wave/emblems/independence_wave_formable_form_05.dds`
- `gfx/event_pictures/006_independence_wave/mediterranean/report_event_independence_wave_form05_charter_congress.dds`
- `interface/006_independence_wave_form05.gfx`

## Meaningful validation and review

- `notes/validation.json` validates exactly 45 TGA and 12 DDS finals, every
  header, dimensions, pixel depth, alpha/origin field, expected byte length,
  PNG decode equality, flag palette, and intentional ideology-family hash
  equality.
- The DDS validator confirms legacy uncompressed BGRA8888 masks/caps and
  target alpha; no visible chroma-key pixels remain.
- All three contact sheets were visually reviewed at original resolution. The
  10x7 Sicilian charge threshold was tightened after the first review so it
  remains a compact central gold mark rather than spreading across the ecru
  band.
- Live consumer searches confirm the seven decision names in the FORM-05
  decision/category files, all three idea pictures in the Mediterranean ideas
  file, and the report sprite in every FORM-05 event entry.

## Protected boundary and unrelated work

No advisor icon or portrait asset was touched or created. Specifically, this
handoff did not open, copy, generate, edit, register, reference as an art
input, or retain any advisor icon, leader/character/army-small portrait,
BAY/RHI protected portrait, or Event 14 asset. It also did not edit gameplay,
localisation, character, idea, decision, event, focus, or unrelated interface
files. Existing unrelated dirty flags and Mediterranean assets were left
untouched.

## Simplifications, omissions, and blockers

None within the requested bounded visual scope. The report scene is explicitly
fictional and does not depict a real person; the `MIX` flag and emblem are
explicitly fictional. The Sardinian and Sicilian normalizations and historical
evidence limits are fully disclosed in the manifest rather than hidden.

No commit was created. The parent agent owns staging, integrated revalidation,
and the final commit.
