# Chaos Warfare Achievement Implementation Prompt

## Task

Implement a difficult, route-diverse achievement set for the accepted Chaos Warfare rework. Read the achievement section of the main spec, current achievement registry, localisation, icon pattern, and asset handoff. Use the exact final achievement IDs consistently across script, localisation, GFX, three DDS variants, docs, and tracking.

Working labels below are not final player-facing localisation. Write final titles and descriptions during implementation using the specified direction.

## Achievements

### `chaos_warfare_air_still_breathable`

Eligibility: any major or regional power with enemy chemical use.

Unlock: win or survive a major war after confirmed enemy chemical use, maintain high military protection, keep own chemical contribution to Air Cleanliness below a strict limit, and never conduct offensive first use.

Disqualifiers: strategic civilian chemical or biological attack, doomsday release.

Difficulty: hard.

Icon: intact respirator against a clear sky with distant contaminated front.

### `chaos_warfare_masks_before_guns`

Unlock: before the first confirmed chemical attack in the campaign, reach high civilian coverage in every core state and maintain a military reserve above mobilisation need.

Difficulty: very hard for a large population.

Icon: stacked respirator crates in front of an arsenal gate.

### `chaos_warfare_prepared_army`

Unlock: field several fully equipped protected armies with CBRN headquarters, then repel a prepared chemical offensive while keeping military deaths below the tuned threshold.

Icon: masked staff officer and protected formation.

### `chaos_warfare_poisoned_victory`

Unlock: win a major war after using several distinct Chaos Warfare operations, reach a high Condemnation tier, and survive active sanctions and serious domestic or occupied-state contamination.

Disqualifier: none. The cost is the achievement identity.

Icon: victory wreath corroded by chemical droplets.

### `chaos_warfare_clean_hands_dirty_work`

Hidden.

Unlock: complete multiple covert chemical or biological operations, keep public attribution below probable for a long period, and achieve the target strategic result.

Disqualifier: discovered coverup before unlock.

Icon: gloved hand holding an unmarked sample vial.

### `chaos_warfare_evidence_survives`

Unlock: capture an enemy CBRN facility with a Biological Security Assault Detachment, preserve evidence, confirm the responsible country, and trigger sanctions or inspection.

Icon: sealed evidence case and broken facility door.

### `chaos_warfare_no_wind_is_friendly`

Unlock: suffer a forecast reversal and friendly exposure during a prepared chemical offensive, then recover the affected army and win the campaign objective without another chemical operation.

Icon: torn wind sock and masked troops.

### `chaos_warfare_antidote_arrived`

Unlock: contain a severe nerve-agent attack using advanced protection, medical countermeasures, and decontamination while keeping combined civilian and military deaths below a strict limit.

Icon: antidote injector over a respirator.

### `chaos_warfare_quarantine_without_collapse`

Unlock: contain a catastrophic biological outbreak inside its original country, prevent foreign spread, and maintain minimum stability, supply, and medical capacity.

Icon: closed transport gate with medical seal.

### `chaos_warfare_arsenal_dismantled`

Unlock: reach Arms Embargo or higher, accept a credible inspection, destroy or surrender offensive stockpiles, and return below Formal Censure without regime change, defeat, or hiding stock.

Icon: crushed chemical shell under inspection lamp.

### `chaos_warfare_terminal_contagion`

Unlock: complete all four doctrine tracks, field a fully equipped Chaos Assault formation, execute a doctrine capstone operation, and remain at war for a tuned period afterward.

Icon: four doctrine emblems around a sealed command mask.

### `chaos_warfare_mask_for_every_door`

Eligibility: Britain or another approved mass civil-defence profile.

Unlock: reach near-total civilian coverage, maintain replacement reserves, and send protective aid to at least three allies before first confirmed chemical use.

Icon: row of household doors with respirator boxes.

### `chaos_warfare_weapon_turns_home`

Unlock: suffer a major domestic stockpile accident, contain the resulting contamination or outbreak, reform safety to maximum, then dismantle or safely reduce the arsenal.

Icon: damaged depot with inward-pointing hazard sign.

### `chaos_warfare_unbroken_supply_corridor`

Unlock: maintain a decontamination corridor across several contaminated states, keep assigned army supply above the threshold, and complete a major offensive objective.

Icon: convoy moving through washed roadway.

### `chaos_warfare_first_user_pays`

Unlock: under a retaliation-only policy, defeat the first confirmed chemical user without conducting a strategic civilian chemical or biological attack.

Icon: sealed scales over a captured chemical shell.

## Tracking requirements

Use flags and variables only where the final state cannot prove the route. Track:

- starting eligibility
- offensive first use
- retaliation status
- strategic civilian attacks
- doomsday use
- maximum military and civilian coverage
- protection at the time of attack
- CBRN headquarters and formation counts
- operation types completed
- forecast failure and friendly exposure
- military and civilian deaths per relevant episode
- outbreak spread boundaries
- Condemnation peak and recovery
- inspection credibility and stockpile destruction
- facility capture and evidence preservation
- capstone operation and survival duration
- aid recipients

Add cleanup and prevent route switching from collecting incompatible achievements.

## Balance rule

No achievement unlocks solely from selecting the doctrine, researching a technology, or clicking one decision. Each must require campaign performance, risk, counterplay, or recovery.

## Assets

Coordinate exact IDs with the asset worker. Create completed, grey, and not-eligible variants through the approved achievement process. Do not resize unrelated icons.
