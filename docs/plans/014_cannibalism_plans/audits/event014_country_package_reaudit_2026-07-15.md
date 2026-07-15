# Event 014 Country Package Final Reaudit

> Superseded for current authority by `event014_country_package_consolidation_reaudit_2026-07-15.md`. This same-day checkpoint remains historical evidence only.

Date: 2026-07-15

Audit basis: live shared working tree at Git HEAD `7f15cf8b0b1ab764c1d7aee04c02c5c6e8f73614`. The working tree contains concurrent Event 014 work. Live source files, not Git HEAD or an older audit, are the implementation authority for this report.

Audit mode: final source, asset, and control-flow reaudit after player-first host selection and atomic manual-scenario remediation. No gameplay patch was required by this pass.

## Verdict

- P0: 0
- P1: 0
- P2: 0
- P3: 0

The Event 014 country package passes the requested final audit. CBA through CBH are eight origin-agnostic reusable slots. CBL is the dedicated ordinary unified country. The original Event 2 ZZZ Wendigo country is preserved and transformed in place. Player-controlled eligible hosts win before AI scoring. Player control is transferred before any elected human absorption. Exactly three warlord origins remain. Formation and recruitment are population-accounted. Unit creation does not generate free manpower or equipment. Larder gains are tied to population, operations, or combat outcomes. Regional leaders, names, flags, and portraits are wired across all slots. AI, reinforcement, response outcomes, reference-safe cleanup, and post-reveal secrecy gates are present.

The former manual-scenario P3 is closed. Manual launch now proves and freezes the complete actor, opening-state capacity, external state, origin distribution, and reusable-slot plan before the first gameplay mutation. Planned states and slots are consumed from those exact temporary arrays. The required quantities match every downstream profile branch. A failed preflight changes only the launcher's failure marker and temporary planning state.

## Finding disposition

### Resolved P2: player-first deterministic host selection

Ordinary unification:

- `common/scripted_effects/014_cannibalism_unification_effects.txt:147-176` searches viable human warlords first.
- The AI pass runs only when `cannibalism_human_unification_host_found` remains zero.
- `common/scripted_effects/014_cannibalism_unification_effects.txt:115-145` preserves the strength score within the selected control class and resolves an equal score by lower numeric country ID.
- `common/scripted_effects/014_cannibalism_unification_effects.txt:513-581` records whether the selected host is human and calls `change_tag_from` before the host is annexed.

Wendigo unification:

- `common/scripted_effects/014_cannibalism_wendigo_effects.txt:78-101` searches valid human original-ZZZ survivors first.
- The AI pass runs only when `cannibalism_human_wendigo_merge_host_found` remains zero.
- `common/scripted_effects/014_cannibalism_wendigo_effects.txt:47-76` preserves the Wendigo merge score within the selected control class and resolves equality by lower numeric country ID.
- `common/scripted_effects/014_cannibalism_wendigo_effects.txt:443-502` keeps a human ZZZ host in place, protects a dual-human donor from forced absorption, and transfers a human donor to an AI ZZZ host before absorption.

### Resolved P3: atomic manual scenario preflight

The old failure path began runtime and country mutations before every profile resource was known. The live implementation removes that reachable path.

- `common/scripted_effects/014_cannibalism_scenario_effects.txt:1151-1163` prepares only temporary scale values and the preflight manifest before setting the launch-active flag or calling global runtime preparation.
- `common/scripted_effects/014_cannibalism_scenario_effects.txt:263-369` builds the complete temporary manifest and sets `cannibalism_scenario_preflight_result` only after exact equality checks pass.
- The preflight helper contains no country, state, population, unit, technology, idea, war, scheduler, history, achievement, or global-runtime mutation.
- `common/scripted_triggers/014_cannibalism_scenario_triggers.txt:29-77` proves the canonical opening-state capacity for every planned actor. High and maximum Discipline Collapse require two opening states in the source because one additional source state is seeded after initialization.
- `common/scripted_triggers/014_cannibalism_scenario_triggers.txt:79-171` proves valid AI destructive controllers, clear states, population, supported region, origin geography, formation and consumption locks, and exclusion of every planned actor controller.
- Island, Siege, and March predicates are disjoint. The manifest also checks cross-array membership explicitly at `common/scripted_effects/014_cannibalism_scenario_effects.txt:309-348`.
- `common/scripted_effects/014_cannibalism_scenario_effects.txt:195-260` records the exact available CBA-CBH scopes in deterministic slot order.
- `common/scripted_effects/014_cannibalism_scenario_effects.txt:351-367` requires exact equality between every planned count and every required count before commit.
- `common/scripted_effects/014_cannibalism_scenario_effects.txt:662-840` consumes the exact planned state and slot arrays. Each selected reusable slot is revalidated immediately before its canonical allocator is called and is removed from the plan only after formation succeeds.
- `common/scripted_effects/014_cannibalism_scenario_effects.txt:913-958` consumes the same Island, Siege, and March counts declared by the preflight matrix.
- The setup is one synchronous effect chain. No Event 014 pulse or external callback can consume a planned state or slot between preflight and its consumer.
- `common/scripted_effects/014_cannibalism_scenario_effects.txt:1186-1198` records launch history, counters, scheduler work, and manual-scenario achievement disqualification only after setup success.
- A failed preflight reaches only `cannibalism_manual_scenario_setup_failed` at `common/scripted_effects/014_cannibalism_scenario_effects.txt:1199-1201` and temporary-array cleanup at lines 1217-1221. It does not enter runtime preparation.
- Reservation cleanup is limited to a committed preflight at `common/scripted_effects/014_cannibalism_scenario_effects.txt:1203-1216`.
- `common/scripted_effects/014_cannibalism_scenario_effects.txt:1107-1145` explicitly sets `cannibalism_scenario_use_preflight_plan` to zero for automatic Evolution III prefire, preserving its separate dynamic path.

Exact manual profile plan and consumption matrix:

| Profile | Low | Medium | High | Maximum |
| --- | --- | --- | --- | --- |
| Discipline Collapse | 1 actor, 1 opening state | 2 actors, 1 opening state each | 3 actors, 1 opening state each, source has 2 | 5 actors, 1 opening state each, source has 2 |
| Ritual Cells | 1 actor, 2 opening states | 2 actors, 2 opening states each | 3 actors, 2 opening states each | 5 actors, 2 opening states each |
| Silent Islands | I1, hosts 0, slots 0 | I2, hosts 1, slots 1 | I4, hosts 1, slots 1 | I6, hosts 2, slots 2 |
| Warlord States | S1, slots 1 | I1 plus S1, slots 2 | I1 plus S2 plus M1, slots 4 | I2 plus S2 plus M2, slots 6 |
| Convergence | I1 plus S1 plus M1, slots 3 | I2 plus S1 plus M1, slots 4 | I2 plus S2 plus M1, slots 5 | I2 plus S2 plus M2, slots 6 |

`I`, `S`, and `M` mean Island, Siege, and March external states.

## Country package evidence

### Origin-agnostic reusable slots and three origins only

- `common/country_tags/014_cannibalism_countries.txt:8-16` maps exactly CBA-CBH to neutral reusable slot definitions and reserves CBL for unification.
- Eight matching `common/countries/Cannibal Warlord Slot CB?.txt` files and eight matching dormant `history/countries/CB? - Cannibal Warlord Slot.txt` files exist.
- Dormant histories have no active OOB and no research slots. Runtime setup overwrites politics, popularities, stability, war support, research slots, leader, origin, ideas, tree, technology minimums, and forces.
- `common/script_constants/014_cannibalism_country_constants.txt:9-39` defines eight slots and only Island Host, Siege Commune, and March Host.
- `common/scripted_effects/014_cannibalism_country_effects.txt:61-135` derives the origin and one of seven supported regions from the actual origin state.
- `common/scripted_effects/014_cannibalism_country_effects.txt:558-577` clears all origin flags and applies exactly one of the three live origin flags and ideas.
- `common/scripted_effects/014_cannibalism_country_effects.txt:858-955` gives CBA-CBH the same first-available allocator contract.
- The warlord focus tree has exactly three origin overlay roots at `common/national_focus/014_cannibalism_warlord_focus.txt:813-824`, `896-907`, and `979-990`.
- `common/decisions/014_cannibalism_warlord_decisions.txt:360-412` has one paid origin operation for each live origin.
- `common/ideas/014_cannibalism_ideas.txt:49-123` has three starting origin ideas and three origin upgrades.
- `common/country_leader/014_cannibalism_traits.txt:9-25` has three origin leader traits.
- A case-insensitive runtime search across `common/`, `events/`, `history/`, `interface/`, and `localisation/` found zero removed Prison Host, origin-prison, Lockhouse, or fixed CBG/CBH prison identifiers. Generic prison nodes, prisoner objectives, and prisoner logistics remain because they are baseline Event 014 content, not a fourth country origin.

### Territory, forces, technology, ideas, and paid reinforcement

- `common/scripted_triggers/014_cannibalism_triggers.txt:498-535` requires a supported region, one valid live origin, a mature feeding-state node, a valid normal controller, and a free reusable slot.
- `common/scripted_effects/014_cannibalism_country_effects.txt:797-855` transfers the origin state and at most two adjacent active-node states controlled by the same former controller. It cores only selected states and uses the actual origin state as the capital.
- `common/scripted_effects/014_cannibalism_country_effects.txt:683-711` requires the canonical exact population transaction to succeed before final formation, starting forces, focus load, and success bookkeeping.
- `common/scripted_effects/014_cannibalism_country_effects.txt:402-455` derives force capacity and manpower from `cannibalism_population_loss_applied`.
- `common/script_constants/014_cannibalism_country_constants.txt:148-150` sets spawned-unit starting equipment and manpower factors to zero and derives unit capacity from consumed population.
- `common/scripted_effects/014_cannibalism_country_effects.txt:457-551` creates only zero-filled template shells. The population-backed manpower pool and bounded stockpile package must reinforce them.
- `common/scripted_effects/014_cannibalism_country_effects.txt:640-657` inherits technology from the real former controller, then adds the shared military minimum without clearing inherited research.
- `common/scripted_effects/014_cannibalism_country_effects.txt:255-400` creates and locks the Event 014 template families and disables normal queue recruitment.
- `common/scripted_effects/014_cannibalism_warlord_decision_effects.txt:279-347` requires an exact population loss, pays the full Larder cost, then grants population-derived manpower and creates a zero-filled unit shell or emergency reinforcement.
- The same transaction records unit caps and applies a state cooldown. There is no spawn before population success and no spawn when the Larder cost is zero.
- `common/scripted_effects/014_cannibalism_core_effects.txt:2991-3226` derives all consumption Larder from the exact applied population loss. Other Larder additions in the warlord package are gated operation, focus-contract, or major-victory rewards. No free population, unit, or Larder path was found.
- `common/scripted_effects/014_cannibalism_unification_effects.txt:314-327` reopens inherited paid recruitment without unlocking normal template recruitment.

### Ordinary CBL unification and leader outcomes

- `common/scripted_effects/014_cannibalism_unification_effects.txt:513-628` creates CBL from the selected host's capital, additive technology, identity variables, origin templates, paid recruitment, wars, troops, and actor references.
- `common/scripted_effects/chaosx_dynamic_effects.txt:571-617` unions researched tokens additively and protects mutually exclusive industry branches.
- CBL joins the selected host's wars before `annex_country` with `transfer_troops = yes`.
- `events/014_cannibalism.txt:450-543` gives every surviving warlord explicit retained-command submission, disposable submission, autonomy, resistance, and challenge choices.
- `common/scripted_effects/014_cannibalism_unification_effects.txt:698-771` migrates references, unions technology, preserves wars and troops, records the leader disposition, and transfers a human player before annexation.
- `common/scripted_effects/014_cannibalism_unification_effects.txt:776-872` implements all five outcomes. Autonomy, resistance, and challenge leave the warlord on the map. The submit options are hidden when both the current warlord and destination are human.

### Original-ZZZ Wendigo preservation

- `common/scripted_triggers/014_cannibalism_wendigo_triggers.txt:10-24` accepts only a live original-tag ZZZ country with the exact Event 2 weaponized independent Wendigo identity and surviving territory or divisions.
- `common/scripted_effects/014_cannibalism_wendigo_effects.txt:289-340` mutates that same country scope in place with the Winter Host cosmetic identity, Event 014 state, inherited templates, paid recruitment, Hannibal leader, and persistent targets.
- `common/scripted_effects/014_cannibalism_wendigo_effects.txt:368-422` adds donor technology and troops without replacing recipient technology or units.
- `common/scripted_effects/014_cannibalism_wendigo_effects.txt:443-522` never creates or releases a replacement ZZZ country.
- The merge contains no OOB reload, unit deletion, technology clear, idea clear, stockpile clear, research-slot reset, or special-project reset. Existing ZZZ territory, control, divisions, templates, technology, ideas, recruitment state, equipment, and special projects remain attached to the original country.

### Regional leaders, names, flags, and portraits

- `common/scripted_localisation/014_cannibalism_scripted_localisation.txt:138-167` maps 28 regional leader names.
- `common/scripted_localisation/014_cannibalism_scripted_localisation.txt:213-232` maps all eight slot tokens and all seven region tokens.
- `localisation/english/014_cannibalism_l_english.yml:194-329` gives CBA-CBH dynamic country, adjective, and party localisation.
- `localisation/english/014_cannibalism_l_english.yml:405-419` resolves the eight internal slot tokens and seven region tokens.
- `interface/014_cannibalism.gfx:161-224` registers eight portrait names per slot. The generic and Europe names share the Europe DDS, producing 64 registrations backed by 56 distinct regional files.
- All 56 expected warlord DDS files exist. Every file is 156 by 210. All 56 SHA-256 hashes are unique.
- The CBA-CBD and CBE-CBH contact sheets were visually rechecked. They show distinct bald male warlords. CBG and CBH have no prison cell, bars, cage, restraints, or prisoner-uniform direction. The required CBA South America skull-lick portrait is present.
- All 120 expected CBA-CBH flag files exist. This is eight tags times five ideology filenames times three sizes. Header checks found zero dimension mismatch at 82 by 52, 41 by 26, and 10 by 7.

### AI, cleanup, and reuse

- `common/ai_strategy/014_cannibalism_warlords.txt:10-56` defines one common profile and one profile for each of the three origins. Every profile uses `abort_when_not_enabled = yes`, so a retired or reused slot cannot retain stale identity priorities.
- The warlord focus and decision surfaces contain origin-aware `ai_will_do` or `ai_chance` logic. Reinforcement remains on the exact population and Larder transaction instead of normal recruitment.
- `common/scripted_effects/014_cannibalism_core_effects.txt:2317-2366` removes all Event 014 timed missions and clears family runtime before an incarnation reset.
- `common/scripted_effects/014_cannibalism_country_effects.txt:1051-1145` closes decisions, removes Event 014 ideas and templates, clears actor and spread references, retires state references, and leaves the slot pending verified release.
- `common/scripted_triggers/014_cannibalism_triggers.txt:869-928` requires country, state, array, and global references to be clear.
- `common/scripted_effects/014_cannibalism_country_effects.txt:1147-1185` applies the reuse quarantine and releases CBA-CBH symmetrically.

### Hannibal secrecy

- `common/scripted_effects/014_cannibalism_unification_effects.txt:526-570` sets `cannibalism_reveal_complete` before CBL receives territory, focus tree, ideas, leader, portrait, public identity, or named threat.
- `common/scripted_effects/014_cannibalism_wendigo_effects.txt:472-489` sets the reveal flag before the original ZZZ receives its Hannibal cosmetic identity, leader, portrait, focus overlay, or public route state.
- `events/014_cannibalism.txt:426-445` and `546-565` require the reveal flag and the corresponding Hannibal character before either public reveal event can display.
- `common/decisions/014_cannibalism_achievement_tracker_decisions.txt:82-86` hides the Hannibal-named tracker entry until the reveal flag exists.
- The native Hannibal achievement is statically hidden at `common/achievements/chaos_redux_achievements.txt:2188-2196`.
- Event log details use separate pre-reveal and revealed localisation. The pre-reveal text identifies only a concealed command. No player-visible pre-reveal Hannibal name, portrait, country identity, focus tree, event, tracker entry, or named threat path was found.

## Task-specific validation

- Counted 8 reusable tag mappings, 8 neutral country definitions, and 8 dormant histories.
- Counted exactly 3 origin constants, 3 origin focus roots, 3 paid origin operations, 6 origin idea stages, 3 origin leader traits, and 3 origin AI overlays plus the common profile.
- Confirmed zero runtime matches for removed Prison Host and fixed prison-slot identifiers.
- Traced formation from selected state through exact population loss, territory transfer, zero-filled unit creation, rollback, and slot quarantine.
- Traced every paid warlord recruitment template through exact population loss, Larder payment, unit cap, and cooldown.
- Re-ran human-first ordinary and Wendigo selection branches, equal-score tie breaks, human-to-AI control transfer, and dual-human nonabsorption.
- Traced CBL creation, later submission and absorption, additive technology union, war transfer, troop transfer, autonomy, resistance, and challenge.
- Traced original-ZZZ selection and in-place mutation. No replacement-country effect or destructive recipient-state reset was found.
- Counted 64 portrait registrations, 56 live portrait files, 56 valid dimensions, and 56 unique hashes.
- Counted 120 CBA-CBH flag files with zero missing file and zero dimension mismatch.
- Compared the manual preflight requirement matrix against every downstream consumer call. Actor, Island, Siege, March, host, and slot quantities are equal for all five profiles and all four intensities.
- Confirmed preflight planning has no gameplay mutation, commit follows preflight success, failed preflight changes only the launcher marker, and automatic prefire explicitly stays on its dynamic path.
- Rechecked the implementation against official effect and trigger documentation and vanilla precedents for event targets, `change_tag_from`, `annex_country` with troop transfer, additive technology inheritance, focus-tree loading, and locked division-template recruitment.

This is a source and asset audit, not an in-game runtime session. The zero-finding verdict is based on reachable live control flow, exact inventory checks, and direct asset inspection.

## Exact files changed by this final audit

- `docs/plans/014_cannibalism_plans/audits/event014_country_package_reaudit_2026-07-15.md`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_country_package_final_reaudit_handoff_2026-07-15.md`

No gameplay, localisation, interface, asset, manifest, or spreadsheet file was changed by this final audit. No commit was created.

## Simplifications, omissions, and blockers

None. No fallback, placeholder, weakened substitute, omitted route, omitted origin, missing asset, missing AI behavior, missing player-control branch, or unverified scenario allocation remains in the assigned country-package scope.
