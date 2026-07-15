# Event 014 Country Package Consolidation Reaudit

Date: 2026-07-15

Audit basis: live shared working tree at Git HEAD `7dd903a81d59db08f16e02c97262a43803827ea5`. The working tree contains concurrent Event 014 work, so the live files cited below, not Git HEAD or the pre-consolidation audit, are the implementation authority.

Audit mode: source, control-flow, inventory, and direct visual-asset re-audit after the Event 014 runtime consolidation, the recovery-state population fix, the focus layout repair, and the CBA-CBD portrait refresh. No country-package gameplay repair was required by this pass.

## Verdict

| Severity | Open findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

The consolidated Event 014 country package satisfies the assigned contract. CBA-CBH are eight symmetric, origin-agnostic reusable country slots. Exactly three playable origins exist: Island Host, Siege Commune, and March Host. The warlord tree contains exactly 68 focuses and one four-focus overlay for each origin. All 56 slot-by-region portraits are present, uniquely backed, dimensionally valid, and bound through the live slot and region tokens. The live portrait art contains no prison setting. The two public characters are Hannibal Lecter, with exact static portrait bindings and no ancient-general disclaimer or Carthaginian identity. The original Event 2 ZZZ Wendigo country is mutated in place, while its country scope, player control, territory, units, technology, ideas, recruitment state, and special-project state survive. Formation and later recruitment consume real state population before zero-filled formations are created. Ordinary and Wendigo unification preserve player control and protect dual-human outcomes. Hannibal remains absent from player-facing pre-reveal surfaces.

The P1 recovery-state consumption defect found by the parallel decision audit is closed in the live tree at `common/scripted_triggers/014_cannibalism_triggers.txt:3026-3041`. `cannibalism_can_consume_current_state` now rejects `cannibalism_recovery_active`, and every country-package recruitment path inherits that canonical predicate. This pass did not duplicate that repair.

## Authorities used

- Required offline wiki coverage: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, Unit modding, Division modding, Technology modding, National focus modding, and Interface Modding.
- Required official coverage: script concepts and script constants, effects, triggers, modifiers, dynamic variables, localisation, characters, decisions, on actions, equipment, and AI strategy documentation from the installed HOI4 build.
- Concrete vanilla precedents included direct civilian character portrait binding in `common/characters/VIN.txt:4-9`, locked division templates in `events/AAT_Denmark.txt:1892-1899`, human continuity through `change_tag_from` in `events/LaR_France.txt:3995-4003`, and annexation with `transfer_troops = yes` in `events/AAT_Finland.txt:637-642`.

## Consolidation before and after

The earlier country-package audit correctly described the behavior, but most of its file references pointed at loader fragments that were subsequently folded into the 23-file Event 014 runtime surface. This report replaces those stale references with the live canonical locations.

| Pre-consolidation surface | Live consolidated authority | Rechecked result |
| --- | --- | --- |
| `common/script_constants/014_cannibalism_country_constants.txt` | `common/script_constants/014_cannibalism_constants.txt:1303-1453` | Eight slots and only the three accepted origins remain; starting formations use zero start-equipment and start-manpower factors. |
| `common/scripted_effects/014_cannibalism_country_effects.txt` | `common/scripted_effects/014_cannibalism_effects.txt:4475-5660` | Region/origin derivation, leaders, templates, population-backed formation, symmetric allocation, cleanup, quarantine, and release remain intact. |
| `common/scripted_effects/014_cannibalism_unification_effects.txt` | `common/scripted_effects/014_cannibalism_effects.txt:11810-12684` | Human-first host selection, CBL creation, war and troop transfer, five response outcomes, and dual-human protection remain intact. |
| `common/scripted_effects/014_cannibalism_wendigo_effects.txt` | `common/scripted_effects/014_cannibalism_effects.txt:18159-18955` | Exact original-ZZZ selection, in-place identity mutation, donor handling, counterplay, terminal lock, and focus overlay remain intact. |
| `common/national_focus/014_cannibalism_warlord_focus.txt` | `common/national_focus/014_cannibalism_focus.txt:1434-2857` | One 68-focus warlord tree, one root, and three origin overlays remain. The current edit is coordinate-only. |
| `common/decisions/014_cannibalism_warlord_decisions.txt` and the other decision fragments | `common/decisions/014_cannibalism_decisions.txt` | All 127 decision IDs are unique; the three origin operations and population-backed recruitment decisions remain wired and localized. |
| Seven Event 014 GFX fragments | `interface/014_cannibalism.gfx` | One `spriteTypes` root retains the 56 regional warlord files, the two exact Hannibal portraits, focus and decision icons, and animation registrations. |

The dedicated runtime inventory remains exactly 23 current files. The consolidation left section markers for former file boundaries and did not rename gameplay identifiers.

## Acceptance evidence

### Eight reusable countries and symmetric lifecycle

- `common/country_tags/014_cannibalism_countries.txt:8-16` registers CBA-CBH as eight reusable warlord slots and CBL as the ordinary unified country.
- All eight `common/countries/Cannibal Warlord Slot CB?.txt` definitions exist and use distinct colors.
- All eight `history/countries/CB? - Cannibal Warlord Slot.txt` histories use capital 1, zero research slots, and the empty `014_cannibalism_dormant` OOB. `history/units/014_cannibalism_dormant.txt` contains `units = { }`; no live formation is preloaded.
- `common/script_constants/014_cannibalism_constants.txt:1320-1331` defines slot indices CBA=1 through CBH=8.
- `common/scripted_effects/014_cannibalism_effects.txt:5334-5420` gives every slot the same allocator contract. `common/scripted_triggers/014_cannibalism_triggers.txt:3563-3613` gives every slot the same availability contract.
- `common/scripted_triggers/014_cannibalism_triggers.txt:3484-3561` requires country, state, array, target, generation, release-verification, and reuse-date references to be clear before reuse.
- `common/scripted_effects/014_cannibalism_effects.txt:5466-5660` removes state and source references, Event 014 ideas and templates, actor entries, timed state, and global slot flags before applying the reuse quarantine and releasing CBA-CBH symmetrically.

### Exactly three origins

- `common/script_constants/014_cannibalism_constants.txt:1333-1343` contains only `none`, `island_host`, `siege_commune`, and `march_host`.
- `common/scripted_effects/014_cannibalism_effects.txt:4535-4565` derives one of those three origins and one of seven portrait regions from the actual origin state.
- `common/scripted_effects/014_cannibalism_effects.txt:5034-5052` clears all origin identity and applies exactly one Island, Siege, or March flag and idea.
- `common/ideas/014_cannibalism_ideas.txt:55-128` contains the three starting origin ideas and their three upgraded forms. `common/country_leader/014_cannibalism_traits.txt:15-33` contains the corresponding three origin traits.
- `common/ai_strategy/014_cannibalism_warlords.txt:10-56` contains one common reusable-slot profile and exactly one self-removing profile per accepted origin.
- `common/decisions/014_cannibalism_decisions.txt:2373-2425` contains one paid, AI-weighted origin operation for Island, Siege, and March.
- `common/national_focus/014_cannibalism_focus.txt:2248-2496` contains exactly three four-focus origin overlays. Their roots are gated at lines 2248-2249, 2331-2332, and 2414-2415.
- An exact live-runtime scan found zero `Prison Host`, `prison_host`, `origin_prison`, `warlord_prison_host`, `lockhouse`, or `lock_house` identifiers. General prisoner ledgers, detention, prisons, and depots remain ordinary Event 014 mechanics; they do not define a fourth origin.

### Focus tree, decisions, ideas, and AI

- The consolidated warlord tree contains 68 focus IDs plus its tree ID, with no duplicate focus ID. All 68 focus titles and all 68 descriptions exist in the consolidated English localisation.
- The parallel focus audit's fresh HOI4 focus inspection found one root, 68 reachable focuses, zero blocking diagnostics, zero edge crossings or node intersections in the warlord tree, and exactly the three accepted four-focus overlays. Its source repair changed coordinates only; identifiers, prerequisites, rewards, AI, and gates were unchanged. The current artifact is `docs/plans/014_cannibalism_plans/audits/event014_focus_tree_consolidation_reaudit_2026-07-15.md`.
- All 68 custom warlord focus icons resolve to definitions in `interface/014_cannibalism.gfx`. All 109 custom Event 014 decision icons referenced by the decision file resolve, as do all 37 idea pictures.
- The consolidated decision file contains 127 unique decision IDs. All 127 have a title and description. The dedicated decision re-audit separately proved AI coverage for all 95 selectable non-mission decisions and complete cost text and cost trigger coverage for all 94 paid decisions.
- Origin AI profiles use `abort_when_not_enabled = yes`, preventing a retired reusable slot from retaining an earlier incarnation's production or force-allocation priorities.
- Pre-lock and post-lock Wendigo strategy values are distinct and constant-backed. Pre-lock play prioritizes anchors, paid Pack capacity, and counterwar exposure; post-lock play escalates targeting and global war only after the terminal contract passes.

### Portraits, flags, names, and characters

- `interface/014_cannibalism.gfx:167-230` registers a generic name and seven region names for each of CBA-CBH. The generic and Europe names share the Europe texture, so 64 registrations resolve to exactly 56 live slot-by-region DDS files.
- `common/scripted_effects/014_cannibalism_effects.txt:4699-4711` builds the initial leader portrait as `GFX_portrait_[slot]_warlord_[region]`. Lines 12248-12310 reuse the same retained slot and region pair for integrated CBL commanders and servants.
- `common/scripted_localisation/014_cannibalism_scripted_localisation.txt:384-408` maps all eight slot tokens and all seven region tokens. `localisation/english/014_cannibalism_l_english.yml:408-422` resolves those tokens exactly.
- The live portrait inventory is 56/56 files, seven for each slot. Every file is 156x210. All 56 SHA-256 hashes are unique, with zero duplicate-hash group and zero dimension mismatch.
- Direct visual review of both current contact sheets found distinct faces, clothing, settings, and disturbing actions. None of the 56 images uses a prison cell, bars, cage, restraints, prisoner uniform, or prison-origin framing. The regenerated CBA-CBD set keeps the required CBA South America skull-lick composition and corrects the remaining baldness inconsistencies.
- The current CBA-CBD contact sheet is `docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/contact_sheets/cba_cbd_warlords_contact_sheet.png`, SHA-256 `a084cad054387fd6e66a6ecf32a48999630b26e445fd836afe50ba7cf6312f72`. Its 28 source, processed, and DDS files have independent provenance recorded in the adjacent prompt and validation documents.
- The CBE-CBH contact sheet is `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/contact_sheets/processed_contact_sheet.png`; its 28 live files complete the same seven-region matrix.
- All 120 CBA-CBH flag TGA files exist: eight tags times five ideology filenames times three sizes. All 120 hashes are unique. Header checks found zero dimension mismatch at 82x52, 41x26, and 10x7.
- `localisation/english/014_cannibalism_l_english.yml:197-332` supplies complete dynamic country, adjective, ideology, and party localisation for all eight reusable tags.
- `common/characters/014_cannibalism_characters.txt:10-26` defines only the roleless dormant `CBL_hannibal` and `ZZZ_hannibal_wendigo` characters. Their direct large portraits are `GFX_portrait_CBL_hannibal` and `GFX_portrait_ZZZ_hannibal_wendigo`.
- `interface/014_cannibalism.gfx:231` binds CBL directly to `gfx/leaders/014_cannibalism/hannibal.dds`; line 561 binds the transformed character directly to `hannibal_wendigo.dds`. Both are 156x210. Their SHA-256 hashes are respectively `5C48C9A5B503C3185DCB38EE1AABC403D7668094079B78A20010323930D10B88` and `26D7566F7B93D17C4D7FDE5B262AB8B6E4B04FBA0B862315404D6A33ABE34717`.
- `localisation/english/014_cannibalism_l_english.yml:362-363` names both characters exactly `Hannibal Lecter`. The live Event 014 runtime contains zero ancient-general, Carthaginian, Carthage, or Punic disclaimer or identity text.

### Population-backed formations and paid recruitment

- `common/scripted_triggers/014_cannibalism_triggers.txt:3026-3041` is the canonical consumption predicate. It excludes recovery-active and stabilized/recovering population states before any route can consume or recruit from them.
- Warlord creation reaches the exact consumption transaction first at `common/scripted_effects/014_cannibalism_effects.txt:5159-5166`. Formation continues only when the result is `applied`.
- `common/scripted_effects/014_cannibalism_effects.txt:4878-4931` derives the starting unit cap, reinforcement cap, and manpower from `cannibalism_population_loss_applied`. Starting equipment stockpiles are bounded by that population-derived unit count and origin package.
- `common/script_constants/014_cannibalism_constants.txt:1452-1453` sets initial unit equipment and manpower factors to zero. The spawn effects at `common/scripted_effects/014_cannibalism_effects.txt:4933-5027` therefore create empty formations which must draw from the already-accounted population-backed pool and stockpile.
- Paid warlord recruitment at `common/scripted_effects/014_cannibalism_effects.txt:16361-16429` requires the exact requested population loss, then pays Larder, derives manpower from the applied loss, and only then creates the zero-filled unit. The state cooldown and unit cap are applied in the same successful branch.
- Unified recruitment at `common/scripted_effects/014_cannibalism_effects.txt:14728-14806` follows the same population equality, Larder payment, derived manpower, and zero-start formation sequence. Its zero factors are at `common/script_constants/014_cannibalism_constants.txt:2698-2699`.
- Wendigo Pack training at `common/scripted_effects/014_cannibalism_effects.txt:17750-17789` requires exact state-population loss before manpower and the empty Pack are granted. `common/script_constants/014_cannibalism_constants.txt:3481-3482` sets the Pack's start equipment and manpower to zero.
- Every `create_unit` occurrence in the consolidated Event 014 effects file belongs to one of the starting, warlord, unified, receipt-backed, or Wendigo transactions above. No free formation path was found, and `history/units/014_cannibalism_dormant.txt` remains empty.

### Player-safe ordinary unification and character outcomes

- `common/scripted_effects/014_cannibalism_effects.txt:11958-11989` searches viable human hosts first and only scores AI hosts when no human host exists.
- `common/scripted_effects/014_cannibalism_effects.txt:12324-12432` captures the host inheritance, sets the reveal flag before public identity, transfers a human player with `change_tag_from`, joins the host's wars, and annexes the former host with `transfer_troops = yes`.
- `common/scripted_effects/014_cannibalism_effects.txt:12509-12585` migrates later respondents, technology, wars, troops, slot identity, and the selected commander outcome before annexation.
- `common/scripted_triggers/014_cannibalism_triggers.txt:5324-5332` hides both submit options when the respondent and unified destination are both human. Therefore one human cannot displace another human already controlling CBL.
- `events/014_cannibalism.txt:453-549` exposes retained-command submission, disposable submission, autonomy, resistance, and challenge. `common/scripted_effects/014_cannibalism_effects.txt:12603-12684` leaves autonomy, resistance, and challenge countries on the map; the latter two enter an explicit war.
- `common/on_actions/014_cannibalism_on_actions.txt:19-83` captures warlord and pre-lock Hannibal capitulations. `events/014_cannibalism.txt:694-865` provides escape, public trial, tribunal, local prosecution, intelligence cooperation, execution, disappearance, and battle-death outcomes as applicable. `common/scripted_effects/014_cannibalism_effects.txt:875-959` records the outcome and retires the relevant character unless the selected outcome preserves escape.
- The player-transfer ordering follows the vanilla precedent in `events/LaR_France.txt:3995-4003`; the troop-preserving annex follows `events/AAT_Finland.txt:637-642`.

### Exact original-ZZZ preservation and terminal lock

- `common/scripted_triggers/014_cannibalism_triggers.txt:5276-5291` accepts only a surviving `original_tag = ZZZ` country with the exact Event 2 dynamic, weaponized, independent, Wendigo type and archetype flags, and rejects the legacy terminal idea.
- `common/scripted_effects/014_cannibalism_effects.txt:18180-18262` selects a human original-ZZZ host before any AI candidate.
- `common/scripted_effects/014_cannibalism_effects.txt:18449-18500` mutates that exact country in place. It applies only the public cosmetic identity, Event 014 route variables and flags, inherited templates and paid recruitment, the Hannibal role, and route ideas. It does not release or reconstruct ZZZ, reload an OOB, clear technology, reset research slots, delete existing units, clear stockpiles, or reset special projects.
- `common/scripted_effects/014_cannibalism_effects.txt:18528-18582` unions donor technology, joins donor wars, transfers troops, and annexes only an absorbable warlord donor into the existing ZZZ scope.
- `common/scripted_effects/014_cannibalism_effects.txt:18603-18680` protects a dual-human donor from forced absorption and from premature Larder transfer. A human donor is transferred into an AI ZZZ before absorption; a human ZZZ remains in place.
- `common/scripted_effects/014_cannibalism_effects.txt:18942-18955` loads the dedicated focus overlay only for the revealed, transformed, original-ZZZ country and does not replace the country.
- `events/002_zombie_outbreak.txt:874-909` blocks the legacy Event 2 Wendigo terminal during the Event 14 transition and after the Hannibal country exists. `common/on_actions/002_zombie_outbreak_on_actions.txt:180-207` prevents generic ZZZ leader refresh from overwriting the revealed identity.
- Pre-lock defenders can identify, disrupt, assault, and break anchors and recruitment sites. `common/scripted_triggers/014_cannibalism_triggers.txt:5367-5423` requires the winter network, completed route, enabled scenario, minimum anchors, reach, territory, consumed population, victories, authority, Larder, an active countdown, the terminal route, and maximum progress before lock.
- `common/scripted_effects/014_cannibalism_effects.txt:18866-18890` applies the effectively undefeatable package only after that terminal contract passes. It sets world end, global war, locked anchors, the locked national spirit, the terminal leader trait, and the super event in the same terminal branch.
- The intentional locked package at `common/script_constants/014_cannibalism_constants.txt:3366-3384` supplies +300% attack, defense, breakthrough, and recovery; +200% organization; +100% speed; -99% supply use; no ordinary attrition or out-of-supply penalty; and terminal surrender protection. The additional leader package is defined at lines 3451-3455 and used by `common/country_leader/014_cannibalism_traits.txt:259-265`. None of this power is present before the locked route completes.

### No pre-reveal Hannibal exposure

- The CBL and ZZZ histories recruit the dormant character definitions without assigning a country-leader role.
- `common/scripted_effects/014_cannibalism_effects.txt:12337-12340` sets `cannibalism_reveal_complete` before CBL territory, leader role, focus, named threat, events, or news can expose Hannibal.
- `common/scripted_effects/014_cannibalism_effects.txt:18632-18649` sets the same reveal gate before the transformed ZZZ identity, leader role, portrait, focus, decisions, events, news, and audio-facing state.
- `events/014_cannibalism.txt:432-451` and 552-570 require the reveal flag and the corresponding character before either public reveal event can display.
- `common/national_focus/014_cannibalism_focus.txt:2877-2919` requires the reveal flag, exact original-ZZZ identity, and transformed character before the Wendigo tree or its root is eligible.
- `common/decisions/014_cannibalism_decisions.txt:373-377` hides the Hannibal-named achievement tracker until reveal. The native achievement is independently hidden at `common/achievements/chaos_redux_achievements.txt:2188-2196`.
- The external Event 2 profile refresher at `common/scripted_effects/zombie_special_project_effects.txt:2633-2643` restores the transformed Hannibal name and portrait only when both the reveal flag and the exact Hannibal Wendigo country flag exist.
- Pre-reveal event-log and focus text identifies only a concealed command. No reachable player-facing pre-reveal Hannibal name, portrait, focus tree, country identity, event, news item, tracker, or named threat was found.

## Task-specific validation

- Current consolidated identifier inventory: 786/786 unique scripted effects, 428/428 unique scripted triggers, 107/107 unique script-constant namespaces, 127/127 unique decision IDs, 207/207 unique focus IDs across all three trees, 781/781 unique GFX sprite names, and 1975/1975 unique English localisation keys.
- All 127 decision names and descriptions exist. All 68 warlord focus names and descriptions exist.
- All 68 custom warlord focus icons, 109 custom decision icons, 37 idea pictures, and 60 Event 014 leader texture paths resolve to registered, existing files.
- The final live asset matrix contains 56/56 unique 156x210 warlord portraits, 2/2 exact 156x210 Hannibal portraits, and 120/120 unique correctly sized reusable-slot flags.
- The live-runtime forbidden-identity scan returned zero match for the retired fourth-origin identifiers and zero ancient-general or Carthaginian disclaimer/identity match.
- Direct source traces covered single-human and dual-human ordinary unification, human ZZZ and human donor Wendigo paths, all respondent choices, capitulation outcomes, slot cleanup and reuse, population-backed formation and recruitment, legacy Event 2 interlocks, reveal ordering, pre-lock counterplay, and the terminal lock.
- A narrow HOI4 event-inspector attempt could not retain its artifact because the tool reported `ARTIFACT_STORAGE_LIMIT`; it returned no inspected file and made no change. Direct source and asset checks remained complete for the country-package scope, and the parallel focus audit completed a successful fresh focus inspection. This is a tooling limitation, not an open content finding.

This is a live-source and direct-asset audit, not an in-game runtime session. The zero-finding verdict is based on reachable control flow, exact inventories, authoritative engine references, and direct inspection of the current visual files.

## Exact files changed by this re-audit

- `docs/plans/014_cannibalism_plans/audits/event014_country_package_consolidation_reaudit_2026-07-15.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_country_package_consolidation_reaudit_handoff_2026-07-15.md`

No gameplay, localisation, interface, asset, manifest, spreadsheet, or source specification was changed by this country-package re-audit. The live recovery guard, focus coordinates, and CBA-CBD portrait assets were separately owned concurrent changes and are cited here only as audited current state. No commit was created.

## Simplifications, omissions, and blockers

None. No fallback, placeholder, weakened substitute, omitted origin, omitted route, missing asset, missing AI behavior, free-formation path, destructive ZZZ reconstruction, forced player displacement, pre-reveal identity leak, or unresolved P0-P3 finding remains in the assigned country-package scope.
