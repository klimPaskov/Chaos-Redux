# Event 019 Claimant Identity Specialist Re-Audit

> Superseded visual evidence: all human-portrait, face, sex-presentation, source-dimension, hash, and contact-sheet claims in the body describe rejected art. Current fixed slots show twenty regional claimant armies/musters, six derivative massed hosts, and one neutral unassigned muster with no individual focal human/person; see `019_full_portrait_regeneration_handoff_2026_07_16.md`, `019_neutral_unassigned_muster_asset_handoff_2026_07_16.md`, and the current 27-row crosswalk. Runtime claimant sex/name correction remains governed by `019_male_claimant_identity_correction_handoff_2026_07_16.md`; nonvisual regional/profile audit reasoning below is historical evidence only.

Date: 2026-07-16  
Mode: read-only live-source audit plus this handoff only  
Final disposition after remediation: **P0: 0, P1: 0, P2: 4**

## Scope and authority

This pass audited the complete twenty-profile claimant identity package: generated source portraits, processed portraits, runtime DDS files, sprite registration, gender metadata, four-name pools, profile titles and descriptions, region gates, profile reuse, dynamic commander creation, report localisation context, takeover promotion, cleanup, Muster Board display, and asset documentation.

The audit used the required repository guidance and the complete `chaos-redux-event-assets`, `chaos-redux-events`, and `chaos-redux-subagents` skills. It also consulted the required offline wiki pages (Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, Scripted GUI Modding, Country Creation, and Portrait Modding), the installed vanilla character/scripted-GUI/localisation/script-concept/effect documentation, and vanilla dynamic-character precedents in `common/decisions/ENG.txt`, `common/decisions/HOL.txt`, and `common/national_focus/spain.txt`.

The worktree already contained extensive concurrent changes. No gameplay, localisation, asset, interface, specification, manifest, or registry file was edited by this specialist.

## Executive verdict

The runtime identity system is complete enough to clear P0 and P1 after the parent remediation tranche. The two material defects found in the first audit snapshot are closed:

1. Reports `.200` through `.203` load the exact claimant row into localisation context before firing. The appearance report freezes the newly appended row before primary-claimant refresh can change selection.
2. Historical claimant rows no longer consume portrait profiles forever. Live identity owners reserve profiles; released terminal histories do not. A completed takeover is terminal for ordinary claimant creation, so the persistent ruler portrait cannot reduce a three-profile region below the advertised three-active-claimant ceiling.

The remaining four findings are P2 documentation or defensive-presentation gaps. There is no missing portrait, missing name pool, wrong gender flag, region-mismatch fallback in live profile selection, duplicate final portrait, broken DDS, or missing GFX registration.

## Remediation closure — 2026-07-16

### Closed: exact report identity context

The shared exact-row loader is `infantry_spawn_load_claimant_localisation_context` in `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:80-98`. Input is the temporary `infantry_spawn_claimant_localisation_index`. It clears all five visible identity variables first, proves ledger alignment and row bounds, and then copies profile, name variant, archetype, UID, and headquarters from the same aligned row.

The current report call graph is:

| Report | Event definition | Fire site and exact-row proof | Result |
| --- | --- | --- | --- |
| `chaosx.nr19.200` | `events/019_infantry_spawn.txt:128` | `infantry_spawn_create_claimant`, `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:342-381`; the appended row index is frozen at line 364, archetype refresh may reselect at line 366, and the frozen row is loaded at lines 370-371 before the event at line 372 | Exact newly created claimant, not the current primary and not stale GUI state |
| `chaosx.nr19.201` | `events/019_infantry_spawn.txt:144` | `infantry_spawn_issue_selected_claimant_demand`, `common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt:151-155` | Exact demanding claimant |
| `chaosx.nr19.202` | `events/019_infantry_spawn.txt:171` | `infantry_spawn_stage_selected_claimant_revolt_warning`, `common/scripted_effects/019_infantry_spawn_claimant_effects.txt:269-273` | Exact claimant whose warning was staged |
| `chaosx.nr19.203` | `events/019_infantry_spawn.txt:184` | `infantry_spawn_execute_selected_claimant_takeover`, `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt:225-229` | Exact promoted claimant; the loader intentionally accepts the now-terminal takeover row |
| `chaosx.nr19.204` | `events/019_infantry_spawn.txt:197` | `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt:261` | Generic failed-coup copy does not interpolate a claimant name |

The four named descriptions consume `[This.GetInfantrySpawnSelectedClaimantName]` in `localisation/english/019_infrantry_spawn_l_english.yml:27,31,36,40`. `GetInfantrySpawnSelectedClaimantName` maps all eighty profile/name-variant pairs in `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt:155-236`.

The Muster Board no longer owns a separate copy path. `infantry_spawn_muster_board_load_selected_claimant_view` at `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt:483-486` delegates the selected row to the same loader.

### Safest existing exact-row helper contract

When the exact row index is already known, the safe existing sequence is:

```text
set_temp_variable = { infantry_spawn_claimant_localisation_index = <exact aligned row index> }
infantry_spawn_load_claimant_localisation_context = yes
```

This does not need to change `infantry_spawn_selected_claimant_index`, so it avoids accidentally replacing the stable GUI selection.

When only claimant UID is known, use the existing UID resolver first:

1. Set `infantry_spawn_lookup_claimant_uid` to the frozen UID.
2. Call `infantry_spawn_find_claimant_row` (`common/scripted_effects/019_infantry_spawn_claimant_effects.txt:10-24`).
3. Require aligned claimant ledgers and a returned `infantry_spawn_claimant_row_index` greater than the invalid index and below the claimant row count.
4. Copy that returned index into `infantry_spawn_claimant_localisation_index` and call `infantry_spawn_load_claimant_localisation_context`.

Do not use `infantry_spawn_muster_board_rebuild_view` to prepare report text: it deliberately selects the primary claimant. Do not require `infantry_spawn_selected_claimant_index_is_valid` for a takeover report: that trigger accepts only status values below `retired`, while the exact takeover row must remain readable after its status becomes `takeover`.

### Closed: reusable profile ownership and regional capacity

`infantry_spawn_evaluate_current_claimant_profile_availability` in `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:54-75` scans aligned profile/status rows. A matching row reserves its profile only when it is a live identity owner:

- any ordinary claimant status below `constant:infantry_spawn_claimant_status.retired` (`inactive`, `emerging`, `recognized`, `demanding`, or `countermanded`);
- `constant:infantry_spawn_claimant_status.takeover`, because the promoted ruler still visibly owns the identity;
- `constant:infantry_spawn_claimant_status.revolt_staged`, because the staged claimant still owns the identity.

These terminal history outcomes release the profile:

- `retired`;
- `arrested`;
- `revolted`;
- `defeated`.

The scan therefore prevents two simultaneous live claimants in one country from sharing a portrait while allowing normal terminal churn without deleting historical rows. It also handles multiple historical rows for one profile correctly: any later matching live-owner row still marks the profile unavailable.

`infantry_spawn_select_current_claimant_profile` calls the evaluator in both the random-attempt path and deterministic scan (`common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:100-163`). Both paths still require regional compatibility. There is no catch-all or region-mismatched selection branch.

The final takeover edge is closed by `infantry_spawn_can_create_claimant` at `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:160-170`, which now requires the absence of `infantry_spawn_claimant_takeover_complete`. This matters because takeover sets the winner to `takeover` and resets ordinary active count to zero at `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt:209-210`; without the new gate, a persistent ruler would reserve one of only three compatible profiles in the smallest regional pools while ordinary pulses tried to create three more claimants.

Fresh/live-owner regional coverage is:

| Capital continent | Compatible profiles | Count |
| --- | --- | ---: |
| Europe | 01, 02, 05, 09, 10, 13, 14, 18 | 8 |
| Middle East | 03, 11, 16 | 3 |
| Africa | 03, 15, 16 | 3 |
| Asia | 04, 05, 06, 07, 11, 12, 17 | 7 |
| Australia | 04, 12, 20 | 3 |
| North America | 08, 09, 19 | 3 |
| South America | 08, 13, 19 | 3 |

The user-corrected special cases are exact in `infantry_spawn_current_claimant_profile_is_regionally_compatible` (`common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt:27-110`):

- profile 09 (`Lucien Vautrin`) is Europe or North America at lines 62-64;
- profile 13 (`Matteo Vellani`) is Europe or South America at lines 78-80;
- profile 20 (`Mara Voss`) is Australia only at lines 106-108.

## Asset and identity evidence

### Portrait package

- Source PNGs: 20 files under `docs/assets/019_infantry_spawn/source_png/portraits/claimants/`; 20 unique SHA-256 hashes.
- Source dimensions: seventeen `1086x1448` RGB files and three `1024x1536` RGB files (profiles 05, 09, and 20).
- Processed PNGs: 20 files under `docs/assets/019_infantry_spawn/processed_png/portraits/claimants/`; all `156x210` RGB and all twenty hashes unique.
- Runtime DDS: 20 files named `gfx/leaders/019_infantry_spawn/portrait_019_claimant_01.dds` through `_20.dds`; all twenty hashes unique.
- Every DDS is `156x210`, 131,168 bytes, uncompressed 32-bit BGRA with pitch 624, pixel-format flags 65, no FourCC, masks `00ff0000/0000ff00/000000ff/ff000000`, and texture caps `0x1000`. Decoded pixels match the corresponding processed PNGs.
- Minimum 64-bit dHash distance is 17 among source portraits and 18 among processed portraits. There is no duplicate or near-copy pair.
- Original-detail source and processed contact-sheet inspection confirms twenty different one-person faces, stable period/HOI4 framing, odd-slot male presentation, even-slot female presentation, and no council/crowd substituted for a claimant.

`interface/019_infantry_spawn.gfx:51-130` registers exactly twenty unique claimant sprite names and twenty unique numbered DDS paths. The Muster Board consumes the selected sprite dynamically at `common/scripted_guis/019_infantry_spawn_muster_board_scripted_gui.txt:226`.

### Gender, names, titles, and descriptions

`docs/assets/019_infantry_spawn/notes/claimant_identity_metadata.md` contains twenty rows, exactly ten male-presenting and ten female-presenting identities. The female rows are the even profiles 02, 04, 06, 08, 10, 12, 14, 16, 18, and 20. `infantry_spawn_set_current_claimant_profile_metadata` encodes exactly those ten profiles at `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:29-46`.

`infantry_spawn_create_current_claimant_commander` (`common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:207-266`) uses one female and one male `create_corps_commander` branch. The female branch sets `female = yes`; the male branch omits it. Both inject the exact selected name, portrait token, stable claimant UID, traits, and stats. This follows the inspected vanilla dynamic-character precedents. Takeover and derivative promotion use `add_country_leader_role = { promote_leader = yes ... }` on the exact existing character, preserving name, portrait, gender, and ID.

The English localisation file is UTF-8 with BOM and contains exactly:

- 20 unique `infantry_spawn_claimant_profile_XX` titles;
- 20 unique `infantry_spawn_claimant_profile_XX_desc` descriptions;
- 80 unique `infantry_spawn_claimant_name_XX_1..4` personal names;
- 20 portrait-token values.

Every metadata primary name matches variant 1 for the same profile. All four names for each row match the row's apparent gender and declared regional pool. Profiles 09, 13, and 20 match their corrected multi-region or Australia-only gates. The creation name selector and report/Muster Board selector each cover all eighty profile/variant pairs.

### Cleanup and persistent identity

- Failed coup removes the exact unit leader, sets the row to `arrested`, decrements active count, and now releases the profile for later use.
- Takeover retires and removes competing claimant commanders, preserves the winner, promotes that exact character, records status `takeover`, and reserves the ruler's profile. The terminal creation gate prevents new ordinary claimant churn afterward.
- Derivative promotion also promotes the exact existing claimant character rather than recreating a lookalike.
- Full teardown clears claimant arrays and the visible claimant context. Scenario rollback truncates only its appended claimant tail. Historical terminal rows can remain without exhausting the portrait pool.
- Muster Board cycling is limited to valid live rows; the shared localisation loader prevents stale row mixing.

## Remaining findings

### P2-01 — Twenty authored profile titles and descriptions have no runtime consumer

Evidence:

- Keys `infantry_spawn_claimant_profile_01..20` and `_desc` exist at `localisation/english/019_infrantry_spawn_l_english.yml:1139-1292`.
- A non-localisation runtime search finds no consumer for any of those forty keys.
- The command panel at `interface/019_infantry_spawn_muster_board.gui:198-207` displays name, archetype, status, demand, and generic identity prose. `infantry_spawn_muster_gui_claimant_identity` at localisation line 1091 does not use the unique profile title or description.

Impact: all forty strings are internally correct but invisible; the twenty-profile narrative distinction is reduced in the only detailed claimant UI.

Recommended closure: add selected-profile title and description scripted-localisation selectors keyed by `infantry_spawn_muster_gui_claimant_profile`, then consume them in the claimant command panel or its tooltip. Acceptance is a runtime reference to every title and every description with no generic substitution for valid profiles.

### P2-02 — The no-fallback contract is correct in region selection but contradictory in documentation and defensive selectors

Evidence:

- Live regional selection is fail-closed and has no global or mismatched-region branch.
- `docs/specs/019_infantry_spawn_specs/matrices/019_possessed_general_matrix.md:71` still requests “a fallback that still matches portrait presentation,” contradicting the user correction that no global fallback is allowed.
- `GetInfantrySpawnClaimantPortraitToken` defaults to profile 01 at scripted-localisation line 116; `GetInfantrySpawnSelectedClaimantPortraitToken` does the same at line 141; the trait selector defaults to Quartermaster at line 151. The GUI declaration also starts from profile 01 at `interface/019_infantry_spawn_muster_board.gui:196`.
- These defaults are not reached by the validated creation/report paths, but an invalid or deliberately cleared context visually substitutes claimant 01 even though the loader comment says it clears visible identity.

Impact: no current normal path receives a wrong regional portrait, but invalid-state presentation can impersonate profile 01 and the source-of-truth matrix still authorizes a fallback that runtime intentionally forbids.

Recommended closure: remove or supersede the fallback sentence in the matrix. Hide the portrait/identity widget when the exact context is invalid, or route invalid context to a clearly non-claimant diagnostic/empty state; do not substitute another claimant. Keep the creation invariant fail-closed rather than using the default trait/profile as recovery.

### P2-03 — Claimant manifest/provenance is aggregate rather than the required row-level asset record

Evidence:

- `docs/assets/019_infantry_spawn/manifest.md` describes the claimant portraits only as a twenty-sprite range.
- `docs/assets/019_infantry_spawn/gfx_handoff.md:23` likewise records a numbered range.
- `docs/assets/019_infantry_spawn/notes/claimant_identity_metadata.md` supplies excellent row-level role, gender, name-pool, archetype, and sprite data, but not each source PNG, processed PNG, DDS, source mode, image-generation prompt, prompt/provenance record, validation/hash reference, and final status.
- No claimant-portrait prompt record exists under `docs/assets/019_infantry_spawn/prompts/`; the retained prompt file covers generated icons and flags.

Impact: runtime art is complete and reproducible processing exists, but the package does not satisfy the event-assets skill's requirement that the manifest list every generated asset and retain its prompt/source mode. A future portrait replacement cannot be audited row-by-row from the manifest alone.

Recommended closure: add a twenty-row claimant portrait crosswalk to the manifest (or a claimant submanifest linked from it) with exact source/processed/DDS paths, sprite, apparent gender, name pool, region gates, source mode, retained prompt/provenance, dimensions, hashes or validator reference, and status. No new art is required.

### P2-04 — Australia reaches the three-profile ceiling through two undocumented diaspora-compatible profiles

Evidence:

- Runtime correctly allows profiles 04, 12, and 20 in Australia, giving the continent the required minimum of three.
- The possessed-general matrix and metadata describe profiles 04 and 12 only as South/Southeast Asian and East/Southeast Asian. Their descriptions at localisation lines 1164 and 1228 do the same.
- Only profile 20 is explicitly described as Australasian in the matrix, metadata, and localisation.

Impact: the two Asian profiles and their name pools are plausible for Australasian diaspora identities, and the portraits themselves do not contradict that use, but the trigger-to-metadata pairing is implicit. The required region/name/portrait compatibility proof therefore depends on an unstated interpretation.

Recommended closure: explicitly record profiles 04 and 12 as Asia/Australasia diaspora-compatible in the matrix and claimant metadata, and align the profile descriptions if those descriptions are exposed in the GUI. Do not broaden profile 20; it must remain Australia-only.

## Simplifications, omissions, fallback, and blockers

- No portrait or name-pool asset is missing.
- No duplicate, recolour-only, placeholder, real-person, or wrong-size portrait was used.
- No runtime global region fallback remains. Profile 20 is not a fallback and is Australia-only.
- No gameplay simplification was found in gender/name/portrait creation or takeover identity preservation.
- The residual fallback wording and invalid-context profile-01 defaults are reported as P2-02, not accepted as a simplification.
- The residual manifest/provenance and Australia-compatibility documentation omissions are P2-03 and P2-04.
- There is no approval-gated engine blocker for claimant identity.

## Final acceptance checklist

| Requirement | Result |
| --- | --- |
| 20 fictional source portraits | Pass |
| 20 processed `156x210` portraits | Pass |
| 20 valid pixel-matched `156x210` BGRA DDS files | Pass |
| 20 unique GFX registrations and consumers | Pass |
| Visual distinctness | Pass |
| Exact 10 female / 10 male metadata and creation flags | Pass |
| 20 titles, 20 descriptions, 80 names defined and internally aligned | Pass |
| All valid creation/report name and portrait selectors complete | Pass |
| Profile 09 Europe/North America | Pass |
| Profile 13 Europe/South America | Pass |
| Profile 20 Australia only | Pass |
| No runtime global region fallback | Pass |
| At least three compatible profiles per continent before the active ceiling | Pass |
| Terminal churn releases reusable profiles without simultaneous live duplicates | Pass |
| Takeover ruler identity remains reserved and ordinary post-takeover creation is closed | Pass |
| Reports `.200-.203` bind the exact claimant row | Pass |
| Dynamic commander and takeover promotion preserve full identity | Pass |
| Cleanup avoids permanent historical-row exhaustion | Pass |
| Unique titles/descriptions visible in runtime UI | P2-01 |
| No-fallback source documentation and invalid-context presentation aligned | P2-02 |
| Row-level claimant manifest and prompt provenance | P2-03 |
| Australia compatibility explicitly documented for profiles 04 and 12 | P2-04 |

Final exact open count: **P0: 0, P1: 0, P2: 4**.
