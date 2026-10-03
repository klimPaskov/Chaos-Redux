# Event 24 runtime and restriction localisation audit

Status: bounded read-only source audit completed with actionable owner repairs, visual and native acceptance blocked.
Acceptance basis: the parent explicitly assigned this audit on 2026-10-03 and made every file in `docs/specs/024_video_game_in_sweden_specs/` binding.
All 16 specification files, report 16, audit 20, AGENTS.md, and the full events, decisions/missions, and subagents skills were read.
The explicit retirement of Field-Validated Planner and deliberate `SWE_wargames` selection remain binding.
Only this handoff was written.
No gameplay, YAML, scripted localisation, asset, workbook, export, index, or commit was changed.
No service restart or Hearts of Iron IV launch occurred.

## Findings that need owner repair

### L24-1: restriction report describes work that has already finished

Source: `events/024_hearts_of_iron.txt:503-531`, `common/scripted_effects/024_video_game_in_sweden_effects.txt:1573-1598,2865-2876`, and `localisation/english/024_hearts_of_iron_l_english.yml:70-73`.
Successful enforcement closes the programme, clears its global host target through ownership-aware cleanup, records the pending report on the country, and queues `.34` for one day later.
The report trigger deliberately accepts the closed country receipt without requiring the cleared global target.
Its only success option acknowledges the receipt, rather than starting enforcement.
However, `.34.d` says the office reports whether the order has held, and `.34.a` tells the player to seal the cabinets and publish an order already issued.

Recommended exact replacements in the existing English YAML:

- `chaosx.nr24.34.d`: "The Ministry has closed the officer leagues, removed tournament scores from policy papers, and returned the public playing rooms to municipal custody. The restriction office has received all three departmental receipts and closed the programme."
- `chaosx.nr24.34.a`: "File the three departmental receipts."

Keep `.34.b` localised and retain the owner’s failure/cancellation design.
The current invalid-system path does not establish delivery of a failure popup, so this audit does not invent a new visible failure outcome.
There is no missing `.34` title, description, or option key.
`.91` and `.90` are hidden receivers without visible title, description, or options and do not need invented visible labels.

### L24-2: restriction duration and backlash units need precision

Sources: runtime effects `125-147`, constants `160-173,335,346-347`, YAML `221-248`, and dynamic modifiers `59-62`.
The three receipts arrive at elapsed days 20, 40, and 60, derived from the existing 60-day proof constant.
The native mission timeout is 90 days.
Objective satisfaction at day 60 and engine mission resolution are separate claims.
The ten source tests verify the receipt boundaries and a single 90-day aftermath grant, but do not execute the native mission or expiry.

The existing hover already states that backlash lasts 90 days after enforcement.
It does not claim a permanent Stability debit.
Its `3%` wording should distinguish a flat Stability modifier from a proportional reduction and from the immediate reserve-limited payment.
Keep the modifier hidden and keep its description available without adding another staged idea.

Recommended `video_game_restrict_use_cost_tooltip`:

"Payment: £pol_power [GetVideoGameRestrictionPoliticalPowerCost]  £stability_texticon [GetVideoGameRestrictionStabilityCost]  £war_support_icon [GetVideoGameRestrictionWarSupportCost]. Each charge is limited to the reserve still available, so the order can be issued with exhausted reserves. After enforcement, resentment applies a temporary penalty of [?constant:video_game_in_sweden_cost.backlash_stability_display|0] percentage points to £stability_texticon Stability for [?constant:video_game_in_sweden_timing.backlash_days|0] days."

Recommended `video_game_restriction_mission_requirements_tt`:

"Complete the league closures, policy exclusions, and withdrawal of public playing rooms over [?constant:video_game_in_sweden_timing.restriction_proof_days|0] days. Enforcement requires no further payment."

The existing enforcement description is concrete and accurately explains the departmental sequence.
Retain it.
The three new receipt keys in `024_video_game_in_sweden_requirement_flags_l_english.yml:27-29` are present and meaningful.
Do not publish the private receipt flags or elapsed counter as new player-managed values.

### L24-3: upfront Trust text can show an unavailable date and an achievement condition as an action requirement

Sources: YAML `136,230,233,289-290,299-300`, scripted localisation `157-169`, and effects `video_game_in_sweden_start_trust_model`.
`GetVideoGameReassessment` requires an existing deadline.
The deadline is created by taking Trust the Model, so its decision description can display "mandatory reassessment at N/A" before commitment.
The decision description and requirement tooltip also say a qualifying war must be found before reassessment.
That is achievement qualification, rather than a prerequisite to use the accepted peacetime surge.
Keep the opponent qualification in the achievement tooltip and retain all actual risk-route blockers.

Recommended `video_game_trust_model_desc`:

"Let the cabinet's forecasts direct military planning for up to [?constant:video_game_in_sweden_timing.trust_model_days|0] days. Simulation Reliance rises to §R[?constant:video_game_in_sweden_value.maximum|0]§!, strengthening planning at the cost of supply, recovery, and political attention. The government must reassess the programme when the term ends or a campaign crisis intervenes."

In `video_game_trust_model_requirements_tt`, preserve the existing Stability, surrender, crisis, and wartime resource conditions but remove its final stronger-opponent sentence.
Use the existing dated getter for an already active surge, rather than weakening its fallback to a fabricated date.

### L24-4: mission text leaves the player guessing about time, locations, and interrupted proof

Sources: YAML `126,132-133,236-245`, triggers `196-235,616-734`, runtime effects `30-75`, and mission resolvers `2773-2849`.
The field mission requires the named regional presence, Stockholm ownership and control, retained stores and fuel, a campaign supply-gap check, and either review.
Its full-success resolver separately rejects sticky resource or region interruptions.
The full audit uses all three named regions, while the narrow audit uses the one-region presence test and a different proof duration.
Both currently share a tooltip that describes only the full audit.
Neither division-presence trigger proves that the individual divisions are supplied.
The daily observer strengthens interruption evidence but does not repair that missing native predicate.

Required owner changes:

- `video_game_field_validation_resources_tt`: name Skåne, Södermanland, and Norrbotten using the existing `$STATE_138$`, `$STATE_141$`, and `$STATE_666$` tokens instead of "one field region".
- `video_game_field_validation_mission_requirements_tt` and `video_game_field_validation_mission_desc`: show `field_validation_proof_days`, require both ownership and control of Stockholm, and explain that an interruption prevents full success even after recovery.
- `video_game_reality_audit_regions_tt` and `video_game_reality_audit_mission_desc`: branch on `video_game_in_sweden_narrow_reality_audit_started`, using `reality_audit_proof_days` for the full audit and `narrow_reality_audit_proof_days` for the narrow audit.
- `video_game_reality_audit_requirements_tt`: show the existing `minimum_audit_stability` value, not merely "the Stability threshold".
- Reserve wording must describe the documented post-payment condition rather than imply an unspecified new commitment quantity.
Current retained-resource constants are zero with strict positive checks.
Supply-gap constants are three trains, twenty trucks, and one hundred fuel during war, checked separately.
Do not combine those into a fabricated supplied-division test or choose new reserve thresholds.

Recommended field proof wording, subject to the owning agent retaining the complete resource requirements:

"Keep [?constant:video_game_in_sweden_event.reality_audit_min_divisions_display|0] Swedish divisions in §Y$STATE_138$§!, §Y$STATE_141$§!, or §Y$STATE_666$§! for [?constant:video_game_in_sweden_timing.field_validation_proof_days|0] days. Own and control Stockholm, retain the required field reserves, and complete either the rail-table review or independent staff review. A recorded interruption prevents full success even if conditions recover."

This accurately describes the current regional count requirement without asserting per-division supply proof.
It is not an approved replacement for the accepted supplied-region or equivalent-front mechanic.
The accepted native supply and equivalent-front requirements remain blocked.
The full-audit logistics and red-team prerequisites also remain unreachable from some high-Chaos openings because the prerequisite decisions are confined to earlier phases.
Do not hide that route blocker by changing the requirement text.

### L24-5: duplicated visible predicates can expose the raw checks behind custom tooltips

`common/decisions/024_video_game_in_sweden_decisions.txt:676-681,708-713,740-745,772-777` calls each objective directly in `available`, then calls the same objective again inside a custom tooltip's hidden block.
The second call does not hide the first call.
The full audit and restriction actions follow the same duplicated-predicate pattern in their availability blocks.
The raw mission checks can therefore expose flags, numeric variables, state predicates, and stockpile conditions alongside the intended explanation.

Owner repair: keep one authoritative predicate in the custom tooltip's hidden condition, or explicitly hide the standalone duplicate.
Do not remove affordability or objective checks.
Do not introduce a visible localisation key for every private runtime flag as a substitute for hiding implementation-only checks.
Render verification remains required after the repair.

### L24-6: eight icon-bearing dynamic modifier names are missing

No localisation definition for these IDs was found anywhere under `localisation/`.
They have icons in `common/dynamic_modifiers/024_video_game_in_sweden_dynamic_modifiers.txt:9-57`, so native modifier names require coverage.
Recommended names, to add to the event-owned English YAML:

| Missing key | Recommended wording |
| --- | --- |
| `video_game_in_sweden_model_surge` | The Cabinet Directs the Campaign |
| `video_game_in_sweden_dual_track_package` | Independent Staff Comparison |
| `video_game_in_sweden_field_failure_penalty` | Unresolved Field Findings |
| `video_game_in_sweden_commercial_aftermath` | Municipal Campaign Clubs |
| `video_game_in_sweden_foreign_copy` | Swedish Training Tables |
| `video_game_in_sweden_foreign_study` | Study of Swedish Campaign Tables |
| `video_game_in_sweden_foreign_ban` | Restrictions on Swedish Campaign Tables |
| `video_game_in_sweden_foreign_ridicule` | Dispute over Swedish Campaign Tables |

These are names for existing effects, not a proposed new content batch.
The restriction-backlash name and description already exist.
Its lack of an icon is deliberate and must not become an asset request.

## Cost and icon crosswalk

All 17 paid actions have inline, blocked, and hover keys.
`video_game_conclude_trial` is free.
The suffix lookup agrees with the installed Chinese decision precedent and vanilla localisation.
The inline strings contain no more than three icon/value pairs.
The complete payment contracts contain no fifth spendable type.
Capacity requirements, regional control, divisions, and ongoing reserves are distinct from upfront spendable payments.

| Action suffix after `video_game_` | Spendable or reserved types | Inline coverage | Hover coverage and finding |
| --- | --- | --- | --- |
| `controlled_exercise` | Army XP, support equipment, fuel | All three | No missing fourth type |
| `logistics_module` | Trains, trucks, support equipment, civilian factory | First three | Factory shown, but its 45-day reservation is not stated |
| `expand_access` | PP, Army XP | Both | Present, prose repeats access rather than explaining its one-time extension |
| `rules_revision` | Army XP, command power | Both, dynamic levy | Escalation explained, preserve the dynamic values |
| `field_validation` | Fuel, support equipment, trains, Army XP | First three | Fourth shown, retained reserves remain vague |
| `red_team` | PP, Army XP | Both | No missing cost |
| `officer_league` | Command power, Army XP | Both | No missing cost |
| `national_league` | PP, civilian factory | Both | Add actual native reservation duration |
| `protect_shifts` | PP, civilian factory | Both | Add actual native reservation duration |
| `preparedness_clubs` | PP, support equipment | Both | No missing cost |
| `foreign_licenses` | Convoys, PP, civilian factory | All three | Native decision reservation lasts 5 days, separate helper burden counter is 30 days |
| `separate_policy` | PP, Stability | Both | Hover repeats already visible two-cost debit and public reaction |
| `begin_reality_audit` | Army XP, support equipment, fuel, trains | First three through `video_game_reality_audit_cost` | Fourth shown, see L24-4 |
| `narrow_reality_audit` | Army XP, support equipment, fuel, trains | First three | Fourth shown, needs its own mission proof wording |
| `dual_track` | Army XP, command power, civilian factory | All three | Native action reservation is 120 days, helper counter is 30 days |
| `restrict_use` | PP, Stability, War Support | First two | All three actual quotes shown, see L24-2 |
| `trust_model` | Command power, PP, Stability, War Support | First three | Fourth shown, preserve the four-type contract |

The factory reservations are real native `modifier = { civilian_factory_use = @VIDEO_GAME_DECISION_FACTORY_BURDEN }` blocks.
Do not misdiagnose them as absent simply because the helper only writes a burden counter.
However, native reservation duration follows each decision's `days_remove`, not the otherwise independently decremented helper counter.
National repeat helper burden is 60 days but the native row remains 45 days.
Foreign and dual-track duration differences require owner reconciliation, rather than a localisation promise based on the helper counter.
Add duration to cost hover text using the actual native duration constant after that reconciliation.
No cost icon was found missing: the eleven tokens resolve to installed vanilla definitions or the event's existing support-equipment and motorized-equipment texticons.
`£war_support_icon` is an existing vanilla sprite in `interface/topbar.gfx:257-259`, not a missing custom icon.
No new asset is recommended.
Blocked strings colour every amount red using one aggregate affordability result, even when only one reserve is insufficient.
Selective resource colouring is a dynamic-text opportunity, with native fit still unverified.

## Scripted localisation, encoding, and public value

Missing explicit event/option/description/custom-tooltip keys: none found in the inspected Event 24 sources.
Missing referenced scripted-localisation output keys: none found.
Duplicate keys: none found in the two event YAML files or among their keys across the English localisation tree.
Missing getter definitions: none found for their YAML consumers.
All 19 `GetVideoGame*` definitions were inspected.
Phase, status, mission, foreign-result, and incident enums use explicit equality and retain fallback output.
The existing phase, route, state, and result labels resolve to named YAML entries.
The cost getter helper calls preinitialize the exact temporary outputs they consume.
The payer preinitializes all three outputs before one coherent fresh quote and debit.
There is no scoped temporary-variable display token or formatting symbol embedded in the scripted-localisation file.

Restriction nominal fees remain `30 / 0.04 / 0.03`, bounded by nonnegative reserves.
The PP value key uses five decimals and percentage keys use three fractional percentage digits, preserving the documented five-place underlying precision.
The PP whole-number branch currently recognises only zero and the nominal full fee.
Thus an integral partial quote such as 25 takes the five-decimal branch.
That is precise but unnecessarily wide, not a payment discrepancy.
Consider a verified integer branch only if the native row proves the width matters.
Do not round fractional quotes or use display values to govern payment.

The category prints `simulation_reliance` once and exposes no second player-managed numerical value.
Phase, next threshold, mission status, and reassessment are context, not extra meters.
No receipt count or internal supply score should be added to that header.
Both English YAML files have UTF-8 BOM and valid language headers.
No encoding concern was found.
The three state-name tokens resolve in installed English localisation to Skåne, Södermanland, and Norrbotten.
Source name resolution is not map/supply evidence.

## Prose-quality findings within this tranche

| Category | Before | Actionable after or repair |
| --- | --- | --- |
| Vagueness | "for the proof period", "some trains", "the Stability threshold" | Use the existing duration and Stability constants, named states, and exact reserve condition in L24-4 |
| Bloat | `.34.d` has four sentences about formal restriction and whether it held | Two concrete sentences naming the three completed departments, L24-1 |
| Obvious explanation | `video_game_separate_policy_cost_tooltip` repeats its already visible two payments and explains the obvious Stability charge | Remove the repeated debit prose, retain any distinct ongoing consequence after owner review |
| Repetition | Mission `available` repeats the same objective outside and inside the explanatory custom tooltip | Keep one hidden authority predicate and one readable requirement, L24-5 |
| Overcomplication | `video_game_dual_track_desc` says "preserves a finite military benefit below Worldview until the verification is filed" | "Require the simulation staff to compare its forecasts with a second ledger of roads, stores, weather, and field reports. Simulation Reliance returns to §YDoctrine§!, and temporary planning support continues during verification." |
| Style-rule repair | `video_game_phase_baseline` says "Baseline trial" | "Staff trial" |
| Style-rule repair | `video_game_conclude_trial_desc` refers to "the chosen Swedish opening" | "Close the trial after its review and leave the useful papers with the officers, publishers, or clubs that ran it." |
| Style-rule repair | `video_game_validated_wargaming_methods_desc` begins "A finite recovery office" | "Swedish instructors retain the useful exercises and check their assumptions against field reports." |
| Mechanical/achievement leakage | Trust description says "a qualifying campaign must be found" and prints a pre-action deadline | Separate the action term from achievement qualification, L24-3 |

These are recommendations, not edits or accepted changes to mechanics.
No em dash, semicolon, modern gamer slang, or sourced quotation was found in the inspected Event 24 YAML passages.
The institutional language is generally specific and appropriate to the accepted dry satire.
The field/audit report bodies still describe generic verdicts instead of the actual selected full, partial, or failed result.
Outcome-specific descriptions are a useful follow-up once the owner settles the proof implementation.
Do not claim the full report proves supplied divisions merely by writing stronger report prose.
No actual sourced or attributed quotation was altered, and all dynamic tokens and formatting codes remain untouched.

## Cross-surface and spreadsheet handoff

The `.34` narrative mismatch and narrow/full mission mismatch are confirmed above.
The new restriction receipt labels match the source departments.
The backlash description names the closed leagues and returned municipal rooms and does not promise validated methods.
The category has only the accepted public Reliance value.
Achievement wording preserves the full Reality Audit, consecutive-year proof, and meaningful-war requirements rather than calling them supplied by these source tests.
Independent Dual-Track institutional proof remains incomplete in source: its objective checks elapsed days and Stockholm, not independent plans or comparison receipts.
Its text must not be treated as implementation evidence for that accepted mechanic.

The authoritative workbook was not opened or edited in this bounded pre-repair audit.
Current workbook equality is unresolved.
The old planning catalog snapshot is not evidence of current workbook contents.
No export was generated or edited.
After the owner settles final text, `chaosx_spreadsheet_doc_worker` must compare these exact existing keys with Event 24's Details and evolution fields:

- `chaosx.event_details.24`: "Sweden created an advanced campaign simulation from relay cabinets, projected maps, and printed scenario sheets. The military can use it for training and analysis. If its circulation widens, its categories may pass from staff officers into schoolrooms, factory schedules, and diplomatic files, where a tidy forecast can become an order."
- `video_game_in_sweden.evolution.1.title`: "The Staff College Takes the Board"
- `video_game_in_sweden.evolution.1.body`: "Swedish officers have made the cabinet part of professional culture, with rankings, repeated scenarios, and a growing dispute over what the tables truly measure."
- `video_game_in_sweden.evolution.2.title`: "The Nation Takes Its Turn"
- `video_game_in_sweden.evolution.2.body`: "Clubs, schools, newspapers, and workplaces have turned the Swedish cabinet into a public institution. Evening leagues alter factory shifts, teachers use its campaigns to discuss geography, and political organisers cite its simplified alignments in municipal halls."
- `video_game_in_sweden.evolution.3.title`: "When the Board Directs the Cabinet"
- `video_game_in_sweden.evolution.3.body`: "Senior offices are applying the cabinet's categories to transport, weather, production, diplomacy, and real operations."

These are current source wording for comparison, not a claim that the catalog already matches or authorisation to change its status.
The restricted-success popup is not a new evolution or catalog route.

## Meaningful validation and MCP blockers

The six actual-source lifetime tests were rerun through unittest discovery with `-B`, avoiding the script's JSON-writing main routine.
All six passed, including exact reserve quote/payment, getter output lifetime, PREV/current-host scope, and forwarded-output cases.
The ten tests in `tests/test_runtime_observation.py` were rerun with `-B` and all ten passed.
They cover daily elapsed advancement, sticky interruptions, one pending receiver, transaction-time Stockholm loss, early reassessment scheduling, stale-owner cleanup, idempotent closure, cloned host receipts, 20/40/60 enforcement boundaries, and one finite restriction aftermath without validated-methods reward.
They stub native predicates, record queued events without delivering them, and do not establish per-division supply, native mission timing, in-game expiry, save persistence, or rendered localisation.

Connected tool metadata exposes reference, source, event, GUI, decision, probability, and technology routes.
The existing read-only bridge was read completely and used without editing it.
Live initialization and `tools/list` confirmed `hoi4-agent-tools` version `3.6.0`, protocol `2024-11-05`.
The client sent empty capabilities, so no native task negotiation or helper-expansion execution is claimed.
Official installed `docs/events.md:27-36` confirms selector `{ kind: "event", eventId: "chaosx.nr24.34" }`.
Initial missing-kind selector probes were rejected and supply no inspection evidence.
The corrected bounded retries are recorded separately below.

| Read-only request | Exact outcome |
| --- | --- |
| Localisation reference context, limit 2 | `TimeoutError: MCP id 2 returned no result after 35s` |
| Exact `localization_key` reference search, limit 1 | First session timed out during initialization at id 1 after 35s, retry initialized then `MCP id 2 returned no result after 30s` |
| `.34` trace, corrected event selector, depth 1, nodes 2, edges 2 | `TimeoutError: MCP id 2 returned no result after 35s` |
| `.34` options render, corrected event selector, depth 1, nodes 2 | `TimeoutError: MCP id 2 returned no result after 35s` |
| `GetVideoGameRestrictionPoliticalPowerCost` source lookup, references disabled, one definition, twelve lines | `TimeoutError: MCP id 2 returned no result after 30s` |
| `video_game_restrict_use` decision inspection | Bridge raised `ValueError: Only read-only HOI4 tools are permitted` because `hoi4.decision_inspect` is absent from its fixed allowlist, despite live exposure of the read-only route |

Each owned bridge session returned `ownedSessionSurvivors: []` and an empty stderr tail.
No useful domain artifact URI, current MCP source revision, scenario hash, or numeric result was returned.
No reference-read id was obtained, so detailed references were read directly as permitted.
No successful render/compare or clipping, wrapping, alignment, or native row-fit acceptance is claimed.
The installed tool list does not expose `hoi4.decision_render`.
An event-chain graph or decision-source inspection is not a rendered native decision row.
Production GUI rendering remains the required one-to-one visual authority when available.
This audit does not dismiss unobserved defects as renderer differences.
No focus, technology, doctrine, dedicated scripted GUI, or map-edit surface is introduced by this tranche.
The shared GUI and map/supply acceptance limits in report 16 and audit 20 remain unresolved.
No probability target was changed or numerical proof inferred.

Standalone Technology Tree Viewer was checked separately against the exposed tools and the installed npm package's files and binary manifest.
The package has stdio, HTTP, and setup entry points and no standalone Technology Tree Viewer entry point or matching viewer file.
No separate viewer route is exposed here.
Record this as a package gap, not proof that technology inspect/render/compare are healthy or that no viewer could exist elsewhere on the machine.

## Direct reference evidence

All wiki reads used the repository's offline snapshot.
No Paradox wiki web access occurred.
Installed root: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`.

| Reference | Relevant read spans | SHA-256 revision |
| --- | --- | --- |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 63-93, 183-215, 659-788 | `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064` |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 430-446, caller-owned temporary output lifetime | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md` | 517-525, flat Stability modifier | `FE41A26F2B8D3B8E78A9B0DEA9CE1A55F001D1E27886807A0A3FB2D2F535F14F` |
| Installed `documentation\script_concept_documentation.md` | 217-240, constants and fixed-point access | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| Installed `documentation\dynamic_variables_documentation.md` | 431-442, numeric reserve readers | `538525747F0C285062C9CE8DB14B4E07C3CF6BAC1013115FA4F57291CB4EBDDA` |
| Installed `documentation\modifiers_documentation.md` | 4825-4833, country Stability modifier | `00A0ECA6D2B3A70CE4B8A0D38997DD609AA0C9349DDCD04C8CAC92849425BE7E` |
| Installed `common\scripted_localisation\00_scripted_localisation.txt` | 1-65, named-key and trigger precedent | `6F490E33736F4DC31568ADD5753A1AFDEF916F3993804FEBFBBE6D1583827587` |
| Installed `common\decisions\CHI_decisions.txt` | 271-298, custom cost precedent | `EFCEC834A71901A5DA66EEF97F8B817D1B7299C36F16E48893FF9F3918039068` |
| Installed `localisation\english\decisions_l_english.yml` | 169-171, cost/blocked/hover suffixes | `ED305836A44B0CE34CBB361F7EA5FF08C84DB51795F99C3EEB91A4606ECBF4A4` |

The installed `documentation\scripted_localisation_documentation.md` path is absent.
The actual installed scripted-localisation comments and vanilla definitions above were used instead.
That missing file is not represented as a successful reference read.

## Audited source identities

These hashes bind the inspected shared-tree state and are not immutable replacement snapshots.
The parent must recheck affected findings if other agents edit these files before repair.

| Source | SHA-256 |
| --- | --- |
| `localisation\english\024_hearts_of_iron_l_english.yml` | `B592952DE06CF1EC8E14007750A669F6858D6236B30043C6C1F8CE77B1E1B1B0` |
| `localisation\english\024_video_game_in_sweden_requirement_flags_l_english.yml` | `E4BC29C9A933D871C5F8F3ADEA10E331D92585478569B2F5B86EB941547866A8` |
| `common\scripted_localisation\024_video_game_in_sweden.txt` | `8D1D97965BBCDD572503950684BB8677D10BB65A124146BBBB20011E616A92AD` |
| `common\scripted_effects\024_video_game_in_sweden_effects.txt` | `0C2150446C29082BF684301D885375E9A3C516F7598F80F470C70EB7EF7A6223` |
| `common\scripted_effects\024_video_game_in_sweden_runtime_effects.txt` | `4AA52824D237180D59C2E57E8C23D4DC5A6841B93D243E779004F20466B89EFB` |
| `common\scripted_triggers\024_video_game_in_sweden_triggers.txt` | `3904B9A6DB454C6C6ABADAF5421514B354D1BD72F0563A2B9AD31C8CCB41EB48` |
| `common\decisions\024_video_game_in_sweden_decisions.txt` | `8B19FCB187FF40BCFD66C49FF54EC18B009D5724CC6D74EC5BC416AF463B6EEF` |
| `common\script_constants\024_video_game_in_sweden_constants.txt` | `A498C1C0458A69B9E377EFEB0A4E3D4C94828185DB48797E520E1DC1E6159C19` |
| `common\dynamic_modifiers\024_video_game_in_sweden_dynamic_modifiers.txt` | `E78B8FA660C12808FD36E0F4E0F3BF951BF79F9B8871E83A053590741DE34670` |
| `events\024_hearts_of_iron.txt` | `36A3BE4F03A942E08EA6DC3BDB3C20A8E112A54D667BDA91D031BEAECC51C159` |

## Disposition and owner handoff

Completed: named localisation/source comparison, cost/icon coverage, getter and enum review, quotation/token preservation review, six lifetime and ten observer source regressions, bounded MCP retries, and this report.
Owner repair required: L24-1 through L24-6, factory-duration reconciliation, and prose recommendations within this tranche.
Blocked: rendered popup/category/row fit, native localisation evaluation, native supplied-unit and equivalent-front proof, full-audit prerequisite reachability, independent Dual-Track proof, and current workbook equality.
Keep all other accepted unresolved items in report 16 and audit 20 unresolved or accepted and queued.
No simplification was applied or approved.
No new expansion plan was written because these gaps already belong to the accepted owner implementation.
Changed gameplay files and keys: none.
Dynamic localisation added or fixed by this auditor: none.
Before/after gameplay and display: unchanged by this auditor.
Skills used: chaos-redux-events, chaos-redux-decisions-missions, and chaos-redux-subagents.
No skill was created or updated.
The main agent owns repair, final review, any required probability comparisons, spreadsheet alignment, and the repair commit.
