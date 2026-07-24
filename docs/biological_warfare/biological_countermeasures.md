# Biological Countermeasures

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

| Investment | Immediate cost | Duration | Completion |
| --- | --- | --- | --- |
| Expand Medical Countermeasure Stores | 50 Political Power, 120 Support Equipment, 40 Trucks | 90 days | +20 Medical Capacity |
| Expand Biological Security Capacity | 50 Political Power, 80 CBRN Instruments, 80 Support Equipment | 90 days | +20 Biological Security |

An investment can begin only when the full 20-point gain fits under the normal capacity ceiling.

The investment totals are gameplay tuning rather than historical estimates.

## Surveillance

Activating the Biological Surveillance Network consumes 40 Political Power, 80 CBRN Instruments, 60 Support Equipment, and 20 Trucks.

It also commits 10 Medical Capacity for the life of the program.

After 60 days, the network adds 25 Surveillance to every ordinary-pathogen response in the country.

When an agent is detected, the network adds 10 evidence points to that exact agent record.

Standing the network down takes 30 days and restores the committed 10 Medical Capacity.

The program's continuing national idea imposes 3% Consumer Goods and -5% Political Power Gain.

## Exact-state field hospitals

Field hospitals target one controlled state with a detected ordinary outbreak.

The deployment consumes 10 Command Power, 120 Support Equipment, 60 Trucks, and 20 CBRN Instruments when ordered.

The order immediately reserves 8 Medical Capacity on the selected state so parallel deployments cannot spend the same response teams twice.

The state stores the provider and the current ordinary-outbreak cycle when the order is placed.

After seven days, the hospitals become active only if the provider, controller, and outbreak cycle still match the original order.

An active field hospital reduces outbreak deaths and medical saturation through the shared lifecycle and adds the lifecycle's field-hospital Medical Response.

The exact state stores the original provider country and exact committed amount.

When the last ordinary episode in that state ends, cleanup restores the 8 Medical Capacity to that original provider if it still exists.

If the deployment cannot arrive, the reserved Medical Capacity returns to its provider, but Political Power, Command Power, equipment, and supplies already spent do not.

## Exact-state quarantine

Quarantine targets one controlled state with a detected ordinary outbreak.

The order consumes 25 Political Power, 10 Command Power, 80 Support Equipment, 40 Trucks, 200 Infantry Equipment, 1,000 Manpower, and 1% Stability.

The state stores the ordering country and current ordinary-outbreak cycle.

After ten days, the quarantine is established only if the provider, controller, and outbreak cycle still match the original order.

An active quarantine reduces local pathogen growth and cross-state spread while improving detection.

It simultaneously reduces state construction, local factories, resources, and supplies by 15–20% and increases resistance growth by 10%.

These tradeoffs are state modifiers because national Political Power and Stability modifiers do not belong in state scope.

The quarantine clears when no ordinary episode remains in the state.

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

Anthrax, Plague, and Tularemia each have a separate emergency-development program, continuing production idea, and exact-state distribution decision.

Emergency development does not require an offensive biological program.

It becomes available when the country detects the matching agent or when confirmed public-use history records that the matching weapon has been used.

Confirmed attribution sets an agent-specific world-history flag, so threat availability does not repeatedly scan every country and does not reveal a secret foreign project.

The doomsday batch writes the same agent-specific public flag only for agents whose stockpile was actually consumed.

| Agent | Development | Research penalty | Production preparation | Consumer Goods |
| --- | --- | --- | --- | --- |
| Tularemia | 60 days | -15% | 60 days | 8% |
| Anthrax | 75 days | -20% | 75 days | 10% |
| Plague | 90 days | -25% | 90 days | 15% |

Mass production creates national stores but does not protect every contaminated state automatically.

A treatment course must be dispatched to one controlled state with a detected matching outbreak.

Each course consumes 10 Political Power, 50 Support Equipment, and 20 Trucks.

The first dispatched course in a state immediately commits 5 Medical Capacity, preventing parallel courses from overcommitting the national reserve.

The commitment remains while at least one Anthrax, Plague, or Tularemia treatment course is active or in transit in that state.

It returns to the recorded provider when the last treated agent recovers or when the last paid course cannot arrive.

Political Power and consumed equipment are never refunded.

Each agent has a separate course counter and 45-day cooldown.

At most three courses may be sent for the same agent during one state episode.

Every in-transit course stores the original provider and the exact agent episode count.

A course can arrive only if both records still match, so a paid order from an earlier episode cannot attach to a newly seeded outbreak of the same agent.

Courses after the first use weaker agent-specific growth and death multipliers, representing diminishing emergency effectiveness without fabricating drug resistance as a new agent.

## Smallpox vaccination

Smallpox vaccination requires Integrated Epidemic Control and a real Smallpox threat.

The 180-day national program consumes 150 Political Power, 250 Support Equipment, 100 Trucks, and 50 CBRN Instruments.

It commits 10 Medical Capacity and imposes 25% Consumer Goods and -25% Political Power Gain while active.

The shared lifecycle applies the vaccination only to Smallpox.

It reduces Smallpox growth, spread, and deaths and does not alter the effects of Tularemia, Anthrax, or Plague.

Ending the program takes 30 days and restores the committed 10 Medical Capacity.

## International medical missions

An international mission targets one controlled state with a detected ordinary outbreak.

Access requires an active observer or inspection arrangement, an allied relationship recognized by the engine, or a real outward guarantee connection.

Pariah and defiance routes cannot use the mission unless the existing Condemnation system provides a compliance path.

The request consumes 30 Political Power, 50 Support Equipment, 25 Trucks, and 20 CBRN Instruments.

The request immediately reserves 8 Medical Capacity on the exact state so parallel missions cannot spend the same teams twice.

The state stores the original provider and ordinary-outbreak cycle.

After 14 days, the mission becomes active only if the provider, controller, and outbreak cycle still match the original request.

If the mission cannot deploy, the reserved Medical Capacity returns to its provider, but Political Power, equipment, and supplies already spent do not.

The mission adds 15 Surveillance, 15 Containment, and 15 Medical Response to that state.

It adds 20 evidence points to each active ordinary agent record in the state and reduces the same record's concealment by 5.

The requesting country gains 8 Condemnation decay credit through the existing compliance ledger.

A country with a real biological stockpile loses attribution control and risks exposing 20% of its actual hidden biological evidence.

The mission never fabricates an offensive program or a donor country.

## Outbreak containment missions

An outbreak containment mission targets one controlled state that already has active quarantine and either a field hospital or an international medical mission.

Starting the mission consumes 35 Political Power, 15 Command Power, 150 Support Equipment, 75 Trucks, and 40 CBRN Instruments.

It commits 10 Medical Capacity until resolution.

The reservation is guarded by an explicit capacity marker, and the mission stores the current ordinary-outbreak cycle.

The selected state's maximum current ordinary-agent intensity fixes the mission duration at the moment the mission begins.

| Maximum starting intensity | Duration |
| --- | ---: |
| Below 20 | 90 days |
| 20 to 39.999 | 180 days |
| 40 to 59.999 | 270 days |
| 60 or higher | 365 days |

The mission records the exact starting intensity and increments an exact state-owned spread counter only when that state successfully seeds a new connected outbreak during the mission.

There is no country, state, or world scan for spread accounting.

Full success requires the provider to retain at least 5 uncommitted Medical Capacity, preserve the quarantine and a field hospital or international mission, retain the final sustainment stores, prevent new outbound spread, keep control of the state, and reduce every active agent below the recorded starting maximum.

A full success consumes a final 75 Support Equipment, 30 Trucks, and 10 CBRN Instruments, lowers active-agent intensity by 15, lowers exposed share by 0.05, lowers medical saturation by 15, and grants 1% Stability.

Partial success requires the provider to retain the same Medical Capacity and final stores, keep control, prevent new outbound spread, keep at least one response measure active, and prevent every active agent from rising above the recorded starting maximum.

A partial success consumes the final sustainment stores, lowers active-agent intensity by 5, lowers exposed share by 0.01, and lowers medical saturation by 5.

Failure raises active-agent intensity by 10, exposed share by 0.02, and medical saturation by 10 in the exact mission state.

An outbreak that fully recovers before mission resolution counts as a full success without consuming unnecessary final sustainment stores.

The original provider's 10 committed Medical Capacity is restored after success, partial success, or failure.

A mission cannot resolve against a later outbreak cycle.

If the original provider ceases to exist, the exact-state lifecycle removes the orphaned mission record without creating a replacement provider or refund.

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

The runtime sprite names are:

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

Future treatment UI may display exact state commitments and remaining course counts through the existing disease-containment scripted GUI.
