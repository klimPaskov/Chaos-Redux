# Implement the Fuel Crisis achievement

Read Part 4 in full and all other canonical parts under `docs/specs/109_fuel_crisis_specs/`, then the implementation handoff, decision-mission prompt, asset prompt, and review record. Follow current `AGENTS.md`, events, event-assets, decisions-missions, subagents, and the current achievement patterns in the actual checkout.

Implement one difficult visible achievement with proposed key `109_fuel_crisis_running_on_empty`. Running on Empty is a working label, not a finished title. Write final title and description from the recovery-through-imported-supply direction after the exact conditions and supported UI are verified. Use the existing description and any supported eligibility tooltip to communicate requirements. Do not add a new diagnostic interface.

## Exact unlock contract

| Requirement | Condition |
| --- | --- |
| Occurrence | One committed ordinary shared occurrence or normal non-force manual trigger that satisfies shared eligibility |
| Excluded origins | Deliberate force and raw direct-debug opening calls |
| Recipient | The same existing player-controlled country at the wipe and task assignment |
| War | At war at both those moments. Winning the existing war after assignment preserves eligibility |
| Demand | Verified meaningful positive D0 from active commitments before the wipe |
| Material loss | Pre-wipe stored fuel F0 is at least seven days of D0 |
| Storage | Pre-wipe capacity C0 is at least twenty-eight days of D0, and assignment capacity holds the full target |
| Assignment supply | Dependable usable inflow J0 is at most D0, with Part 3's active-action and no-passive-task gates satisfied |
| Ordinary task | A genuine active Event 101 Fuel Crisis reserve task for the same country and receipt |
| Imported improvement | A real post-assignment imported-oil action creates at least 0.25 times D0 of additional actually delivered recurring fuel-equivalent flow |
| Reserve | Actual fuel reaches at least fourteen days of frozen D0 |
| Hold | Full reserve, imported increment, selected ordinary action, and continuing task conditions all pass for seven complete daily observed intervals |
| Cutoffs | Final qualifying observation and genuine success resolution occur within ninety days of the wipe and by the original task cutoff |
| Validity | The existing registry's verified campaign validity also passes |

The capacity gate makes the ordinary reserve target equal to the full fourteen-day achievement quantity. Use the existing active Tasks evaluation and genuine success hook. A conservation-selected task still needs its conservation action as well as the imported increment. A supply-selected task cannot replace the required imported-oil action with a domestic or one-time change.

The first qualifying daily observation starts at zero elapsed days. Seven subsequent confirmations establish seven complete intervals. A failed condition resets the hold. Do not infer missing observations, claim intraday continuity from daily samples, extend a cutoff on load, or combine evidence from different occurrences.

This is difficult because it combines a real wartime reserve loss, no assignment surplus, an active imported-supply intervention, a full operational buffer, and a shorter onset-based window. Arithmetic plausibility in the spec does not prove that the installed game can observe or realistically support it. Demonstrate at least one feasible supported campaign case before calling the achievement implemented.

## Ownership and disqualifiers

Verify the real Event 101 API, demand and capacity readings, actual imported delivery, conversion units, source attribution, timer convention, and terminal-success semantics. A nominal import agreement, unrelated conversion technology, domestic production increase, one-time gift, or synthetic success callback is insufficient proof. Missing required accessors leave the achievement blocked.

Preserve frozen receipt origin and onset facts in existing occurrence and Tasks records. Do not read current force mode later as a substitute for origin. Keep the task's action, target, deadline, hold, and genuine terminal disposition with Event 101. The validated success hook sets only the minimal durable achievement completion flag and provenance needed by the existing registry.

AI recipients, later-created countries, recreated tags inheriting old context, different recipients, invalid onset facts, trivial demand, insufficient stock or capacity, passive completion, missing import proof, expired cutoffs, and forced or raw-debug origins cannot qualify. Apply the standard owner cancellation for country disappearance, transfer to AI, disabled Tasks, technical invalidity, and a replaced crisis context. Ordinary wartime setbacks retain the agreed task risk.

Normal task success must still resolve and reward promptly even when achievement proof is missing. The achievement does not delay success, modify the reward, add a second mission, or remain active after the task ends. A later ordinary success can earn its normal reward without the badge. All rewards and consequences remain with Event 101.

## Registry, assets, and final evidence

Inspect the existing root registry `common/achievements/chaos_redux_achievements.txt` and reuse its verified identifier, grouping, validity, and per-country completion patterns. Do not create a duplicate registry unique ID. Confirm the actual key and root icon lookup before choosing final filenames. Bind final localisation to the real consumer keys with the required encoding.

Route the original 64x64 empty-fuel-can and supply-hose subject to `chaosx_icon_artist` with `fork_turns="none"` and the current role profile. Require the completed, grey, and not-eligible triplet, immutable templates, owner processing script, strict DDS checks, native-size decoded review, and the root paths defined in Part 4. The asset prompt contains the complete production contract.

Validate the ordinary success case, every eligibility boundary, interrupted and missing observations, both deadline edges, victory after assignment, Tasks success without the badge, country changes, save/load, force-first, replay, direct debug, wrong receipt, repeated terminal callback, and multiplayer recipient isolation. Use required supported source and MCP routes and preserve unsupported capability findings. The parent owns final wiring and review, and the user owns live-game validation.

Return exact changed files, final keys, durable tracking fields and lifecycle, native and Tasks evidence, all icon states and consumer acceptance, final localisation coverage, feasibility evidence, scenario results, and blockers. A flag that can be set or an icon that renders does not by itself satisfy this achievement contract.
