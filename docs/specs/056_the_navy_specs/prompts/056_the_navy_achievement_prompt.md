# Achievement Implementation Prompt: Event 056 The Navy

Implement the complete Event 56 achievement set from:

- `docs/specs/056_the_navy_specs/specs/056_the_navy_spec_part_7_presentation_assets_and_achievements.md`
- `docs/specs/056_the_navy_specs/specs/056_the_navy_spec_part_8_acceptance_criteria.md`

Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, and the existing Chaos Redux achievement framework. Inspect current achievement definitions, tracking patterns, localisation, root-only asset naming, and icon consumers before editing.

## Achievement 1

ID: `the_navy_from_steppe_to_sea`

Working label direction: From Steppe to Sea.

Eligible player state:

- directly landlocked when Event 56 first manifests globally
- later directly owns and controls usable coast
- receives an Event 56 package on a later firing

Unlock:

- a defining ship from that granted cohort participates in a meaningful naval victory with a real enemy loss or another reliable nontrivial threshold

Disqualifiers:

- coast exists only through a subject
- no actual package was delivered
- the qualifying battle has no granted defining ship
- an invalid stable-country transition breaks ownership proof

Ordinary ideology or cosmetic changes must not disqualify the run. Persist the first-manifestation landlocked proof through save and reload.

Difficulty: very hard.

Visibility: visible.

Icon direction: inland horizon or steppe becoming an anchor, naval bow, or wake. Do not use a literal map or flag.

## Achievement 2

ID: `the_navy_three_gifts_one_admiralty`

Working label direction: Three Gifts, One Admiralty.

Unlock:

- receive packages from three separate Event 56 firings
- all three primary identities are distinct
- use Full or Phased Commissioning for all three
- retain at least 75 percent of actually delivered combined cohort value one year after the third receipt
- win meaningful naval battles in at least two different strategic regions with defining ships from the tracked cohorts

Disqualifiers:

- choose Break Up the Package for any tracked receipt
- fall below the retention threshold
- lack reliable cohort participation or region proof

Define one bounded restart policy if an attempt fails. Do not keep an unlimited rolling history of all package triples or battles.

Difficulty: very hard.

Visibility: visible.

Icon direction: three different ship silhouettes under one admiralty star, pennant, or wreath.

## Achievement 3

ID: `the_navy_wrong_fleet_right_war`

Working label direction: Wrong Fleet, Right War.

At package receipt, evaluate a small registered set of objective mismatch predicates before the new ships change the country's posture. Supported mismatch directions include:

- carrier package with no operational carrier arm or active carrier-air support
- capital package with no capital fleet and severe fuel or port limits
- invasion-support package with no amphibious force or active invasion preparation
- submarine package for an overwhelmingly surface-oriented navy with no submarine arm
- convoy-escort package for a country with almost no overseas naval activity or convoy pressure

Unlock within 540 days by one reliably provable result with direct cohort participation:

- sustained naval supremacy in a contested strategic region
- successful naval invasion supported by granted ships
- sinking meaningful enemy capital value
- defeating a materially stronger enemy task force with the cohort in a central role

Choose only result checks the engine and shared systems can prove safely.

Disqualifiers:

- choose Break Up the Package
- fail to commission the defining core
- finish without cohort participation
- exceed the deadline

Difficulty: hard.

Visibility: visible.

Icon direction: a mismatched naval silhouette or tool redirected toward a victory symbol. Avoid comic treatment.

## Tracking standard

Use bounded country and cohort facts. Do not create a permanent per-battle or per-ship ledger. Tracking must survive save and reload, clear on invalid country transitions, and distinguish ships granted by Event 56 from pre-existing ships.

Use the same package identity and cohort proofs as the event. Do not duplicate parallel origin systems.

Implement explicit success, failure, deadline, disqualifier, and cleanup behavior. Prevent unlocks from harmless battles, subject-only coastline, cancelled tranches, converted hulls, or ships unrelated to Event 56.

## Localisation and icons

Write final achievement titles, descriptions, requirements, progress text, and failure tooltips from the specification direction. Do not copy working labels blindly if better final wording fits the existing achievement tone.

Coordinate with the Event 56 asset package for all three icon triplets. Achievement files must use the exact final IDs and the repository's root-only asset convention.

## Validation

Test each achievement through positive and negative scenarios, including save and reload, cosmetic changes, subject coastline, breakup, delayed delivery, destroyed ships, unrelated naval victories, expired deadlines, and distinct strategic regions.

Document the tracking state, final IDs, localisation keys, icon paths, meaningful validation, and any unresolved engine limitation. Do not weaken a condition because it is difficult to prove without reporting and resolving the design impact.
