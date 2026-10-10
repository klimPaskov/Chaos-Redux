# Event 080: Decision and mission prompt

Implement and audit Airship's operations using `chaos-redux-decisions-missions` and the complete seven-part source spec. Read the implementation handoff, validation matrix, and current owner contracts. Preserve the event's three headline values: Condition, progress, and people aboard.

## Phase map

Underway, expose standing orders, next-stop assistance, and a currently eligible experiment. At a stop, expose repair, passenger handling, eligible experimentation or refit, and departure; the host's reception choice arrives as its own event. An emergency replaces routine choices with landing, a valid diversion, or a warned continuation. Missing contact shows the bounded search work. After a crash, flight choices vanish and the rescue controller receives actual rescue work. Shared fire recovery remains in its owner interface.

The host receives only its relevant reception, service, inspection, crowd-control, or rescue choices. The United States controls expedition policy and its own payments. Other observers may view the public map without acquiring controls. Keep three to five main actions per phase, a hard maximum of six, and one to three relevant missions. Use variants and filters instead of an always-visible long decision list.

## Required services and commitments

Implement basic scheduled service once per actual visit and the four services from Part 2: patch repair, major repair, specialist inspection, and pre-crash emergency evacuation, plus the poor-field variant. Provision shortages and longer public programmes are options inside their story and reception events, not standing decisions. Apply the baseline, Grand Tour, and Flying City material scaling exactly once. Show real cost and capped Condition benefit before payment.

Implement Grand Tour refit, experimental-suite installation, Flying City refit, and all four trial-family commitments from Part 5. A physical refit needs a capable actual stop and its Condition prerequisite. Trial progress uses actual completed flight steps. Only one trial is active, at most four are committed, and each family can earn its successful reward once.

Implement post-crash rescue as the separate people-based work order in Part 4. It costs 25 motorized equipment and 25 support equipment for each started group of 600 living people requiring rescue, without the physical-form service multiplier. Smaller assistance must show how many people it covers.

## Timing and ownership

Departure is position 0. Every uninterrupted route transition takes two days, with success at 121 after 242 days. Scheduled routine stop activity fits its ordinary window. Only a declared extension adds time. Preserve partially consumed travel time through repair, inspection, search, and other holds. A mission cannot accidentally create a second route scheduler or advance the map while repair is underway.

Implement the repair, missing visitor, contact restoration, ship search, ground rescue, passenger release, and five-flight-step trial missions from Part 2. Use their real durations, response defaults, outcomes, and terminal cancellation rules. The one-day urgent response window is explicit because the ongoing flight step is only two days. Expiry must execute the displayed valid default once in multiplayer.

Transfer undelivered ground work to a new controller only through a valid consent and ownership transaction. Preserve delivered help and actual rescue credit. The original impact controller remains the war target even if the rescue controller changes. A recent host's missing-visitor work can continue after the airship departs, without restoring its flight controls. Unresolved missing cases are presumed lost only when the voyage closes.

## Costs and affordability

Use real stockpile, fuel, Political Power, and Air Experience costs where specified. Keep each action at four or fewer spendable resource types, with at most three inline cost entries and any remaining cost in the hover treatment.

The available and custom cost triggers must share inclusive affordability. Exactly the displayed resources are enough. One payer is debited once, inputs are reset correctly for each shared helper, and benefits occur only after the work is actually delivered. Expose a useful AI Political Power cost hint where the framework requires it, without substituting PP for the physical price.

Cancellation, interrupted control, failed delivery, and terminal events must follow one declared refund policy. Do not permit repair benefits before a refund, repeated embarkation transfers, repeated stop rewards, or trial rerolls by reopening an action. A disabled button is not proof that the hidden effect has a valid guard.

## AI and event choices

Audit all American policies, host responses, emergency options, trial choices, searches, release work, and safe-abort decisions. The AI should repair before known difficult stretches, avoid unnecessary over-repair, stop optional trials when damaged, and use partial real assistance when a full package is unaffordable. Low opinion by itself is not a default order to destroy a civilian ship.

Have `chaosx_ai_probability_auditor` evaluate the complete contextual pools; `ai_will_do` scores are preferences, not click probabilities. Cover loops, expiry, recurring visits, changing hosts, and terminal cleanup.

## Acceptance

Deliver a phase decision map, mission ownership map, costs and inclusive-boundary evidence, tested cancellation and controller-transfer cases, complete AI review, localisation keys, correct icons, and matched native UI evidence. Trace all sixty story situations into actual eligibility and outcome surfaces without adding sixty permanent menu entries.

Keep shared disaster recovery, Deaths registration, event history, and war authority under their owners. Report any missing required owner contract. Do not label a decision complete because it has a visible button while its actual outcome or required resource validation remains unimplemented.
