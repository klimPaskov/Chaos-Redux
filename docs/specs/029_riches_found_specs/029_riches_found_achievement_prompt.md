# Event 029 achievement implementation prompt

Implement the complete achievement package for Chaos Redux Event 029, Riches Found.

Read repository `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-assets`, the current achievement registry and precedent, and every file under `docs/specs/029_riches_found_specs/` before editing.

Treat the achievement IDs and labels below as working values until the parent confirms that they do not conflict with existing IDs.

Keep all Event 029 achievements grouped inside the single root Chaos Redux achievement registry.

Do not create a new achievement database with another `unique_id`.

Every achievement requires route tracking, disqualifiers, localisation, completed icon, grey icon, not-eligible icon, documentation, and test coverage.

Use `chaosx_icon_artist` with `fork_context=false` for final icon triplets after the exact IDs and runtime filenames are locked.

The parent owns final registry, localisation, event and decision hooks, docs, catalog references, and live validation.

## Shared tracking state

Create stable Event 029 achievement tracking for:

- original discovering country
- original mine state
- discovery date
- current controller
- controller-transfer count
- mature-development date
- continuous control period
- public-settlement completion
- citizens' dividend completion
- local-revenue settlement completion
- public project completion
- exclusive-concession history
- contract and controller-transfer history
- Resource Curse history
- Gold Disease history
- Demons Beneath the Mine history
- Gilded Sovereignty history
- Bottomless Account history
- permanent-sealing history
- evacuation completion
- scientific, religious, or engineering assistance completion
- mass-death disqualifier
- foreign-military-intervention disqualifier
- pay-route mission successes
- active controlled mine count
- duplicate-contribution safety proof when needed for multi-mine verification

Use flags for boolean state.

Use variables only for counts, dates, or values that need arithmetic.

Do not derive a historical achievement from the current final state when the route requires a past action or avoided event.

Clear temporary per-mission state without clearing permanent achievement history.

Follow the repository's standard rule for achievements under debug, force-trigger, custom scenario, game-rule, or non-eligible states.

## Achievement 1: `029_public_fortune`

Working label: Public Fortune.

Visibility: Visible from campaign start or after Event 029 appears, according to repository convention.

Difficulty: Hard.

Eligible actor: The country that received the mine's original discovery event.

Required conditions:

- control the original mine state continuously for at least two years after the mine reaches mature development
- maintain Revenue Legitimacy in the high band throughout the final verification period
- maintain Local Order in the high band throughout the final verification period
- keep Extraction Pressure below the severe band throughout the final verification period
- complete a citizens' dividend or local-revenue settlement
- complete at least one permanent public-development project in the mine state
- keep the mine open and productive
- never grant an exclusive foreign concession for that mine
- never record The Resource Curse for that mine

Disqualifiers:

- mine lost before the hold period completes
- mine permanently sealed or destroyed
- mass killing linked to the mine
- patronage-dominance resolution
- invalid transfer or duplicate tracking state

Implementation notes:

- Start the two-year timer only after mature development and the required public settlement exist.
- Reset the continuous-control timer on loss of control.
- Do not reset permanent disqualifiers after recapture.
- The achievement should unlock only after the final verification period confirms the values remained in range.

Icon direction:

A valuable ore specimen above a public road, civic buildings, or worker housing with a balanced treasury motif.

## Achievement 2: `029_claim_jumper`

Working label: Claim Jumper.

Visibility: Visible.

Difficulty: Medium to hard.

Eligible actor: Any country that did not receive the original discovery event for the selected mine.

Required conditions:

- gain control of a mine discovered by another country through normal war, civil war, annexation, liberation, or peace settlement
- keep the mine under control for one year
- keep it operational at the end of the period
- complete at least one transfer settlement, contract renegotiation, administration replacement, or physical repair
- receive the reconciled controller contribution without duplication

Disqualifiers:

- permanent closure before the hold period
- invalid debug-only controller state under the repository's achievement rules
- contribution remains with the former controller

Implementation notes:

- Save the original discoverer on mine creation.
- Set transfer history only when the current controller differs from the original discoverer through a valid control change.
- Start the hold timer after the new controller's contribution refresh succeeds.
- Reset the timer if control is lost.

Icon direction:

A hand or claim stake taking control of marked ore across a broken boundary marker.

## Achievement 3: `029_the_pay_train_runs`

Working label: The Pay Train Runs.

Visibility: Visible.

Difficulty: Medium.

Eligible actor: Any current mine controller with a valid rail or convoy pay route.

Required conditions:

- complete three distinct Protect the Pay Train or equivalent shipment-protection missions
- each mission must begin under a real raid, disorder, or route-risk state
- no pay robbery succeeds during the sequence
- the mine remains open
- supplied security is maintained on the named route for every mission

Disqualifiers:

- duplicate mission completion counted twice
- mission auto-completes from a condition already satisfied without a fresh objective
- mine closes or is lost before the third success
- a robbery succeeds between counted missions

Implementation notes:

- Use a bounded integer success counter.
- Store a mission instance or sequence proof so the same event cannot increment twice.
- Reset the sequence after a successful robbery, mine loss, or permanent closure.
- Do not reset after a harmless pause if the mine remains operational.

Icon direction:

A guarded period train or pay wagon carrying a sealed strongbox through a mining district.

## Achievement 4: `029_all_that_glitters`

Working label: All That Glitters.

Visibility: Visible.

Difficulty: Very hard.

Eligible actor: Any ordinary country.

Required conditions:

- control at least three active Event 029 mine states at the same time
- every mine is open or regulated, not closed, collapsed, or sealed
- every mine has positive Local Order and Revenue Legitimacy above the accepted safe bands
- no controlled mine has Gold Disease
- no controlled mine has Demons Beneath the Mine
- no controlled mine is in The Gilded Sovereignty
- the country aggregate is valid and under its intended hard cap
- hold the complete condition for a defined verification period, recommended 180 days

Disqualifiers:

- any mine contribution duplicated
- any mine permanently closes during the verification period
- one mine enters a forbidden evolution or crisis during the period
- control falls below three mines

Implementation notes:

- Count Event 029 registry entries controlled by the country through the bounded registry, not a whole-world state scan.
- Rebuild the condition after controller transfer, closure, and evolution entry.
- Use the same controlled-mine count as the aggregate system.

Icon direction:

Three distinct mine entrances or ore specimens balanced under one national ledger.

## Achievement 5: `029_no_man_owns_the_mountain`

Working label: No Man Owns the Mountain.

Visibility: Hidden until The Gilded Sovereignty becomes active for a player-controlled mine.

Difficulty: Very hard.

Eligible actor: The current controller of the affected mine.

Required conditions:

- The Gilded Sovereignty was active
- dismantle or reform the rival authority through buyout, charter revocation, representative settlement, or another accepted non-destructive route
- restore government access and civil administration
- raise Revenue Legitimacy to the high band
- keep the mine open
- avoid foreign military intervention
- avoid catastrophic collapse
- avoid a mass-killing resolution

Disqualifiers:

- accept a permanent private enclave as final state
- permanently close or destroy the mine
- use a massacre, forced entombment, or other disqualifying violent resolution
- lose control before reform completes

Implementation notes:

- Record that Gilded Sovereignty existed before recovery.
- Track foreign military intervention separately from diplomatic or economic pressure.
- Require a stable post-reform verification period before unlock.

Icon direction:

A broken private gate or charter seal above an intact mine and restored public authority.

## Achievement 6: `029_close_the_account`

Working label: Close the Account.

Visibility: Hidden until The Bottomless Account becomes active.

Difficulty: Extreme.

Eligible actor: The current controller of the affected supernatural mine.

Required conditions:

- deliberately enter The Bottomless Account
- reject further terms through Close the Account or a successful bound-terms closure
- evacuate the workforce or keep Event 029 deaths below the accepted containment ceiling
- complete permanent sealing or another accepted final closure that ends the positive supernatural contribution
- keep national stability above the specified floor at completion
- retain control of the mine until closure finishes

Disqualifiers:

- unrelated deaths satisfy an obligation
- accept Predatory Prosperity as the final state
- catastrophic collapse from a broken term
- lose control before closure
- mass-death disqualifier set

Implementation notes:

- Bottomless Account entry is a late outcome inside Evolution III and must not require an Evolution V log row.
- Verify that the supernatural contribution is gone before unlock.
- Use Event 029-specific deaths only for the containment ceiling.

Icon direction:

A shut ledger chained over a sealed mine entrance with one extinguished golden light.

## Achievement 7: `029_the_last_shift`

Working label: The Last Shift.

Visibility: Hidden after Demons Beneath the Mine is recorded for a player-controlled mine.

Difficulty: Very hard.

Eligible actor: Any controller of the affected mine.

Required conditions:

- complete the dedicated workforce and district evacuation mission
- complete one valid scientific, religious, or controlled engineering assistance route
- permanently seal the mine
- avoid mass deaths
- avoid military purge
- avoid The Bottomless Account
- retain control until sealing completes
- never reopen the sealed deep sections after the route begins

Disqualifiers:

- abandon or entomb the workforce
- use mass killing
- lose the mine before sealing
- accept a supernatural agreement
- reopen the sealed sections

Implementation notes:

- Record the accepted assistance family.
- Assistance must be real Event 029 content and must not create unsupported Event 016 progression or invented real religious claims.
- Require the evacuation mission success before final sealing.

Icon direction:

Miners leaving a dark shaft while a reinforced final gate closes behind them.

## Icon production

After IDs are locked, issue a context-complete prompt to `chaosx_icon_artist`.

Every achievement requires:

- original ImageGen source art
- completed 64x64 PNG and DDS
- grey 64x64 DDS
- not-eligible 64x64 DDS
- exact achievement filename matching the registry ID
- native-size contact sheet
- alpha and DDS round-trip evidence
- manifest entry
- handoff under `docs/plans/029_riches_found_plans/subagent_handoffs/`

Keep final achievement DDS files in `gfx/achievements/` if repository and vanilla inspection confirm the root-only convention.

Do not resize a decision, idea, or report image into an achievement icon.

## Localisation direction

Final achievement titles can retain or replace the working labels after a writing pass.

Descriptions should state the public campaign feat and avoid hidden variable names.

Hidden achievements should remain vague before reveal and precise after their reveal condition if the repository supports dynamic description state.

Do not expose debug disqualifiers, contribution-ledger checks, or hidden evolution pressure.

## Validation

Before completion:

- inspect every tracking call site
- confirm flags and counters persist through save and reload
- test each achievement in a dedicated scenario
- test every disqualifier
- confirm one achievement cannot unlock twice
- confirm AI-controlled countries do not create player achievement state unless repository convention allows later takeover
- confirm debug and force-trigger eligibility follows the shared achievement rule
- confirm icons and localisation resolve
- confirm event docs and achievement documentation match final behavior

Report every missing tracking hook, asset, localisation key, or untested route as a blocker.
