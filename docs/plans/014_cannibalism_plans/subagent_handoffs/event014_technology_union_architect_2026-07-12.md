# Event 014 additive technology-union handoff

Date: 2026-07-12  
Mode: bounded scripted-system implementation  
Commit: none

## Files changed

- `common/scripted_effects/chaosx_dynamic_effects.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_technology_union_architect_2026-07-12.md`

Parent integration subsequently wired the shared helper into the ordinary and
Wendigo unification effects described below. The original Event 014-private
helper file was removed after promotion into the documented shared contract.

## Helper contract

Helper: `union_compatible_researched_technologies_from_donor`

- Recipient scope: the current scope must be the country receiving technologies.
- Donor pointer: the caller must save the donor country as the regular event target `technology_union_donor` in the same effect chain.
- Timing: call the helper before annexing, retiring, or otherwise invalidating the donor country.
- Operation: the helper iterates `event_target:technology_union_donor.researched_techs`. Each entry is a live technology token. It checks `has_tech = var:technology_union_entry` in recipient scope and calls `set_technology` only when the recipient does not already own that technology and the donor entry does not conflict with the recipient's established industry branch.
- Additive guarantee: no recipient technology is ever assigned `0`, and `inherit_technology` is not used. Donor state is read only.
- Idempotence: repeating the same donor-to-recipient union does not change already-owned technologies and does not re-run their completion effects.
- Missing-target behavior: there is no fallback or silent no-op branch. Calling without the required event target violates the contract and leaves an invalid event-target error, making bad wiring visible.
- Persistence: the helper creates no regular variables, flags, arrays, or global event targets. Its loop value is temporary. The regular donor event target clears with its originating effect chain.

Canonical caller shape:

```text
event_target:SOURCE_COUNTRY = {
	save_event_target_as = technology_union_donor
}
event_target:RECIPIENT_COUNTRY = {
	union_compatible_researched_technologies_from_donor = yes
}
```

## Engine side effects

`set_technology` grants a newly missing technology through the normal runtime effect. The technology's `on_research_complete` block therefore executes when one exists. `popup = no` suppresses the research popup, not the completion payload. The recipient-side `has_tech` check ensures those payloads are not repeated for technologies the recipient already owns. There is no documented runtime effect that grants an arbitrary technology additively while suppressing `on_research_complete`.

### Mutually exclusive industry guard

The recipient's established industry choice takes priority. The helper mirrors the approved Kaiserreich multi-donor transfer precedent and skips these conflicting donor entries:

- `flexible_line` when the recipient has `streamlined_line`
- `streamlined_line` when the recipient has `flexible_line`
- `concentrated_industry` through `concentrated_industry5` when the recipient has `dispersed_industry`
- `dispersed_industry` through `dispersed_industry5` when the recipient has `concentrated_industry`

All other technology families remain eligible. The helper never removes the recipient's branch to make room for a donor branch.

### Special-project boundary

This is a technology-state helper, not a special-project-state helper. It does not copy `is_special_project_completed` state, prototypes, facilities, scientists, project progress, or project rewards stored outside `researched_techs`. If a completed project has granted an ordinary technology token that appears in the donor's `researched_techs` array, that technology token is processed under the same missing-technology and industry-conflict checks. The live original-ZZZ Wendigo host retains its own special-project state because the transformation occurs in place on the same country scope.

## Current technology coverage evidence

The native iterator inspects the donor's complete live `researched_techs` array, so inspection coverage is not limited to a generated list. A brace-depth inventory of every direct technology definition under the current vanilla and Chaos Redux `common/technologies/*.txt` directories produced:

| Source | Definition files | Unique technology IDs | Duplicate IDs inside source |
| --- | ---: | ---: | ---: |
| Vanilla | 13 | 552 | 0 |
| Chaos Redux | 2 | 31 | 0 |
| De-duplicated union | 15 | 583 | 0 cross-source overlaps |

Hash normalization: sort the 583 unique IDs with ordinal text ordering, join them with LF, retain one terminal LF, encode as UTF-8, and calculate SHA-256.

- Vanilla SHA-256: `6e56633d30023fccb0d4d1f921aae3667023f302069b3fa57b8ae28b3d54410f`
- Chaos Redux SHA-256: `ac4725e51c2fe70a3f2e2a77891a7260d6dad8145db00f94d2f5909eb1a35d41`
- De-duplicated union SHA-256: `cce7141f1c37520596d337b914cbb80887bb329dd44e20ead39f68424c0a9e5a`

The current database maximum of 583 potential entries is below vanilla `NDefines.NGame.MAX_EFFECT_ITERATION = 1000`. Because the helper iterates only technologies actually researched by the donor, its live iteration count is at most 583 in the current database. If the loaded technology database later exceeds 1000 unique IDs, this guard rail must be re-audited before claiming exhaustive coverage.

Per-file inventory:

| File | IDs |
| --- | ---: |
| `air_techs.txt` | 42 |
| `armor.txt` | 50 |
| `artillery.txt` | 33 |
| `bba_air_techs.txt` | 43 |
| `electronic_mechanical_engineering.txt` | 42 |
| `industry.txt` | 43 |
| `infantry.txt` | 89 |
| `MTG_naval.txt` | 54 |
| `MTG_naval_Support.txt` | 43 |
| `naval.txt` | 33 |
| `NSB_armor.txt` | 29 |
| `special_projects_tech.txt` | 6 |
| `support.txt` | 45 |
| `chaosx_technologies.txt` | 30 |
| `zombie_special_project_technologies.txt` | 1 |

## Exact parent wiring sites

Line numbers describe the inspected 2026-07-12 workspace and may move as concurrent Event 014 edits land. Match the named helper blocks and nearby statements before applying.

### Initial CBL host

File: `common/scripted_effects/014_cannibalism_unification_effects.txt`

Helper block: `cannibalism_create_unified_country_from_selected_host`

1. In the donor block, save the selected host as `technology_union_donor` alongside the existing migration source setup.
2. In the `CBL = { ... }` block, call `union_compatible_researched_technologies_from_donor = yes` before research-slot assignment.
3. Keep the union before the host annexation currently at lines 541 through 545.

This replacement gives newly activated CBL the host's full researched set without using a whole-state copy effect.

### Later warlord absorption into CBL or the active Wendigo host

File: `common/scripted_effects/014_cannibalism_unification_effects.txt`

Helper block: `cannibalism_absorb_current_warlord_into_unified_host`

1. In the source warlord block, save current scope as `technology_union_donor` alongside `cannibalism_absorbed_warlord`.
2. After `cannibalism_runtime_migration_result > 0`, call `union_compatible_researched_technologies_from_donor = yes` inside `event_target:cannibalism_unification_host` at the start of the recipient block.
3. Keep the call before player transfer and before `annex_country` at lines 683 through 698.

This shared absorption helper serves ordinary submitted and surrendered warlords. It also serves later warlords absorbed by the Wendigo route because that route saves its live original-ZZZ country as `cannibalism_unification_host`.

### Primary warlord donor absorbed by live original ZZZ

File: `common/scripted_effects/014_cannibalism_wendigo_effects.txt`

Helper block: `cannibalism_absorb_primary_warlord_donor_into_wendigo`

1. In `event_target:cannibalism_primary_warlord_donor`, save the donor as `technology_union_donor` alongside `cannibalism_absorbed_warlord`.
2. After `cannibalism_runtime_migration_result > 0`, call the union helper inside `event_target:cannibalism_wendigo_merge_host` at the start of the recipient block currently spanning lines 294 through 304.
3. Keep the call before donor annexation at lines 318 through 322.

Do not move this call into the unconditional reveal block. When both the primary donor and original ZZZ are human, the donor is deliberately not absorbed. Its technology must remain separate until an explicit later disposition resolves it.

### Original-ZZZ technology preservation

No self-union call is required. `cannibalism_prepare_wendigo_merge_identity` transforms the selected live original-ZZZ country in place at lines 206 through 247. It sets a cosmetic tag and Event 014 state without changing country tag or calling `inherit_technology`, so the country's existing technologies remain on that same country scope. The primary-donor and later-absorption calls above add donor-only technologies without replacing that preserved set.

## Reference evidence

- Official `documentation/effects_documentation.md` documents `for_each_loop`, country-scoped `set_technology`, and `inherit_technology` as copying technology state.
- Official `documentation/dynamic_variables_documentation.md` documents country `researched_techs` as the array of researched technology objects and global `technology` as the technology database array.
- Official `documentation/script_concept_documentation.md` documents arrays and token-capable script data.
- Offline `Data structures - Hearts of Iron 4 Wiki.md` documents `researched_techs`, the `for_each_loop` contract, token-valued technologies, scoped arrays, event targets, and `GetTokenKey`.
- Offline `Technology modding - Hearts of Iron 4 Wiki.md`, `Effects - Hearts of Iron 4 Wiki.md`, and `Triggers - Hearts of Iron 4 Wiki.md` document `set_technology`, `inherit_technology`, and `has_tech` behavior.
- Vanilla files use `inherit_technology` for one-source country initialization, including `events/LAR_Spain.txt` and `common/decisions/GER.txt`. They do not provide a multi-donor additive union helper.
- Approved Kaiserreich precedent `common/scripted_effects/00_transfer_technology_effects.txt`, helper `transfer_technologies`, uses the same engine-native pattern: `for_each_loop` over `PREV.researched_techs`, recipient `has_tech = var:technology`, and `set_technology = { var:technology = 1 popup = no }`.

## Meaningful validation and remaining work

- The implementation uses the engine-native donor array and dynamic technology tokens. Every technology entry actually researched by the donor is inspected, with no static family allowlist. Only a donor industry entry that conflicts with the recipient's established mutually exclusive branch is deliberately skipped.
- The recipient `has_tech` and industry-conflict guards prove monotonic behavior: an existing recipient technology remains researched, a compatible missing donor technology is set to researched, and no code path unsets technology.
- The current 583-ID database fits within the 1000-iteration engine limit.
- Parent wiring is present at all three named call surfaces. Final country and completion audits must retain focused integration proof for multi-donor accumulation, recipient-branch preservation, research slots, and reusable-slot cleanup.
- A final integrated scenario should give the CBL host and an absorbed warlord disjoint compatible technologies and verify both are present after annexation. The same scenario should give live original ZZZ and its absorbed donor disjoint compatible technologies and verify the union after transformation.
- A conflict scenario should give the recipient `flexible_line` and the donor `streamlined_line`, then reverse them in a second run. Repeat with concentrated and dispersed industry. In every case the recipient branch must remain and the conflicting donor branch must be skipped.

## Simplifications, omissions, and blockers

No donor path or current technology definition is absent from inspection. The deliberate exception to literal set union is the approved mutually exclusive industry guard listed above, which preserves the recipient's existing production branch. Special-project completion state is outside this technology-only contract; the live original ZZZ country retains its own project state because transformation occurs in place. All three parent call sites are wired. The other engine constraint is the documented `on_research_complete` execution for newly granted technologies. No silent fallback was added.

## Skills used or changed

- Used: `chaos-redux-events`
- Used: `chaos-redux-subagents`
- Created or updated: none
