# Event 027: Doctrine Research acceptance criteria

## Purpose

These criteria define what must be true before Event 027 can be presented as complete. They focus on behavior that could realistically fail or create an unapproved simplification.

Passing parser hygiene alone is insufficient.

## Event identity and registration

- [ ] Entry event identity remains `chaosx.nr27.1` under the current event namespace convention.
- [ ] Event 027 is registered as Minor Repeatable.
- [ ] The event is enabled by default only when its full rework is ready for normal selection.
- [ ] Event Details, debug name, history name, and catalog identity all resolve to Doctrine Research.
- [ ] The event can be selected automatically, manually through the normal event test surface, and as a National Breakthroughs member when the cluster is active.
- [ ] Impossible or globally unavailable Event 027 state shows `N/A` and never a misleading zero weight.
- [ ] One firing creates one global History row with no country actor.
- [ ] Country choice pages do not create additional random-event History rows.

## Global participant snapshot

- [ ] The participant set is captured once per firing.
- [ ] Every live country with at least one valid registered doctrine action receives one batch.
- [ ] Every human country receives its own independent chain.
- [ ] Every AI country resolves through the same valid pool.
- [ ] Countries created after the snapshot receive no retroactive batch.
- [ ] A country annexed before resolution loses its active and queued batches.
- [ ] Unused choices never transfer to an annexer, overlord, successor, civil-war opponent, or liberator.
- [ ] Government-in-exile participation follows current country-scope validity.
- [ ] Cosmetic tag, ideology, subject, faction, and leadership changes do not erase a valid batch.
- [ ] A civil-war split after the snapshot does not duplicate the original batch.
- [ ] Special or nonhuman countries participate only through valid ordinary or custom doctrine adapters.
- [ ] Placeholder, observer, and invalid system scopes never receive a batch.

## Baseline choice rules

- [ ] Baseline grants one choice per valid country.
- [ ] A choice begins with a valid doctrine-domain selection.
- [ ] A selected domain without a Grand Doctrine offers every eligible Grand Doctrine in that domain.
- [ ] Successful Grand Doctrine adoption consumes one choice.
- [ ] Grand Doctrine adoption grants zero event mastery steps.
- [ ] The event never replaces an active Grand Doctrine.
- [ ] A selected domain with an active Grand Doctrine offers every track that can receive one event mastery step.
- [ ] A selected active subdoctrine advances exactly one event-attributed mastery level.
- [ ] An empty track can select one eligible subdoctrine and receive its first event mastery step in the same choice when the local doctrine transaction proves this safe.
- [ ] A successful mastery result consumes exactly one choice.
- [ ] Navigation, pagination, and invalidated selections consume no choice.
- [ ] A fully mastered branch is absent from the valid pool.
- [ ] A fully exhausted country receives no political power, experience, research bonus, or other compensation.
- [ ] Normal doctrine purchase cost is waived only for the valid action selected through Event 027.
- [ ] The event provides no refund for prior experience spending.
- [ ] DLC, route, country, and custom-system eligibility remain active.

## Exact mastery behavior

- [ ] The implementation uses a verified next-level operation or exact threshold calculation.
- [ ] One Event 027 mastery receipt cannot cross two event-attributed mastery levels.
- [ ] Branches with fewer or more than five levels remain valid under the one-step rule.
- [ ] Current mastery is re-read at confirmation time.
- [ ] Combat, training, faction sharing, focus, decision, and other mastery changes can invalidate a stale target safely.
- [ ] Native banked mastery is preserved.
- [ ] Selecting an empty track does not delete or reset banked mastery.
- [ ] Native banked progress and Event 027 progress are attributed separately.
- [ ] A branch completed by native progress before the event step returns to the valid pool without wasting a choice.
- [ ] The local engine sequence for branch selection and banked mastery has been documented.
- [ ] Every supported domain passes a direct one-step test at low, middle, and final mastery levels.

## Doctrine-domain registry

- [ ] Army adapter is complete for the current installed graph.
- [ ] Navy adapter is complete for the current installed graph and DLC combinations.
- [ ] Air adapter is complete for the current installed graph and DLC combinations.
- [ ] Supported Special Forces content is either fully adapted or explicitly absent from Event 027 under the current ruleset.
- [ ] Chaos Warfare adapter uses the owning compatibility identities and mastery transitions.
- [ ] Every future custom domain in the registry has the full adapter contract.
- [ ] Track order matches the doctrine interface.
- [ ] Current and maximum mastery levels are exact.
- [ ] Invalid branch identities fail closed before reaching a trigger or effect.
- [ ] A broken custom adapter does not remove valid ordinary domains.
- [ ] Every visible option has a verified doctrine-owned icon or an approved existing fallback already used by the doctrine system.
- [ ] The event does not use technology-union or Kruger technology helpers as doctrine substitutes.

## Chaos Warfare integrity

- [ ] Event 027 cannot establish Chaos Warfare without the owning establishment prerequisites.
- [ ] The event waives only the selected doctrine purchase cost.
- [ ] Hazard Assault Formations advances through the owning mastery route.
- [ ] Toxic Armored Warfare advances through the owning mastery route.
- [ ] Contaminant Fire Support advances through the owning mastery route.
- [ ] Integrated CBRN Command advances through the owning mastery route.
- [ ] Event 027 never directly grants a downstream CBRN unit, equipment type, use policy, operation, idea, or Condemnation modifier.
- [ ] Separate technology, formation, equipment, policy, readiness, and operation gates remain effective after a mastery step.
- [ ] Chaos Warfare AI factors read actual CBRN readiness and strategy.

## Evolved batch sizes

- [ ] Baseline batch contains one choice.
- [ ] Evolution I batch contains two separate choices.
- [ ] Evolution II batch contains three separate choices.
- [ ] Evolution III batch contains four separate choices.
- [ ] Evolution IV batch contains five separate choices.
- [ ] Evolution IV is the highest implemented batch-size stage.
- [ ] Each stage uses normal evolution pacing and does not switch instantly on the same day as the tier change.
- [ ] A pre-fire unlocked evolution changes the first firing's batch size.
- [ ] A post-fire evolution changes later firings without granting an immediate free batch.
- [ ] A batch snapshots its size and stage at firing.
- [ ] An evolution unlocked during a batch does not enlarge that batch.
- [ ] Disabled lower evolutions do not block higher enabled stages.
- [ ] Disabled evolutions set no record or progression flag used by later content.
- [ ] Evolution records have no country actor.
- [ ] Evolution detail text uses two, three, four, and five choices accurately.

## Stacking and distribution

- [ ] A player can spend consecutive choices on the same branch until it completes.
- [ ] A player can distribute choices across tracks in one Grand Doctrine.
- [ ] A player can distribute choices across doctrine domains.
- [ ] A Grand Doctrine adopted by one choice appears as active for the next choice in the same batch.
- [ ] A completed branch disappears from later choices in the same batch.
- [ ] The event imposes no hidden player diversity quota.
- [ ] The event imposes no hidden player stacking cap.

## Batch queue and persistence

- [ ] One country can hold one active batch and an ordered queue.
- [ ] A later firing appends a new batch without overwriting the active batch.
- [ ] Batches with different evolution stages remain separate.
- [ ] Batch identity, size, stage, remaining choices, date, and achievement ledger persist through save and reload.
- [ ] A transaction receipt prevents duplicate effects after save and reload.
- [ ] A completed batch closes cleanly and starts the next queued batch.
- [ ] A queued batch rebuilds doctrine options when it starts.
- [ ] A queued batch with no valid option closes without compensation.
- [ ] Human-to-AI control change preserves the batch and allows bounded AI completion.
- [ ] AI-to-human control change opens the next unresolved choice for the human.
- [ ] Tag switching does not redirect a batch into the current player tag.
- [ ] Queue cleanup removes every batch-owned temporary state after annexation or final closure.

## Human choice flow

- [ ] Opening report shows total and remaining choices.
- [ ] Opening report distinguishes Grand Doctrine adoption from mastery development.
- [ ] Domain page lists every currently valid domain and no invalid domain.
- [ ] Grand Doctrine page lists every eligible doctrine and no replacement action.
- [ ] Track page shows current branch, current level, next level, and completion state.
- [ ] Empty-track page lists every eligible subdoctrine in native graph order.
- [ ] Back navigation returns to the correct rebuilt page.
- [ ] Pagination reaches every valid option.
- [ ] No valid option is hidden by a random subset.
- [ ] Every consuming option states that it uses one choice.
- [ ] Confirmation revalidates the target.
- [ ] Successful result page names the adopted doctrine or level reached.
- [ ] Final summary reports visible batch outcomes without hidden tracking.
- [ ] A no-option human country receives a concise closure report.
- [ ] Dynamic names and levels render without raw keys.

## AI behavior

- [ ] AI uses the same valid domain, doctrine, track, and subdoctrine pool as the human flow.
- [ ] AI recalculates after every choice.
- [ ] Army relevance responds to land force, production, war, borders, and route strategy.
- [ ] Navy relevance responds to coastline, fleet, dockyards, convoys, war, and maritime plans.
- [ ] Air relevance responds to production, wings, air war, bases, and air strategy.
- [ ] Conditional Special Forces relevance responds to fielded and planned special-force roles.
- [ ] Chaos Warfare relevance responds to actual CBRN readiness and route strategy.
- [ ] Grand Doctrine scoring reuses native or country-specific strategy where available.
- [ ] Track scoring uses force fit, production, war, theater, route, continuity, and completion value.
- [ ] Completion value cannot force a severe strategic mismatch.
- [ ] Strong score lead can produce stacking.
- [ ] Close scores can produce diversification.
- [ ] Branch completion forces a fresh target choice.
- [ ] Bounded randomness does not allow low-value candidates to dominate.
- [ ] Invalid candidates have zero participation.
- [ ] Human and AI candidate pools match under the same state.
- [ ] Every named scenario in `027_doctrine_research_probability_scenarios.md` has baseline and final evidence.
- [ ] Every weighted source change has a same-scenario `hoi4.probability_compare` result.

## Repeatable-event balance

- [ ] Event 027 uses shared repeatable weight recovery.
- [ ] Its cap reduces through the shared repeatable contract after firing.
- [ ] No batch subevent changes event weight or timer pressure.
- [ ] No country fanout page adds major-event gain.
- [ ] Sequence analysis uses a complete event-pool manifest before making exact recurrence claims.
- [ ] The final balance report states that Evolution IV can complete a fresh five-level branch.
- [ ] The final balance report checks whether Event 027 starves other positive repeatable events.
- [ ] Any event-specific cooldown added after audit is centralized and documented.
- [ ] Event 027 directly changes no Chaos Meter value.

## National Breakthroughs cluster

- [ ] A free cluster ID is verified in the current registry and workbook.
- [ ] Event 027 maps to National Breakthroughs.
- [ ] Event 027 displays Medium severity.
- [ ] Event 027 minimum tier matches Calm World.
- [ ] Event 027 is guaranteed when it is the originally selected member.
- [ ] Event 027 can join as an optional member when another member is selected.
- [ ] One cluster firing can call the Event 027 global fanout only once.
- [ ] Event 027 uses its current normal evolution stage inside the cluster.
- [ ] Cluster inclusion grants no extra Event 027 choices.
- [ ] The cluster counts as one global pacing event.
- [ ] Event 027 retains its own repeatable cap update and history.
- [ ] Unavailable cluster members remain skipped and logged honestly.
- [ ] Cluster probability evidence uses the complete implemented member pool.
- [ ] Catalog status remains unavailable or partially available until runtime member coverage supports a stronger status.

## Event Logs and Event Details

- [ ] History shows one Event 027 row per global firing.
- [ ] History details describe the current batch size accurately.
- [ ] Event Details explains the premise without raw effects or hidden state.
- [ ] Evolution catalog shows all four stages and correct choice counts.
- [ ] Main evolution history rows show date, event, stage, and enabled state.
- [ ] Related evolution history uses the same real log metadata.
- [ ] Event Details evolution preview contains no fake history index or date.
- [ ] No actor flag appears for the global event or its evolutions.
- [ ] Event enable and disable state controls automatic selection and evolution gates cleanly.

## Achievements

- [ ] `027_first_lesson` tracks one Grand Doctrine adoption followed by an Event 027 mastery step in the same domain and batch.
- [ ] `027_single_school` tracks five Event 027 mastery receipts in one verified five-level branch during one Evolution IV batch.
- [ ] `027_joint_curriculum` tracks four distinct track identities in one batch.
- [ ] Native mastery, faction sharing, focus, decision, other event, and debug progress cannot satisfy an Event 027 receipt.
- [ ] Batch cancellation or annexation cannot create a false unlock.
- [ ] Achievement IDs are unique in the root registry.
- [ ] Player-facing descriptions state the public requirements.
- [ ] Each achievement has complete tracking, disqualifiers, documentation, and icon triplet.
- [ ] The set does not duplicate the official all-subdoctrine achievement.

## Assets and presentation

- [ ] One final report-event image exists at the verified event-picture size.
- [ ] The report image uses a period-authentic joint-service training or military-school scene.
- [ ] The report image contains no readable generated text, modern equipment, national ownership cue, or generic command-table composition.
- [ ] Source PNG, processed preview, final DDS, manifest, and GFX handoff exist during production.
- [ ] Final runtime path is event-scoped.
- [ ] Every achievement has a distinct generated source and full state triplet.
- [ ] Doctrine icons are reused from verified owning sprites.
- [ ] No focus, idea, or decision icon is substituted for a missing doctrine icon without an existing doctrine-owned fallback precedent.
- [ ] Dynamic text distinguishes mastery level from Grand Doctrine Milestone.
- [ ] Option text remains concise and result-focused.
- [ ] Broad visible localization receives an independent localization audit.

## Documentation and catalog

- [ ] `docs/events/` documentation describes the final implemented behavior.
- [ ] Source specs remain under `docs/specs/027_doctrine_research_specs/`.
- [ ] Any implementation handoffs live under `docs/plans/027_doctrine_research_plans/`.
- [ ] Accepted implementation changes are folded back into the source spec when they change design.
- [ ] The authoritative XLSX row replaces the stale catalog concept.
- [ ] Event type, evolutions, cluster ID, severity, and status match runtime.
- [ ] National Breakthroughs row matches the runtime registry and honest member status.
- [ ] CSV exports are regenerated from the XLSX through the repository exporter.
- [ ] Event Details, evolution text, docs, and spreadsheet wording agree.
- [ ] No CSV snapshot is edited directly.

## Mandatory evidence and audits

- [ ] Relevant offline Paradox wiki pages were read.
- [ ] Relevant installed vanilla documentation was read.
- [ ] Current vanilla doctrine definitions and at least one direct mastery precedent were inspected.
- [ ] Existing Chaos Redux event and doctrine patterns were inspected.
- [ ] `hoi4.event_inspect`, `hoi4.event_render`, and post-change comparison evidence cover the event chain.
- [ ] `hoi4.tech_inspect`, `hoi4.tech_render`, and `hoi4.tech_compare` cover every supported doctrine domain and Chaos Warfare.
- [ ] `chaosx_scripted_system_architect` reviewed or implemented the adapter and batch transaction design.
- [ ] `chaosx_ai_probability_auditor` completed baseline and final weighted evidence.
- [ ] `chaosx_localisation_auditor` reviewed broad visible text.
- [ ] `chaosx_event_completion_auditor` compared implementation with this full package.
- [ ] `chaosx_spreadsheet_doc_worker` aligned the authoritative workbook after final implementation wording existed.
- [ ] The improvement-loop disposition remains closure, or any later addendum has been implemented, promoted, queued with a reason, or rejected with a reason.

## Completion claim

Event 027 can be marked complete only when every required criterion above is satisfied or an item is explicitly not applicable under the verified local graph.

Any missing doctrine adapter, unverified one-level operation, unresolved banked-mastery sequence, missing AI evidence, missing asset, missing achievement triplet, stale catalog row, or untested queue behavior is a blocker. It cannot be replaced by military experience, a generic research bonus, a reduced country pool, a vanilla-only implementation, or a silent omission.
