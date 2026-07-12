# Event 014 country-package audit — 2026-07-12

## Audit status

Read-only country-package audit. No gameplay, localisation, asset, spreadsheet, or shared-document files were edited, and no commit was created.

Verdict: **not completion-ready**.

- P0: 0
- P1: 5
- P2: 3
- P3: 0

The blocking defects are the unification slot-release path, duplicated starting force resources, the unified country's research/technology continuity, incomplete route/origin/character inheritance, and loss of the live Wendigo country's established daily zombie mechanics.

## Scope reviewed

- Reusable CBA–CBH tag allocation, origin pairing, territory selection, release, and reuse.
- Regional country names, leader names, portrait selection, traits, flags, and character reconstruction.
- Politics, ideas, technologies, research slots, division templates, starting forces, equipment, recruitment, caps, AI, and cleanup.
- CBL host selection, reveal order, player control, wars, troops, technology, route history, origin access, Larder, and warlord dispositions.
- Live original-ZZZ Wendigo selection, in-place transformation, identity, units, templates, ideas, technologies, recruitment, AI, anchors, counterplay, player control, and terminal lock.
- Player-facing pre-reveal identity surfaces.

## Required references consulted

The repository `AGENTS.md` and the `chaos-redux-events`, `chaos-redux-subagents`, and `hoi4-focus-trees` skills were read before the audit.

The offline wiki snapshot was used rather than the online Paradox wiki. The required core pages were consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. Country creation, Portrait modding, Division modding, Technology modding, National focus modding, Equipment modding, and Cosmetic tag pages were also consulted for the package surfaces.

Vanilla documentation consulted included `documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, character documentation, on-action documentation, AI strategy/template/equipment documentation, unit/equipment documentation, and `common/script_constants/documentation.md`. Vanilla precedents included `common/decisions/GER.txt` for created-country technology inheritance and `common/ai_strategy/default.txt` for equipment, role, and naval strategy differentiation.

## Findings

### P1 — Unification permanently strands reusable CBA–CBH slots and bypasses the canonical reset

**Evidence**

- Formation gives every transferred state a core for the allocated reusable tag in `cannibalism_create_selected_warlord_country_from_current_state` (`common/scripted_effects/014_cannibalism_country_effects.txt:866-900`).
- The canonical release path is `cannibalism_begin_current_warlord_slot_release` (`common/scripted_effects/014_cannibalism_country_effects.txt:1132-1227`). It resets focus contracts and incarnation state, removes Event 14 ideas and templates, removes runtime modifiers, and sends every core/source state through `cannibalism_retire_current_state_from_warlord_slot`.
- That state helper removes the old tag's core and clears its state references (`common/scripted_effects/014_cannibalism_country_effects.txt:1090-1128`). `cannibalism_finalize_current_warlord_slot_release` then releases the global slot only after the reference audit succeeds (`common/scripted_effects/014_cannibalism_country_effects.txt:1230-1255`).
- By contrast, `cannibalism_prepare_current_warlord_slot_for_unification` only unregisters selected runtime references, clears two state slot variables, clears global in-use flags, and marks the slot verified (`common/scripted_effects/014_cannibalism_unification_effects.txt:230-279`). It does not remove cores, node-source references, ideas, templates, focus contracts, modifiers, or incarnation state.
- The unification helper clears `cannibalism_warlord_slot_in_use` at line 273 before annexation. The `on_annex` cleanup calls the canonical release only when the annexed source still has that flag (`common/on_actions/014_cannibalism_on_actions.txt:73-88`), so host, submitted-warlord, and Wendigo-donor annexations skip the canonical reset.
- The reuse gate rejects a dead slot if any state remains `is_core_of = PREV` or retains a matching node-source reference (`cannibalism_current_warlord_slot_references_are_clear`, `common/scripted_triggers/014_cannibalism_triggers.txt:892-950`). The cores added at formation therefore make each absorbed slot permanently fail reuse.
- `cannibalism_apply_current_warlord_ai_profile` uses persistent `add_ai_strategy` calls (`common/scripted_effects/014_cannibalism_country_effects.txt:601-610`). No documented reset effect exists in the vanilla effect documentation, so bypassing cleanup also leaves a latent strategy-stacking risk if reuse is repaired without changing the AI strategy pattern.

**Impact**

After ordinary or Wendigo unification, every absorbed CBA–CBH tag is advertised as available globally but fails the tag-local reference gate forever. Later Event 14 warlord formation loses capacity, and any partial workaround that removes only cores would reuse a tag with stale focus, idea, template, modifier, and AI state.

**Required remediation**

1. Do not clear `cannibalism_warlord_slot_in_use` before annexation.
2. Preserve the already-captured inheritance and migrated references, then let `on_annex` call `cannibalism_begin_current_warlord_slot_release`, or refactor that canonical helper into a shared post-migration reset used by both normal defeat and unification.
3. Keep `cannibalism_finalize_current_warlord_slot_release` as the only place that marks the slot reusable after the state/core/reference audit and quarantine.
4. Convert origin AI injections to an explicitly resettable or flag-gated strategy pattern before slot reuse; do not allow prior-incarnation target and production strategies to accumulate.
5. Exercise host absorption, submitted absorption, surrender absorption, and Wendigo-donor absorption separately, because all currently call the defective preparation helper.

### P1 — Every starting division receives duplicated free equipment and manpower

**Evidence**

- `cannibalism_warlord_creation.starting_equipment_factor` and `.starting_manpower_factor` are both `0.25` (`common/script_constants/014_cannibalism_country_constants.txt:130-131`).
- `cannibalism_spawn_current_warlord_starting_units` passes both factors to every created starting division, including each origin specialist (`common/scripted_effects/014_cannibalism_country_effects.txt:495-598`). Thus every one of the dynamically selected 1–14 opening divisions begins with 25% equipment and 25% manpower.
- The same setup separately adds 50% of the exact population loss to the country's manpower pool (`cannibalism_prepare_current_warlord_starting_force`, lines 440-467) and separately grants infantry/support plus origin-fit artillery, motorized, trains, fuel, or convoys to the stockpile (lines 469-492).
- The offline Country creation and Division modding pages state that `start_equipment_factor` equipment is not subtracted from national reserves. They also state that explicit `start_manpower_factor` sets the division's starting manpower; reserve subtraction is the behavior used when that factor is left unset.
- Part 4 explicitly requires the starting package not to duplicate free equipment (`docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_4_country_packages.md:340-380`).

**Impact**

The intended population-backed manpower and origin-scaled stockpile are supplemented by a second free 25% fill on every division. Larger 10- and 14-division openings amplify the duplication.

**Required remediation**

Set both creation factors to zero, as the paid CBL and Wendigo recruitment paths already do. Spawn the divisions empty and let only the exact population-backed manpower pool and explicit origin-fit stockpile grants reinforce them. Retain `start_experience_factor`; it does not create manpower or equipment.

### P1 — CBL has zero research slots and does not preserve later warlords' technologies

**Evidence**

- CBL's dormant history explicitly sets `set_research_slots = 0` (`history/countries/CBL - Cannibal Unified Host.txt:7`).
- Each runtime CBA–CBH country is explicitly raised to three research slots in `cannibalism_setup_current_warlord_country` (`common/scripted_effects/014_cannibalism_country_effects.txt:699-720`; constant at `common/script_constants/014_cannibalism_country_constants.txt:120`).
- CBL creation calls `inherit_technology` from the selected host but never calls `set_research_slots` or `add_research_slot` (`common/scripted_effects/014_cannibalism_unification_effects.txt:410-433`).
- The vanilla effect documentation defines `inherit_technology` as copying technology state, while `set_research_slots` is a separate effect that sets the slot count. The offline Country creation page gives two slots as the ordinary default and two to four as the normal minor/major range. The Event 14 runtime standard is three; zero means CBL cannot research at all.
- `cannibalism_absorb_current_warlord_into_unified_host` captures the later source at lines 566-568, then migrates references, Larder, character identity, wars, troops, and territory at lines 571-620. It never transfers that source's technology.

**Impact**

The unified country begins with the initial host's researched technologies but no ability to continue research. Technologies held only by later submitted warlords are lost from the playable unified package.

**Required remediation**

1. Explicitly assign CBL at least the Event 14 constituent standard of three research slots at creation, or implement a documented dynamic slot rule with three as the minimum.
2. Implement a union-safe technology transfer for each absorbed warlord before the source disappears. Do not blindly chain `inherit_technology`: vanilla documentation describes it as copying the target's whole technology state, so repeated donors need a checked, additive transfer contract for the relevant technology families.
3. Add a regression scenario in which the host and a submitted warlord own different technologies and confirm both survive in CBL.

### P1 — Unification preserves only part of route, origin, idea, and character inheritance

**Evidence**

- The selected host's hierarchy, Larder route, network route, Larder, Frenzy, alignment, origin, region, name, slot, and personality are captured (`cannibalism_capture_current_warlord_inheritance`, `common/scripted_effects/014_cannibalism_unification_effects.txt:140-163`).
- `cannibalism_apply_inherited_host_identity_to_cbl` stores hierarchy/Larder/network route variables and sets corresponding `cannibalism_unified_inherited_*` flags (`lines 165-227`). A search across the unified focus, decision, trigger, and effect files finds no consumer for the hierarchy/Larder/network variables or those route flags. The completed local route therefore does not mechanically alter the unified opening, contrary to Part 7's focus-integration contract (`...part_7_hannibal_reveal_and_unification.md:216-221`).
- CBL receives `cannibalism_unified_command_burden` at creation, but no source-origin or completed-route national spirit is transferred (`common/scripted_effects/014_cannibalism_unification_effects.txt:410-433`).
- The initial host's origin knowledge is functional: `cannibalism_apply_inherited_host_identity_to_cbl` sets one knowledge flag, and the unified origin-specialist decision/effect uses it with exact population conversion and zero-filled unit creation (`common/decisions/014_cannibalism_unified_decisions.txt:274-286`; `common/scripted_triggers/014_cannibalism_unified_decision_triggers.txt:315-358`; `common/scripted_effects/014_cannibalism_unified_decision_effects.txt:1910-1928`).
- Later absorption captures the submitted warlord's origin (`common/scripted_effects/014_cannibalism_unification_effects.txt:566-583`) but never applies that origin to CBL. Only the initial host's specialist family can therefore be recruited after integration.
- The current specialist effect is an `if/else_if` priority chain: island, then siege, then march, then prison (`common/scripted_effects/014_cannibalism_unified_decision_effects.txt:1910-1925`). If later origin knowledge is added without redesigning the choice, multiple known origins still collapse to the first matching template.
- Retained warlords are reconstructed with matching name, regional portrait, and origin trait (`cannibalism_create_integrated_warlord_commander`, `common/scripted_effects/014_cannibalism_unification_effects.txt:344-370`). The captured personality is not applied. Surrender records `disposable_servant` in a slot variable but creates no servant, prisoner, or minor character (`lines 333-341, 585-594, 637-642`). This does not satisfy the character/region consequences required by Part 7 lines 136-161 and the acceptance criteria.

**Impact**

The host's local route history is largely inert after conversion; later origins do not expand specialist access; local ideas are not deliberately mapped; retained commanders lose personality; and the surrender disposition is ledger-only. The unification result does not reflect the full countries that entered it.

**Required remediation**

1. Define explicit unified-opening modifiers/effects for each inherited hierarchy, Larder, and network route, and consume the existing variables/flags during CBL initialization.
2. Deliberately map source ideas into CBL-safe unified ideas rather than copying incompatible local spirits wholesale.
3. On every later absorption, register the source origin on CBL. Replace the single priority-chain specialist decision with one selectable/capped paid path per known origin so all inherited families remain available.
4. Preserve the source personality where compatible with commander traits, and implement a real character/region consequence for surrender, servant, prisoner, governor, rival, and purge outcomes rather than only recording a number.

### P1 — The transformed original-ZZZ country is removed from established daily zombie processing

**Evidence**

- The merge correctly selects the live original-ZZZ Wendigo country in place (`cannibalism_is_valid_wendigo_merge_host`, `common/scripted_triggers/014_cannibalism_wendigo_triggers.txt:10-21`) and does not create a replacement country or load a replacement OOB.
- After transformation, `common/on_actions/002_zombie_outbreak_on_actions.txt` excludes `cannibalism_wendigo_hannibal_country` from all three original daily branches:
  - controlled-state decay at lines 123-132;
  - weaponized hostility, canonical neighboring-horde merge, and expansion at lines 134-145;
  - original-ZZZ world-threat refresh, continent rejoin pressure, expansion, annexation of neighboring dynamic outbreaks, automatic coring, capital relocation, and Americas war continuity at lines 147-214.
- Event 14's on-actions and Wendigo pulse do not call any of those helpers. They process Event 14 defeat, anchors, countdown, and terminal logic instead.
- The preservation specification requires the live original tag's zombie-system links and established mechanics to remain, and Part 4 requires existing units, technologies, powerful bonuses, and both recruitment systems (`...part_4_country_packages.md:650-678`; `docs/plans/014_cannibalism_plans/014_wendigo_preservation_map.md`).

**Impact**

The country's tag, units, technologies, ideas, templates, and AI files remain, but a large part of its established campaign behavior switches off at merge. This is not an in-place preservation of the live Wendigo package.

**Safest Event 14-compatible remediation pattern**

Factor the original-ZZZ daily operations into a shared country-scoped helper and call it exactly once for both normal original ZZZ and transformed original ZZZ. For the transformed branch, preserve controlled-state decay, weaponized hostility, canonical merge/expansion, threat refresh, rejoin pressure, dynamic-outbreak annexation, coring, capital relocation, and war-continuity handling. Gate only the original leader refresh and any generic defeat/world-end transition that would conflict with Event 14's transformed leader, anchors, countdown, or terminal lock.

Use the existing Event 2 daily branch or an exact `on_daily_ZZZ` hook; do not add a second Event 14 whole-world daily iterator. This keeps the original processing cadence, avoids double execution, and makes the intentional exclusions explicit.

### P2 — March Host formation can underflow the required weak opening, and tiered starting Larder is dead tuning

**Evidence**

- Island, siege, and prison formation require `cannibalism_warlord_start.weak_population_k`, which is 250K (`common/scripted_triggers/014_cannibalism_triggers.txt:440-494`; constant at `common/script_constants/014_cannibalism_country_constants.txt:201`). March formation has no equivalent population gate and only rejects states below the shared 10K usable-Larder floor (`common/script_constants/014_cannibalism_core_constants.txt:321`).
- Warlord creation consumes 5% of population and grants one unit of capacity per 4K people actually consumed (`common/script_constants/014_cannibalism_core_constants.txt:882`; `common/script_constants/014_cannibalism_country_constants.txt:132`; `cannibalism_prepare_current_warlord_starting_force`, lines 440-459). A 10K March state consumes only 500 people, rounds to zero capacity, is clamped to one, and therefore creates one division. States below roughly 120K can remain at one division after rounding.
- Part 4's weak opening calls for two to four irregular formations plus an organizer cadre (`...part_4_country_packages.md:340-351`).
- `cannibalism_warlord_starting_larder` is assigned as 45/90/160/240 by tier (`common/scripted_effects/014_cannibalism_country_effects.txt:105-146`; constants at `common/script_constants/014_cannibalism_country_constants.txt:218-221`) but is never consumed by another effect.
- Actual starting Larder comes only from the 5% creation consumption at 0.20 Larder per consumed 1K, capped at 120. At the three population thresholds this yields about 2.5, 7.5, and 20 Larder rather than the configured 45, 90, and 160; the configured 240 high-chaos value is unreachable through that variable.

**Required remediation**

Give March formation a population/equipment/defecting-unit contract sufficient for its intended opening, or compute a lower package that still meets the documented minimum without creating resources from nothing. Either use the tiered Larder values through an explicitly population-backed transaction or remove them and rebalance/document the actual exact-consumption values.

### P2 — All four origin archetypes receive the same runtime AI production and army profile

**Evidence**

- `cannibalism_apply_current_warlord_ai_profile` gives every origin the same build-army, infantry/support production, infantry-template/role, and former-controller target strategies (`common/scripted_effects/014_cannibalism_country_effects.txt:601-610`). It contains no origin branch.
- Focus and decision `ai_will_do` weights provide some route differentiation, so this is not a complete AI absence. However, there is no Island naval/convoy strategy, Siege fortification/artillery strategy, March mobile/fuel/rail strategy, or Prison rear-area/infiltration production/target profile.
- The required archetype behavior is explicit in Part 9 (`docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_9_ai_balance_and_integrations.md:156-185`). Vanilla `common/ai_strategy/default.txt` demonstrates equipment and role-specific strategy families rather than a single infantry-only profile.

**Required remediation**

Create resettable, origin-gated AI profiles aligned with the four archetypes and their paid operations. Include equipment-production and role priorities that match the templates actually available, plus naval access for Island Hosts and mobile/fuel behavior for March Hosts. Keep the shared former-controller pressure only as the common base layer.

### P2 — CBL host supply and coherence are scoring bonuses, not viability requirements

**Evidence**

- `cannibalism_is_viable_unification_host` requires an existing, uncapitulated warlord with a controlled, usable capital, but no supply node, port, railway, infrastructure, or connected-region requirement (`common/scripted_triggers/014_cannibalism_triggers.txt:1024-1033`).
- `cannibalism_calculate_current_unification_host_score` adds points for a supplied capital and railway and subtracts an isolation penalty, but clamps every candidate to at least one (`common/scripted_effects/014_cannibalism_unification_effects.txt:74-105`). A fully isolated, unsupplied candidate remains valid if no better host exists; a human candidate also receives +1000.
- Part 7 requires valid capital, supply, and contiguous core in host selection (`...part_7_hannibal_reveal_and_unification.md:93-105`), and the acceptance criteria require valid capital, supply, and map coherence.

**Required remediation**

Add a hard host-capital logistics/coherence contract with a player-safe exception only when the map genuinely has no alternative and the design explicitly supplies an immediate corridor/port outcome. Do not treat supply solely as a score bonus.

## Passing evidence

### Reusable tag and territory design before unification

- `common/country_tags/014_cannibalism_countries.txt:8-16` provides eight unique regional slots plus CBL: CBA/CBB Island, CBC/CBD Siege, CBE/CBF March, and CBG/CBH Prison.
- Origin selection and allocation keep each archetype inside its two-slot pair (`common/scripted_effects/014_cannibalism_country_effects.txt:66-93, 1017-1034`).
- Formation transfers the origin plus at most two directly adjacent active-cell states (`lines 864-901`; constants `maximum_starting_states = 3`, `maximum_neighbor_states = 2`). The resulting ordinary package is connected to the origin rather than a disconnected state sweep.
- Unsupported regions block formation rather than selecting a generic identity (`common/scripted_triggers/014_cannibalism_triggers.txt:506-558`).

### Regional identity and assets

- The seven-region selector covers Europe, Asia, Africa, Middle East, North America, South America, and Oceania (`common/scripted_effects/014_cannibalism_country_effects.txt:96-103`).
- The same stored region/name index drives leader name and portrait construction, and retained commanders reuse the same slot/region identity (`common/scripted_effects/014_cannibalism_unification_effects.txt:344-365`).
- There are 28 regional name keys: four names for each of seven regions.
- All 56 expected CBA–CBH regional portrait DDS files are present and have 56 distinct SHA-256 hashes. `interface/014_cannibalism.gfx` contains 64 CBA–CBH portrait sprite declarations: one default and seven regional names per slot, with the default/Europe pair intentionally sharing the Europe file.
- CBA–CBH each have base, democratic, fascist, communist, and neutral flag variants in regular, medium, and small sizes; no required flag file is missing.
- The generated leader receives one origin and one personality trait. The audit proves file presence, distinct binaries, region/name/portrait coupling, and GFX wiring; subjective portrait-art acceptance should rely on the dedicated asset review rather than hash uniqueness alone.

### Templates, paid recruitment, and population accounting

- Nine ordinary template families are created, individually locked, and force-blocked from normal recruitment (`common/scripted_effects/014_cannibalism_country_effects.txt:420-437`).
- Ongoing warlord and CBL recruitment uses exact state-population removal, Larder payment, caps, cooldowns, territory checks, and equipment reserve gates. Created paid units start at zero manpower and zero equipment.
- `cannibalism_state_is_unusable_larder` blocks wasteland, fully consumed, severe contamination, irreversible air contamination, ineligible nonhuman ownership, and low-population/exhausted states (`common/scripted_triggers/014_cannibalism_triggers.txt:349-371`). No unusable-state Larder gain or duplicate population transaction was found.
- The shared request/receipt path records the actual applied population loss before Larder or manpower is credited (`common/scripted_effects/014_cannibalism_core_effects.txt:2925-3081`).

### CBL reveal and player-control handling

- The global reveal flag is set before CBL ownership, public leader, portrait, focus, decisions, news, or audio-facing operations (`common/scripted_effects/014_cannibalism_unification_effects.txt:397-431`).
- Human host scoring receives +1000 and `change_tag_from` transfers the player into CBL (`lines 25-29, 435-442`).
- A second human warlord cannot be silently displaced: submission is allowed only when the source or destination is AI (`common/scripted_triggers/014_cannibalism_wendigo_triggers.txt:58-65`).
- CBL joins the selected host's enemy wars before annexing it, and annexation transfers troops (`common/scripted_effects/014_cannibalism_unification_effects.txt:457-475, 596-619`).
- The initial host's Larder, origin identity, name/portrait, wars, troops, and paid origin-specialist access are preserved. The defects above concern route mechanics, later absorptions, research slots, and full disposition coverage.

### Live Wendigo in-place merge

- Valid selection requires the live original-ZZZ, dynamic weaponized independent Wendigo profile and rejects an already completed generic Wendigo world end (`common/scripted_triggers/014_cannibalism_wendigo_triggers.txt:10-21`).
- Transformation occurs in the selected ZZZ country. No replacement tag or replacement OOB is loaded. Existing units, templates, technologies, ideas, politics, territory, and original recruitment remain in scope while Event 14 adds its overlay.
- Reveal precedes transformed leader/cosmetic/focus/news surfaces (`common/scripted_effects/014_cannibalism_wendigo_effects.txt:346-421`).
- The Wendigo Pack remains force-recruitable and locked against template editing (`cannibalism_wendigo_focus_preserve_pack_contract`, `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt:80-95`). Additional Event 14 pack training uses exact population and Larder costs and creates empty units.
- Player control is preserved for a human ZZZ, transferred from a human donor when ZZZ is AI, and not forcibly merged when both countries are human (`common/scripted_effects/014_cannibalism_wendigo_effects.txt:353-406`).
- Anchors are population-backed, registered, visible, destructible before lock, and feed the countdown; the locked terminal package and transformed assets are present.
- The original ZZZ AI strategy and equipment-template files remain applicable through the original-tag/dynamic-profile checks. The daily-processing exclusion remains the blocking preservation defect.

### Secrecy and shared classification

- No player-facing pre-reveal country, character, focus, decision, idea, GUI, achievement, report, news, or super-event identity leak was found.
- Public CBL and transformed-ZZZ operations are sequenced after `cannibalism_reveal_complete`.
- CBA–CBH and CBL use the shared special-chaos-country classification. The transformed ZZZ route additionally uses the actual-nonhuman classification.

## Remediation order

1. Repair unification slot cleanup and prove reuse after host, submitted, surrender, and Wendigo-donor absorption.
2. Zero the starting manpower/equipment factors and re-evaluate all four start tiers.
3. Give CBL research slots and implement union-safe technology continuity.
4. Complete route/origin/idea/character inheritance, including selectable specialist families for later origins.
5. Restore the safe subset of original-ZZZ daily mechanics without duplicating daily processing or replacing the transformed leader.
6. Fix March minimums/starting Larder, then add origin-specific AI and hard host logistics viability.
7. Re-run the full country-package audit after the remediation tranche; completion should not be claimed from individual fixes alone.

## Skills used or changed

- Used: `chaos-redux-events`
- Used: `chaos-redux-subagents`
- Used: `hoi4-focus-trees`
- Created or updated: none

