# Alien Infantry and D’Rhonda Acceptance Scenarios

## Purpose

This checklist is the parent-owned acceptance contract for the alien-infantry API, D’Rhondan contact chain, Empire of D’Rhonda country package, and reusable model package. Source review, HOI4 MCP evidence, subagent audits, and final parent review must cover every scenario before the tranche can be presented for in-game acceptance.

## Contact and project access

- A country with no contact receipt cannot produce alien laser weapons, call a landing, receive the locked cohort template, or use either alien tactic through a non-alien formation.
- An active Kruger host with the required operational work can construct `sp_dhrondan_envoy_craft`; a later-appointed Kruger host holding `antarctica_success` receives the recovered-craft bypass once.
- Event 036 evidence never completes or bypasses the craft project.
- Mengele’s eligible program can build the craft and complete its expedition without modifying Mandate, Dependence, Exposure, Independent Capacity, or Grievance.
- A future-event source receipt can grant contact without impersonating Kruger, Mengele, Event 019, or DHR sovereignty.
- Removing one contact source leaves access intact while any other positive source receipt remains.

## Kruger and Mengele expeditions

- Kruger authorization consumes exactly 50 political power and 500 fuel, applies the authorization Directorate changes once, suspends the canonical character through the obligation system, and starts a 180-day mission.
- Successful return restores the same canonical character, applies the return Directorate changes once, grants the Kruger contact receipt once, and cannot duplicate any advisor, scientist, event actor, or leader role.
- Death, host destruction, invalid transfer, cancellation, and competing obligations restore or clean the character state exactly and never award contact or Directorate power.
- Eligible AI always authorizes the expedition.
- Mengele’s parallel expedition grants only the Mengele receipt and its own program state.

## Landing conservation

- A valid state-targeted call removes exactly 2,000 `alien_laser_weapon_equipment_1`, reserves the selected state for seven days, blocks another pending call, and starts the post-landing cooldown only through the defined lifecycle. The baseline is 30 days; DHR's landing-network, guarded-descent, and near-space focus receipts reduce it to 24, 18, and 12 days respectively without altering cost, reservation time, or concurrency.
- Losing the selected state before arrival cancels the call and refunds exactly 2,000 weapons once.
- A successful landing creates one locked ten-battalion, twenty-width `D’Rhondan Landing Cohort`, consumes no human manpower or ordinary equipment, and never refunds the reserved weapons.
- The template cannot be trained, duplicated, edited, or manually deployed by the player or AI.
- A landing marks the state, records persistent history, increases Alien Presence, and adds exactly five Pact Strain.
- Existing alien formations reinforce only from alien laser weapons.
- Event 019 provider 508 grants its own receipt and landing access; provider cleanup removes only receipt 508 and does not use its former training or manpower ledger.
- Every Event 019 provider-508 request or scenario actor creates at most one cohort and one 2,000-gun debit. Automatic generation narrows only its own selected-state target, anomalous scenarios keep the shared global intensity unchanged, a successful wrapper commits state history and cooldown once, and a failed or delayed same-tag rollback deletes the exact cohort and refunds once before stockpile verification.
- `Honor the D’Rhondan Accord` costs exactly 75 political power, removes ten Pact Strain, and observes its 180-day cooldown.

## Rebellion probability

- No rebellion pulse exists below six successful arrivals, Pact Strain 30, or shared chaos 600.
- A qualifying country runs one country-scoped ninety-day pulse without a global daily, weekly, or monthly country scan.
- Six or seven arrivals at chaos 600–799 produce a ten-percent revolt chance unless a higher tier condition applies.
- Eight or nine arrivals, Pact Strain 50, or chaos 800 produce a twenty-percent revolt chance unless the top tier applies.
- Ten or more arrivals while chaos is at least 800 produce a forty-percent revolt chance.
- MCP probability evaluation and comparison use named scenarios matching these tiers and their boundary values.

## DHR formation and conservation

- First formation initializes dormant tag `DHR`, its characters, three regimes, advisors, commanders, identity, AI, decisions, and focus tree once.
- Every marked state still owned by the pact host becomes DHR-owned and controlled; a third party’s ownership is never stolen, and a lost marked state becomes a DHR claim.
- DHR receives cores on transferred territory while the origin host retains its cores for reclamation.
- The first viable marked state becomes the capital, with a deterministic viable marked-state fallback.
- Surviving host alien formations are deleted without refund, the full host alien-laser stockpile moves to DHR, and one-time expedition stores are consumed to create the initial army.
- The ordinary initial cohort grant equals `max(5, min(15, marked_states + floor(arrivals / 2)))`; each cohort consumes 2,000 weapons.
- Every disconnected transferred enclave receives at least one cohort before remaining cohorts concentrate at the capital. If more than fifteen viable components exist, each component beyond the fifteenth receives one separately recorded supplemental cohort and one matching 2,000-weapon grant; those supplemental stores cannot create additional capital cohorts.
- If DHR already exists, a later uprising joins the existing empire. Reinitialization after annexation does not duplicate characters, ideas, equipment, or one-time forces.

## Country routes and focus tree

- The focus tree contains exactly 88 focuses with category counts 8/24/10/12/8/8/12/6 and exactly eight political focuses for each regime.
- Emperor Vael IX, First Calculant Sera Qel, and Speaker Ilyr Ren routes are mutually exclusive and drive distinct identities, rewards, diplomatic behavior, expansion behavior, and AI priorities.
- No more than three focus-created national spirits coexist; each political, military, and off-world-corridor slot upgrades or replaces its prior stage.
- No focus or decision enables normal alien training or bypasses the 2,000-weapon landing price.
- Focus navigation, search filters, branch lanes, connectors, symmetry, icons, and normal-zoom legibility pass MCP render comparison.
- Origin-host reclamation, postwar integration, disconnected-enclave crises, news, Event Log history, Event Details, and existing achievement hooks remain reachable in their intended routes.
- Event 016 still has exactly four logged evolutions, no cluster, and no D’Rhondan super-event.

## Unit and asset acceptance

- `alien_infantry` and `alien_laser_weapon_equipment` are the authoritative provider-neutral unit and equipment identifiers across Event 016, Event 019, D’Rhonda, and documentation consumers.
- Battalion, equipment, and tactic values match the binding specification exactly, and both tactics require an alien-infantry unit type.
- The final Meshy input is the single approved transparent full-body reference. Native alpha failed, so the recorded background-removal fallback preserves the source soldier and has inspected clean edges.
- `alien_infantry_entity` is calibrated against vanilla infantry scale and reimports through the installed PDX exporter with packed materials.
- Idle, move, laser attack, defend, support attack, retreat, and death are genuine verified skeletal actions, not transform-only stand-ins.
- Verified laser-fire, movement, idle, and death audio has provenance, checksums, timing notes, and alien-only consumer bindings.
- Large and on-map counters match the inspected vanilla-green reference family; all equipment, technology, tactic, project, decision, event, focus, flag, country-interface, portrait, and existing-achievement assets resolve through registered sprites.

## Delivery boundary

- Each implementation tranche receives parent review before its commit.
- The context-free improvement-loop addendum is resolved, explicitly queued with a reason, or rejected before near-completion review.
- Focus-tree, decision/mission, country-package, localisation, event-completion, and AI-probability auditors return handoffs and all actionable findings are resolved or reported.
- Event 016 specs, Event 019 coverage, shared API documentation, asset/model manifests, persistent-history documentation, and the event catalog workbook agree with the shipped identifiers and behavior; catalog CSV exports are regenerated from the workbook.
- Completion remains withheld until model reimport evidence, MCP comparisons, asset resolution, auditor acceptance, and the user’s in-game acceptance exist.
