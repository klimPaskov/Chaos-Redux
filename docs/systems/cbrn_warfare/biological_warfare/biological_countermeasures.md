# Biological Countermeasures

The active flow combines the owner's A12 direct hospitals, quarantine, separate antibiotic actions, and vaccination with optional national preparedness, surveillance, international relief, and finite state treatment accepted under the later preservation instruction.
The Disease Containment Board and intensity-banded sustainment missions have no active decision entry points.
See [the restoration comparison](../../../plans/biowarfare_restore_comparison_2026-10-12.md) for historical restoration evidence.

## Active direct-response contract

The owner's preservation instruction retains recent exact-state lifecycle protections behind the restored direct decisions.
Field hospitals remain one map action costing 10 Command Power and 150 Support Equipment, with an eight-day deployment.
Quarantine remains one map action costing 10 Political Power, with a fifteen-day deployment.
Neither requires Medical Capacity, an assigned division, a board, or another setup action.

Selection records the ordering country and the state's current ordinary-outbreak cycle.
Expiry checks that country, current controller, surviving ordinary episode, cycle, and normal civilian eligibility before applying the response.
Canceled or stale orders clear only their original provider's receipt.
Lifecycle cleanup also clears these receipts when the last ordinary episode ends, and a later outbreak receives a new cycle.
The historical payment remains spent on cancellation, with no added fee or invented refund.

State modifier burdens are rebuilt from intensity, medical saturation, and current response on every refresh, then the historical hospital, quarantine, national-treatment, vaccination, and zombie-prevention reductions apply once.
Their remaining multiplier is `max(0, min(1, 1 - total_reduction))`.
Field Hospital IV plus quarantine retains its historical 70% reduction, leaving 30% of the rebuilt burden.
Overlapping measures can remove that remaining penalty but cannot reverse its sign into a state benefit.
The modern growth, death, medical-load, detection, and spread multipliers retain their separate `cbrn_hazard_budget.residual_floor` of 50% after foundational agent treatment.
That hazard floor does not replace the historical state-penalty reduction.

### Private helper contracts

| Helper | Scope and inputs | Output and side effects | Call sites and cleanup |
| --- | --- | --- | --- |
| `bio_countermeasure_record_direct_field_hospital_order` | State, `ROOT` is the ordering country. Requires a controlled eligible detected ordinary episode and its existing cycle, with no hospital or pending order. | Sets pending, provider, and cycle receipts. Writes temporary `bio_direct_field_hospital_order_recorded = one` only on success, so the caller initializes it to zero. Reserves no capacity or equipment. | `deploy_field_hospitals.complete_effect` records before the existing payment. |
| `bio_countermeasure_direct_field_hospital_order_is_current` | State, same ordering country. Checks pending/provider/cycle, control, normal civilian eligibility, and an ordinary episode. | Read-only predicate. Rejects capacity-backed legacy receipts. | Hospital completion and cancellation. |
| `bio_countermeasure_clear_direct_field_hospital_order` | State, same ordering country. No defaults. | Clears pending/provider/cycle only when the provider matches and no legacy capacity receipt exists. No refund or active-hospital removal. | Hospital expiry and cancellation. Last-episode lifecycle cleanup already owns the same fields. |
| `bio_countermeasure_record_quarantine_order` | State, ordering country in `ROOT`, existing cycle. | Stores pending/provider/cycle without another payment. | Direct quarantine selection reuses this existing helper. |
| `bio_countermeasure_quarantine_order_is_current` | State, ordering country in `ROOT`. | Existing episode/provider/controller check also requires normal civilian eligibility. | Direct quarantine expiry and cancellation. |
| `bio_countermeasure_clear_owned_quarantine_order` | State, ordering country in `ROOT`. No defaults. | Calls the existing order cleanup only for that provider. No refund or removal of another active response. | Quarantine expiry and cancellation. |
| `reduce_contamination_effects` | State, freshly rebuilt pathogen modifier variables and existing protection flags/effectiveness values. | Scales those variables once by the bounded historical remaining multiplier. No stock debit, persistent target, or lifecycle intensity change. | `bio_lifecycle_refresh_state_modifiers` after all four detected-agent baselines are rebuilt. |

These helpers introduce no global event target, tuning constant, recurring hook, UI key, or asset.
The restored decision IDs and sprites remain their consumers.
Possible future response extensions should reuse these episode receipts without adding a required staging step.

## Optional response depth

These six decisions use the existing board-free category and never gate direct hospitals, quarantine, or raids.
National preparedness remains limited by researched technology and room below the existing capacity ceiling.
Surveillance start and stand-down replace one another according to the network's current state.
International relief and antibiotics appear only on eligible outbreak states, with one combined treatment card rather than one card per pathogen.

| Decision | Payment or commitment | Timing | Distinct result |
| --- | --- | --- | --- |
| `bio_expand_medical_capacity` | 50 PP, 120 Support Equipment, 40 Trucks, with the existing Black Friday quote where applicable | 90 days | +20 Medical Capacity for response and optional medical teams |
| `bio_expand_biosecurity_capacity` | 50 PP, 80 CBRN Instruments, 80 Support Equipment | 90 days | +20 Biological Security for the lifecycle response |
| `bio_activate_surveillance_network` | 40 PP, 80 CBRN Instruments, 60 Support Equipment, 10 Medical Capacity committed, and 20 Trucks on hand without consumption | 60 days | +25 Surveillance and +10 evidence when an outbreak is detected |
| `bio_stand_down_surveillance_network` | No extra payment | 30 days | Removes the network and returns its 10 committed Medical Capacity once |
| `bio_request_international_medical_mission` | 30 PP, 50 Support Equipment, 25 Trucks, 8 Medical Capacity committed, and 20 Instruments on hand without consumption | 14 days | +15 Surveillance, Containment, and Medical Response, with a public-evidence and hidden-program disclosure tradeoff |
| `bio_distribute_antibiotics` | 10 PP, 50 Support Equipment, 20 Trucks, and 5 Medical Capacity committed once per state | 3 days | Agent-specific growth and mortality treatment, capped at three courses per episode with a 45-day cooldown and weaker courses after the first |

The national antibiotic ideas provide factory-scaled state-burden protection automatically.
The optional state courses separately activate the modern lifecycle growth and mortality multipliers.
The national ideas do not establish a course receipt or consume a medical team's capacity on their own.

National investment and surveillance selection recheck current affordability and normal civilian eligibility.
Paid or activation receipts guard delayed completion, and canceled activation returns only its recorded capacity commitment.
International and treatment orders retain the exact provider and outbreak or agent episode, so changed control, a later episode, or a nonhuman controller cannot turn an earlier payment into a new treatment.
A canceled international order returns its own eight-point capacity reservation once, while consumed PP and equipment remain spent.
Antibiotic cancellation clears only that provider's pending orders, preserves already active treatment, and returns its five-point team commitment only when no active or pending treatment remains.

## Purpose

The biological countermeasure system turns surveillance, containment, treatment, vaccination, and international assistance into resource-backed national and exact-state actions.

Ordinary Anthrax, Plague, Tularemia, and Smallpox outbreaks use this system through the shared biological lifecycle.

Weaponized-zombie systems remain separate.

No countermeasure helper infers a target state, substitutes an unrelated equipment type, or runs a recurring all-country pass.

## Canonical agent model

Overall weapon strength is `Tularemia < Anthrax < Plague < Smallpox`.

Tularemia is low severity, Anthrax is moderate, Plague is serious, and only Smallpox belongs to the severe weapon tier.

Agent strength controls lifecycle harm, persistence, medical load, spread, and death potential.

Native strategic-raid delivery reliability is a separate operational axis.

All four ordinary agents use the same strategic-raid base factors: 0.50 success, 0.12 critical success, and 0.10 disaster.

Countermeasure AI may respond more urgently to a stronger agent, but agent identity never changes the raid's native delivery chance.

## National capacities

`cbrn_medical_capacity` represents organized Medical Countermeasure Stores and response personnel.

`cbrn_biological_security` represents secure handling, laboratory control, detection discipline, and epidemiological readiness.

Both values are bounded from 0 to 100.

Uncommitted Medical Capacity and Biological Security contribute half their current value to the shared outbreak response calculation.

The national investment decisions create these capacities from real equipment instead of granting a free baseline.

Where a response pays trucks, its generic motorized requirement spends the oldest available model first from the real stockpile, using the same whole-truck price shown to the player.

| Investment | Immediate cost | Duration | Completion |
| --- | --- | --- | --- |
| Expand Medical Countermeasure Stores | 50 Political Power, 120 Support Equipment, 40 Trucks | 90 days | +20 Medical Capacity |
| Expand Biological Security Capacity | 50 Political Power, 80 CBRN Instruments, 80 Support Equipment | 90 days | +20 Biological Security |

An investment can begin only when the full 20-point gain fits under the normal capacity ceiling.

During Event 026's Black Friday sale, Medical Countermeasure Stores uses the discounted Political Power, Support Equipment, and truck quote for its availability check and payment. The displayed sale prices are sufficient when owned exactly; ordinary prices apply outside the sale.

The investment totals are gameplay tuning rather than historical estimates.

## Surveillance

Activating the Biological Surveillance Network consumes 40 Political Power, 80 CBRN Instruments, and 60 Support Equipment. It requires 20 Trucks on hand without consuming them.

It also commits 10 Medical Capacity for the life of the program.

After 60 days, the network adds 25 Surveillance to every ordinary-pathogen response in the country.

When an agent is detected, the network adds 10 evidence points to that exact agent record.

Standing the network down takes 30 days and restores the committed 10 Medical Capacity.

The program's continuing national idea imposes 3% Consumer Goods and -5% Political Power Gain.

## Exact-state field hospitals

Field hospitals use the direct action and episode receipts in the active contract above.
Their existing 20% to 50% hospital-grade reduction scales the rebuilt state burden, and the deployed flag adds the lifecycle's Medical Response and reduces deaths and medical load.
No Medical Capacity reservation belongs to this direct route.

## Exact-state quarantine

Quarantine uses the direct action and episode receipts in the active contract above.
Its 20% state-burden reduction accompanies the lifecycle's improved containment, detection, and cross-state spread prevention.
The existing quarantined-state modifier retains construction, factory, resource, supply, and resistance tradeoffs.
The quarantine clears when no ordinary episode remains, while independent Black Plague measures retain their own ownership.

## Bilateral border controls

Border closure is an exact relationship between the acting country and one infected neighbor.

It records the neighbor in `closed_bio_borders`, blocks market access and volunteer deployment through the existing relation-rule override, and reduces lifecycle spread across that exact border.

Either side's recorded closure is sufficient to reduce spread between the pair.

Reopening removes only the selected bilateral record.

There is no global border-closure proxy.

The first closure starts one self-scheduled cleanup job for that country.

Every 30 days, the job checks only the country's recorded closure array, removes extinct or no-longer-adjacent targets, unregisters the relation overrides if the array becomes empty, and stops rescheduling when no pair remains.

No all-country daily, weekly, or monthly pulse is used.

## Agent-specific antibiotics

Anthrax, Plague, and Tularemia retain separate research, production, withdrawal, national protection, and treatment-course records.

The historical research, production, and withdrawal decisions retain their own pathogen prerequisites and timing.
The optional Antibiotics for a state card treats every eligible detected outbreak in that state that has a production line, under one payment and one medical-team commitment.

Confirmed attribution sets an agent-specific world-history flag, so threat availability does not repeatedly scan every country and does not reveal a secret foreign project.

The doomsday batch writes the same agent-specific public flag only for agents whose stockpile was actually consumed.

| Agent | Research penalty | Consumer Goods |
| --- | --- | --- |
| Tularemia | -15% | 8% |
| Anthrax | -20% | 10% |
| Plague | -25% | 15% |

Production takes 100 days for Anthrax, 120 for Plague, and 50 for Tularemia.
Retroactive research takes 120, 180, and 75 days respectively, and withdrawal takes 20, 30, and 20 days.

Mass production automatically supplies the matching factory-scaled state-burden protection.

An optional treatment course supplies the separate lifecycle growth and mortality protection to one controlled state with an eligible detected outbreak.

Each course consumes 10 Political Power, 50 Support Equipment, and 20 Trucks.

The first dispatched course in a state immediately commits 5 Medical Capacity, preventing parallel courses from overcommitting the national reserve.

The targeted decision's cost hover states whether this course makes a new Medical Capacity commitment or uses the medical team already committed in that state.

The commitment remains while at least one Anthrax, Plague, or Tularemia treatment course is active or in transit in that state.

It returns to the recorded provider when the last treated agent recovers or when the last paid course cannot arrive.

Political Power and consumed equipment are never refunded.

Each agent has a separate course counter and 45-day cooldown.

At most three courses may be sent for the same agent during one state episode.

Every in-transit course stores the original provider and the exact agent episode count.

A course can arrive only if both records still match, so a paid order from an earlier episode cannot attach to a newly seeded outbreak of the same agent.

Courses after the first use weaker agent-specific growth and death multipliers, representing diminishing emergency effectiveness without fabricating drug resistance as a new agent.

## Smallpox vaccination

The historical Smallpox program consumes 150 Political Power and takes 180 days to begin, with its original live-threat visibility and 30-day withdrawal.
It reserves no Medical Capacity and adds no equipment payment.
Its national idea supplies the existing Consumer Goods and Political Power tradeoff, while the shared lifecycle applies vaccination to Smallpox growth, spread, and deaths.
The historical state-penalty reduction applies as well.
`bio_lifecycle_prepare_legacy_antibiotic_protection` sets `smallpox_vaccination_protection_active` on a detected Smallpox state while its controller holds the program idea, with an effectiveness of controlled civilian factories times `smallpox_vaccination.weekly_per_10civ`, limited to `smallpox_vaccination.weekly_cap`.
It clears the flag and effectiveness on the next refresh after the program ends, and last-episode lifecycle cleanup clears them as well.

## Biological special projects in the ordinary outbreak lifecycle

Completed Mass Vaccine Production uses separate susceptibility factors for Anthrax, Plague, Tularemia, and Smallpox. Each matching factor reduces new exposure, intensity growth, and connected spread in the controlled state. An active Smallpox vaccination program supplies the Smallpox foundation instead of compounding a second project vaccine factor. The project does not clear an existing episode.

Completed Field Antibiotics lowers mortality for the three bacterial agents, Anthrax, Plague, and Tularemia. It has no Smallpox treatment effect. An active agent-specific antibiotic course takes precedence in that state. The project also grants its defined Field Hospital and CBRN medical detachment casualty-trickleback bonuses.

Completed Regenerative Serum improves the Medical Response contribution to intensity decline, exposed-share clearance, and medical-saturation recovery. Its national idea adds an army recovery benefit with a 2% Consumer Goods cost. Recovery still requires the scheduled outbreak lifecycle to work through the state record.

Completed Broad-Spectrum Antiserum lowers mortality only during an active ordinary-agent outbreak with a deployed field hospital, an international medical mission, or positive national Medical Capacity backed by support equipment in stock. It consumes no second shipment when the lifecycle tick runs. The project research costs resources and breakthroughs, while hospital and mission deployment retain their existing equipment and capacity commitments.

Additional growth, mortality, medical-load, and connected-spread protections share one 50% residual hazard budget after agent-specific foundational treatment. Detection improvements also retain at least half of the baseline non-detection chance. This limit prevents stacked response programs from erasing an outbreak through modifiers alone. Quarantine, border closure, response capacity, and exact-state medical commitments retain their normal costs and operational tradeoffs.

## International medical missions

An international mission targets one controlled state with a detected ordinary outbreak.

Access requires an active observer or inspection arrangement, an allied relationship recognized by the engine, or a real outward guarantee connection.

Pariah and defiance routes cannot use the mission unless the existing Condemnation system provides a compliance path.

The request consumes 30 Political Power, 50 Support Equipment, and 25 Trucks. It requires 20 CBRN Instruments on hand without consuming them.

The request immediately reserves 8 Medical Capacity on the exact state so parallel missions cannot spend the same teams twice.

The state stores the original provider and ordinary-outbreak cycle.

After 14 days, the mission becomes active only if the provider, controller, and outbreak cycle still match the original request.

If the mission cannot deploy, the reserved Medical Capacity returns to its provider, but Political Power, equipment, and supplies already spent do not.

The mission adds 15 Surveillance, 15 Containment, and 15 Medical Response to that state.

It adds 20 evidence points to each active ordinary agent record in the state and reduces the same record's concealment by 5.

The requesting country earns 8 points toward faster Condemnation recovery through international cooperation.

A country with a real biological stockpile loses attribution control and risks exposing 20% of its actual hidden biological evidence.

The mission never fabricates an offensive program or a donor country.

## Inactive sustainment mission backend

The four intensity-banded sustainment missions have no decision entry points.
Their helper definitions and cleanup remain for source compatibility, but they do not establish a player prerequisite or an active mission ladder.

## Cleanup and ownership

Every state-level Medical Capacity commitment stores the original provider country and exact committed value on the selected state.

Field hospitals, international missions, and containment missions also use explicit reservation markers, so repeated helper calls cannot debit the same capacity twice.

Delayed field-hospital, quarantine, and international orders store the state's ordinary-outbreak cycle.

Delayed antibiotic courses store the matching agent's episode count.

The shared lifecycle calls `bio_countermeasure_cleanup_state_commitments` only after the state has no remaining ordinary-pathogen episode.

Agent recovery releases an antibiotic-service commitment as soon as no other supported antibiotic course is active or in transit.

Final state cleanup restores any remaining field-hospital, antibiotic-service, and international-mission commitments to their recorded providers.

Cleanup clears the state response flags, treatment course counters, cooldowns, order records, reservation markers, and quarantine modifier.

The Black Plague response system keeps its own hospital and quarantine ownership flags.

Its cleanup cannot remove an ordinary-pathogen hospital or quarantine that still owns the shared response flag, and ordinary-pathogen cleanup preserves the shared response flag while the matching Black Plague measure remains active.

Confirmed deliberate-use attribution requires a deliberate or doomsday source record.

Evidence added to connected spread, surveillance, or international transparency can raise suspicion, but cannot relabel a spread or accident record as a confirmed attack.

Actor-independent public confirmed-use history is preserved even if the responsible country ceases to exist before confirmation.

National surveillance and vaccination commitments are restored only by their own stand-down decisions because they are national continuing programs rather than outbreak-state commitments.


The optional national medical investment uses the existing `black_friday_bio_medical_investment_paid` receipt, and the biosecurity investment uses `bio_biosecurity_investment_paid`.
Both clear the receipt on expiry or cancellation and publish no capacity gain after loss of normal civilian eligibility.
`bio_countermeasure_stand_down_surveillance_network` also clears a canceled activation's progress flag, returns committed capacity only while its commitment marker exists, and can be called repeatedly without another refund.

`bio_countermeasure_release_owned_international_mission_order` is state scoped with the ordering country in `ROOT`.
It has no optional inputs or defaults, checks the pending flag and matching provider, and then calls the existing reservation-release helper.
It neither touches a completed active mission nor refunds another country's receipt.
The international decision's stale-expiry and cancellation branches call it, while ordinary-episode cleanup owns the active mission's eventual capacity release.

`bio_countermeasure_record_antibiotic_orders` writes temporary `bio_antibiotic_order_recorded = one` only after recording a current matching order, and its decision caller initializes that output to zero before selection.
`bio_countermeasure_has_current_antibiotic_order` is a read-only state predicate over the three exact provider/agent-episode receipts and controls the one combined card's cancellation.
`bio_countermeasure_resolve_antibiotic_orders` applies only current courses, then calls `bio_countermeasure_clear_owned_antibiotic_orders`.
That state-scoped cleanup uses the ordering country in `ROOT`, clears only matching pending providers, and invokes the existing team-release helper only for the matching team provider.
It leaves active treatment and another provider's pending orders intact.

## Designer integration

Completed Biological Security Directorate and Medical Countermeasure Directorate traits enter the same exact-state lifecycle rather than a parallel response system.

Distributed Surveillance multiplies the final ordinary-agent detection chance by 1.25 before the normal detection cap.

Mobile Containment Team multiplies only the outbound spread chance of an episode whose persisted source is an exact captured-facility release by 0.75.

Vaccine Scale multiplies Smallpox growth, spread, and death pressure by 0.75 and does not affect Tularemia, Anthrax, or Plague.

Mobile Casualty Sorting multiplies biological medical-saturation growth by 0.75.

When an active international medical mission records an existing provider with International Medical Mission completed, that provider's Surveillance, Containment, and Medical Response contributions are each multiplied by 1.25.

The same trait multiplies the existing Condemnation system's calculated compliance credibility by 1.15 before its normal zero-through-one cap.

No designer trait changes ordinary-agent raid success by agent identity.

## AI profiles

AI weights distinguish agent potency, political profile, capacity, industry, and historical emergency routes without changing delivery reliability.

Chinese emergency profiles prioritize field hospitals, surveillance, exact-state treatment, and international assistance during detected outbreaks.

Democratic profiles give additional weight to surveillance, vaccination, and transparent international assistance.

Authoritarian profiles give additional weight to quarantine.

Low industry reduces willingness to undertake expensive national programs.

Low stability reduces quarantine willingness because the state resistance and economic costs are real.

Smallpox receives the greatest response urgency, Plague receives the next-highest urgency, Anthrax is moderate, and Tularemia is the lowest ordinary-agent priority.

## Runtime assets

Countermeasure decision sprites are registered in `interface/biological_countermeasures.gfx`.

Unique decision DDS files live under `gfx/interface/decisions/biowarfare/countermeasures/`.

Unique continuing-idea DDS files live under `gfx/interface/ideas/biowarfare/countermeasures/`.

The registered package sprites include the active consumers and retained unused quarantine and sustainment artwork:

- `GFX_decision_bio_expand_medical_capacity`
- `GFX_decision_bio_expand_biosecurity_capacity`
- `GFX_decision_bio_activate_surveillance_network`
- `GFX_decision_bio_quarantine_state`
- `GFX_decision_bio_border_control`
- `GFX_decision_bio_anthrax_antibiotics`
- `GFX_decision_bio_plague_antibiotics`
- `GFX_decision_bio_tularemia_antibiotics`
- `GFX_decision_bio_international_medical_mission`
- `GFX_decision_bio_sustain_containment`
- `GFX_idea_bio_surveillance_network`
- `GFX_idea_smallpox_vaccination`

The existing `GFX_decision_deploy_field_hospitals` and `GFX_decision_biowarfare_smallpox_vaccination` sprites remain in use and are not overwritten.

The source, processed previews, final DDS files, contact sheet, manifest, and visual inspection record live under `docs/assets/chaos_warfare_system/stage_7_biological_countermeasures/`.

No raid icon in `gfx/interface/military_raids/` is removed or overwritten by this package.

## Tuning sources

National and state response costs, commitments, durations, modifiers, treatment curves, and AI factors live in `common/script_constants/biological_countermeasure_constants.txt`.

The 45-day timed antibiotic cooldown uses a file-local `@BIO_ANTIBIOTIC_COURSE_COOLDOWN_DAYS` token because the current timed-state-flag parser requires a literal-compatible token.

It is mirrored by `bio_countermeasure_timing.antibiotic_course_cooldown_days` in the central tuning file.

Canonical agent strength, lifecycle growth, spread, mortality, detection, doctrine, and countermeasure multipliers remain in `common/script_constants/biological_lifecycle_constants.txt`.

Strategic-raid operational probability remains file-local in `common/raids/biological_raids.txt` because the native raid parser consumes those `@` values in the same file.

## Future plans

Future extensions may add agent-specific vaccination technology for non-Smallpox threats if a numbered specification promotes that surface.

Future international missions may gain named contributor records if a verified current-version engine hook can expose the actual contributing country without inference.

Future treatment tooltips may display exact state commitments and remaining course counts without a required board or staging step.
