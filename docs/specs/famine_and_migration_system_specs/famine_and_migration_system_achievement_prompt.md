# Achievement Prompt: Famine and Migration Mechanics

> **Current design clarification (2026-08-25):** The user clarification and accepted split implementation supersede any shared mechanic, category, or runtime-namespace wording retained below as historical design context. The current implementation uses independent `famine_*` and `migration_*` mechanics, separate famine and migration achievement namespaces where applicable, `famine_decision_category` and `migration_decision_category`, and `famine_state_map_mode` and `migration_state_map_mode`; no combined mechanic, category, runtime namespace, or mapmode is current. Use [source_of_truth_map.md](../../plans/famine_and_migration_system_plans/source_of_truth_map.md) and [completion_report.md](../../plans/famine_and_migration_system_plans/completion_report.md) for current status, including the incomplete blockers.

Use the existing Chaos Redux achievement registry and `chaos-redux-event-assets` for icon production.

These are separate mechanics with no event IDs. Use famine-owned or migration-owned achievement IDs according to the earning contract; use narrow `humanitarian_achievement_*` infrastructure only where the recorder genuinely crosses both owners.

The titles below are working labels and direction. Final localisation should be written after implementation review.

## Achievement 1: Break the Blockade

Working ID:

`famine_break_the_blockade`

Eligible countries:

Any human country that owns or controls an island state with a proven wartime blockade famine.

Unlock conditions:

- the state reaches famine or catastrophic famine through the full island-blockade proof
- the player restores a valid relief route
- the state recovers below the mortality stages
- the player does not solve the crisis through forced population removal, deliberate requisition from another famine state, or concealed mass mortality
- a meaningful share of the original threatened population survives

Disqualifiers:

- force-trigger or debug bypass
- the state becomes wasteland
- the player caused the blockade through an exploit involving its own route toggles

Difficulty:

Hard.

Why it is not trivial:

The player must preserve convoys, escort, port access, and relief capacity during active war.

Icon direction:

Relief ship entering a damaged harbor beneath a broken blockade chain. Create as an achievement triplet with separate state art, not a resized decision icon.

## Achievement 2: No One Left at the Gate

Working ID:

`migration_no_one_left_at_the_gate`

Eligible countries:

Any country receiving a foreign cohort fleeing a proven camp, genocide, exterminatory occupation, or catastrophic famine.

Unlock conditions:

- accept or arrange safe transit for every valid cohort in one major trapped-border crisis
- record no deaths from violent pushback or forced return in that crisis
- prevent the receiving network from entering catastrophic famine
- reach voluntary return, local integration, or third-country resettlement for the cohort

Disqualifiers:

- forced repatriation before origin safety
- internment or forced labor of the protected cohort
- debug launch

Difficulty:

Hard.

Icon direction:

Open border gate, shelter lantern, and civilian luggage. Avoid modern humanitarian symbols unless supported by the period reference.

## Achievement 3: Roads Home

Working ID:

`migration_roads_home`

Eligible countries:

Any origin or host country involved in a large war-driven displacement.

Unlock conditions:

- a major cohort remains displaced for a meaningful period
- the war or persecution cause ends
- restore food, housing, route, and protection in the origin
- complete voluntary return for a large majority of the return-eligible cohort
- no forced return action was used on that cohort

Disqualifiers:

- origin remains under the same active persecution profile
- return duplicates or loses population
- debug bypass

Difficulty:

Medium to hard.

Icon direction:

Families returning by rail toward repaired homes, composed as a compact achievement emblem.

## Achievement 4: Bread Across the Front

Working ID:

`famine_bread_across_the_front`

Eligible countries:

Any country that negotiates or supports a humanitarian corridor across an active front.

Unlock conditions:

- corridor connects a famine or trapped-population state to valid relief or evacuation access
- keep the corridor open for the full mission duration
- deliver enough relief or evacuation capacity to move the target below famine or trapped status
- no attack by the player against the protected corridor during the mission

Disqualifiers:

- corridor opened through force-trigger mode
- player deliberately starved the state before opening the corridor to farm the achievement

Difficulty:

Hard.

Icon direction:

Bread crate crossing a guarded bridge with white relief markings represented symbolically without generated text.

## Achievement 5: They Were Hungry, Not Contagious

Working ID:

`migration_hungry_not_contagious`

Eligible countries:

Any host country receiving a famine-displaced cohort from a state that also has an outbreak risk.

Unlock conditions:

- use controlled medical reception and avoid indiscriminate closure
- prevent a new host-state outbreak caused by the cohort
- prevent catastrophic reception overload
- reach a durable outcome for the cohort

Disqualifiers:

- cohort had no proven outbreak exposure
- internment, forced labor, or forced return
- debug bypass

Difficulty:

Medium.

Icon direction:

Shelter, food bowl, and medical screening symbol. Do not use a generic plague icon or imply that the people are the disease.

## Achievement 6: A Place at the Table

Working ID:

`migration_a_place_at_the_table`

Eligible countries:

Any host country.

Unlock conditions:

- receive displaced cohorts from at least three different countries or origins
- the total integrated population reaches a meaningful share of the host's initial core population
- maintain food security above famine in all major receiving states
- complete local integration without forced labor, violent pushback, or forced return
- retain political stability above the accepted threshold

Disqualifiers:

- population gained through repeated transfer cycling
- debug bypass

Difficulty:

Very hard for small and medium countries.

Icon direction:

Shared table, several travel tokens, and a home symbol. Keep the imagery period-neutral within the HOI4 visual language.

## Achievement 7: The Grain Stayed Home

Working ID:

`famine_the_grain_stayed_home`

Eligible countries:

Any country with a historical or dynamic extraction profile.

Unlock conditions:

- face a state-level crop or transport shock while military or export extraction is active
- suspend extraction before the state reaches catastrophic famine
- preserve the front or national survival through another logistical solution
- recover the state without requisitioning another strained state

Disqualifiers:

- no real extraction policy was active
- the state never reached acute shortage
- debug bypass

Difficulty:

Medium to hard.

Icon direction:

Sealed grain store protected from a military requisition stamp represented without readable text.

## Achievement 8: The Country Did Not Empty

Working ID:

`migration_the_country_did_not_empty`

Eligible countries:

Any country that suffers simultaneous severe war, famine, and displacement pressure.

Unlock conditions:

- at least three core states enter famine or severe displacement
- total threatened displacement exceeds a high share of national population
- prevent any core state from falling below its protected recovery floor
- recover all famine states
- resolve every major cohort through return, integration, or resettlement
- remain independent

Disqualifiers:

- annexation or tag-switch exploit
- debug bypass

Difficulty:

Very hard.

Icon direction:

Country silhouette formed from repaired homes, rail, and grain symbols. Use a generic shared emblem and avoid a specific map outline.

## Implementation requirements

For every achievement:

- inspect the current root achievement registry and existing Chaos Redux patterns
- create stable tracking flags or variables
- use one-time unlock guards
- prevent debug, force-trigger, and scenario bypass where the project achievement policy requires it
- prevent transfer cycling and repeated cohort farming
- keep population thresholds dynamic or normalized where country size differs
- implement localisation
- create the full achievement state triplet under `gfx/achievements/`
- keep the achievement filename aligned with the full achievement ID
- document unlock conditions and disqualifiers
- add route and system hooks without duplicating population or death logic

## Audit requirements

The completion audit should test:

- ordinary success path
- every disqualifier
- save and reload persistence
- tag and cosmetic-tag changes
- origin or host annexation
- cohort integration and return cleanup
- force-trigger and debug exclusion
- no automatic unlock from historical starting memory

Do not convert a difficult achievement into an automatic result because one state modifier or event fires.
