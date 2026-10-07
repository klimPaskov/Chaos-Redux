# Event 24 Evolution Timing and Rulebook Commander Baseline

Audit date: 2026-10-07.

Status: read-only source baseline complete; numerical timing, event-option ranking, and commander assignment probability remain unresolved because the HOI4 probability route returned no analysis result.

This handoff records current source at HEAD 63f0799041f303d5d051dbdf22f8cd0bca5f7a48, including the committed post-9065313 Event24 expansion. The 3 October snapshots and their “no MTTH entry” conclusions are historical and were not used as current source evidence.

No gameplay source was edited, no balance target was selected, no Git index entry was changed, and no commit was made. The only task-owned writes are the one-time physical snapshot under probability_snapshots/2026-10-07_pre_evolution_timing/ and this handoff.

## Scope, authority, and reading

The requested weighted surfaces are the Event24 evolution pacing entries, opening choices P24-O1 through P24-O4, and the Rulebook Commander random result and trait definition.

The 16 files in docs/specs/024_video_game_in_sweden_specs/, the current takeover_status_2026-10-06.md, reports 16 and 22, and handoffs 19 and 21 were read. The four required skills were read in full: chaos-redux-subagents, chaos-redux-events, chaos-redux-mtth, and chaos-redux-decisions-missions.

No file named newAGENTS.md was found in the repository. The repository AGENTS.md and the user-supplied AGENTS.md instructions were applied.

The explicit retirement of Field-Validated Planner remains in force. The current trait source defines Rulebook Commander only. The selected vanilla SWE_wargames spirit picture is unrelated to this audit and was left untouched.

D16’s supplied-division proxy is unresolved pending the user’s explicit approval question. The 6 October status document’s description of it as “previously accepted” is not treated as current approval. P24-E3A’s field-validation state therefore remains an assumed scenario input whose gameplay proof basis is unresolved.

The old handle 26 was confirmed absent by the parent, with no old handoff and no resumed live job. This is the new handoff at the requested path.

## Immutable current-source snapshot

The snapshot destination did not exist before capture. Each file was copied once with Copy-Item into a mirrored path, not hard-linked. SHA-256 and byte length matched the live source at capture for all 17 Event24 source files and the accepted scenario matrix. No snapshot was a reparse point, and no live source had its ReadOnly attribute set.

Snapshot root: docs/plans/024_video_game_in_sweden_plans/probability_snapshots/2026-10-07_pre_evolution_timing/

| Current source or fixture | Bytes | Frozen SHA-256 |
| --- | ---: | --- |
| events/024_hearts_of_iron.txt | 69,755 | 60904703034703c8254f080b0bf63d2cf1829923db29087fe5687385ec09b095 |
| common/mtth/024_video_game_in_sweden_mtth.txt | 6,738 | fd8518e333ca2e1aafbe8437496cec0baea55ca8a073fb9a95f08bfaae64352f |
| common/script_constants/024_video_game_in_sweden_constants.txt | 24,387 | 11872d5dd1da14b70a3cd231817e7d5c672a10ef46eb05cfc475558c5fefdb78 |
| common/scripted_effects/024_video_game_in_sweden_effects.txt | 229,488 | dd4d51cd739cfd59222c2981433a13fc7e0296089a30311eeb70b7c577f001d5 |
| common/scripted_effects/024_video_game_in_sweden_runtime_effects.txt | 14,513 | 3af61bfe7bd8d051fd9eecae37f99ed85ecf1a83884d6629d75bb92ce0335dba |
| common/scripted_effects/024_video_game_in_sweden_cxt_effects.txt | 1,858 | 84e2d9f1143504fb308720047d33c7e669cbecbe6e2cd29309a372855095469d |
| common/scripted_triggers/024_video_game_in_sweden_triggers.txt | 57,876 | e0bfc38415f180643f69e29ba482d43deec996777a74fd760607e419c0262098 |
| common/decisions/024_video_game_in_sweden_decisions.txt | 50,131 | d854c1affee958fb66068866056a71760dbd423f1a795fa7d1f985024b84dc6d |
| common/decisions/categories/024_video_game_in_sweden_categories.txt | 945 | 12778be8725534f1872a568f137f079f2f7f69e3f8d775e2c89653991ddac68b |
| common/scripted_localisation/024_video_game_in_sweden.txt | 25,096 | 50486c2af8598f1004a6889bc518320af7155f30f4de6ae8072b0e2941e8d622 |
| common/unit_leader/024_video_game_in_sweden_traits.txt | 899 | 7c2d54263803ac2d1b8c5541183d6366c5c8368a0ceadd07ced320b956129ba5 |
| common/ideas/024_hearts_of_iron_ideas.txt | 4,209 | 19c5de8267f6dc02713ea9962211b3c44a65198c09c44834142f09ef6510d2ed |
| common/ideas/024_video_game_in_sweden_cxt_ideas.txt | 563 | 8db195e24487f97fbdcc8429c8c5c80672e17eb957fbeca1d9ff75e3e1b00e29 |
| common/dynamic_modifiers/024_video_game_in_sweden_dynamic_modifiers.txt | 5,754 | e1c38f8e712dee22af800746b0b15ff060ce4eca42349f6274a95c822db98004 |
| common/on_actions/024_video_game_in_sweden_lifecycle_on_actions.txt | 1,075 | c484096bed6686d1ed22f98492a2da56db4cbf4d9c52b993e5203e22ac8b8e31 |
| common/on_actions/024_video_game_in_sweden_cxt_on_actions.txt | 1,228 | 34ab09370af68a547cf69c99626c8a42c0dd4747efda7efe84fa75ae40905812 |
| common/opinion_modifiers/024_video_game_in_sweden_opinion_modifiers.txt | 791 | dff1d84b330cc2c2d82e3dd4d78c568aae8a55e5ab104b8bba0953c66a438a34 |
| docs/specs/024_video_game_in_sweden_specs/024_video_game_in_sweden_ai_probability_scenarios.md | 10,091 | 288cd312f9bedac91159f970cce16ed6dcf71dfb1d459411360dea0a355b34ca |

The broad shared worktree was not clean: git status reported 717 entries. None of the 17 in-scope Event24 source paths above had a status entry at capture. Unrelated shared-tree work was preserved.

## Current-source timing facts

The current source has three MTTH entries at common/mtth/024_video_game_in_sweden_mtth.txt:15, :60, and :130. They are read by video_game_in_sweden_advance_evolution_progress in common/scripted_effects/024_video_game_in_sweden_effects.txt:4146-4164.

This is an MTTH-derived pace accumulator sampled by the Event24 maintenance event, not a native daily event hazard. Each eligible monthly maintenance adds the MTTH pace multiplied by maintenance_days to that evolution’s persistent progress variable; the evolution begins when its progress reaches its configured threshold. The thresholds are 120, 150, and 120 days for Evolutions I, II, and III, and maintenance_days is 30. Separate Policy adds a further 90 days to Evolution III’s threshold. No time distribution or median is claimed from those source facts.

| Pace entry | Base and source modifiers | Additional source gate or timing input |
| --- | --- | --- |
| video_game_in_sweden_evolution_i_pace | Base 1.0; war 1.4; army experience below the configured gate 1.25; Officer route or completed Officer League 1.4; recent victory 1.2; Controlled route 0.75; Red Team complete 0.7; Field Validation success 0.6; recently admitted mismatch 0.75. | Eligibility requires baseline phase, evolution enabled and unrecorded, Chaos at least 200, and either Reliance at least Habit or an Officer-route/league/high-Chaos-opening flag. |
| video_game_in_sweden_evolution_ii_pace | Base 1.0; Commercial route 1.3; each of the one-season and two-season predicates adds a separate 1.2 factor; high War Support together with high global threat 1.2; recent victory 1.2; licensing days or a foreign response 1.15; completed Officer League together with expanded access 1.2; protected shifts 0.7; Separate Policy 0.7; low stability 0.75; Red Team complete 0.8; auxiliary doctrine 0.85; Field Validation success 0.8; recently admitted mismatch 0.8. | Eligibility requires broad public reach, Chaos at least 400, Reliance at least Doctrine, enabled/unrecorded Evolution II, and either Evolution I active or the commercial baseline route. |
| video_game_in_sweden_evolution_iii_pace | Base 1.0; competitive command culture or completed Officer League 1.25; public exhibition or at least one national league season 1.2; no Field Validation success 1.15; recent victory 1.2; Totalen Chaos 2.0; Red Team complete 0.7; protected shifts 0.8; recently admitted mismatch 0.75. | Eligibility requires active Evolution II, enabled/unrecorded Evolution III, Chaos at least 600, and Reliance at least Worldview. Separate Policy adds 90 days to the 120-day progress threshold. |

The global-threat and War-Support thresholds for Evolution II are both 0.5. The Totalen pace factor for Evolution III applies only when Chaos exceeds 799.

Evolution I and II can begin immediately from qualifying high-Chaos openings: the Officer opening invokes Evolution I at Chaos 200 or higher, while the Commercial opening at Chaos 400 or higher sets broad reach and Doctrine Reliance and invokes Evolution II. Those immediate-opening paths are separate from P24-E1A through P24-E3B’s monthly pace scenarios. Evolution III is not invoked in that opening chain; its progress starts after Evolution II is active and its progress variable is reset.

## Named timing scenarios and completeness

The only accepted timing scenario IDs are P24-E1A, P24-E1B, P24-E2A, P24-E2B, P24-E3A, and P24-E3B. The full accepted matrix is copied byte-for-byte under fixtures/024_video_game_in_sweden_ai_probability_scenarios.md.

| Scenario | Accepted state and expected comparison | Candidate pool and unresolved inputs |
| --- | --- | --- |
| P24-E1A | Gathering Storm, Reliance 30, Controlled route, one successful exercise, Red Team active, peace; slower than the base target. | One relevant pace entry is identified. Host, baseline phase, progress counter, exact Chaos, army experience, current route and Red Team receipts, and whether the exercise sets a pace-read flag remain unbound. The MTTH entry contains no direct ordinary-exercise check. |
| P24-E1B | Gathering Storm, Reliance 45, formal Officer League, war, no Field Validation; materially faster than E1A. | One relevant pace entry is identified. Host, starting phase, program/progress counters, army experience, league receipt, and whether this is the immediate high-Chaos Officer opening or a timed baseline route remain unbound. |
| P24-E2A | Rising Chaos, Reliance 55, Commercial route, protected shifts, play separated from policy, high stability; slower than the base target. | One relevant pace entry is identified. Broad public reach, current phase, exact stability, active policy/protection receipts, host, progress counter, War Support, and global threat remain unbound. |
| P24-E2B | Rising Chaos, Reliance 65, two league seasons, foreign licensing, high world tension; faster than E2A and the base target. | One relevant pace entry is identified. Season count, licensing days/response count, public reach, phase, host, progress counter, War Support, and global threat are not bound. The high-tension modifier requires both War Support above 0.5 and global threat above 0.5. |
| P24-E3A | Chaos Tier, Reliance 78, Red Team active, recent successful Field Validation, Separate Policy; eligible but slower than E3B. | One relevant pace entry is identified. Active Evolution II, the Field Validation receipt, Red Team/protection flags, Separate Policy, host, exact Chaos, and progress counter are not MCP-bound. D16’s supplied-unit proof remains unresolved pending user approval. |
| P24-E3B | Chaos Tier or Totalen Chaos, Reliance 90, Officer League and national league active, no recent validation, apparent prediction successes; faster than E3A, with a separate review interval. | One relevant pace entry is identified. Active Evolution II, league/exhibition state, validation absence, victory/prediction receipt, host, exact Chaos, and progress counter are not bound. The “several apparent prediction successes” description maps in the MTTH entry to a recent-victory flag, not a success count. The Totalen factor only applies above 799 Chaos. |

The local three-entry MTTH catalog is source-complete. The adapter did not return input discovery, poolComplete, external-factor coverage, a scenario hash, a source revision, a timing trace, or an analysis ID. The six scenario conclusions are therefore unresolved, not empty and not exact. The fact that all three symbols exist in source is not proof that the adapter interpreted the progress accumulator correctly.

## Opening candidate pool P24-O1 through P24-O4

The current Event24 entry is chaosx.nr24.2. Its complete source-local option pool is chaosx.nr24.2.a Controlled Staff Trial, chaosx.nr24.2.b Civilian Commercial Release, and chaosx.nr24.2.c Competitive Officer League. Their raw ai_chance bases are 4.0, 3.0, and 2.0. These are option weights, not normalized probability outputs.

| Candidate | Current raw modifier trace from events/024_hearts_of_iron.txt and constants | Scenario relevance |
| --- | --- | --- |
| Controlled Staff Trial | Peace 1.8; low stability 0.5; severe crisis 8.0; democratic 1.5; neutral 2.0; fascist 0.4; low-autonomy subject 1.5; Totalen Chaos 0.5; low army experience 0.7. | O1 and O4 expect it to lead. Crisis validity and the current Swedish host are not MCP-bound. |
| Civilian Commercial Release | High stability 1.5; war 0.4; severe crisis 0.0; communist 1.6; fascist 0.4; low-autonomy subject 0.6; high global threat 1.5. | O2 permits this to be close to Controlled. O4 expects it near zero or invalid. |
| Competitive Officer League | War 2.0; low army experience 1.4; supply-crisis flag 0.25; severe crisis 0.25; fascist 2.5; democratic 0.6; neutral 0.6; Totalen Chaos 2.0. | O3 expects it to lead. O4 expects it to remain low. |

This current inventory supersedes handoffs 19 and 21 where they say the opening lacks government/subject/Totalen modifiers or a high-tension modifier. Current source contains those modifiers. P24-O1’s “democratic or neutral” wording spans two distinct government factors. P24-O2’s high-tension factor applies only to Commercial. P24-O3’s “military or strongly authoritarian” wording is not a generic trigger; the current route factors explicitly name Fascist, Democratic, and Neutral governments. Good industry has no direct opening modifier.

P24-O1 through P24-O4 have a complete three-option pool at the source-definition level. Their external-factor pools remain incomplete: the accepted descriptions do not bind one exact government in O1/O3, numeric stability and army experience, valid host/event target, Stockholm ownership/control, the severe-crisis helper inputs, current supply state, event-enabled state, or exact Chaos value. No poolComplete result was returned. Any option share would be conditional on chaosx.nr24.2 firing and would not include the event’s own firing chance.

The accepted ordering requirements remain O1 Controlled dominant; O2 Controlled and Commercial close; O3 Officer dominant with Controlled credible; and O4 Controlled first with Commercial near-zero/invalid. No MCP ranking or conditional share was returned, so all four orderings are unresolved.

## Rulebook Commander trait and random result

The current trait is video_game_in_sweden_rulebook_commander in common/unit_leader/024_video_game_in_sweden_traits.txt. It is a land personality trait with +1 attack, +1 planning, and -1 logistics. new_commander_weight has factor 0, so it is not assigned through ordinary leader generation. The retired Field-Validated Planner trait is absent from this trait file.

video_game_in_sweden_roll_rulebook_commander in common/scripted_effects/024_video_game_in_sweden_effects.txt:967-992 has a complete local two-entry random_list: video_game_in_sweden_commander_chance and video_game_in_sweden_commander_miss. The miss weight is initialized to 100 minus the current chance and clamped to the 0–100 range. Source constants provide raw chance inputs of 20 for the Officer opening, 35 for Competitive Command Culture, and 25 for Officer League formalization. These are source weights/inputs, not MCP-confirmed probabilities.

Each roll is gated on the commander not already being granted, a positive chance, and at least one assigned army leader with units. On a successful roll, target assignment first samples among eligible serving field marshals with units; generals are sampled only if no eligible field marshal exists. At most one successful grant is retained by the program flags and stored leader target.

A failed roll does not set an attempted/consumed receipt. Later qualifying source calls can therefore roll again while no commander has been granted. The source has separate opening, Competitive Command Culture, and Officer League opportunity paths, including configured 25-point call sites. The aggregate campaign chance and the exact opportunity count for each route are unresolved; no multiplication of per-roll values was performed.

The random_list’s two outcome weights are complete at source level, but the dynamic eligible commander roster is incomplete without a declared campaign leader catalog. The nested random_unit_leader target pool has a field-marshal-first rule and cannot be treated as one complete uniform pool across all Swedish leaders. The probability route returned no candidate trace or target-validity result.

The commander opportunities map to already accepted scenarios rather than a new scenario ID: the opening roll is conditional on the Officer option in P24-O1 through P24-O4, with P24-O3 the route-aligned militarized case, and the Evolution I Competitive Command Culture path is P24-C2. Those scenarios were not separately evaluated for the commander roll.

The current source establishes an at-most-one successful assignment, not a guaranteed eligible trait and not a one-attempt-per-program rule. Whether misses should preserve later opportunities is a design/acceptance question for the owner; this auditor sets no chance target and recommends no numeric change.

## MCP evidence and completed outcomes

Workspace ID: mod_chaos_redux_ea3b2d67c2c0.

Parent-reported probability baseline: probability_inspect on common/mtth/024_video_game_in_sweden_mtth.txt with the default adapter and refresh=false timed out after 600 seconds. Parent also reports that full Event24 state_flow and focused root lint timed out after 600 seconds, while reference/source/script_validate routes returned partial evidence. Current source regression coverage is 33 runtime cases plus six lifetime cases, totaling 39, alongside 87 raw immutable byte checks. These parent results were not rerun by this auditor.

This auditor first called probability_inspect for event_mean_time_to_happen on common/mtth/024_video_game_in_sweden_mtth.txt. The request remained pending and returned no CallToolResult, source revision, scenario hash, candidate trace, or artifact. A retry narrowed to the three named pace entries likewise produced no result before the client cell was stopped.

After the parent’s latest instruction, one corrected narrow request used the default adapter, refresh=false, source path common/mtth/024_video_game_in_sweden_mtth.txt, and candidatePool containing only video_game_in_sweden_evolution_i_pace. No structured result or analysis identifier was observable before its client handle disappeared. This is unresolved service evidence, not PROBABILITY_SURFACE_EMPTY. The route was exposed and its live top-level schema was available, but the weighted analysis did not return.

No separate probability_inspect request was queued for the event_option_ai_chance or random_list adapters after that corrective pacing request, following the user’s instruction to finalize without further weighted requests. Their O1-O4 and commander probability conclusions therefore remain unresolved without adapter-specific evidence.

No probability_evaluate or probability_sweep result exists for P24-E1A through P24-E3B or P24-O1 through P24-O4. They were not submitted after inspect produced no required-input report, candidate trace, poolComplete flag, or scenario hash. No probability_simulate call was justified because the accepted scenarios define no probability distribution or seed. No probability_sequence call was justified for the commander draw because no complete manifest of all route opportunities, cadence, eligibility, failure transitions, and terminal state was submitted. probability_render was unavailable without an analysis ID. probability_compare was intentionally not run because this is a prepatch baseline; the owner will request the mandatory same-scenario comparison after the next source tranche.

Structural event inspection returned code EVENT_INSPECTED_PARTIAL for selector kind=event, eventId=chaosx.nr24.1, downstream trace, maxDepth 6, maxNodes 100, and maxEdges 200. Workspace revision is 8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0; graphHash is d494c41cf68a6eb896650d0f95ea38572ce93b8c83273a07a92d60c74eb41ceb. The linked event trace artifact is hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1df20004196875ff0df251ad5d007284a99b1d4125c7cd5dd6f29966973280d5/90fb053b5e0d01764328a373c38d561081e49aa974ca78013423527ea5e822a3/event-trace-8f4a82aa5d84.json.

The event inspection is focused and partial, with 2,285 diagnostics, 10,444 unresolved nodes, helpers=0, and the inline inventory limited to 64 of 403 paths. It is structural context only, not timing or probability evidence. Event_render was attempted first for a timing view and then retried with depth 1 and 20 nodes; neither call returned a rendered artifact before its client cell was stopped.

Reference context/search/read responded. The context result was limited to two sections and listed omittedSources, so targeted references were read. Offline wiki evidence includes AI modding MTTH blocks at lines 26-37, revision 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818; Event modding options at lines 151-179, revision 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d; and Effects random effects/random_list at lines 4504-4568, revision 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c. Installed game documentation for random_list was read at documentation/effects_documentation.md:5413-5432, revision 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af.

Source_lookup’s symbol query for video_game_in_sweden_evolution_i_pace returned a complete workspace-index response with definitionCount=0 at revision 247a4e713770ab567b1d6d34dfa2e0a241b3b6d86d41d972f035dcfd2890bdb1. A corrected path/line batch did not return before the client cell was stopped. The exact source was independently read from the current physical files listed above. A vanilla source_lookup request for game:events/AAT_Generic_Events.txt line 42 returned the source location and key path at revision 8a069c1e5049b5f1356f651580963c6afa9dba88b3a039db153d06d61194b243, but that line is a comment and supplied no event-option definition.

The Probability workflow’s exact blocker is missing weighted-tool results, not an absent tool registration. No probability result should be replaced with source arithmetic or memory.

## Validity, dominance, repetition, and uncertainty

No MCP result confirmed opening option ranks, rank reversal, conditional share, poolComplete, MTTH-derived timing, sampled timing, or sensitivity breakpoints. No candidate is declared dominant or starved by an evaluated probability result.

Source-level validity guards exist for a current Swedish host, event-enabled state, evolution phase, Chaos gate, Reliance threshold, and the commander’s assigned-army-leader requirement. Their runtime bindings and external state were not confirmed by the probability adapter.

Commercial Release has a source factor of zero in the severe-campaign-crisis case. The crisis predicate and complete O4 inputs were not evaluated, so this is a conditional source weight observation, not a confirmed campaign selection result.

The commander’s successful grant is bounded to one per program, while failed rolls leave later opportunities open. This creates a route-dependent repetition/cumulative-chance question. Its magnitude is unresolved because the attempt sequence and eligible leader pools are incomplete and no MCP trace returned.

The E1 MTTH entry does not directly inspect an ordinary controlled exercise. The E2 tension modifier requires both high War Support and high global threat. The E3 “several apparent prediction successes” scenario maps to a single recent-victory flag in the current pace entry. E3 has no separate below-base multiplier for a completed field validation; the source instead removes the above-base “unvalidated” factor, while Red Team and other safeguards provide their own modifiers. These are source-to-scenario mapping findings, not balance conclusions.

The Totalen factor in E3 applies only above 799 Chaos. A P24-E3B case described only as Chaos Tier must not silently be treated as Totalen.

## Recommendations, not applied

1. When the weighted route responds, begin with probability_inspect for each specific pace symbol and the complete opening option pool, then evaluate P24-E1A through P24-E3B and P24-O1 through P24-O4 with explicit actor, stage, host, flags, state values, progress counters, and any scheduled changes.
2. Sweep the source thresholds and input boundaries only after the adapter reports its accepted paths and required inputs; keep incomplete host, phase, roster, and campaign facts unresolved.
3. Inspect the two-outcome commander random_list separately from the field-marshal-first/general-fallback target selection. Declare each possible attempt route and the “miss leaves future rolls open” state transition before claiming an aggregate campaign chance.
4. Preserve the owner’s current weights and 120/150/120 progress thresholds until the owner reviews probability evidence. This audit selects no numeric replacement.
5. Keep P24-E3A’s field-validation input unresolved until the user answers the D16 supplied-division proof approval question.
6. After the owner’s source change, use the same named scenarios and immutable 2026-10-07 BEFORE files for the required probability_compare pass. Do not compare against the historical 2026-10-03 snapshots.

## Skipped analyses and remaining blockers

Probability evaluation, sensitivity sweep, seeded simulation, sequence analysis, probability rendering, and source comparison produced no results or were not run for the route and evidence reasons above. Event rendering produced no artifact. No live game, save, or desktop validation was performed.

The Evolution I/II/III option pools, incident-family weights, foreign response pools, the current 23-decision AI score race, host-ticket selection, and other event AI surfaces were not audited here because the parent scoped this baseline to evolution timing, P24-O1 through P24-O4, and Rulebook Commander. They require their own complete candidate pools and named scenarios.

The audit is incomplete for numeric probability, campaign timing, ranking, rank reversal, conditional option shares, commander target distribution, repeated-roll frequency, and balance signoff. The current source implementation is present; this handoff does not propose a pacing rewrite, does not choose weights or timing targets, and does not claim balance or Event24 completion.
