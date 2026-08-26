# Event 016 final event-completion audit

Date: 2026-08-26

Accepted commit boundary: `18f7c7d6708bf252708353f3a50b7301162d37ac` (`docs: attest directorate gui and localize dhrondan outcomes`).

Mode: final read-only source and evidence audit.

Overall status: **INCOMPLETE**.

Event 016 has substantial static implementation, but it does not satisfy the accepted completion contract because custom-unit packages, Portal beachhead lifecycle ownership, populated probability scenarios, legal MCP comparisons, cross-provider runtime proof, current asset provenance reconciliation, and user-owned live acceptance remain open.

No gameplay, localisation, interface, workbook, binary asset, model, or sound source was edited by this audit.

## Evidence boundary

This pass read `AGENTS.md`, every file under `docs/specs/016_brilliant_scientist_specs/`, the Event 016 source-of-truth map, core-runtime map, package manifest, completion status, current and historical Event 016 audits and handoffs, Event 019 interoperability documentation, model/counter/audio handoffs, Event Log and Event Details source, and the authoritative workbook row.

The applied repository skills were `chaos-redux-events`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, `chaos-redux-event-planning`, `chaos-redux-event-assets`, `chaos-redux-3d-model-pipeline`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-super-events`, and `xlsx` for read-only workbook inspection.

The required offline wiki pages were read for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus, Country creation, Division modding, Equipment modding, Technology modding, Interface modding, Scripted GUI modding, and Graphical asset modding.

Installed vanilla documentation was read for effects, triggers, script concepts, and script constants, with prior handoffs retaining the exact vanilla event, decision, focus, technology, unit, entity, and counter precedents used by the implementation owners.

The committed boundary is `18f7c7d67`, but the current shared worktree is not a clean representation of that commit.

At the audit cutoff, the worktree deleted 491 tracked files under `docs/assets/portraits/016_brilliant_scientist/`, deleted the three tracked DHR event-art evidence files `gfx_handoff.md`, `manifest.md`, and `notes/processed_alpha_qa.json`, modified all six Event 016 super-event WAVs, modified the core-runtime map, package manifest, and prior final completion audit, and contained an untracked final localisation audit.

Those changes were not made or reverted by this auditor.

The runtime portrait and DHR packages still have other retained source, processed, DDS, and handoff evidence, but completion cannot rely on the deleted tracked evidence tree or on committed audio checksums until the parent reconciles the current worktree intentionally.

## Mandatory HOI4 MCP evidence and limits

### Fresh Event 016 opening inspection

`hoi4.event_inspect` was run for `{ kind = event, eventId = chaosx.nr16.1 }` in both directions with helper expansion, depth 4, 120 nodes, and 200 edges.

It completed after approximately 68 seconds with status `ok` and code `EVENT_INSPECTED_PARTIAL` at MCP revision `2b3b330f662608cdaac0d1c2b27f7e233c232225f39fbfe52312dc45d434449c`.

The graph hash is `5beef431819384db41d090e8b375d32e4678137d49103df67811d083f8ca596e`.

The artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a36a46f3869f2ebd22c2889459b8c0fcbe5b65e25e490fd26a229637befd1be/cfaf8dcfa4fd8d19e1f07548e030d5d9a1072cafedbc6d8b2497d8df56872d1c/event-trace-2b3b330f6626.json`.

The response was not isolated clean evidence for Event 016.

It reported 24,110 workspace-wide issues, 14 blocking workspace diagnostics, 8,314 unresolved nodes, and an inventory truncated to 64 of 350 entries.

No sources were skipped, but the partial global graph and unrelated diagnostics cannot certify the opening's once-only, recipient, transfer, or helper semantics.

### Fresh Event 016 opening render

`hoi4.event_render` was run for the same root and revision in overview mode.

It returned status `ok`, code `EVENT_RENDERED_PARTIAL`, five artifacts, nine selected nodes, and 41,249 omitted nodes.

The manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e17c1bad3801d4a04a5de6d6f284f0dfdd9fce72fa222f7942d936b42ea952f8/da7b800bf37a6a5da7161f81f2aec001ad2e3f3cbb8cc514860c437c4225bafc/event-overview-2b3b330f6626-manifest.json`.

The render retained the same 14 workspace-wide blocking diagnostics and therefore proves only that a bounded overview artifact was produced.

### Event comparison

Three read-only `hoi4.event_compare` attempts failed before a legal comparison could be produced.

Passing nested workspace IDs was schema-rejected because `workspaceId` is not accepted in the before/after objects.

Passing before revision `f588a2607444400ec9fa9d102943fc0e10dc4482ebca9935232a4df2966f59d5` and after revision `2b3b330f662608cdaac0d1c2b27f7e233c232225f39fbfe52312dc45d434449c` returned status `error`, code `EVENT_REVISION_NOT_CACHED`, `artifactCount = 0`, and blocker `Requested event graph revision is not cached.`

Passing an artifact URI as the before value was schema-rejected because the route requires an object.

No `event_compare` artifact exists, and Git commits or historical render artifacts are not substituted for MCP revisions.

### Retained narrow MCP evidence

The current shared MCP receipt records `chaosx.nr16.47` inspection at revision `f588a2607444400ec9fa9d102943fc0e10dc4482ebca9935232a4df2966f59d5` with status `EVENT_INSPECTED_PARTIAL`, zero selected-view blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/94eaa4862016956958bae29a2fba697a0e3f1efd857ff96c4fbb3381c76ccb38/cf509287edc5293ffdfebfa2f78ddcd1972b2ee23764f5d60435b01fa7a2b23b/event-state_flow-f588a2607444.json`.

Its matching state-render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bd81c30903ef30ef048a6478c0c9e6795e0e6371e82631f253c3e17581525cda/ca626de89826dfcdd32e35b58609f9f2491151a02727e318add020b45e91049e/event-state-f588a2607444-manifest.json`.

Event 019 `.1` returned `EVENT_INSPECTED_PARTIAL` at the same revision with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0676ae7909104fca3360c55205ebbb4cb452f62d4b8be7a19aa28648c2613095/701a8468b6893f1b27cb6829ae2478ce65997462e0eee17b947da8b454a9aaad/event-state_flow-f588a2607444.json`.

These are structural partial views, not one-cohort, 2,000-gun, rollback, cleanup, or cross-provider conservation proof.

The latest DHR focus audit records a successful `FOCUS_INSPECTED` result with 88 focuses, 102 connectors, no crossings or long connectors, and no DHR-specific diagnostics at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7f094589a3899fd52e6b1d05e13777d76d9783faa3751b3887d7cfcf6d228ee/9c81fe28bc00eb91a4c4039c31272b633591ce197dbe936eb31832b8acf64570/focus-inspect.abe2c73eb5b5af0a.json`.

The named `chaosx_event_ui_worker` attestation for `kruger_directorate_container` retains successful exact-window GUI inspect/render evidence, states, resolutions, hierarchy, and click regions, but records offline glyph substitution, primary-frame approximation for multi-frame controls, truncated workspace diagnostics, and unavailable separate per-state and per-resolution artifacts.

Alien Infantry technology inspection/rendering is partial and source-linked only; no complete prerequisite, unlock, bonus, asset, consumer, and before/after technology comparison exists for the entire reusable technology family.

## Completion status by surface

| Surface | Status | Evidence and disposition |
| --- | --- | --- |
| Minor fire-once opening | Partial | `common/scripted_effects/chaosx_logic_effects.txt:243` registers the Event 016 fire-once ID, and `events/016_brilliant_scientist.txt:14-318` contains the `.1` dispatcher and recipient reports. The fresh MCP root inspect/render is partial and does not prove once-only execution, AI acceptance/referral, recipient uniqueness, or transfer conservation. |
| Fixed Kruger identity | Partial | `history/general/016_brilliant_scientist_character_recruitment.txt:13` installs `KRG_warren_kruger`; `common/scripted_effects/016_brilliant_scientist_effects.txt:2687-2723` transfers that identity and `:2810-2847` installs the roles. Duplicate-character and host-to-KRG transfer scenarios remain unproved. |
| Exactly four evolutions and no cluster | Finished statically | `events/016_brilliant_scientist_evolutions.txt:12-321` defines `.21`, `.22`, `.23`, and `.24`; `.90` is the hidden scheduler, not Evolution V. Workbook `Events!D17:G17` contains I-IV, `H17` is blank, and the Event 016 cluster cell is blank. Delayed/MTTH and one-time delivery remain runtime-unproved. |
| Directorate and fifteen projects | Partial | Visible Mandate, Dependence, Exposure, and Project Capacity, hidden Independent Capacity and Grievance, four project stages, fifteen families, decisions, facilities, incidents, recovery, state consumers, and route effects are present. The event-owned GUI has named-worker evidence, but presentation, balance, state transitions, and live consumer behavior remain incomplete. |
| KRG country and focus package | Partial | The fixed KRG package and 100-focus tree, 100 focus icons, ideas, decisions, route and terminal consumers, carried project forces, and AI source are present. Formation, character transfer, route exclusivity, terminal balance, and live map/runtime behavior are not certified. |
| Reusable technologies and units | Partial | Clone Infantry and Autonomous Robot have installed reusable model/entity packages. Alien Infantry has a promoted V13 static package. Portal Raider, Paleogenetic Creature, Xenobiological Organism, and Temporal Guard remain without accepted dedicated runtime models. Provider registration and vanilla sprite fallback do not satisfy the accepted 3D packages. |
| Alien contact and landing | Partial | Events `.40-.47`, the five public API surfaces `alien_infantry_grant_contact`, `alien_infantry_revoke_contact`, `alien_infantry_can_call_landing`, `alien_infantry_spawn_landing_cohort`, and `alien_infantry_reconcile_country`, exact source receipts, seven-day reserve, exact 2,000-gun cost, cooldowns, and host-owned landing registry source are present. Two-provider isolation, loss/refund, duplicate-state idempotence, and transfer/capture behavior remain unproved. |
| Event 019 interoperability | Partial | Providers 504-510 and strict provider 522 are statically registered with callback parity, including Alien Infantry provider 508. Dynamic selection, derivative isolation, one-cohort materialization, 2,000-gun debit/refund, rollback retry, management, defeat, and final cleanup remain unproved. |
| DHR country and 88-focus tree | Partial | Fixed tag, history, four flag families, twelve characters, advisors/commanders, country effects, decisions, 88-focus tree, 88 inline AI blocks, and the accepted `8/24/10/12/8/8/12/6` section distribution are present. Dynamic release, capital, core/claim, foreign-owner, annexation/rejoin, route timing, and live acceptance remain open. |
| Portal Warfare raids | Partial | Native state-installation and exact-facility raids, seven-day preparation, ten Command Power, sixty Teleportation Equipment, six-battalion formation requirement, formation consumption/reconstruction, and building extraction are statically present. The active-beachhead flag has no accepted lifecycle owner, and the Portal Raider runtime model is rejected and unwired. |
| World ends and super-events | Partial | Laboratory World and Strategic Singularity are statically mutually exclusive terminal routes, and visible super-event IDs 90-95 are registered with text, image, audio, localisation, and queue source. Current WAV bytes differ from the committed boundary, and live playback, queue, settings, fallout, and terminal scenario proof are missing. |
| Achievements | Finished statically, runtime-unproved | `common/achievements/chaos_redux_achievements.txt:3205-3291` contains exactly 17 Event 016 keys. `public_method` and `clean_break` are separate at `:3215` and `:3225` and use separate scripted triggers. Unlock and disqualifier runtime scenarios are not certified. |
| Event Log and Event Details | Partial | Four evolution previews, actor rebinding, terminal rows, conditional DHR sovereignty clause, scripted localisation, and report/news sprite references are present. Full in-game presentation, actor persistence, terminal chronology, and current MCP render comparison are missing. |
| Catalog and documentation | Partial | Workbook row 17 has ID 16, `Brilliant Scientist`, four evolutions, blank Evolution V, both world ends, `Minor Fire-Once`, chaos level 1, blank cluster, and conservative `Needs Testing`. The apparent `D�Rhondan` terminal output is console mojibake; workbook codepoint inspection confirms U+2019 and the CSV exports `D’Rhondan`. Current asset deletions and contradictory stale handoffs prevent documentation closure. |
| CXT extension | Partial | The hidden carrier, matching `_apply` setup effect, bounded startup registration, `on_daily_CXT` synchronization, project, equipment, subunit, locked template, and test units are present. No live CXT invocation or idempotence proof exists. |
| AI and probability | Partial and blocked | Some conditional branch arithmetic is known, but the current weighted evidence is source-revision-fragmented, several adapters expose incomplete pools, populated scenarios are absent, and no legal same-scenario `probability_compare` exists. |

## Implemented in static source

- The default-enabled minor fire-once registration, eligible-host dispatcher, public, secret, and send-away branches, recipient reports, AI paths, fixed Kruger character, and transfer helpers exist.
- Event 016 defines exactly four evolution events and no evolution cluster.
- The Directorate contains the accepted visible and hidden governance values, fifteen project families, four project stages, facilities, foreign interaction, incidents, recovery, route administration, and terminal consumers.
- The fixed KRG country, 100-focus tree, country history, characters, ideas, decisions, units, technologies, project-force adapters, and terminal branches exist.
- The reusable Alien Infantry API and provider-neutral unit/equipment/technology package exist, including caller-owned landing targets introduced by `d77afae7e`.
- Event 019 exposes providers 504-510 and 522 with static registration and callback parity.
- The DHR contact chain, paid landing system, rebellion pulse, fixed DHR country, country effects, 88-focus tree, four flag families, twelve fictional characters, and route decisions exist.
- Both native Portal Warfare raid targets and their preparation, reservation, formation, and extraction source exist.
- The two terminal world ends and exactly six visible Event 016 super-event packages are registered.
- Exactly seventeen achievements exist, with separate `public_method` and `clean_break` conditions.
- Event Log, Event Details, conditional DHR detail text, localisation, report/news art registration, workbook row 17, CSV export, and CXT setup source exist.
- Report, news, GUI, focus, decision, technology, achievement, flag, portrait, counter, and most model/audio evidence families have retained wiring or handoffs.

These items are implemented claims about present static source only unless a narrower MCP artifact is cited above.

## Queued accepted work

- The Portal beachhead lifecycle plan remains queued because the accepted design does not yet define expiry, defender resolution, owner scope, duplicate-selection prevention, or cleanup ownership.
- Dedicated Portal Raider, Paleogenetic Creature, Xenobiological Organism, and Temporal Guard 3D packages remain queued or rejected rather than complete.
- The optional KRG biological stockpile and delivery ledger remains queued behind a stable idempotent native CBRN reservation, outcome, cancellation, and expiry callback.
- Complete populated probability scenarios, quantitative balance, Event 019 isolation, KRG transfer/formation, DHR release/capture, terminal world-end, CXT, and live presentation acceptance remain queued validation work.
- DHR route plans intentionally leave some cross-lane support priorities to inline focus weights; the country/focus audit classifies this as a queued AI-quality gap, not a dead route.
- Parent disposition is still required on the stable approved DHR identity roster versus any top-level requirement interpreted as runtime-random fictional names.

Broader country-specific chains, extra evolutions, a DHR super-event, new formables, additional shared GUIs, and filler raid families were closed or rejected by accepted improvement-loop dispositions and are not counted as queued requirements.

## Disclosed simplifications

- `docs/specs/016_brilliant_scientist_specs/package_manifest.md` explicitly labels KRG project-force access simplified: seven KRG batch decisions and six equipment lines use the operational family stage as the direct active-Kruger entry while preserving costs, capacity, history, and failure locks.
- Paleogenetic Creature currently uses cavalry presentation, Xenobiological Organism and Temporal Guard use vanilla infantry presentation, and Portal Raider has counters without an accepted entity. These are visible fallback presentations, not completion of the required dedicated packages.
- The Directorate offline renderer substitutes glyphs and represents multi-frame controls by a primary frame. This is an evidence simplification, not proof that live GUI states are correct.
- The DHR stable portrait roster avoids a runtime random-name system. The binding addendum and parent-approved portrait roster support stable route identities, but a contrary top-level interpretation remains unresolved and must not be silently treated as accepted.

No new fallback or simplification was introduced by this audit.

## Missing requirements

- There is no accepted cleanup or transition owner for `brilliant_scientist_portal_beachhead_active` after `common/scripted_effects/016_brilliant_scientist_raid_effects.txt:53-64` sets it.
- Portal Raider has no accepted firearm-bearing model, packed final entity, required genuine actions, PDX export/reimport proof, entity/GFX registration, synchronized action/audio points, or runtime acceptance.
- Paleogenetic Creature, Xenobiological Organism, and Temporal Guard have no accepted dedicated model/entity/action/audio/counter-complete packages.
- Alien Infantry has no supported authored muzzle/effect locator, so the registered muzzle particle and flash definitions have no proven binding.
- Alien Infantry lacks acceptable sourced provenance for strict selection, acknowledgement, impact, and special-role audio coverage, and positional playback is unproved.
- The current portrait handoffs contain strong source, ImageGen, processing, DDS, and wiring evidence, but they do not explicitly identify `chaosx_portrait_creator` as owner. The DHR handoff names `/root/dhr_portraits`, and the Kruger handoffs predate the required role attribution. Under the current completion contract, explicit portrait-worker handoff attribution remains missing.
- Current worktree deletion of 491 tracked Event 016 portrait evidence files and three DHR event-art evidence files has not been reconciled into an accepted asset-manifest disposition.
- No legal current Event 016 `event_compare` artifact exists.
- No complete populated technology comparison exists for the reusable technology families.
- No complete runtime scenario proves opening uniqueness, transfer conservation, four evolution delivery, one origin conclusion, terminal mutual exclusion, achievements, Event Log chronology, or Event Details actor persistence.
- No live CXT setup receipt or live Event 019 provider conservation receipt exists.

## Unwired or runtime-unproved requirements

- Alien Infantry particle/light definitions are registered but not bound to a supported effect point.
- Portal Raider counters are wired, but the model/entity/actions are not.
- Paleogenetic, Xenobiological, and Temporal units are functional script consumers using fallback presentation, not wired bespoke 3D consumers.
- Six super-event WAV files are wired by source, but their current modified bytes are not reconciled against the committed manifests and checksums.
- Event 019 provider 508 is statically connected to Alien Infantry, but exact selection, materialization, debit, rollback, management, and cleanup are unproved.
- DHR transfer code is statically connected to the caller-owned registry, but duplicate registration, state loss, capital selection, owner/control changes, claims, cores, foreign-owner handling, annexation, and rejoin are unproved.
- The landlocked DHR focus `DHR_salvage_the_shuttle_docks` can advance its receipt without a proven dockyard result; the accepted design has no fallback disposition for that edge.
- Directorate per-state and per-resolution presentation remains unproved beyond the packaged primary-frame renderer evidence.
- Super-event queue playback, audio/settings interaction, world-end fallout, and post-terminal cleanup are unproved.

## AI and probability evidence

All weighted surfaces were routed through the required probability-audit workflow, but the available receipts are not sufficient for completion.

The retained rebellion audit discovered the complete two-entry random list and records exact prior conditional shares of `0/100`, `10/90`, `20/80`, and `40/60` for its named threshold scenarios.

The current empty-fixture evaluation could not resolve the temporary revolt and no-revolt weights, and no complete 90-day cadence, recovery, or terminal sequence was supplied.

Current source still leaves an ambiguous rebellion band: arrivals at or above the high arrival threshold with chaos below the high threshold and strain below the high threshold fail both the high and medium triggers and fall back to the low 10% branch at `common/scripted_triggers/016_dhrondan_contact_triggers.txt:162-195` and `common/scripted_effects/016_dhrondan_contact_effects.txt:351-365`.

That is a concrete balance/design gap because the declared low and medium maximum constants do not partition the 10-plus-arrival edge.

The contact mission audit found both Kruger and Mengele expedition choices using dominant score 10000; the helper is deterministic Kruger-first when both routes qualify.

Current source now charges political power only after `dhrondan_expedition_in_progress` is set at `common/scripted_effects/016_dhrondan_contact_effects.txt:193-210`, so an older probability-handoff warning about pre-debit is stale and must not be treated as a current defect.

Current `.49` source now permits a bounded invalid-offer delivery branch at `events/016_dhrondan_country_events.txt:26-40`, so an older warning that `.49.c` is unreachable is also stale.

Landing AI is one decision score with unresolved receipt, equipment, cooldown, and target-state inputs; it is not a normalized state-selection probability.

The CBRN pool has nine candidates, but the DHR craft's dynamic eligibility is unresolved, so no exact normalized DHR selection chance is valid.

The Event 019 custom weighted-pool adapter discovered zero candidates for the hand-rolled provider arrays and withheld normalized results with `PROBABILITY_CANDIDATE_POOL_INCOMPLETE`.

The DHR focus pass declared all 88 candidates but produced 130 unresolved values and 34 fixture-driven diagnostics under empty scenarios; it does not prove route timing or selection quality.

There is no installed `special_project_ai_will_do` adapter, so the DHR envoy craft's base 100 remains source-only.

No same-scenario `hoi4.probability_compare` exists because there is no accepted before/after MCP revision pair and no owner balance patch.

The current probability handoff is internally stale in places because concurrent source repairs landed during its run, and its closing summary repeats a selector warning that its own correction section withdrew.

It must be reconciled before use as release evidence.

## Blocked requirements

- Full Event 016 event comparison is blocked by the MCP revision cache contract: `EVENT_REVISION_NOT_CACHED`, no artifact.
- Full isolated event proof is blocked by large-workspace partial graphs, 41,249 omitted render nodes, 8,314 unresolved graph nodes, and workspace-wide diagnostics that are not Event 016-isolated.
- Weighted completion is blocked by incomplete adapters, empty fixtures, unresolved dynamic variables, stale analysis revisions, absent special-project adapter support, and no legal same-scenario comparison baseline.
- Cross-provider DHR and Event 019 proof is blocked by the lack of an engine/runtime matrix that can execute and observe the caller-owned array, selected-state ownership, cohort count, equipment ledger, rollback, transfer, and cleanup together.
- The optional KRG biological ledger is blocked by the missing native idempotent CBRN callback contract.
- Alien Infantry completion is blocked by the unsupported authored muzzle locator, unbound effects, incomplete strict audio roles, positional playback, and live acceptance.
- Portal Raider completion is blocked by the rejected rifle-less generation and absence of an accepted recovery package.
- Current audio and portrait/event-art completion evidence is blocked by uncommitted binary changes and tracked evidence deletions in the shared worktree.
- Live gameplay, map placement, unit animation, sound playback, GUI presentation, decision targeting, super-event playback, and campaign acceptance remain user-owned and unavailable to this read-only auditor.

## Accepted-plan disposition

| Accepted plan or requirement | Final disposition |
| --- | --- |
| Minor fire-once opening | Implemented statically; dynamic once-only and transfer proof missing. |
| One persistent Kruger identity | Implemented statically; transfer and KRG formation proof missing. |
| Exactly four evolutions and no cluster | Implemented in source, log/details, localisation, and catalog; timed runtime delivery unproved. |
| Directorate, fifteen project families, and four stages | Substantially implemented; GUI has named-worker evidence; balance, transitions, and live presentation remain open. |
| Reusable technologies and project forces | Script/API coverage substantially implemented; four dedicated 3D packages remain incomplete and Alien Infantry remains runtime-blocked. |
| Alien contact, landing, and Event 019 provider 508 | Implemented statically; two-provider and transaction-conservation proof missing. |
| Fixed DHR country and exact 88-focus tree | Implemented statically; dynamic country transfer, route AI, landlocked dock edge, and live acceptance remain open. |
| Native Portal raids | Mechanics implemented statically; beachhead lifecycle and Portal Raider runtime package incomplete. |
| Laboratory World, Strategic Singularity, and six super-events | Implemented statically; current audio reconciliation, render comparison, queue, fallout, and live playback missing. |
| Exactly seventeen achievements | Implemented statically with separate `public_method` and `clean_break`; runtime scenario proof missing. |
| Event Log, Event Details, catalog, and CXT | Statically aligned and catalog remains `Needs Testing`; live and full MCP proof missing. |
| Optional KRG biological stockpile | Queued and blocked on the native CBRN callback; no fallback approved. |
| Broader routes, countries, formables, extra GUI, extra evolution, DHR super-event | Closed or rejected by accepted dispositions; not missing accepted work. |

## Documentation and stale-claim findings

- Workbook row 17 is correctly conservative at `Needs Testing`; it must not be promoted to complete.
- The apparent DHR apostrophe corruption is a terminal rendering artifact, not workbook corruption.
- Older audits that describe all Event 016 models as absent are superseded by the installed Clone Infantry and Autonomous Robot packages and the promoted Alien Infantry V13 static package.
- Older audits that describe the Alien Infantry caller-owned registry defect as open are superseded by `d77afae7e`, but dynamic acceptance remains open.
- Older audits that describe the Directorate GUI as lacking a named event UI worker are superseded by `016_dhrondan_gui_worker_attestation_2026-08-26.md`.
- Older probability claims about AI political-power pre-debit and unreachable `.49.c` are superseded by current source.
- `016_event19_generic_unit_family_3d_model_backlog.md` and parts of `016_core_runtime_handoff_map.md` still say Portal Raider recovery requires new user approval, which conflicts with current pipeline policy that planned generation and failure-driven provider recovery are preauthorized while balance and capability permit it.
- The current probability handoff both withdraws and later repeats the Event 019 total-plus-one selector warning; the selector uses an exclusive maximum and the warning is withdrawn.
- The previous final completion audit says fresh Event 016 root inspect/render timed out; this audit supersedes only that transport statement with the fresh partial artifacts above. It does not supersede the remaining validation blockers.
- The current worktree asset deletions and WAV modifications are not reconciled in the package manifest and therefore prevent a clean current asset attestation.

## Meaningful validation completed

- Cross-compared the binding acceptance criteria and Alien Infantry/DHR addendum against the opening, exactly four evolutions, Directorate/projects, KRG, reusable technologies and units, DHR/Event 019, raids, world ends, super-events, achievements, Event Log/Details, catalog, assets, CXT, AI, and validation handoffs.
- Counted exactly four evolution events and confirmed that `.90` is a scheduler.
- Inspected workbook row 17 directly and confirmed four evolution cells, blank Evolution V, blank cluster, both world ends, and `Needs Testing`.
- Counted exactly 17 Event 016 achievement definitions and confirmed separate `public_method` and `clean_break` scripted triggers.
- Reconciled the five public Alien Infantry API names, country-owned registry source, provider 508 adapters, CXT registration, and fixed DHR consumers.
- Reconciled the exact DHR 88-focus count and accepted section distribution with the successful focus MCP artifact.
- Reconciled the custom-unit model, counter, source, licence, checksum, audio-role, action, export/reimport, and runtime handoffs without treating counter or source-only evidence as an entity proof.
- Ran fresh Event 016 root inspect and render and recorded their exact partial artifacts and limits.
- Attempted legal Event 016 comparison forms and recorded the exact schema and cache blockers.
- Reconciled stale probability findings against current source before carrying them into this audit.

## Meaningful validation still missing

- Narrow current inspect/render/compare for the opening, each evolution, Directorate transitions, DHR `.40-.47`, Event 019 provider 508, both terminal world ends, and achievement transitions.
- A cached before/after MCP revision pair for Event 016 and every changed supported technology, focus, decision, and weighted surface.
- Populated same-scenario probability comparisons for opening host/referral choices, all evolution options, Directorate choices, DHR contact and rebellion, landing targets, CBRN selection, Event 019 provider selection, 88 DHR focuses, AI strategy factors, and terminal routing.
- Two-provider Alien Infantry registry isolation and Event 019 debit/materialization/rollback/cleanup conservation.
- KRG character, territory, project-force, and terminal transfer scenarios.
- DHR capital, transfer, core/claim, owner/control, annexation, rejoin, and landlocked dockyard scenarios.
- Portal beachhead transition and cleanup scenarios.
- Complete technology tree projections and comparisons for reusable operational packages.
- Custom-unit model/entity/action/audio/effect runtime evidence for every accepted consumer.
- Reconciled current portrait/event-art provenance and super-event WAV checksums.
- Live CXT, Event Log/Details, Directorate GUI, focus tree, unit, raid, super-event, world-end, and campaign acceptance.

## Recommended closure order

1. Reconcile or intentionally discard the current Event 016 worktree asset deletions and six modified super-event WAVs, then refresh affected manifests and checksums without using this audit as authority to overwrite user changes.
2. Promote an exact Portal beachhead lifecycle contract and implement one bounded owner for active state, duplicate prevention, resolution, and cleanup.
3. Complete Alien Infantry locator/effect and strict sourced-audio roles, then finish the separate Portal Raider semantic model/action/audio package and the remaining Paleogenetic, Xenobiological, and Temporal packages under their accepted scope.
4. Correct or explicitly accept the ambiguous 10-plus-arrival DHR rebellion tier, then run populated named probability scenarios and same-scenario comparisons for all weighted surfaces.
5. Rebuild a cached MCP baseline and run narrow current event, focus, technology, decision, and comparison evidence for the accepted chains.
6. Execute the two-provider DHR/Event 019 transaction and country-transfer matrices, then reconcile KRG, DHR, CXT, achievement, Event Log/Details, super-event, and terminal scenario evidence.
7. Add explicit `chaosx_portrait_creator` attestation or a durable role mapping for the Kruger and DHR portrait handoffs, and resolve the stable-roster versus runtime-random-name interpretation.
8. Reconcile the package manifest, source-of-truth map, workbook status, exported CSVs, asset manifests, and completion handoffs only after the runtime and validation blockers close.

## Final completion decision

Event 016 is **not complete** at or through commit `18f7c7d67`, and the current dirty worktree cannot be promoted as a cleaner completion state.

The exact-four/no-cluster contract, seventeen achievements, six super-event registrations, Directorate/project breadth, KRG and DHR packages, reusable APIs, provider registrations, native raids, Event Log/Details source, catalog row, and CXT source are materially implemented.

The missing custom-unit consumers, incomplete Alien Infantry effect/audio runtime, rejected Portal Raider entity, unowned Portal beachhead lifecycle, ambiguous rebellion tier, incomplete probability and comparison evidence, cross-provider and country-transfer proof, portrait-worker attestation, dirty asset provenance, and live acceptance remain explicit blockers.

No source-only, historical, partial MCP, counter-only, or catalog evidence should be treated as proof that those blockers are resolved.
