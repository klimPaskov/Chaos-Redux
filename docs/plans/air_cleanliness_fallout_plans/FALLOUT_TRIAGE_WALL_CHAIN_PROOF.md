# Fallout Triage Wall Chain Proof

Status: implemented as a dormant reviewed candidate. It is not activation proof and it contributes zero blocks to the 660-block release floor until the scheduler activation audit opens the ordinary human and hidden AI lanes.

## Scope

The chain is owned by the Fallout namespace and is separate from Air Winter and zombie content. It uses event suffixes `175` through `187` and history id `9111`.

- `175` opens the human choice
- `176` resolves the hidden AI choice
- `177` through `180` resolve the four human policies
- `181` through `184` resolve the four hidden AI policies
- `185` is the human doctor's callback
- `186` is the hidden AI callback
- `187` releases the authenticated cleanup ticket

The four policies are children first, workers first, soldiers first, and equal chance. Each policy has success, partial, and failure effects. Failure uses the Deaths system through `apply_exact_state_civilian_population_loss`. Success and partial outcomes change medicine, recognition, cohesion, stability, manpower or war support, and a policy-specific dynamic modifier. State flags preserve the medical ethics memory. The callback adds a second delayed result and a durable doctor memory.

## Candidate gate

The candidate producer selects the lowest owned state with a produced Air Winter snapshot, shelter capacity above `fallout_event_175_threshold.state_shelter_minimum`, and current country medicine below the reviewed pressure band. The producer also requires the country to afford the smallest policy cost. Missing state identity, source provenance, generation, ownership, or shelter evidence rejects the row. No generic state is substituted.

The candidate row uses candidate id `175`, transaction key `710006`, route `7106`, medicine resource index, and the first-season phase. The producer still sets no activation flag and never fires an event by itself.

## Delayed transaction and cleanup proof

The opening consumes one ordinary receipt only after the result transaction is accepted. The selected branch, outcome, generation, day, state target, registry owner, and cleanup ticket are stored. Result resolution records the first history payload, applies the policy, and schedules the callback. Callback resolution records the second history payload, prepares delayed cleanup, and marks the callback receipt. Cleanup releases only the authenticated result or callback ticket, then releases the remaining ticket and clears the state registry. Stale generation, stale target, wrong owner, wrong token, wrong branch, or wrong mode fails the entry triggers.

## Event log and localization

History id `9111` carries fifteen explicit payloads. The event log maps the name to `fallout.event_log.triage_wall.name` and maps each branch and outcome to a concrete detail key. Event title, descriptions, options, tooltips, callback text, dynamic modifier names, and history detail keys are in `localisation/english/fallout_consolidated_l_english.yml`.

## Asset proof

The visible events use `GFX_report_event_fallout_triage_wall`. The dedicated asset package is documented in `docs/assets/fallout_triage_wall/manifest.md` and wired by `interface/fallout_consolidated.gfx` to `gfx/event_pictures/fallout/fallout_triage_wall_report.dds`. The report scene is a generated fictional clinic triage wall. It does not reuse zombie or existing Fallout ids, assets, audio, sprites, or paths.

## UI and icon surfaces

The chain needs no focus, idea, decision, or map icon. Its only visual surface is
the report-event sprite `GFX_report_event_fallout_triage_wall`, registered in
`interface/fallout_consolidated.gfx`. The event log uses text payloads rather than
a second icon surface.

## Static review performed

- Event ids `175` through `187` are unique within the Fallout event file.
- Event id constants, candidate constants, branch tokens, thresholds, result values, log payloads, dynamic modifier names, event triggers, and event effects agree.
- The localization file has a UTF-8 BOM and no em dash or semicolon.
- The asset manifest records source, processed preview, DDS, dimensions, and SHA256 values.
- Braces and localization key coverage were checked with repository-local text checks.

HOI4 was not launched, per the task instruction. Runtime timing, save reload, multiplayer authority, scheduler activation, and GUI behavior remain unobserved.

## Remaining gates

This tranche does not claim the 660-block release floor, successor allocation, player continuation, or live activation. The exact native all-valid-land-province sweep remains an external engine proof blocker. The dormant scheduler still needs its activation ledger, region and archetype coverage, and human review before this chain can be counted.
