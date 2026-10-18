# Codebase cleanup — 2026-10-17

Repository-wide dead-code, duplication and reference-integrity cleanup, run with the `chaos-redux-codebase-cleanup` skill and `.tools/audit_script_references_static.py`.
Base commit `b4dc57c08`; cleanup commits `4e9041c37` to `c36f19699` (9 commits, 266 files, about 12,000 lines removed and 2,300 added).
Disposition: implemented for the committed groups; the design decisions listed below are unresolved.
Validation limits: every removed name was re-searched across script, interface, localisation, docs, skills and tools with zero live references; brace balance, BOM and line endings were checked on every touched file; touched `.tools/test_*` suites pass; no in-game run was made.

## Commits

| Commit | Area | Summary |
|---|---|---|
| `4e9041c37` | Event 006 | 281 byte-identical per-package helpers replaced by shared effects and triggers in the Event 006 decision helper files; dead aliases, triggers, selectors and 8 constant categories removed. |
| `59edbf0cf` | CBRN | 3 dead trigger files, 28 constant categories and 2 opinion modifiers removed; identical helper pairs delegate to one body; always-true/false sabotage flag checks removed; chemical doomsday requirement tooltips added. |
| `c60c53bde` | Core systems | Dead crisis-pressure, scenario and settings helpers, the outdated welcome event and an empty scenario stub removed; Fury payments, death-environment multipliers and startup facility/grant helpers shared; dynamic effects index completed. |
| `62ac8d64f` | Fallout | 31 dead target triggers removed; 41 callback admission triggers delegate to delayed-result triggers; shared pilot roster; Event 243 factory-removal marker set as the flag its guard reads. |
| `12e4560f6` | Humanitarian | 30 unused scripted-localisation selectors with 92 keys, two famine aliases, one runtime effect and two constant categories removed. |
| `c266656ee` | Events 021+ | 44 triggers, 3 effects, 29 selectors with 55 keys and 22 constant categories removed; Event 027 Special Forces steps shared; Event 039 and Event 025 identical effects merged. |
| `f7229cfe3` | Tooling | `audit_script_references_static.py` and the `chaos-redux-codebase-cleanup` skill. |
| `6f37b6085` | Events 001–020 | Dead selectors (178 keys), effects, triggers and 50 constant categories removed; retired Event 013 per-family reports, Event 005 custom successor events and 622 orphaned Event 005 sprites removed; two identical pairs merged; Black Plague royal basin flag fixed. |
| `c36f19699` | Localisation | 56 requirement flags shown in decision, mission and focus tooltips localised. |

## Behaviour changes

- `black_plague_rat_transfer_to_king` sets `black_plague_royal_basin`, the flag the Crown Strike target, royal-seal and aftermath checks read; the previously set name was never read.
- `fallout_event_243_apply_factory_commitment` sets the country flag its guard and cleanup read instead of a variable of the same name; the only caller already ran once, so play is unchanged.
- Requirement tooltips show text instead of raw flag identifiers.

## Audit before and after

| Measure | Before | After |
|---|---|---|
| Exact clone groups (effects and triggers) | 186 | 99 |
| Unreferenced events (literal and built ids) | 1,410 literal-only | 15 |
| Exposed requirement flags | 56 | 0 |

The remaining `dead` counts are verified keeps: the generated per-state registry triggers (5,405), names built at runtime, documented APIs and hooks, CXT setup, generated catalogs, trigger names that double as tooltip keys, and code in files with other uncommitted work.

## Design decisions needed

Lost wiring or regressions:
- Fallout `chaosx.fallout.852` to `858` (The First Regional Standard) were overwritten by commit `edb4ee710`; restore from `d1e42a5d4`. `events/fallout_world_end_events.txt` has other uncommitted work.
- Event 021 critical-launch helpers have no caller and nothing fires `chaosx.nr21.18`, although the docs say the scheduler does both.
- `chaosx_bioweapon.207`/`.208` (first smallpox use and arrival news) and `chaosx_contamination.5`/`.6` (nuclear winter news) lost their callers in `de656ed03`.
- `chaosx.news.84` lost its only caller in `ebc2199c5`.
- Camp checks of `camp_rework_pingfang_anchor` and related flags never pass since the legacy setters were removed in `1850d88c3`, including the Japan and Manchukuo subject-authority branch.

Flags checked but never set (feature never applies):
- `cbrn_achievement_covert_coverup_history` (cover-up exclusion of the "Clean Hands, Dirty Work" achievement), `cbrn_active_distribution_disruption` (mask distribution cost multiplier), `smallpox_vaccination_protection_active` (vaccination never reduces contamination).
- `chaos_meter_deaths_details_open` (Deaths details view never refreshes live).
- `germany_mengele_civil_war_country` / `germany_mengele_post_coup_state` (the faction uses `germany_mengele_faction`).
- `black_plague_rat_brood_succession_crisis` (the brood succession decision is unreachable).
- `fallout_event_{614,621,740,747}_target_invalidated` (siblings 579, 586, 600 and 607 set theirs).
- `missiles_special_payload_compromised`.
- Event 006 `recognition_blockade_active`, `permanent_border_war_active`, the IW-046 Chuvashia flag and two league-collapse flags; `independence_wave_iw093_government_route_locked` looks like a typo for the shared route lock.

Unwired features:
- Event 039 `murder_mystery_focus_veiled_compact` has no caller, so the Necessary Hypocrisy achievement cannot be earned.
- Event 029 mine quarantine and exhaustion are set only by two unwired effects.
- Event 012 `africa_breach_first_proof_*` helpers have no caller.
- The migration closed-border report scene is complete but never triggered.
- 32 fallout event-log blocks are never called while sibling chains use theirs.

Consolidation proposals left for their owners:
- Event 19 providers carry byte-identical `pay_management_action`, `refund_management_action` and `get_equipment_token` hooks (8 copies each); shared defaults behind one-line wrappers would save about 140 lines.
- `black_friday_cbrn_decon_sale_source_is_active` duplicates `cbrn_protective_aid_sale_source_is_active`; `020_black_plague_scenario_effects.txt` writes `global.chaos_meter_value` directly.

## Not cleaned, with reason

- Files with other uncommitted work at the time of the cleanup (Event 005, 014, 019, 021, 023, 033, 038 and others); each subsystem handoff lists the dead code found there for a later pass.
- Unreferenced sprites outside the removed Event 005 routes: the asset audit does not model implicit engine naming, so they stay.
- 239 image files left orphaned by the removed Event 005 and Event 013 sprites are listed in the cleanup scratch folder and were not deleted.
- `chaosx_nr25_incident` is declared in both Event 025 field and incident constants files with disjoint keys; it loads without error and was left as it is.
- `docs/events/005_soviet_collapse/overview.md` and `common/scripted_effects/cbrn_scripted_effects.md` contain stale references but have other uncommitted work.

## Approved design fixes (2026-10-18)

The user approved the design decisions above. Disposition: implemented for the items below; validation is source review, `hoi4_script_validate` with partial coverage, the touched `.tools/test_*` suites, and a hands-off launch. No in-game play was performed.
Commits `87e19f0a2` to `f1053f375` on master; per-item evidence is in the subagent handoffs `handoff2_{cbrn,core,hum_fallout,iw,events,event19}.md` of the task scratch folder.

Restored or wired:
- Startup crash and launch errors fixed (`87e19f0a2`); Fallout 852 to 858 restored (`bbe5394fc`) and their comparisons corrected (`f1053f375`); Malta principality flags added (`858bbf3ab`).
- Smallpox news 207/208 and smallpox vaccination protection; nuclear winter news 5/6 through the Air Winter finalizer; discovered CBRN cover-ups recorded for the achievement; mask distribution disruption from recent bombing or border conflict (`cbrn_mask_distribution.active_bombing_days = 10`).
- Deaths details refresh by selected country; Event 018 global field news; Mengele checks point at `germany_mengele_faction` and `germany_mengele_victorious`; Brood Succession crisis opens on the Rat Nation; Black Plague scenario Chaos floor through the shared Chaos path; the Black Friday decontamination sale-source trigger delegates.
- Pingfang bureau opens through the monthly camp Administration pass after 180 days (the legacy decision stays retired); restored French and Belgian camp actions visible to players; closed-border migration report shown on rejected spontaneous flight; Fallout 614/621/740/747 target invalidation; 32 Fallout event-log details wired.
- Independence Wave league member war, permanent border war flag and failed-rescue latch, IW-093 route lock; Event 039 Veiled Compact founded by The Subject Compact focus after Evolution IV; shared Event 19 provider default hooks.
- The Event 32 compromised-payload check was removed as obsolete; the Event 021 Critical launch path stays removed by the 2026-10-13 user decision and its docs were corrected.

Launch: two hands-off launches reached the main menu without a crash; the second produced an empty `error.log` and no localisation collisions.

Unresolved (needs new design, not restorable):
- Event 029 mine quarantine and exhaustion endpoints; Event 012 `africa_breach_first_proof_*` breach conditions.
- Independence Wave recognition blockade activation, IW-046 Chuvashia admission, league patron capture threshold.
- `No font with name UPPER_LEFT` appeared only after a campaign map loaded; hands-off launches stay at the main menu, so its absence is not verified.
- Six `test_event32_*` suites fail independently of these changes.

## Approved design completion (2026-10-18)

The user approved designing the items left unresolved above. Disposition: implemented; each design is recorded as accepted in its event spec with basis "user approval 2026-10-18". Validation is source review, `hoi4_script_validate` with partial coverage, the Event 006 audits and the Event 032 regression tests, and a hands-off launch that reached the main menu with an empty `error.log` and no localisation collisions. No in-game play was performed.

- Event 029 (`ce5e9355a`): Gold Controlled Access quarantines the mine for `riches_found_containment.measure_days` and restores its prior state afterwards; deposits exhaust at `riches_found_exhaustion` depth 75 on predatory profiles or 100 otherwise, or on a collapse with no sealed integrity left; `chaosx.nr29.50` reports exhaustion, and an exhausted mine can be permanently sealed.
- Event 012 (`39959c276`): force against a partner credited by the open first proof (war, annexation, puppeting, Impose Emergency Administration, Enforce Congress Settlement) or a later failed Open Aid Corridor to a credited corridor partner breaches the matching proof and fails the mandate into the existing recovery contract.
- Independence Wave recognition blockade (`f44b3d966`): set by a failed Demand Recognition by Force or Border Ultimatum without treaty-backed recognition; ended by treaty-backed recognition, recognized separation, or origin end; blockaded actors weight DM-11 and DM-16 at x2.
- Independence Wave IW-046 Chuvashia (`3f432cc26`): admitted as a Level 1 regional-framework row on the vanilla CHU identity at state 256, separate from the IW-043 Middle Volga identity; allocator weight 175 from chaos band 1 in the shared Middle Volga reservation group.
- Independence Wave league patron capture (`143c88491`): latched when the league's Patron Capture meter first reaches `patron_captured = 60`; cleared on reform, dissolution or restart, and reform returns the meter to `reform_patron_capture = 30`.
- Event 032 regression tests (`ef9d22527`): all seven failures were stale assertions against intentional source changes; the suites pass, and the unused history row text was removed (`5ef64acad`).

Remaining limits: the `No font with name UPPER_LEFT` check needs a loaded campaign map and stays unverified; the IW-046 package contacts (TUR, HUN) are a design choice without a source.

## Push readiness and push (2026-10-18)

Disposition: implemented; the user authorized the push once launches were clean.

LFS and tracking cleanup:
- 90 unused WAVs removed (`11d5c7787`, 1.49 GB): super-event audio plays from the music OGGs, and the unused unit cues had no consumer.
- 576 unreferenced gameplay textures removed (`ba4061baf`, `3485d83e7`, 41 MB); the asset wiring audit is identical before and after.
- 566 evidence and receipt files untracked and ignored (`9b973a45c`, `90f6ee6ad`, 454 MB); local copies stay on disk.
- Every removed binary is archived byte for byte, with its LFS OID, in `C:/Users/klimp/Documents/chaos_redux_lfs_archive/`.

Fixes found on the way:
- The recoloured Austria cosmetic tag uses the Austrian ideology flags (`e24825771`).
- The `generic_bioweapon_aerosol` sound effect that 74 biological raid outcomes play is defined again (`874ec8ea6`).
- HEAD-only consistency: committed files called helpers and textures that existed only as other sessions' uncommitted files. The four helper definitions, one Malta constant, thirteen sprite textures and two duplicate cluster keys were committed (`87f991d04`, `14cb9a1d1`, `0b206aea1`, `d07f471e9`), and a duplicate migration modifier was dropped.
- Stale regression tests realigned with the current source: Events 12, 25 and 33, the CBRN payload reservation model and the national policy law scores.

Launch: a hands-off `-quickstart -start_tag=GER` run reached the 1936 campaign and a second run reached the main menu, both with an empty `error.log`, an empty `text.log` and no crash.

Push: unpublished history was filtered in a separate bare clone (`C:/Users/klimp/Documents/chaos_redux_push/`). 8,802 history-only LFS pointer blobs became small notices naming path, OID and size, and 1,541 commit messages lost their AI co-author lines. Final tree, commit count, parent topology and the published base were verified unchanged. `master` was pushed fast-forward from `a3ef485c5` to `d07f471e9`, uploading 3,004 LFS objects (466 MB) instead of about 3.9 GB. Local `master` was moved onto the pushed history with the five commits other sessions made meanwhile carried over unchanged; the unfiltered history is kept at `refs/backup/master-unfiltered-2026-10-18`.

Commit IDs in this section are the published ones; earlier sections name pre-filter IDs, which resolve through `refs/backup/master-unfiltered-2026-10-18`.

Remaining:
- Event 38 Malta Crusaders: 54 paths of another session's work (focus trees, principality tags, governance and principality effects) are uncommitted since 2026-10-11, so the pushed Malta event loads a focus tree that HEAD does not define. A fresh clone of the pushed repository logs that only when Event 38 fires.
- `chaosx.news.47` in HEAD names a removed picture; it is never fired, and another session's uncommitted edit deletes it.
- Several tests read evidence under `docs/plans` that is now untracked, so they pass here but not in a fresh clone.
- Fallout events 607, 614, 621, 740 and 747 keep their own later cleanup after a lost target instead of queuing it immediately like 579, 586 and 600; unifying them would change behaviour.
