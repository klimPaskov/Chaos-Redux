# Event 32 acceptance criteria

## Completion rule

Event 32 is complete only when every accepted requirement below is implemented, wired, documented, and validated.

A missing evolution, incomplete operation adapter, placeholder asset, unverified probability surface, stale workbook row, or unreported fallback blocks completion.

## Catalog and registration

- [ ] Event ID remains `32`.
- [ ] Event name is Missiles.
- [ ] Event type is Minor Repeatable.
- [ ] Minimum event chaos level is Calm World.
- [ ] Cluster remains unassigned.
- [ ] Entry event remains `chaosx.nr32.1`.
- [ ] Event 32 is registered in the repeatable-event array.
- [ ] Event type resolution returns Minor Repeatable.
- [ ] Repeatable weight recovery and cap reduction use the shared system.
- [ ] Event 32 remains disabled by default until the rework is complete.
- [ ] The completion change adds Event 32 to the reworked-event default enable allowlist.
- [ ] Event name, debug name, Event Details, and catalog mappings agree.
- [ ] Event list shows `N/A` when no valid recipient exists.

## Global firing

- [ ] One Event 32 firing counts as one global pacing event.
- [ ] Recipient pool is frozen before country mutations.
- [ ] Every valid recipient is processed once.
- [ ] Invalid, deferred, and skipped recipients have stable reasons.
- [ ] Human recipients receive one country report.
- [ ] AI recipients receive no popup.
- [ ] First global firing creates one global news item.
- [ ] Repeat firing does not create news spam.
- [ ] One Event 32 history row is recorded per global firing.
- [ ] Recipient processing does not create one history row per country.
- [ ] No recurring daily, weekly, or monthly global country scan is added.
- [ ] Chunked dispatch, if used, preserves one firing date and one repeatable transaction.

## Recipient validity

- [ ] Ordinary countries with controlled land qualify.
- [ ] Subjects can qualify.
- [ ] Landless governments in exile are deferred.
- [ ] Dummy and system carriers are excluded.
- [ ] Special chaos countries use explicit profiles.
- [ ] `is_special_chaos_country` is not a blanket exclusion.
- [ ] A special actor without command or industry is skipped.
- [ ] No site is placed in another country's state.
- [ ] One-state minors can receive a valid site.
- [ ] Country removal cleans program state.

## Technology progression

- [ ] Technology graph is inspected with `hoi4.tech_inspect`.
- [ ] Relevant folder or branch is rendered with `hoi4.tech_render`.
- [ ] Implemented graph changes are checked with `hoi4.tech_compare`.
- [ ] Normalized stages map to exact installed technology.
- [ ] One next valid technology step is granted per firing.
- [ ] Prerequisites and mutual exclusions are respected.
- [ ] Existing later technology is normalized correctly.
- [ ] Completed lines receive a mature package.
- [ ] No unrelated technology is granted.
- [ ] No nuclear, chemical, biological, or Kruger technology is granted by baseline Event 32.
- [ ] DLC and no-DLC paths are documented and functional.

## Program values

- [ ] Operational Reserve exists and cannot go below zero.
- [ ] Reserved missiles are separated from available missiles.
- [ ] Launch Readiness is clamped from `0` to `100`.
- [ ] Command Control is clamped from `0` to `100`.
- [ ] Guidance is derived and explained without adding an unnecessary permanent meter.
- [ ] Retaliation posture is a named state.
- [ ] One program idea or dynamic modifier summarizes current status.
- [ ] Status refreshes after every meaningful transaction.
- [ ] Program variables survive ordinary government and ideology changes.
- [ ] Cleanup runs on permanent country removal.

## Reserve accounting

- [ ] First package scales dynamically and is capped.
- [ ] Mature package scales dynamically and is capped.
- [ ] Replenishment uses real costs and cooldown.
- [ ] Launch preparation reserves missiles once.
- [ ] Launch completion consumes missiles once.
- [ ] Cancellation refunds or destroys missiles according to commitment state.
- [ ] Capture transfer debits former owner and credits new controller exactly once.
- [ ] Civil-war split preserves total reserve.
- [ ] Scuttling destroys a bounded exact amount.
- [ ] No free repeatable reserve loop exists.
- [ ] AI keeps its doctrine reserve floor.

## Launch-site selection

- [ ] First-site candidate pool is complete.
- [ ] Existing site upgrade has priority over unnecessary new site.
- [ ] Owned, controlled core states are preferred.
- [ ] Infrastructure, supply, defense, and strategic depth affect scoring.
- [ ] Active frontline states are strongly penalized.
- [ ] Occupied enemy states receive zero weight.
- [ ] Wastelands and invalid states receive zero weight.
- [ ] Empty isolated regions do not beat useful connected states.
- [ ] Capital is a fallback, not an automatic first choice.
- [ ] One-state minor uses its sole valid state.
- [ ] Secondary sites prefer another strategic region where possible.
- [ ] Site count cap scales with territory and program need.
- [ ] Saturation adds capacity without unlimited sites.
- [ ] Site-selection scenarios pass the probability audit.

## Site lifecycle

- [ ] Site level, capacity, hardening, security, damage, and compromise are stored.
- [ ] State tooltip communicates the site state.
- [ ] Damaged, disabled, destroyed, captured, and rogue states differ mechanically.
- [ ] Repair requires real resources and time.
- [ ] Hardening reduces damage and capture risk without granting immunity.
- [ ] Security reduces rogue risk.
- [ ] Site capture disables ordinary launch until resolution.
- [ ] Prepared operations tied to a captured site are cleaned.
- [ ] Civil war follows physical state control.
- [ ] Country releases use the inheritance contract.
- [ ] Annexation transfers or destroys reserve without duplication.
- [ ] Ownership and control differences are handled.
- [ ] Scuttled sites cannot launch.
- [ ] Site records are removed after destruction or cleanup.

## Decision presentation

- [ ] Event 32 uses a normal decision category.
- [ ] Static category picture is wired.
- [ ] Category header shows reserve, readiness, and command control.
- [ ] Technology, site count, guidance, selected target, and posture appear as compact states.
- [ ] Three to five main actions are normally visible.
- [ ] Six primary visible actions is not exceeded.
- [ ] One to three active missions is the normal cap.
- [ ] Emergency phases replace irrelevant routine actions.
- [ ] No fake buttons or meters are painted into the category picture.
- [ ] No full event-owned scripted GUI is added without a new accepted design.

## Decisions and costs

- [ ] Every action represents concrete work.
- [ ] No action has more than four spendable cost types.
- [ ] Every custom cost has a valid texticon.
- [ ] Political power is not the default program currency.
- [ ] Replenishment, readiness, guidance, security, hardening, capacity, and site construction have distinct costs.
- [ ] Costs scale dynamically where specified.
- [ ] Cooldowns and caps prevent farming.
- [ ] Blocked tooltips name exact reasons.
- [ ] Obsolete actions hide after completion.
- [ ] Targeted actions clean stale selected targets and states.
- [ ] AI uses the same payment and ability checks.

## Missions

- [ ] Site survey is a real timed project.
- [ ] Secondary-site construction is a timed project.
- [ ] Strike preparation is a timed project.
- [ ] Site repair and recovery are timed where appropriate.
- [ ] Warning verification uses a timed response window.
- [ ] Missions auto-complete when the objective is proven.
- [ ] Mission failure has distinct effects.
- [ ] Target invalidation has a precise cleanup path.
- [ ] No passive stockpile checklist is presented as a major mission.
- [ ] Mission durations vary by difficulty and urgency.

## Strike pipeline

- [ ] Actor, victim, exact target state, target profile, sites, reserve, payload, and incident ID are frozen.
- [ ] Operation has a valid state machine.
- [ ] Target is revalidated before commitment and launch.
- [ ] Prepared operation cannot silently retarget.
- [ ] Precision, strategic, counterforce, and saturation profiles have distinct costs and effects.
- [ ] Saturation is unavailable without its evolution and adoption.
- [ ] Exact site capacity is proven.
- [ ] Reach is proven through the accepted adapter.
- [ ] Launch cooldown is enforced.
- [ ] Readiness cost is applied once.
- [ ] Command burden is applied once.
- [ ] Operation cleanup clears every receipt.

## Conventional damage

- [ ] Damage scales with missiles that hit.
- [ ] Damage targets real building levels.
- [ ] Damage clamps at zero and existing levels.
- [ ] Logistics, industry, air and coastal, command, and counterforce profiles differ.
- [ ] Precision has lower spread.
- [ ] Saturation has broader damage and higher readiness cost.
- [ ] Target defense can reduce hits.
- [ ] Hardening protects launch sites.
- [ ] No empty state receives a high-value target result.
- [ ] Civilian losses scale with actual population and collateral factors.
- [ ] State population is reduced once.
- [ ] Deaths are registered once.
- [ ] Military deaths use a supported exact route.
- [ ] Conventional damage remains below nuclear and thermonuclear severity.

## Unreliable Guidance

- [ ] Evolution II has eligibility, MTTH, enable gate, log entry, and behavior.
- [ ] On-target, degraded, wrong-object, near-miss, breakup, wrong-state, neutral, self-strike, and site-accident outcomes are implemented where supported.
- [ ] Wrong-state pool is bounded and defensible.
- [ ] No unrelated world state can be selected.
- [ ] Barrage-level risk is bounded.
- [ ] High readiness and maintenance materially improve outcome.
- [ ] Severe neutral and self-strikes remain a minority of failures.
- [ ] Special-payload accidents call shared systems only after confirmed release.
- [ ] AI accounts for risk.
- [ ] Probability scenarios `GUIDE-01` through `GUIDE-07` are audited.

## Saturation Arsenals

- [ ] Evolution I has eligibility, MTTH, enable gate, log entry, and behavior.
- [ ] Saturation barrage exists.
- [ ] Reserve, capacity, replenishment, range, cooldown, and AI behavior change.
- [ ] Site cap remains finite.
- [ ] Large barrage requires several sites or sufficient capacity.
- [ ] Reserve floor logic remains active.
- [ ] Unreliable Guidance pressure increases with barrage size.
- [ ] Defense saturation is bounded.
- [ ] AI does not use saturation on low-value empty targets.

## Special Warheads

- [ ] Evolution III has eligibility, MTTH, enable gate, log entry, and behavior.
- [ ] Delivery integration is country-specific.
- [ ] No payload is granted by Event 32.
- [ ] Chemical delivery requires exact agent and stockpile.
- [ ] Biological delivery requires exact agent and stockpile.
- [ ] Nuclear delivery requires exact weapon stockpile.
- [ ] Thermonuclear delivery requires exact weapon stockpile.
- [ ] Every payload consumes missiles and payload once.
- [ ] Shared CBRN consequences are called once.
- [ ] Air Cleanliness is not duplicated.
- [ ] Condemnation is not duplicated.
- [ ] Deaths are not duplicated.
- [ ] Confirmed use is recorded only after release.
- [ ] AI respects policy, stockpile, condemnation, guidance, and survival.

## Rogue Launch Commands

- [ ] Evolution IV has eligibility, MTTH, enable gate, log entry, and behavior.
- [ ] Command-pressure model uses real vulnerability.
- [ ] One ordinary active crisis per country is enforced.
- [ ] Global crisis cap is enforced.
- [ ] Unauthorized launch preparation has a timed response.
- [ ] Mutiny, defection, regional seizure, bribery, captured threat, and payload custody have valid prerequisites.
- [ ] Foreign incidents require a valid foreign actor.
- [ ] Launch incidents require reserve and site.
- [ ] Physical payload custody is proven.
- [ ] Civil-war and occupation bridges work.
- [ ] AI can negotiate, isolate, assault, secure, and scuttle.
- [ ] Incident cooldown prevents spam.
- [ ] Probability scenarios `ROGUE-01` through `ROGUE-08` are audited.

## Automatic Retaliation

- [ ] Evolution V has eligibility, MTTH, enable gate, log entry, and behavior.
- [ ] Off, Supervised, Delegated, and Automatic postures exist.
- [ ] Posture adoption has requirements, costs, and cooldown.
- [ ] Warning records store source incident and attribution.
- [ ] Response windows are playable.
- [ ] Verify, delay, sever, isolate, redirect, accept, and restore actions work where valid.
- [ ] False warnings can be exposed.
- [ ] Forged signals require a valid actor and access.
- [ ] Retaliation creates linked incidents, not direct recursion.
- [ ] Generation cap is enforced.
- [ ] Country cap is enforced.
- [ ] Incident cap is enforced.
- [ ] One country responds once per root.
- [ ] No response occurs without a surviving site and reserve.
- [ ] Automatic posture is blocked at low control outside an incident route.
- [ ] Chain closes and cleans every warning.
- [ ] Event 32 never sets `world_end`.
- [ ] Fallout readiness remains owned by the shared consequence system.
- [ ] Warning and posture scenarios are audited.

## Shared systems

- [ ] Event 16 missile-crisis reaction bridge remains functional.
- [ ] Event 5 can split Soviet missile infrastructure.
- [ ] Event 6 can transfer inherited sites.
- [ ] Event 13 can damage sites through a narrow adapter.
- [ ] Event 21 can split programs in civil war.
- [ ] Event 23 nuclear stockpile remains separate.
- [ ] Event 76 remains separate.
- [ ] Chemical system owns chemical effects.
- [ ] Biological system owns outbreak effects.
- [ ] Nuclear systems own blast and fallout effects.
- [ ] Air Cleanliness receives each source once.
- [ ] Condemnation receives each public source once.
- [ ] Deaths receives each death once.
- [ ] Fallout remains the owner of its terminal consequence.
- [ ] Event Logs ownership is not duplicated.

## AI and probability

- [ ] Every weighted surface begins with `hoi4.probability_inspect`.
- [ ] Candidate pools are complete where normalization applies.
- [ ] Named scenarios are used.
- [ ] Sensitive thresholds use sweeps.
- [ ] Bounded chains use simulation where needed.
- [ ] Every weighted patch receives `hoi4.probability_compare`.
- [ ] Final result distinguishes exact, bounded, sampled, score-only, and unresolved evidence.
- [ ] AI maintains reserve and readiness.
- [ ] AI selects strategic targets.
- [ ] AI avoids allies and invalid targets.
- [ ] AI handles incidents and warning windows.
- [ ] AI respects chain caps.
- [ ] AI cannot create resource duplication.

## SCN-015

- [ ] Scenario ID is collision-audited.
- [ ] Raw Fallout reservation at ID 14 is respected.
- [ ] Registry, sort, type, intensity, confirmation, launch, and eligibility are wired.
- [ ] Five scenario profiles exist.
- [ ] Four intensity levels change setup.
- [ ] Scenario preflight is atomic.
- [ ] Failed preflight leaves no partial mutation.
- [ ] Bypass flags are scoped and cleared.
- [ ] Repeat launch is blocked or idempotent.
- [ ] Low Retaliation Network starts no destructive incident.
- [ ] Maximum Retaliation Network remains bounded.
- [ ] Special Payload Crisis grants no payload.
- [ ] Scenario sets no terminal flag.
- [ ] Scenario docs and workbook row agree.

## Assets

- [ ] Country report image exists and is wired.
- [ ] First-news image exists and is wired.
- [ ] Static decision category picture exists and is wired.
- [ ] Program idea icon exists.
- [ ] Required site modifier icons exist.
- [ ] Reserve, readiness, and command texticons exist.
- [ ] Every visible decision has a suitable decision icon.
- [ ] Every visible mission has a suitable mission icon.
- [ ] Raid icons exist or exact shared icons are documented.
- [ ] Eight achievement triplets exist.
- [ ] Source evidence and prompts are retained during active work.
- [ ] PNG previews and DDS files exist.
- [ ] Contact sheets and manifests exist.
- [ ] Final assets are in event-scoped runtime folders.
- [ ] Temporary event workspace is cleaned after evidence promotion.
- [ ] No placeholder or primitive drawing is presented as final art.
- [ ] No custom 3D or animation is added without a new accepted brief.

## Player-facing text

- [ ] First report follows the text direction.
- [ ] Repeat report follows the text direction.
- [ ] First global news follows the text direction.
- [ ] Strike reports name exact target type and state.
- [ ] Accidental incident reports use actual actor and victim evidence.
- [ ] Evolution text shows concrete change.
- [ ] Decision names state the public action.
- [ ] Blocked tooltips are precise.
- [ ] Event Details hides raw tuning and hidden surprises.
- [ ] Scenario wording hides internal bypasses.
- [ ] Achievement wording is final and route-specific.
- [ ] No instruction fragments or working labels remain in localisation.
- [ ] Localisation files use UTF-8 with BOM.
- [ ] Localisation keys omit `:0`.

## Achievements

- [ ] All eight planned achievements are implemented.
- [ ] Each achievement has tracking and disqualifiers.
- [ ] No achievement unlocks from one Event 32 firing.
- [ ] Scenario-origin disqualification is implemented where required.
- [ ] Debug and force-trigger rules match the project standard.
- [ ] Icons and localisation exist.
- [ ] Hard achievements are not reduced to easy automatic unlocks.
- [ ] Achievement docs agree with implementation.

## Documentation and spreadsheet

- [ ] `docs/events/032_missiles.md` exists.
- [ ] API docs exist for every new shared helper.
- [ ] Triggerable scenario docs include SCN-015.
- [ ] Cross-event docs are updated where bridges changed.
- [ ] Asset coverage is documented permanently.
- [ ] Probability evidence is referenced.
- [ ] Test matrix is updated with results.
- [ ] Authoritative workbook is updated.
- [ ] Event row status, detail, chaos level, and evolutions agree.
- [ ] Scenario row agrees.
- [ ] CSV exporter runs successfully.
- [ ] Exported CSVs are not edited directly.

## Audits and report

- [ ] Scripted-system architect review completed.
- [ ] Decision and mission auditor review completed.
- [ ] AI probability baseline and compare completed.
- [ ] Localisation auditor review completed.
- [ ] Improvement-loop addendum or closure resolved.
- [ ] Event completion auditor review completed.
- [ ] Required MCP event and technology evidence exists.
- [ ] Any skipped meaningful validation is reported.
- [ ] Every simplification, omission, fallback, placeholder, or blocker is listed.
- [ ] Final report lists files, systems, assets, AI evidence, docs, spreadsheet changes, and remaining risks.
- [ ] Completion is not claimed while any accepted item remains unresolved.
