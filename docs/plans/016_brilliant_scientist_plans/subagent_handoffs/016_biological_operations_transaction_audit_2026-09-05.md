# Event 016 biological operations transaction audit — 2026-09-05

## Scope and disposition

This bounded audit covers the Event 016 biological production, staging, and decision-led deployment tranche in the shared Chaos Redux worktree.

The transaction is source-reviewed against the accepted biological contract, and two small local defects were patched in owned biological effects/localisation surfaces.

No P0 issue was found.

The tranche is not independently commit-ready until the parent reviews the working-tree/index state and the unresolved MCP visual evidence.

No files were staged or committed by this audit.

## Issue list by severity

### P1/P2 confirmed and fixed

- brilliant_scientist_dispatch_weaponized_zombie_release applied apply_weaponized_zombie_strike_consequences before confirming that spawn_weaponized_zombie_outbreak_from_creator had produced the expected new-country owner.
- The zombie dispatcher now records the supplied dispatch proof only after the spawn owner check and applies deliberate-release strike consequences only after that proof is present.
- Battlefield and covert custom cost rows exposed literal payload and transport resource names instead of an icon-first native equipment cost.
- The biological scripted localisation now resolves the selected native payload icon and exact one-lot or two-lot amount for all six agents, and the battlefield row conditionally resolves the ten-item Portal transport cost.
- Blocked cost variants now colour each displayed spendable amount independently.

### Rejected false positive

- The 90-day staging completion passes a temporary variable to set_country_flag days after assigning the script constant with set_temp_variable.
- This is the accepted repository and vanilla duration handoff pattern, so it is not a defect and was not changed.

### No confirmed defect after review

- The FROM state, original controller/victim, route, target, and payload amount are captured before the deployment debit.
- Refund is guarded by the pending-plus-debited receipt and clears that receipt, so invalid-before-execution cancellation refunds once.
- Success, failure, and accident branches each settle through the pending receipt and cannot settle again after cleanup.
- Capitulation refunds the actor receipt before native equipment capture, and annexation transfers the still-reserved receipt once before clearing the former actor.
- The Black Plague path calls the existing Event 020 weaponized runtime bridge after the ordinary lifecycle proof and does not call the Event 020 public delivery debit a second time.
- Native raid reservations remain outside the Event 016 receipt and stockpile debit helpers.
- The Kruger gate is intentional: bio_kruger_last_resort_authority_is_valid permits ordinary non-Kruger actors while preserving the Kruger-specific aggressive AI factor.

## Changed files and identifiers

Changed working-tree files:

- common/scripted_effects/016_brilliant_scientist_biological_operations_effects.txt
- common/scripted_localisation/016_brilliant_scientist_biological_operations_scripted_localisation.txt
- localisation/english/016_brilliant_scientist_projects_l_english.yml
- This handoff.

Changed gameplay identifiers:

- brilliant_scientist_dispatch_weaponized_zombie_release
- GetBrilliantScientistSelectedBiologicalPayloadIcon
- GetBrilliantScientistBiologicalBattlefieldPayloadAmount
- GetBrilliantScientistBiologicalCovertPayloadAmount
- GetBrilliantScientistBiologicalBattlefieldTransportCost
- GetBrilliantScientistBiologicalBattlefieldTransportCostBlocked
- The brilliant_scientist_biological_payload_icon_*, route-specific payload amount, Portal transport cost, and biological deployment cost localisation keys.

Inspected but not changed: common/scripted_triggers/016_brilliant_scientist_biological_operations_triggers.txt, common/decisions/016_brilliant_scientist_biological_operations.txt, common/decisions/categories/016_brilliant_scientist_raid_lifecycle_categories.txt, common/script_constants/016_brilliant_scientist_raid_lifecycle_constants.txt, and docs/events/016_brilliant_scientist/systems/biological_operations.md.

Portal containment, native raid definitions, Event 020 core, GUI source, focuses, models/assets, and unrelated on-actions were not edited.

## Before and after behavior

Before the zombie patch, a failed outbreak spawn could still apply the actor-side strike consequences and then settle the deployment.

After the patch, deliberate zombie consequences run only after the target state confirms the spawned country owner; an accident remains a home-capital release without deliberate target consequences.

Before the localisation patch, battlefield and covert cost strings used prose such as payload(s) and transport equipment without the actual native equipment icon.

After the patch, the battlefield row shows Command Power, the selected native payload icon and exact one-lot amount, plus the Portal transport icon and ten only for a portal-only target; covert shows Command Power and the selected native payload icon with the exact two-lot amount.

Production support equipment and manpower cost rows also use the shared script constants and native texticons, with matching blocked and tooltip keys.

## Decision-category lifecycle notes

The category exposes six mutually exclusive selection actions for Anthrax, Plague, Tularemia, Smallpox, Weaponized Zombies, and Black Plague, plus production, staging, battlefield, and covert operations once an agent is selected.

Single production lasts 30 days, occupies two civilian factories, consumes 80 Support Equipment and 250 manpower, and creates one selected native payload lot.

Triple production lasts 60 days, occupies four civilian factories, consumes 240 Support Equipment and 750 manpower, and creates three selected native payload lots.

Staging lasts 90 days, occupies one civilian factory, adds the 180-day readiness window, and reserves no payload.

Battlefield deployment lasts seven days, debits one selected native payload and 25 Command Power at start, and accepts a frontline or operational military target or a Portal-enabled rear-area target with ten Teleportation Equipment.

Covert deployment lasts fourteen days, debits two selected native payloads and 50 Command Power at start, and accepts an enemy core industrial or strategic state.

The pending deployment receipt stores the target state, original controller/victim, selected agent, route, payload amount, Portal transport amount, and debit flags before any delayed resolution.

## Cognitive-load and mission quality notes

The visible primary selection set is capped at six, and the selection rows disappear for the currently selected agent; production and release rows are compact operational actions rather than additional agent choices.

Category text explains the selected agent, native-stockpile use, production, staging, and release purpose without exposing raw nested triggers.

Displayed amounts have direct significance: support/manpower fund production, native payload icons identify the exact equipment type, Command Power starts a release, and Portal transport identifies the rear-area route.

Production missions are country-owned biological-category actions with exact support, manpower, factory, and selected-agent requirements, 30/60-day durations, native-stockpile completion, and no output when cancellation invalidates the receipt.

The staging mission is country-owned, lasts 90 days, has no payload payment, and leaves a bounded readiness flag for 180 days after successful completion.

Battlefield and covert missions are state-targeted, retain their route-specific requirements through the timer, and expose success, failure, accident, cancellation, and duplicate-pending behavior through the shared receipt.

## Cost and requirement clarity

Production exposes two spendable types, Support Equipment and manpower, with native texticons and constant-backed values.

Battlefield exposes at most three spendable types, Command Power, the selected native payload, and conditional Portal transport.

Covert exposes two spendable types, Command Power and the selected native payload quantity.

No custom cost row exceeds the four-type limit, and all spendable entries use texticons rather than literal resource names.

Requirements retain prose for the non-consumed target and route conditions, while compact custom cost rows remain icon-first.

## AI validity and route-lock notes

Kruger receives the aggressive biological deployment factor, while ordinary AI remains sensitive to retaliation posture, intelligence-agency status, ideology, authorization posture, and exposure.

Battlefield targeting requires a valid enemy-held state controlled by its owner and either frontline/operational military relevance or Portal technology plus transport stock.

Covert targeting requires an enemy core state with industrial or strategic infrastructure.

Target ownership, controller, wartime relationship, population, wasteland, and zombie-control exclusions are revalidated before delayed execution.

## Localisation and tooltip notes

Native equipment sprite names were checked against interface/chaosx_equipment.gfx for all five ordinary/zombie payload icons, with Black Plague correctly using the existing Plague Bomb stock icon.

The existing teleportation_equipment_1_text_icon alias was checked in the Event 019 localisation family.

The new scripted-localisation keys each resolve to one localisation key, and the related Event 016 localisation file retains UTF-8 with BOM.

## Cleanup and exploit-risk notes

Production and staging cleanup clears their active flags without creating incomplete output or refunding consumed production inputs.

Deployment cleanup clears the pending and debit flags together with all receipt variables.

Capitulation and annexation paths clear the former actor receipt before later delayed callbacks can duplicate a refund or transfer.

The native raid transaction remains independent, so Event 016 does not seize, refund, or settle native raid reservations.

Black Plague provenance is recorded only after the shared bridge accepts the exposure, and Event 016 does not perform a second payload debit through Event 020.

## MCP evidence and blockers

The parent probability inspection used source hash prefix 4f69646916d65070... and recognized five timed mission candidates in the Event 016 source.

The parent evaluation fixture E016_BIOLOGICAL_DEPLOYMENT_CURRENT_2026_09_04 produced analysis probability-a2598cbde2aac4c27030a863 with partial output and unresolved eligibility; no normalized probability is inferred from it.

The earlier probability inspect artifact was hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/081fb05d6bacd2055e1e2d0a685416a8be5fac5e6da123b3b6578aeb2205030f/4bfe067a9574d77e6da28fe719c3a94e3e898b098308e3a42cb45b7fed35a27a/probability-inspect-4f69646916d6.json.

No new probability comparison was run because the AI weight source was unchanged by this audit; the parent evidence remains the applicable baseline, with eligibility unresolved.

Read-only hoi4.gui_inspect and hoi4.gui_render were attempted for the ordinary decision_view using scenario E016_BIOLOGICAL_DECISIONS_BASELINE_2026_09_04, normal/disabled/long-text states, and 1920x1080 at UI scale 1.

Both calls failed with the exact blocker: tool call error: tool call failed for hoi4_agent_tools/hoi4.gui_<inspect|render>; Caused by: timed out awaiting tools/call after 180s.

The corrected Event Inspector lint call used selector kind=file, sourcePath=common/decisions/016_brilliant_scientist_biological_operations.txt and returned EVENT_INSPECTED_PARTIAL with no blocking diagnostics and artifact event-lint-fa39cc8b8775.json.

The lint report is not complete because the large workspace analysis deferred helper projections and lifecycle passes, so it is supporting evidence rather than a full engine validation.

## Validation and remaining risks

Task-specific static checks confirmed balanced Clausewitz blocks in the three changed script surfaces, one-to-one localisation-key resolution for the new scripted-localisation branches, and all five ordinary/zombie payload GFX names plus the Portal texticon alias.

No game executable was launched, no logs were requested, and no live runtime result is claimed.

The unresolved visual risk is whether the optional [FROM.GetBrilliantScientistBiologicalBattlefieldTransportCost] branch renders correctly in the production targeted-decision cost bar; the required GUI MCP calls timed out before producing a render.

The shared worktree currently contains staged deletions and untracked replacement copies across the Event 016 tranche from concurrent work, so the parent must reconcile that index/worktree state before any commit or completion claim.

No design simplification was made; the only remaining limitations are MCP evidence incompleteness and the shared concurrent worktree state.
