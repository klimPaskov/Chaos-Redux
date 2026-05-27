# Event 005 Republic Portrait Wiring Sidecar, 2026-05-27

## Scope

Bounded country-package sidecar for Event 005 Soviet Collapse flag, portrait, and leader consistency. This pass only promoted already-live generated DDS portraits into Event 005 leader creation wiring. It did not edit focus, decision, mission, balance, event outcome, country tag registration, or binary asset files.

Repo context followed:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- clean merged spec parts 6 and 7
- offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Interface modding
- vanilla docs: `~/projects/Hearts of Iron IV/documentation/effects_documentation.html` entries for `create_country_leader` and leader-name/portrait effects

## Patch Applied

Promoted ten existing DDS portraits from `gfx/leaders/005_soviet_collapse/` into live Event 005 wiring:

| Tag | Leader display name | Sprite | DDS |
| --- | --- | --- | --- |
| `EST` | Tallinn Continuity Committee | `GFX_portrait_EST_tallinn_continuity_committee` | `gfx/leaders/005_soviet_collapse/EST_leader.dds` |
| `LAT` | Port and Forest Continuity Council | `GFX_portrait_LAT_port_forest_continuity_council` | `gfx/leaders/005_soviet_collapse/LAT_leader.dds` |
| `ARM` | Mountain Emergency Council | `GFX_portrait_ARM_mountain_emergency_council` | `gfx/leaders/005_soviet_collapse/ARM_leader.dds` |
| `KAR` | Border and Timber Council | `GFX_portrait_KAR_border_timber_council` | `gfx/leaders/005_soviet_collapse/KAR_leader.dds` |
| `KOM` | Mine and River Committee | `GFX_portrait_KOM_mine_river_committee` | `gfx/leaders/005_soviet_collapse/KOM_leader.dds` |
| `CRI` | Port and Peninsula Committee | `GFX_portrait_CRI_port_peninsula_committee` | `gfx/leaders/005_soviet_collapse/CRI_leader.dds` |
| `BSK` | Oilfield and Ural Workshop Council | `GFX_portrait_BSK_oilfield_workshop_council` | `gfx/leaders/005_soviet_collapse/BSK_leader.dds` |
| `YAK` | Lena Resource Board | `GFX_portrait_YAK_lena_resource_board` | `gfx/leaders/005_soviet_collapse/YAK_leader.dds` |
| `BYA` | Baikal Relay Council | `GFX_portrait_BYA_baikal_relay_council` | `gfx/leaders/005_soviet_collapse/BYA_leader.dds` |
| `TAN` | Steppe Compact Council | `GFX_portrait_TAN_steppe_compact_council` | `gfx/leaders/005_soviet_collapse/TAN_leader.dds` |

Changed files:

- `interface/005_soviet_collapse_custom_icons.gfx`
  - Added the ten portrait `spriteType` mappings near the existing Event 005 republic council portraits.
- `common/scripted_effects/005_soviet_collapse_effects.txt`
  - Extended `soviet_collapse_apply_event_created_republic_council_leader` with guarded `create_country_leader` branches for the ten tags.
  - Each branch keeps the existing guard pattern: `NOT = { has_country_flag = soviet_collapse_event_council_leader_created }`, `tag = <TAG>`, then `set_country_flag = soviet_collapse_event_council_leader_created`.

Leader-name handling:

- These promoted portraits use institutional council names, not individual random personal names.
- No `female = yes` metadata was added.
- No random single-person name pools were added for these tags, avoiding gender/name mismatch risk when the portrait represents a council or committee.

## Audit Findings After Patch

History/country package:

- Event 005 custom history files found for the current custom package surface: `ARD`, `ALA`, `KZR`, `SZA`, `BAC`, `MFR`, `TNC`, `NLC`, `CFR`, `KHC`, `DHC`, `KHW`, `BBH`, `SOG`, `IUL`, `MRC`, `PRA`, `UWD`, `FEV`, and `SDZ`, plus related custom tags found in earlier sidecar scans.
- Existing female metadata in history remains limited to tags with female single-person portrait flags and female random-name pools, such as `BAC`, `NLC`, `UWD`, `UDC`, and `TSC`.
- This pass did not alter history files.

Portrait coverage:

- Live Event 005 DDS portraits in `gfx/leaders/005_soviet_collapse/`: `57`
- Portrait DDS files referenced by Event 005 `.gfx` files after this patch: `47`
- Live DDS files with no current `.gfx` reference after this patch: `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, and `TRS`
- Event 005 `.gfx` portrait references with missing live DDS files: none
- Duplicate Event 005 portrait SHA-256 groups: none
- Event 005 DDS portraits matching vanilla leader DDS SHA-256 hashes: none

Flag coverage:

- Scoped custom/Event 005 flag audit checked `435` normal/medium/small TGA files across custom, splinter, restoration, and promoted release tags.
- Bad dimensions, unsupported bpp, short headers, or invalid size buckets: none found.
- TGA origin header distribution: `435` bottom-origin, `0` top-origin.
- Same-tag duplicate hash groups across base/ideology variants: none found.
- No base flag replacement for existing vanilla-supported country tags was introduced by this pass.

## Validation Run

Commands run:

```bash
git diff --check -- common/scripted_effects/005_soviet_collapse_effects.txt interface/005_soviet_collapse_custom_icons.gfx
python3 - <<'PY'
# checked ten promoted portrait sprite names, effect picture references, live DDS paths, and tag branches
PY
identify -format '%f %wx%h\n' gfx/leaders/005_soviet_collapse/{EST,LAT,ARM,KAR,KOM,CRI,BSK,YAK,BYA,TAN}_leader.dds
python3 - <<'PY'
# counted live/wired Event 005 portrait DDS references and duplicate portrait hashes
PY
python3 - <<'PY'
# scanned scoped Event 005/custom flag TGAs for dimensions, bpp, origin header, and same-tag duplicate hashes
PY
python3 - <<'PY'
# compared Event 005 leader DDS SHA-256 hashes against vanilla leader DDS hashes
PY
```

Results:

- `git diff --check`: clean.
- Ten promoted portrait sprite names have matching `picture =` references.
- Ten promoted DDS files exist and are all `156x210`.
- No duplicate Event 005 leader portrait hashes.
- No vanilla leader portrait hash matches.
- No missing normal/medium/small flag sizes in the scoped custom/Event 005 surface checked by this pass.
- No likely upside-down TGA headers found in the scoped flag set; all checked files use bottom-origin headers consistently.

## Skipped Validation

- No in-game launch or live UI validation was run by this sidecar.
- No binary assets were generated, edited, or visually repainted.
- No full repository script parse was attempted because the worktree contains broad unrelated dirty Event 005 changes outside this sidecar.
- No focus, decision, mission, event, or balance files were edited.

## Exact Remaining Asset Queue

For generated art worker or parent follow-up:

1. Reconcile live orphan DDS portraits with no current gameplay or `.gfx` references:
   - `gfx/leaders/005_soviet_collapse/BEC_leader.dds`
   - `gfx/leaders/005_soviet_collapse/BLT_leader.dds`
   - `gfx/leaders/005_soviet_collapse/COU_leader.dds`
   - `gfx/leaders/005_soviet_collapse/ILU_leader.dds`
   - `gfx/leaders/005_soviet_collapse/IRA_leader.dds`
   - `gfx/leaders/005_soviet_collapse/LID_leader.dds`
   - `gfx/leaders/005_soviet_collapse/RCD_leader.dds`
   - `gfx/leaders/005_soviet_collapse/RLD_leader.dds`
   - `gfx/leaders/005_soviet_collapse/SEP_leader.dds`
   - `gfx/leaders/005_soviet_collapse/TRS_leader.dds`

2. Decide whether to promote or archive sidecar-only generated republic portraits currently present under `docs/assets/005_soviet_union_collapse/generated_republic_council_portraits_2026_05_26/`:
   - `UKR_leader.dds`
   - `BLR_leader.dds`
   - `KAZ_leader.dds`
   - `LIT_leader.dds`
   - `GEO_leader.dds`
   - `AZR_leader.dds`
   - `KYR_leader.dds`
   - `TAT_leader.dds`

3. If any sidecar-only portrait is promoted, require the same promotion checklist used here:
   - final DDS copied to `gfx/leaders/005_soviet_collapse/<TAG>_leader.dds`
   - stable `GFX_portrait_<TAG>_...` sprite in `interface/005_soviet_collapse_custom_icons.gfx`
   - guarded Event 005 leader creation branch or an explicit parent decision to leave vanilla leader handling intact
   - institutional name for council/committee portraits, or gender-matched random personal name pool for single-person portraits
   - no replacement of existing base country flags unless a route identity change explicitly calls for it

## Remaining Risks

- The promoted portraits are wired mechanically, but no live in-game country view was checked.
- The asset manifest is still broader than this sidecar and may need a parent-owned reconciliation pass after all Event 005 asset promotions are finalized.
- The ten orphan live DDS files should not be treated as complete content until the parent either wires them intentionally or removes/archives them.
- This sidecar does not claim Event 005 completion.
