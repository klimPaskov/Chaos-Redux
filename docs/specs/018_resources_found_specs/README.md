# Event 018 Resources Found Canonical Planning Package

This is the clean canonical planning package for Event 018, `Resources found`.

The package consolidates the original planning pass, the deepening pass, the focus-by-focus blueprint, scripted GUI wireframe, public repo implementation addendum, verified super-event research candidates, matrices, diagrams, and implementation prompts into one handoff. Temporary continuation prompts were removed from this canonical package.

## Canonical design state

Event 018 remains a minor repeatable economy-positive cluster member with medium severity. The baseline remains simple and preserved: a random valid state receives around 100 of one random resource, and the owner receives a popup. The expanded system adds field exploitation, trade and diplomacy interest, border risk, staged weirdness, sick workers, cave monsters, closure, the Cave Host country, resource-based Host deployment, and a world-end scenario if the Host owns a continent.

The Cave Host rule is preserved exactly as a design constraint: it uses no manpower or equipment, receives automatic divisions from captured resources, gains one division per 10 total resources in captured non-origin states, caps non-origin deployment at 10 divisions per state, and starts with an origin army capped around 30 based on prior exploitation.

Closure before Evolution IV remains the safe sacrifice path. Closing the field removes the resources from that state and blocks Cave Host emergence.

## New in the canonical pass

- Added `specs/018_resources_found_spec_part_11_repo_confirmed_implementation_addendum.md`.
- Added `specs/018_resources_found_spec_part_12_verified_super_event_research.md`.
- Added `research/018_resources_found_public_repo_exploration_handoff.md`.
- Added `matrices/018_resources_found_super_event_verified_candidates.md`.
- Added `research/018_resources_found_canonical_read_manifest.md` and `manifests/018_resources_found_canonical_file_manifest.json`.
- Removed temporary continuation prompts from the clean canonical zip.
- Updated prompt files to point implementation agents at the public repo handoff and verified super-event research candidates.

## Important boundaries

All player-facing text remains direction-only until implementation. Working labels are not final localisation.

No final super-event title, button text, quote, cultural remark, slogan, lyric fragment, or audio choice is approved in this package. The super-event research file contains source-checked candidates only. The implementation agent must still choose exact excerpts, verify final rights and attribution, and write final localisation.

The public Chaos Redux GitHub repository was inspected for current Event 018 paths and old behavior. The local Windows repo, offline Paradox wiki snapshot, vanilla Hearts of Iron IV documentation, final workbook, and custom Codex subagent runner were not mounted here. The coding prompt keeps those as required implementation steps.

No gameplay files were edited. No assets were generated. No audio was downloaded or converted. No spreadsheet workbook was edited.

## Catalog baseline read from provided CSV

```json
{
  "ID": "18",
  "Event Name": "Resources found",
  "Details": "Random province gets 100 production of some resource.",
  "Evo I": "",
  "Evo II": "",
  "Evo III": "",
  "Evo IV": "",
  "Evo V": "",
  "World-End Scenario": "",
  "Type": "Minor Repeatable",
  "Cluster ID": "",
  "Member Severity": "",
  "Status": "To Be Reworked"
}
```

## Folder layout

- `specs/` contains source design parts.
- `diagrams/` contains route and field state diagrams.
- `matrices/` contains decision, AI, country, focus, GUI, asset, acceptance, and super-event candidate matrices.
- `research/` contains reading notes, repo handoffs, and verified research notes.
- `prompts/` contains coding, asset, achievement, decision, repo, spreadsheet, super-event, and goal prompts.
- `manifests/` contains machine-readable package manifests.
