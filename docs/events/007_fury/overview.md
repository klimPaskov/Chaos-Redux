# Event 007: Fury

Fury is a minor repeatable event in the Wars cluster.
The current cluster registration has one primary Medium row, `wars_fury`.
One ordinary entry selects an eligible AI minor, gives its army a finite mobilisation package, and starts a bounded weekly country-event chain.
Player countries, their allies, and their subjects cannot become the initial actor.
An actor needs at least one legal neighbouring target.
Its army attacks without an ultimatum, regroups after victory, and pauses when no legal target remains.

## Entry and reports

Canonical entry `chaosx.nr7.1` uses `fury_prepare_random_event_fire`.
The shared Settings preparer retains its result so the hidden entry does not create the country twice.
A failed manual request gets `.3` and is not counted as a dispatched ordinary event.
One immediate `.7008` World News tells observers about the new batch and uses its first country as the representative.
Simultaneous new actors are summarised in that one bulletin.
The AI actor receives `.2` internally, scans a target at day two, and runs `.20` weekly.
`.30` requires actual territorial gain or an annexation proof before recording the first conquest.
The campaign sends `.7007` conquest news once.

An uninvolved observer receives one custom opening news per outbreak batch, plus the first-conquest news once across the campaign.
The larger escalation and terminal branch have their existing super-events.
Terminal seed failure, initial player notice, subsequent target notice, and terminal defeat are separately guarded milestones rather than repeat weekly reports.

## Army, occupation, and costs

The Fury Column template has six infantry battalions and an engineer company.
Starting strength is 5, 7, 10, or 14 columns, and initial finite reserves are 8, 12, 16, or 20.
Scenario intensity supplies its separately capped reserve bonus.
The weekly loop draws one reserve while any remains, with a lifetime grant cap of 100.
Normal recruitment remains available afterward.
Depot Cadres adds three reserves and Depot Officers adds two through that cap.
Their finite direct recruitment waves use a separate helper and do not bypass a paid-decision receipt.

A paid wartime deployment releases exactly one reserve column for 15 command power, 610 rifles, 40 support equipment, and 6,300 manpower.
The 610 rifles and 6,300 men match the declared base template, and the support charge includes deployment stores.
The action rechecks its actor, focus, reserve, owned deployment state, and resources before payment.
The cost row shows three values and its full tooltip contains all four.
Each component's ready or deficient colour is calculated from the same exact quote and inclusive native affordability used by the payer.

Occupied states have registration, rail work, garrison/crisis missions, and one chosen administration or forced-march coring route.
The ordinary administration path spends CP, manpower, rifles, and support stores.
The forced-march path spends CP, manpower, rifles, and stability.
The basic garrison mission yields to the crisis restoration mission rather than duplicating it.
The source-level category budget is six primary actions, with automatic mission status rows counted separately.

## Focuses, cooperation, and rivalry

The shared AI tree has 52 focuses covering mobilisation, army, expansion, occupation, cooperation, rivalry, and terminal preparation.
War Office access and paid depot deployment are unlocked by their existing focuses.
A paid early Evolution II route choice locks the opposite focus route.
Other Fire Answers admits eligible non-rival commands to the project pact, and Pact Command opens reserve sharing.
This project pact uses membership flags before a native faction is created by a scenario or terminal setup.
Rival wars wait until ordinary neighbours are exhausted, except for the explicit Hostile Fury challenge.
Rival map claims favour a legal third-country target already being pursued by an active non-allied rival.
The last surviving rival has an alternative terminal-preparation path.
The main native pact replaces the rivalry idea rather than stacking the two route spirits.

## Evolutions and manual setup

Hardened Fury improves the existing army and mobilisation policy.
Two Fires introduces cooperation/rivalry through additional actors.
All Borders enables simultaneous neighbour declarations.
The shared evolution checkboxes gate these content branches.
Manual challenge intensity bypasses the chaos-tier prerequisite but still honours each disabled-stage checkbox.

The World in Fury challenge supports Fury Pact and Hostile Fury, with up to 2, 5, 9, or 16 eligible countries.
It reports the actual count through one opening bulletin, and a zero-country setup gives a rejection report without forming a ghost pact.
Country eligibility and player protection remain the same as ordinary selection.

## Terminal branch and cleanup

Terminal Fury requires the existing final chaos tier, candidate focus path, readiness, enough eligible seed countries, and enabled world-end Settings.
It is separate from the manual challenge.
It forms a native pact, seeds continents, issues one initial human notice, and dispatches slot 60.
The lesser slot 59 cannot also fire in the same weekly call.
Actors that become major or pass the existing territorial threshold maintain the Fury world-threat source.
Cleanup removes the actor's ideas, obsolete decisions, missions, current targets, and campaign values.
Country callbacks and delayed actor events make cleanup idempotent.
Native faction departure is limited to known currently Fury-led factions, preserving unrelated or non-Fury-led surviving alliances.
Past Event Log country IDs remain historical data even when the live representative pointer is cleared or retargeted.

## Achievements and integration

Ten existing Fury achievements use local participation and specific outcome proof.
War participation and completed Border Watch are keyed to their actor so unrelated campaigns cannot lend one another proof.
The Event Log uses the first ordinary batch actor, evolution entries retain their own representative, and shared Event Details describe the premise.
The former numeric Reach, Cohesion, and Compliance Drive accumulators were not consumed by gameplay.
Their removal does not remove the real compliance-growth idea, native state compliance, preparation scores, project membership, or physical supplies.

## Assets and audio

| Consumer | Sprite or runtime file |
| --- | --- |
| Reports | `GFX_report_event_fury_war_office`, `gfx/event_pictures/007_fury/fury_war_office.dds` |
| Opening news | `GFX_news_event_fury_begins`, `gfx/event_pictures/007_fury/fury_begins.dds` |
| First conquest | `GFX_news_event_fury_first_conquest`, `gfx/event_pictures/007_fury/fury_first_conquest.dds` |
| Major cue | Slot 59, `GFX_super_event_fury_becomes_a_state`, audio 29 |
| Terminal cue | Slot 60, `GFX_super_event_world_in_fury`, audio 30 |
| Diplomacy overlay | `GFX_fury_leader_flame_overlay_animated`, eight-frame sheet with its static fallback |
| Focus/idea/decision/achievement icons | Existing registered Event 007 asset families |

Original opening-news generation, crop, native-size preview, DDS round-trip, and hashes are recorded in `docs/assets/007_fury/opening_news_2026_10_05/`.
The existing quote/audio source notes remain in the shared super-event documentation.
Existing missing historical provenance is not supplied by the new opening package.

## Validation and remaining work

Acceptance and source repairs are listed in `docs/plans/007_fury_plans/agent_decisions_2026-10-05.md`.
The complete event, helper, focus, decision, localisation, probability, cost-display, and GUI handoffs are in that plans folder.
Source models cover caller lifetime, finite reserves, real deferred financial receipts, resource conservation, correlated achievements, and per-resource display boundaries.
MCP domain inspections/renders/comparisons did not return final acceptance artifacts.
The long last-rival focus link and diplomacy overlay still require visual review, and numeric AI balance is unresolved.
The older unaccepted Internal Fury and ordinary defeat-news proposals remain unresolved rather than completed.
Exact catalog mirror text is queued in `catalog_changes_pending.md`, and no workbook or CSV was edited.
Live acceptance cases for the orchestrator are listed in the completion report.
