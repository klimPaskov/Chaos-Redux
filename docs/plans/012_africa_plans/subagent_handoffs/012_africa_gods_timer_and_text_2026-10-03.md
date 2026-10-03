# Gods demand timer and material text

Disposition: implemented in source, with runtime and full-goal acceptance incomplete.
Acceptance basis: the active user goal requires one frozen demand contract, meaningful response deadlines, real material transactions, and text that agrees with those mechanics.

## Timer correction

The demand mission's fixed 180-day definition previously differed from ceremonial 45-day, standard 90-day, severe 120-day, emergency 60-day, and punitive 150-day deadlines.
The owner tick checked expiry only every 30 days, and negotiation advanced the frozen deadline by 30 days without changing the native timer.

`gods_of_africa_sync_demand_mission_timeout` runs after mission activation and after an extension.
In participant scope it requires a current active demand, its deadline, and an active native mission.
It computes remaining contract days from the deadline and `global.num_days`, subtracts `days_mission_timeout@gods_of_africa_demand_mission`, and applies the difference with `add_days_mission_timeout`.
An already expired contract enters the existing guarded failure resolver.
The helper has no default deadline, consumes no payment, resets no mission, and leaves no persistent helper value.
Demand and reconciliation descriptions use their native remaining timeout.
The owner expiry pass remains a recovery guard for an interrupted or missing timer.

## Material and report text

- `GetGodsOfAfricaDemandFamilyName` includes support equipment.
- Voluntary-aid cost selectors mirror the real equipment-first, otherwise-fuel payment branches and show one selected cost.
- Transport icons follow the convoy-first affordability branch using the same full, partial, or substitute capacity requirement as the corresponding payment.
- The voluntary-aid receipt uses the stored last family and amount, which are written before `.614` is fired.
- Doctrine figures read existing constants, and extra exaction retaliation or ambiguity sanctions retain the host-marked-offender condition.
- Protection text retains its base interval, both interval reductions, doctrine-specific Wrath relief, conditional services, optional transport, and unchanged separate Event 013 price.
- The armor and mobile/artillery family names were restored to the accepted design instead of accepting the incomplete worker rename to motorized equipment.

The assigned localisation worker returned an audit but its patch handle later became unavailable.
The parent inspected and reconciled the existing working-tree patch before adopting these changes.
Raw flag requirements and several outcome-specific descriptions from that audit still need implementation.

## Changed files

- `common/scripted_effects/012_africa_gods_effects.txt`: timeout synchronization, activation and extension call sites, and the recovery-pass comment.
- `common/decisions/012_africa_gods_decisions.txt`: the native timeout anchor's contract.
- `common/scripted_localisation/012_africa_gods_scripted_localisation.txt`: support-family, voluntary-aid, last-aid, and transport selectors.
- `localisation/english/012_africa_gods_l_english.yml`: mission countdowns, material cost leaves, report wording, doctrine figures, and existing icon tokens.
- `docs/events/012_africa/gods_of_africa.md`: timer behavior and the required tank-family gap.

## Reference evidence

- Installed `documentation/effects_documentation.md:1051-1065`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`: native mission timeout adjustment.
- Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:1908-1927`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`: activation ignores decision triggers, and timeout adjustment accepts a variable.
- Installed `documentation/dynamic_variables_documentation.md:238-240`, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`: mission-targeted remaining timeout.
- Installed `documentation/triggers_documentation.md:3022-3029`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`: `has_active_mission`.
- Vanilla `common/decisions/GER.txt:16893-16896,16933-16936`: timeout extension precedent.
- Vanilla `common/decisions/YUG.txt:1227-1229`: signed negative timeout adjustment of 15 days, confirming that synchronization can shorten the activation anchor.
- Vanilla `interface/texticons.gfx:34-36,2150-2152`: convoy and motorized text-icon registrations.

The pertinent reference searches and reads were called.
The installed timeout-effect `reference_read` returned `timed out awaiting tools/call after 600s`, so its exact local section was read directly.
The offline mission section and installed remaining-time section returned revision-bound text.
No online Paradox source was used.

## Source scenario review

| Case | Source result |
| --- | --- |
| Ceremonial demand | Starting at 180 days, adjustment of minus 135 leaves the frozen 45-day timeout. |
| Other demand bands | The same calculation sets 90, 120, 60, or 150 days from the stored deadline. |
| Strategic Ambiguity | Its 30-day frozen extension is included because synchronization reads the resulting deadline. |
| Negotiation | Both the stored deadline and native timeout advance by the configured 30 days. |
| Ambiguity punitive demand plus negotiation | The resulting 210-day deadline can extend beyond the 180-day anchor. |
| Synchronization repeats | The current native timeout is subtracted, so a second call at the same day has zero adjustment. |
| Partial shipment | The mission and deadline remain running, with only the remaining payment updated. |
| Timeout and owner recovery overlap | The first failure clears the active contract, so the second cannot record another failure or punishment. |
| Voluntary aid has both needs | Both the cost selector and payment choose affordable infantry equipment first. |
| Transport can use both stocks | Both the displayed icon and actual payment take convoys first. |

These are source-contract checks, not observed game execution.
No AI score, material price, DLC gate, route, or deadline tuning was changed.
No design simplification was accepted.

## QA and remaining work

The user supplied `docs/testing/live_qa/20261003_full_playtest/logs/cycle1/error.log`, 100,355 bytes, last written at 08:48:28 on 2026-10-03.
The supplied menu-load log contains no `012_africa`, `gods_of_africa`, or `chaosx.nr12.` match, while the full log still contains other reported errors.
That evidence does not exercise this demand timer or establish a globally clean build.
The selected `.603` MCP trace returned `timed out awaiting tools/call after 600s`, with no artifact or lifecycle result.
On the user's requested continuation, a narrower downstream retry selected only `.603` with depth 1, at most 10 nodes and 20 edges, and no refresh.
That retry is pending at the time this tranche is prepared for commit; no result or coverage is claimed for it.
Source-only review is not a replacement for that missing coverage.

The full goal remains incomplete.
The accepted tank-family requirement at `012_gods_of_africa_full_spec.md:442-446` is not met by the current motorized alias and unreachable selection branch.
Tank capacity, need, selection, and actual tank transfers remain required, along with the unresolved visible requirements, weighted scenarios, owner lifecycle, and presentation evidence.

Skills used in this tranche: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`.
No skill file was changed, and reusable native-clock guidance remains queued because the decisions skill contains concurrent edits.
