# Event 014 country-package post-closure re-audit — 2026-07-12

## Verdict

Read-only re-audit of the full live Event 014 country package after the focus-closure tranche.

**Verdict: not completion-ready. Two P1 defects in the new Wendigo receipt/Pack interoperability contract must be closed.**

- P0: 0
- P1: 2
- P2: 0
- P3: 1

The previously accepted CBA–CBH, CBL, and in-place original-ZZZ package remains intact. The blocking findings are confined to the newly connected Wendigo receipt and mixed Pack-muster lifecycle. No gameplay, localisation, asset, spreadsheet, skill, or existing documentation file was edited by this auditor. This report is the only auditor-created file, and no commit was created.

The report filename retains the requested 2026-07-12 audit-series date; the live post-closure baseline was inspected on 2026-07-13. The latest constant-backed tooltip localisation in `zz_014_cannibalism_focus_closure_l_english.yml` was included in the audit.

## Scope and references

The re-audit covered:

- all eight reusable warlord slots and four origins;
- ordinary CBL formation and later inheritance;
- transformation of the existing live original ZZZ country in place;
- player-control survival for ordinary and Wendigo unification;
- origin territory, cores, technology, ideas, units, templates, recruitment, characters, identity, AI, focuses, flags, portraits, and localisation;
- pre-reveal secrecy;
- exact population/Deaths/Larder/equipment accounting;
- the original and focus-closure Wendigo Pack contracts;
- inherited-origin template and commander stages;
- enemy-casualty receipts and receipt-backed muster;
- route-break and terminal-lock cleanup;
- target scorers, targeted-decision wrappers, MTTH wrappers, and pulse cadence.

Required repository guidance was read first: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, and `hoi4-focus-trees`.

The offline `paradox_wiki/` snapshot was used rather than the online Paradox wiki. The core Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding pages were consulted together with Country creation, Division modding, Unit modding, National focus, Technology, and Equipment. Vanilla `effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md` were consulted. Vanilla scorer, `change_tag_from`, and `add_units_to_division_template` implementations were used as precedents.

## Findings

### P1 — The paid two-Pack path can exceed the shared Pack capacity after a one-Pack receipt muster

The new receipt path correctly computes its post-muster count before authorising a one-Pack batch:

- `common/scripted_triggers/014_cannibalism_focus_closure_triggers.txt:200-207` computes `trained_pack_count + muster_pack_batch` and requires the result to be at or below capacity.
- `common/script_constants/014_cannibalism_focus_closure_constants.txt:70` defines the receipt batch as one Pack.

The existing paid Pack path does not apply the equivalent post-batch check:

- `common/script_constants/014_cannibalism_wendigo_constants.txt:227` defines `train_pack_batch = 2`.
- `common/scripted_triggers/014_cannibalism_wendigo_decision_triggers.txt:57-63` checks only that the current trained count is below capacity.
- `common/scripted_effects/014_cannibalism_wendigo_decision_effects.txt:184-187` then creates two Packs and adds two to the counter.

This was safe while all Pack growth was even. It is no longer safe after the receipt path can make the counter odd. With base capacity 12, for example, one receipt muster followed by five ordinary two-Pack musters leaves the count at 11. The ordinary decision remains available because 11 is below 12, then creates two Packs and records 13. The same defect applies at later even capacity values.

This violates the player-facing contract in `zz_014_cannibalism_focus_closure_l_english.yml:85-86`, which says both paid methods remain within the existing Pack cap. It also violates the requested no-free-output/capacity acceptance condition even though the extra units still start empty and paid population/Larder are consumed.

**Required closure:** make the ordinary paid path validate `trained_pack_count + train_pack_batch <= pack_capacity` before any population or Larder transaction and before spawning. The effect should retain its defensive trigger recheck. Re-audit both decision availability and the mixed one/two-Pack sequence at every capacity tier.

### P1 — Enemy casualty snapshots survive inactive-enemy periods and can credit unrelated losses on re-entry

The receipt sampler is bounded and non-retroactive for an uninterrupted enemy relationship, but it does not implement the stronger active-enemy-only lifecycle promised by the focus and flag text:

- `common/scripted_effects/014_cannibalism_focus_closure_effects.txt:194-201` snapshots only countries that are enemies when receipts open.
- `common/scripted_effects/014_cannibalism_focus_closure_effects.txt:258-262` later visits only current enemies.
- Per-country `cannibalism_wendigo_enemy_casualties_snapshot`, `cannibalism_wendigo_enemy_death_remainder`, and `cannibalism_wendigo_enemy_death_receipts_issued` are stored on the enemy country.
- `common/scripted_effects/014_cannibalism_focus_closure_effects.txt:265-270` clears only actor flags and the actor receipt pool. It does not clear or invalidate those per-enemy variables.

If an enemy leaves the war, suffers casualties in another conflict, and later becomes an enemy again, its old snapshot is still present. The first resumed pulse subtracts that old snapshot from its current lifetime casualty total, so losses suffered while it was not an active enemy are eligible for receipts. Route break and terminal cleanup also leave the per-enemy snapshot, remainder, and issued-cap state behind.

Pool cap five and per-enemy cap two still bound the result, and this sampler does not call the Deaths system, so this is not an unbounded duplication or a Deaths double count. It is nevertheless a direct violation of the constant-backed live text in `zz_014_cannibalism_focus_closure_l_english.yml:47` and `:81-82`: only later positive losses “while that country remains an active enemy” are promised, and the mechanic is described as non-retroactive.

**Required closure:** track the bounded sampled-enemy set and invalidate/reset a country's sampling epoch when it ceases to be an active enemy. Route break, terminal lock, and receipt shutdown must clear the sampled set and its owned per-enemy runtime state. This should remain attached to the existing Event 014 pulse; it must not introduce a recurring whole-world scan. Re-audit continuous-war deltas, first contact after receipts open, peace/re-war, capitulation/war transfer, casualty-counter decrease, route break, and terminal lock.

### P3 — The scorer header comment documents the corrected scopes backwards

`common/scorers/country/014_cannibalism_target_scorers.txt:4-9` says the scorer `target_trigger` actor is ROOT/default and the candidate is FROM, while the corrected live scorer and vanilla scorer contract use the candidate as the default scope and the initiating actor as FROM. The `score` half of the comment is correct, and the executable scorer/decision/MTTH wrappers are correct.

This is documentation-only, but it is likely to reintroduce the scope bug during later maintenance.

**Required closure:** correct the header comment to describe candidate default/THIS and initiating actor FROM consistently for both `target_trigger` and `score`.

## Passing country-package evidence

### Eight reusable warlord slots and origins

- `common/country_tags/014_cannibalism_countries.txt:8-16` registers CBA/AHX as Island, CBC/AIX as Siege, CBE/CBF as March, AMX/CBH as Prison, and CBL as the ordinary unified country. Matching country and dormant history files remain present.
- Origin selection, the strict origin-priority mapping, two-slot pools, regional identity selection, population/chaos force scaling, incarnation metadata, core assignment, quarantine, and final reference cleanup remain in the established country effects.
- Release still waits for the dead-country/reference audit before clearing the global slot-in-use marker. CBA through CBH all have allocation and release coverage.
- Regional identity remains bespoke for Europe, Asia, Africa, the Middle East, North America, South America, and Oceania; no generic unsupported-region identity leak was found.

### CBL and player-control survival

- Ordinary unification still creates CBL, applies the opening host's route/origin/identity state, loads `cannibalism_unified_focus_tree`, assigns research capacity, transfers wars and units, and uses `change_tag_from` before donor annexation when the host is human (`common/scripted_effects/014_cannibalism_unification_effects.txt:519-577`).
- Later human-donor handling also performs `change_tag_from` before annexation (`common/scripted_effects/014_cannibalism_unification_effects.txt:725-733`).
- The original ZZZ transformation remains in place. It changes control from a human primary donor only when the existing ZZZ host is AI; an already human ZZZ remains the same player-controlled country. It does not create a replacement ZZZ, reload its OOB, or delete its existing units, templates, research, ideas, equipment, or zombie profile.
- Public Hannibal identity is still revealed before the cosmetic tag, public leader, focus overlay, decisions, or reports become available. No pre-reveal CBL/Wendigo identity leak was found.

### Technology, ideas, units, recruitment, and additive inheritance

- `union_compatible_researched_technologies_from_donor` remains additive and is called before donor annexation for opening CBL, later ordinary donors, and the primary Wendigo donor. It adds only missing compatible researched technologies and preserves the recipient's mutually exclusive industry branch.
- Warlord and inherited templates are created once and locked. Scripted paid recruitment remains separate from ordinary queue recruitment.
- Starting warlord units, ordinary scripted recruitment, CBL inherited recruitment, origin specialists, and Wendigo Pack spawns still use zero starting equipment and zero starting manpower. They therefore reinforce from the paid manpower pool and available stockpiles.
- The canonical consumption helper remains the only Event 014 population transaction in the audited recruitment paths. It requires a controlled, usable state, requests an exact population amount, records the loss through the shared Deaths-aware path, and accepts only an exact applied result before crediting Larder/manpower or creating units.
- No receipt sampler calls the population/Deaths helper. Enemy military casualties therefore do not also increment Deaths.
- Route knowledge, origin knowledge, Larder, Frenzy, hierarchy, alignment, operational profiles, ideas, and route AI remain inherited rather than replaced with a generic package.

### Wendigo Pack and receipt-backed muster

- Both `history/units/ZZZ_weaponized_1936.txt:180-203` and `ZZZ_weaponized_hardened_1936.txt:180-203` define the original Wendigo Pack with exactly sixteen `wendigo_zombies` battalions and no support companies.
- `common/scripted_effects/014_cannibalism_focus_closure_effects.txt:329-351` adds recon, engineer, and logistics support in separate flag-guarded stages. None of the stages changes the sixteen battalions; rerunning a stage does not add the same support company again.
- Inherited-origin support upgrades at `:353-391` require the corresponding learned origin, require the existing named template, and use one-time stage flags. They do not create or unlock a missing template.
- The transformed host receives the inherited templates through the established template-creation helper and locks them before the focus stages can upgrade them.
- The receipt muster at `common/scripted_effects/014_cannibalism_focus_closure_effects.txt:276-323` requests exactly the constant-backed 100K people, requires the canonical exact-applied result, deducts one receipt, Larder, infantry equipment, and support equipment, credits the configured 50% manpower pool, and creates exactly one zero-start Pack. It records one Pack only after the transaction succeeds and applies both state and actor cooldowns.
- The latest localisation uses live constant tokens for receipt cost, 100K population, Larder, infantry equipment, support equipment, manpower factor, receipt thresholds, and operation durations. The visible receipt-muster text now matches the implementation's exact-payment and zero-start semantics. The capacity statement remains incorrect only because of the mixed-batch P1 above.

### Commander and inherited-origin stages

- The captain stages iterate existing army leaders only. They accept inherited `cannibalism_host_commander` or `cannibalism_bound_servant` characters, explicitly exclude `ZZZ_hannibal_wendigo`, and contain no `create_corps_commander` or `create_field_marshal` effect.
- Stage two removes the earlier bound-captain trait before applying the winter-captain trait, so the two stage traits do not stack. Stage flags make the package idempotent, and the transformation pulse refresh covers later inherited commanders.
- No country-leader or Hannibal role is altered by these commander stages.

### Cores, localisation, flags, portraits, AI, focuses, and secrecy

- Absorbed incarnation states still receive the real CBL/ZZZ destination core before the reusable source core and slot metadata are removed. Conquered non-origin territory is not granted automatic cores.
- The previously checked CBA–CBH and CBL country/ideology/party localisation remains complete. New decision, focus, trait, modifier, and tooltip keys inspected in the closure localisation resolve, and the file retains UTF-8 BOM.
- Required CBA–CBH/CBL, CBL route-cosmetic, and `ZZZ_CANNIBALISM_HANNIBAL` flag families remain present across regular, medium, and small sizes. Registered Event 014 portrait references inspected in `interface/014_cannibalism.gfx` still resolve to existing DDS files.
- Missing DDS work elsewhere in the focus-closure asset tranche is not treated as a country-package defect unless it makes one of these audited identity surfaces invisible. No such visibility break was found here.
- Origin AI, unified route AI, Wendigo AI, focus loading, reveal gating, and cleanup of reusable-slot route/origin state remain wired. The only cleanup failure found is the per-enemy receipt runtime identified above.

### Targeting scope and cadence

- All six unified targeted decision blocks call `cannibalism_unified_scored_target_is_valid_from_decision` in both target and visibility gates, with their target-specific trigger scoped through FROM.
- Wendigo terminal-hunt launch and inherited-cell targeting call `cannibalism_wendigo_scored_target_is_valid_from_decision` in both gates.
- The two MTTH entries use the mirrored decision-scope wrappers. The scorer validity, decision validity, and relationship checks now agree.
- Scorers are invoked for bounded one-shot targeting. Enemy receipt sampling runs from the existing Event 014 transformation pulse and uses `every_enemy_country`; no new `on_daily`, `on_weekly`, `on_monthly`, or recurring whole-world country scan was added.

### Route break and terminal lock

- Route break and terminal lock clear the Wendigo operation runtime without deleting ZZZ, its existing territory, original Pack, inherited templates, paid formations, commander traits, technology, public identity, or retained Event 2 mechanics.
- Final lock still occurs through the Wendigo transformation pulse rather than a focus directly setting world-end state.
- The receipt actor flags/pool are cleared on closure. Per-enemy receipt-state cleanup remains incomplete as described in the second P1.

## Simplifications, omissions, and blockers

No fallback, placeholder, skipped origin, skipped route, generic replacement country, missing AI route, free starting-fill substitute, missing country localisation family, or missing country-identity asset family was found.

Completion is blocked by:

1. the ordinary two-Pack payment path authorising a batch that can cross the shared capacity after a receipt-backed one-Pack muster; and
2. receipt snapshots and remainders surviving inactive-enemy periods and shutdown, allowing later credit for casualties outside the promised active-enemy window.

The P3 scorer comment should be corrected in the same closure tranche because its reversed scope description directly contradicts the executable fix.

## Re-audit conditions

Country-package completion should be reconsidered only after all of the following are evidenced:

- a mixed one-Pack/two-Pack muster sequence stops exactly at capacity and never pays population/Larder when the full batch will not fit;
- a continuous enemy relationship records only positive post-snapshot deltas within per-enemy and pool caps;
- peace or loss of enemy status invalidates that sampling epoch, and a later war establishes a fresh non-retroactive snapshot;
- route break and terminal lock clear both actor-owned and sampled-enemy runtime without a whole-world recurring scan;
- the six unified and two Wendigo targeted decision blocks still use the corrected scope wrappers after remediation.

## Skills used

- `chaos-redux-events`
- `chaos-redux-subagents`
- `hoi4-focus-trees`

No skill was created or updated.
