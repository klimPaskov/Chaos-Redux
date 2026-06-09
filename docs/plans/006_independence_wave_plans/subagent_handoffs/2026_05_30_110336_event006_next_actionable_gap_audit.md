# Event 006 Next Actionable Gap Audit

Date: 2026-05-30 11:03 UTC
Scope: read-only audit for the next bounded Event 006 Independence Wave implementation gap.

## Bottom Line

The highest-value next gameplay gap is the missing major-power side of the Patronage and Recognition loop. Current Event 006 implementation has a working breakaway-facing Patron Ledger, Congress actions, Formation Ledger paths, Border Commission, and Dossier Board first layer, but there is no major/regional-power decision family that lets outside powers recognize, arm, missionize, pressure, or sabotage Event 006 releases.

Recommended next tranche: implement `independence_wave_patronage_recognition_category` or equivalent major-power decision family using targeted decisions over `global.independence_wave_released_countries`.

This can be implemented without touching flag assets, `common/countries`, `history/countries`, or Event 005 systems.

## Completion Status By Surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Instant release and origin routing | Implemented/active, not re-audited for runtime | `events/006_independence_wave.txt` runs the release loop and calls Event 006 setup; current event doc says releases receive `chaosx_release_origin_independence_wave`. |
| Dossier Board | First decision-category layer only | Current host actions are recognition, observers, dossier talks, archive evacuation, and capital ministry in `common/decisions/006_independence_wave_decisions.txt:36`. Spec expects wider host tools at `006_independence_wave_spec.md:484`. |
| New States Congress | Recently expanded | Mutual guarantee, volunteer cadre, arms pool, anti-puppet clause, and compact delegate work exist in `common/decisions/006_independence_wave_decisions.txt:408`. |
| Patron Ledger | Breakaway-facing layer implemented | Six breakaway decisions exist in `common/decisions/006_independence_wave_decisions.txt:251`; docs describe this as anti-patron management in `docs/events/006_independence_wave.md:46`. |
| Major-power patronage | Missing | Spec requires major/regional power category at `006_independence_wave_decisions_ai.md:308` and major decisions at `006_independence_wave_decisions_ai.md:396`; repository search found no implemented major-power category or decision ids. |
| Formation Ledger | Active but still partial | Regional compact and several package paths exist under `common/decisions/006_independence_wave_decisions.txt:565`; future package depth remains documented in `docs/events/006_independence_wave.md:137`. |
| Strange/Sealed Dossier | Missing as gameplay | Generic strange package flags/types exist, but no Sealed Dossier decisions, containment review, Unmarked Congress, or Quiet Dead mission were found; spec requires that category at `006_independence_wave_decisions_ai.md:312`. |
| Scripted GUI/assets | Not recommended as next gameplay tranche | Current docs explicitly say to extend GUI only after stable decision data at `docs/events/006_independence_wave.md:140`. Flag/image assets are out of scope by user correction. |

## Primary Gap: Major-Power Patronage Decisions

Source requirement:

- `006_independence_wave_spec.md:522` defines "Major power decision family: Influence the Petitions" with observers, newspapers, rifle supply, recognition pledge, patron cabinet demands, threats, host-border guarantees, autonomy brokering, and rival-patron sabotage.
- `006_independence_wave_decisions_ai.md:308` requires "Patronage and Recognition" for majors and regional powers.
- `006_independence_wave_decisions_ai.md:400` through `:409` gives implementable decision rows: `Recognize the Committee`, `Supply Rifles Through the Port`, `Offer a Military Mission`, `Demand Cabinet Seats`, `Guarantee the Existing Border`, `Broker an Autonomy Settlement`, `Sabotage Rival Patron`, `Recognize the League`, `Arm the Loyalists`, and `Threaten Non-Recognition`.
- `006_independence_wave_decisions_ai.md:500` says the Patron Ledger's AI equivalent should include sponsor and target decisions, but only target/breakaway decisions currently exist.

Current implementation evidence:

- `common/decisions/006_independence_wave_decisions.txt:251` implements only breakaway-side Patron Ledger actions: accept advisers, balance patrons, expose broker, reject clauses, request arms corridor, and convert loans.
- `rg` found no Event 006 major-power decision category or decision ids for recognizing committees, supplying rifles as a major, demanding cabinet seats as a sponsor, brokering settlements, or sabotaging rival patrons. The only "military mission" hit is localisation for a focus/route string, not a major-power decision.
- Existing `global.independence_wave_released_countries` and Event 006 release gates already support targeted decisions, as shown by Congress decisions at `common/decisions/006_independence_wave_decisions.txt:464` and `:495`.

Bounded implementation shape:

- Add category: `independence_wave_patronage_recognition_category` in `common/decisions/categories/006_independence_wave_categories.txt`.
- Add targeted decisions in `common/decisions/006_independence_wave_decisions.txt` over `global.independence_wave_released_countries`.
- Start with three or four high-value actions:
  - `independence_wave_major_recognize_committee`
  - `independence_wave_major_supply_rifles_through_port`
  - `independence_wave_major_offer_military_mission`
  - `independence_wave_major_demand_cabinet_seats`
- Add scripted triggers/effects in `common/scripted_triggers/006_independence_wave_triggers.txt` and `common/scripted_effects/006_independence_wave_effects.txt`.
- Add constants under `independence_wave_decision` in `common/script_constants/006_independence_wave_constants.txt`.
- Add localisation to `localisation/english/006_independence_wave_l_english.yml`.
- Update `docs/events/006_independence_wave.md` after implementation facts exist.

Safety requirements:

- Gate actor as major or regional power, not Event 006 release unless intentionally supporting another release.
- Gate target with `is_independence_wave_release = yes`, `exists = yes`, `is_subject = no` where appropriate, and Event 005 exclusion inherited from `is_independence_wave_release`.
- Costs should use PP, command power, infantry/support equipment, convoys for port supply, army XP for military missions, and relationship/ideology/war-state AI weights.
- Effects should update target variables already used by Patron Ledger: `independence_wave_patron_leverage`, `independence_wave_foreign_attention`, `independence_wave_legitimacy`, `independence_wave_militia_strength`, and `chaosx_iw_patron_accepted` where relevant.
- Do not create factions, puppets, flags-as-assets, country files, history files, or Event 005 links in this tranche.

## Other Recommended Gaps

1. Extend the Dossier Board with host suppression and loyalist decisions.
   Evidence: spec requires suppression, loyalists, autonomy, guarantees, and trade district hooks at `006_independence_wave_spec.md:488`; current host category has only five actions/missions at `common/decisions/006_independence_wave_decisions.txt:36`. This is good, but lower priority than major patronage because the host already has a first usable layer.

2. Add a Sealed Dossier/strange containment first pass.
   Evidence: spec requires a `Sealed Dossier` category at `006_independence_wave_decisions_ai.md:312` and strange containment split at `:330`; current implementation has only generic strange package flags/types and no containment decisions. This is valuable but riskier because true strange packages still need design/assets, so it should remain behind explicit high-chaos gates and avoid final super-event claims.

3. Expand Committee Survival with recognition probation, diaspora committees, elections, and directorate security.
   Evidence: source spec lists these at `006_independence_wave_spec.md:506`; current Committee Survival has recognition, brigades, and depot seizure only at `common/decisions/006_independence_wave_decisions.txt:162`. This is bounded and useful if the parent wants to deepen the release-country player loop before adding outside-power agency.

## Accepted Plans And Disposition

- `006_independence_wave_instant_release_correction_handoff.md`: implemented in current architecture; do not reintroduce pre-release dossier delay.
- `006_independence_wave_event005_separation_handoff.md`: partially implemented through origin gates; continue to avoid Event 005 files and Event 005 logic.
- `006_independence_wave_improvement_addendum_post_focus_formation_tranche.md`: partially implemented. Regional compact, Border Commission, several package overlays, Congress, Patron Ledger, and reduced-release resolver work exist. Major-power patronage, Sealed Dossier/strange packages, full package minimums, GUI, assets, and final catalog/audit closure remain open or queued.
- Recent Congress handoffs are implemented: mutual guarantees, shared arms pool, and volunteer cadre should be treated as completed tranches, not reworked unless an audit finds defects.

## Validation Performed

- Read required repo skills: `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, and `hoi4-decisions-missions`.
- Consulted required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, and scripted GUI modding.
- Consulted vanilla HOI4 documentation for effects, triggers, script concepts, localisation formatting, and decision/scripted GUI precedents.
- Searched Event 006 specs, plans, implementation files, docs, and localisation for major-power patronage, Dossier Board, Patron Ledger, Formation Ledger, Congress, and strange/Sealed Dossier surfaces.
- No gameplay, asset, country, history, flag, or Event 005 files were patched.

## Validation Needed After Implementation

- Brace balance and unsupported operator scan for all touched Event 006 script files.
- Localisation BOM and no-`:0` key scan for `localisation/english/006_independence_wave_l_english.yml`.
- Decision-target audit: major actor cannot target self, non-existing countries, Event 005-origin countries, subjects where inappropriate, or countries already locked by the same patron action.
- AI audit with `chaosx_decision_mission_auditor` after implementation, because this is a decision/mission tranche.
- Check `git status --short -- gfx/flags common/countries history/countries common/decisions/005_soviet_collapse_decisions.txt common/decisions/categories/005_soviet_collapse_categories.txt events/005_soviet_collapse.txt` to confirm forbidden surfaces were not touched.

## Asset And Documentation Gaps

- Do not route flag assets for this tranche.
- Reuse existing generic decision/category icons unless the parent explicitly opens a non-flag icon tranche.
- Update `docs/events/006_independence_wave.md` only after the major-power behavior is actually implemented.
- The open improvement addendum should eventually receive a disposition note once major-power patronage is implemented or explicitly queued.

## Remaining Blockers

- Full Event 006 completion remains blocked by unresolved package minimums, strange/containment gameplay, final GUI or formal GUI downgrade, asset/catalog/super-event depth, and final audits.
- Mapuche remains blocked until a real tag exists per current event docs; do not use it as the next tranche unless the parent separately approves tag/country work.
- PRA/railway baggage remains queued because Event 005 separation is still sensitive.

## Improvement Loop Recommendation

Do not spawn `chaosx_improvement_loop_planner` yet. The accepted post-focus/formation addendum is still open and already covers the depth gap. Implement or explicitly queue/reject the remaining addendum items before asking for another Event 006 improvement-loop plan.
