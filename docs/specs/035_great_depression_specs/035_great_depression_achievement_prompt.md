# Event 35 Great Depression 2.0 achievement implementation prompt

## Goal

Implement the complete six-contract Event 35 achievement package defined in `035_great_depression_spec_part_11_achievements_acceptance.md`. Treat part 11 as the source of truth for required conditions, disqualifiers, tracking, and icon direction.

Do not replace episode mastery with a final-state check. Every achievement must prove the relevant route over time through stable receipts, frozen episode data, and explicit exploit guards.

## Required reading

Before editing, read:

- `AGENTS.md`.
- The full Event 35 specification package.
- `035_great_depression_spec_part_11_achievements_acceptance.md`.
- `035_great_depression_spec_part_10_presentation_assets_text.md`.
- `035_great_depression_reusable_crisis_api.md`.
- `035_great_depression_state_lifecycle_map.md`.
- `035_great_depression_asset_prompt.md`.
- The accepted Event 34 achievement and Event 35 inheritance specifications.
- The current Chaos Redux achievement registry, scripted triggers, localisation, icons, and documentation.
- Current engine documentation and a working vanilla achievement precedent.

Inspect current identifiers before choosing IDs. Do not infer registry structure or asset paths from memory.

## Cross-event ownership

Event 34 owns the inherited Evolution III crash-and-recovery achievement through its accepted `The Long Fall` contract. Event 35 supplies that contract with the final recovery, inherited-center, and country-continuity receipts. Do not create a duplicate Event 35 achievement for the same episode history.

Event 35 owns national depression recovery, center reopening, contagion containment, Social Collapse survival, liquidation-led recovery, and worldwide reconstruction.

## ID rules

Use stable event-scoped IDs with lowercase snake case. Lock every full ID before icon production. Achievement DDS filenames must match the full ID exactly for eligible, grey, and not-eligible states.

Working labels in the specification are not mandatory final IDs or localisation. Final titles should be short, specific, and readable in the achievement interface.

## Contract 1: Back to Work

### Challenge

Recover from a severe independent Event 35 episode while preserving every original Depression Center and losing no civilian or military factory level through Event 35.

### Required tracking

- Player country and Event 35 episode ID.
- Independent source proof.
- Starting Severity and accepted severe minimum.
- Frozen original-center registry.
- Valid later center additions.
- Initial civilian and military factory ledger for each center.
- Event 35 factory-loss receipts.
- Center final states.
- Abandonment and liquidation receipts.
- Recovery proof and episode owner.

### Disqualifiers

- Event 34 inherited source.
- Any Event 35 industrial building loss.
- Center abandonment or liquidation.
- State transfer, annexation, puppeting, or tag switching used to remove a failing center.
- Debug, force completion, or late achievement tracking.

Combat damage does not disqualify the achievement unless Event 35 itself records the factory loss.

## Contract 2: Every Center Reopened

### Challenge

Reach Economic Paralysis and recover every Depression Center without abandoning one.

### Required tracking

- Peak Severity `100` receipt.
- Maximum-Severity emergency result.
- Registered center count and state IDs.
- Every later valid center addition.
- Final center states.
- Final Strong or Uneven Recovery result.
- State-transfer and cleanup history.

### Disqualifiers

- Any center ends Abandoned, Shuttered, unresolved, or invalidly removed.
- A center is liquidated as the final solution.
- State transfer is used to bypass a center requirement.
- Debug or forced recovery closure.

Use every valid center for a smaller economy when fewer than three exist.

## Contract 3: Containment Line

### Challenge

Contain material Financial Contagion without allowing any country materially exposed by the player's source crisis to convert into a full Event 35 crisis.

### Required tracking

- Player source country and episode ID.
- Financial Contagion activation receipt.
- Source Severity threshold.
- Exposure registry and source attribution.
- Highest exposure stage per foreign country.
- Valid-pool-scaled exposed-country count.
- Completed aid, ring-fence, clearing, diversification, or coordinated-rescue action.
- Full-crisis conversion receipts.
- Source recovery and contagion-resolution proof.

### Disqualifiers

- Any attributable foreign Event 35 conversion.
- Deleting, annexing, or invalidly cleaning an exposed country to remove the link.
- Disabling the evolution after exposure begins.
- Debug or force cleanup.
- Loss of source-country ownership.

### Multi-source rule

A conversion disqualifies the achievement when the player's source episode was a material dominant or secondary contributor. An unrelated conversion does not disqualify it unless the player's source crossed the final contribution threshold.

## Contract 4: The Social Peace

### Challenge

Recover from Social Collapse after near-maximum Severity without a successful coup, Event 35 civil conflict, or permanent emergency rule.

### Required tracking

- Social Collapse activation.
- Peak Severity of at least `90`.
- At least one major strike, occupation, riot, mutiny, or government crisis.
- Final settlement or social-peace objective.
- Coup, separatist, and civil-conflict receipts.
- Emergency-government lifecycle.
- Final stability and recovery ownership.

### Disqualifiers

- Successful coup, separatist conflict, or Event 35 civil conflict.
- Permanent military or emergency government created by the crisis.
- Debug incident clearing.
- Crisis ownership moved to another country.

A baseline strike before Evolution II can remain in history but cannot satisfy the required Social Collapse incident by itself.

## Contract 5: Lean but Standing

### Challenge

Complete a liquidation-led recovery after accepting real Event 35 industrial loss while retaining national viability and avoiding political collapse.

### Required tracking

- Final recovery philosophy and route ownership.
- Exact center consolidation, auction, or deliberate-resolution receipt.
- Exact Event 35 civilian or military factory loss by state and building type.
- Protected national industrial floor.
- Coup, separatist, civil-conflict, and government-collapse receipts.
- Final recovery proof.

### Disqualifiers

- Industrial loss came only from war, bombing, disaster, occupation, or another event.
- No real Event 35 industrial loss occurred.
- Doctrine switching or later program history invalidates liquidation-route ownership.
- Country falls below the protected viability floor.
- Debug completion.

Final localisation should describe survival after a harsh choice. It should not praise unemployment or suffering.

## Contract 6: Recovery of Nations

### Challenge

Lead or materially support international recovery during The Second Great Depression while preserving the player's national stability.

### Required tracking

- Evolution III global episode ID.
- Player role as an Event 35 country or registered reconstruction supplier.
- Validated aid, clearing, reconstruction, coordinated-demand, or supplier contributions.
- At least one major recipient improvement caused by player support.
- Player national conversion or recovery state.
- Entry into International Reconstruction.
- Final global recovery proof.
- Major supplier-collapse proof period.
- Country existence and independence.

### Disqualifiers

- Contributions are refunded, duplicated, or registered after recovery was already secured.
- The player triggers a critical supplier collapse during the final proof.
- The global episode is force-ended.
- Country deletion or invalid tag switching.
- Special actor outside normal civilian-system coverage.

## Tracking architecture

Use bounded national and global episode receipts. Do not infer route history from current modifiers after the fact.

At minimum, tracking needs:

- National Event 35 episode ID.
- Source enum and source transaction ID.
- Player owner and continuity proof.
- Initial and later valid Depression Center registry.
- Starting and peak Severity.
- Maximum-Severity receipt.
- Mission and project completion receipts.
- Center factory-loss, abandonment, liquidation, reopening, and transfer receipts.
- Evolution and incident-family receipts.
- Contagion source, exposure, and conversion records.
- Coup, emergency-rule, separatist, and civil-conflict receipts.
- Evolution III global episode and contribution receipts.
- Debug, observer, force-trigger, and invalid tag-switch state.

Receipts must survive save and reload. Clear or archive them only after permanent achievement eligibility facts are frozen.

## Player ownership and multiplayer

Evaluate national achievements for the eligible player country under the repository's established achievement rules. A later tag switch, civil-war child, released country, overlord, or annexer must not inherit progress without an explicit accepted continuity rule.

Multiplayer tracking is country-scoped. One player's national actions cannot satisfy another player's contract. Recovery of Nations may be completed by several players independently when each meets the full contribution and continuity conditions.

## Save persistence tests

Test save and reload:

- Before the first center completion.
- At Severity `100` during the maximum emergency.
- During Financial Contagion.
- After a major Social Collapse incident.
- During an Event 35 liquidation transaction.
- During Evolution III final proof.
- Immediately before national recovery completion.

Receipts must not duplicate, clear, or reroll.

## Icon production

Route all final IDs to `chaosx_icon_artist`.

Every achievement requires:

- `<full_id>.dds`.
- `<full_id>_grey.dds`.
- `<full_id>_not_eligible.dds`.

Follow the exact installed-vanilla achievement reference family and final placement. Use distinct source art. Do not recolor one generic factory icon six times.

Visual directions:

- Back to Work: open factory gate and returning workers.
- Every Center Reopened: several workshops or industrial bays lit again.
- Containment Line: an economic link stopped by a clear firebreak, without disease imagery.
- The Social Peace: reopened factory after negotiated settlement, without readable document text.
- Lean but Standing: one surviving active plant beside closed capacity.
- Recovery of Nations: freight, port, rail, and factory recovery across linked countries without a world map or handshake.

Use native transparency where the reference family uses alpha. Create contact-sheet evidence and final-size review.

## Localisation direction

Titles should be short and specific. Descriptions should state the visible challenge without exposing hidden variable names, contribution scores, conversion weights, or implementation receipts.

Final text may name:

- Independent source.
- Severity threshold.
- Depression Centers.
- Event 35 factory loss.
- Financial Contagion.
- Social Collapse.
- Worldwide recovery.

## Documentation

Update:

- Event 35 permanent documentation.
- Achievement documentation or index.
- Asset manifest and final icon paths.
- Event 34 documentation for `The Long Fall` adapter receipts.
- Completion coverage table.
- Authoritative workbook only when achievement fields exist there.

## Positive and negative tests

For every achievement, implement:

- One valid completion scenario.
- One near-miss that fails for the intended disqualifier.
- One save and reload scenario.
- One tag, annexation, transfer, or crisis-owner scenario when relevant.
- One debug or forced-setup disqualification scenario.

Specific negatives:

- Back to Work fails after one center abandonment or Event 35 factory loss.
- Every Center Reopened fails with one Shuttered center at recovery.
- Containment Line fails after one attributable foreign conversion.
- The Social Peace fails after a successful coup or permanent emergency rule.
- Lean but Standing fails when no factory was lost or the loss came from bombing.
- Recovery of Nations fails when contributions begin after global recovery was already secured.

## Handoff

Return:

- Final achievement IDs and localisation keys.
- Contract-to-receipt map.
- Cross-event ownership note for Event 34 `The Long Fall`.
- New scripted triggers and effects.
- Icon triplet paths and checksums.
- Documentation paths.
- Positive, negative, persistence, and exploit-test evidence.
- Any blocker, merge, fallback, or unimplemented contract.

Do not claim the Event 35 achievement package complete while any of the six contracts lacks stable tracking, exploit guards, final localisation, a full icon triplet, documentation, or test evidence.
