# Exact native Prototype ownership

Cloning, Rocketry and Electronics use exact native source commitments in the existing Mengele provider categories.
The selection layer records a project choice and keeps native research, payment, progress, rewards, and completion under the existing special-project object.
It does not treat a country completed bit as a fresh output or infer a selected Rocketry alternative from an aggregate OR.

## Sources and controls

| Exact project | Source code | Family | Existing category |
| --- | --- | --- | --- |
| sp_brilliant_scientist_cloning | 1 | Cloning | Biological Programs |
| sp_rockets_flying_bomb | 2 | Rocketry | Conventional Programs |
| sp_air_jet_engine | 3 | Rocketry | Conventional Programs |
| sp_air_radar | 4 | Electronics | Conventional Programs |

Four instant selection controls and four withdrawal controls are in common/decisions/016_mengele_native_prototype_selection_decisions.txt.
Selection and withdrawal spend no provider resources and start no provider timer.
A completed exact source enters adoption rather than opening a fresh commitment.
Rocketry permits one selected alternative, and a pending opposite selection blocks the other choice.
The current source remains selectable for adoption if it completes while an earlier output could not privately settle.
A withdrawal requires inactive research and an empty paid family receipt.
The family receipt checks preserve existing timed provider projects.
The no-DLC paid Prototype decisions retain their existing path.
The Electronics selection control also permits an already-completed exact Radar project to be adopted without the DLC, while it exposes fresh native commitments only with the DLC.
An existing Electronics commitment can be withdrawn in either DLC state when its research is inactive and the paid family receipt is empty.

Rocketry AI: the AI selects a Rocketry source only while that exact project is being researched or is complete, or when the other source cannot be researched at all (`brilliant_scientist_mengele_ai_wants_flying_bomb_source`, `brilliant_scientist_mengele_ai_wants_jet_engine_source`); otherwise a zero factor applies.
It releases a held Rocketry selection when that project is neither being researched nor complete while the other source is (`brilliant_scientist_mengele_ai_should_release_flying_bomb`, `brilliant_scientist_mengele_ai_should_release_jet_engine`), so completing the other project can then be adopted through its own selection.
Base weights and the war and factory-margin factors are unchanged; the player's controls, costs, and payload ownership are unchanged.
A narrow `hoi4.probability_inspect` call on these four decisions returned `INTERNAL_ERROR` on 2026-10-05, so the change is source-reviewed only.

## Completion and history

Each of the four existing project country outputs calls its literal source wrapper.
The wrapper records observation and may settle a fresh private Prototype only with the matching selected source, valid provider, private Theory, incomplete Prototype, and empty matching paid receipt.
Fresh settlement does not require completion-bit visibility inside the output boundary.
It records source and mode in fifteen-slot aligned provenance arrays and consumes only the matching selection.
The observed output fact remains distinct from accepted private history.

The after-Theory driver can adopt one unambiguous eligible completed source, or the matching selected source.
It rejects automatic adoption of retired sources and does not choose between two historical Rocketry completions.
The explicit selection controls resolve that two-source case.
Adoption checks the exact completed object, labels the receipt adopted, and does not replay native output or payment.
The generic unrelated-completion scan no longer settles these three families.

The Radar output invokes its literal Prototype wrapper before the existing radar-output marker and original radio_detection grant.
Successful fresh settlement stores its source and mode and consumes the selection before retrying the existing Radar Deployment pair.
Successful explicit or after-Theory adoption makes the same retry after provenance is durable.
That retry still requires the exact radar-output marker, radio_detection, the private Prototype predecessor and an empty paid receipt.
It preserves the dedicated Prototype result even when the nested Deployment helper clears family and stage selectors.

Cloning preserves its existing operational technology and dedicated programme payload through the guarded bridge.
A successful literal Cloning output supplies durable fresh provenance when the country completion bit is not yet visible.
The original CBRN completion adapter runs once, and the dedicated legacy completion effect retains its duplicate-payload guard.
Provider and terminal cleanup retire current selections and preserve observed facts and accepted source/mode history.
The enclosing Theory transaction restores its original selectors and output results.
Each result-consuming caller initializes its temporary result storage before the helper call.
The shared native selection, fresh settlement and exact adoption cores own the family, stage, index and output storage they consume after nested helper returns for every supported source.
The Cloning project country output also initializes the result before using the literal wrapper's success to grant its existing operational package.
This removes a dependency on helper-created temporary values surviving return, as described in the offline Data structures page's Variable types section.

## Reused vanilla and CBRN sources

High Energy (`sp_nuclear_reactor`) and Biological Weapons (six mapped agent projects) record exact provenance without selection controls, because those projects can be completed outside the provider.
The reactor and each agent settle through literal wrappers in their own project country output.
Fresh output requires the exact source witness at that boundary and does not depend on completed-bit visibility there.
The country-level Mengele completion scan is removed, so old unobserved completions cannot be relabeled as fresh when another project finishes.
Theory-time historical adoption queries the exact completed source and retains adopted mode and the existing fixed agent order.
A matching paid receipt continues unchanged when an output arrives, and repeated private Prototype outputs cannot grant another stage.
The six biological hooks preserve the original project payloads, timing, resources, iteration rewards, native AI and facility effects.
Existing provenance is not rewritten from later observations.
The nine fixed Event 016 projects need no selection controls because each family maps to one exact native project.
Their literal output wrappers record source codes 12 through 20 for Computation, Materials, Biomedical, Teleportation, Robotics, Paleogenetics, Xenobiological Synthesis, Alien Arms and Temporal Physics.
Each fresh receipt requires its literal output witness, and each historical receipt queries only the matching completed project.
The six custom operational packages are dispatched after changed private settlement, using exact fresh provenance if the country completed bit is not yet visible.
The original host and CBRN project consumers remain after each hidden hook.
Contracts are in `common/scripted_effects/016_mengele_native_prototype_effects.md`.

## Implementation surfaces

The new native_prototype constants, triggers, effects and matching API document define selection, exact output, adoption, release, and cleanup.
The native_selection_decision triggers/effects define presentation and feedback, and the English localisation file supplies all eight controls and requirements.
The existing stage effects own output application, after-Theory entry, and provider cleanup.
The existing native custom bridge owns operational grants.
Original project payload preservation is recorded in 016_native_prototype_project_preservation_2026-10-03.json.

The controls reuse GFX_decision_brilliant_scientist_project_cloning_prototype and GFX_decision_brilliant_scientist_project_rocketry_propulsion_prototype from interface/016_brilliant_scientist_project_icons.gfx.
Electronics reuses GFX_decision_brilliant_scientist_project_electronics_guidance_prototype in the same file.
Their existing textures remain under gfx/interface/decisions/016_brilliant_scientist/projects/.
No artwork, model, entity, animation, project ID, or technology ID is created or changed for this interface.

## CXT observation

The existing player-triggered native inventory console probe also calls chaosx_cxt_event016_probe_native_ownership.
It snapshots all four sources' selection, observed-output and retired flags, and the Cloning, Rocketry and Electronics source/mode slots into CXT-only debug observations.
It also snapshots the reactor and six biological source-observation flags and the High Energy and Biological Weapons source/mode slots.
The nine fixed families expose their source/mode slots and exact output-observed flags through the same guarded CXT probe.
Absent or short provenance arrays yield unrecorded observations without extending or changing provider receipts.
The probe creates no stage, native completion, selection, resource grant, or timer.
CXT's ordinary setup already completes native projects, so its completed-source path tests adoption and ambiguity, not native payment or a fresh research clock.

## Reference and review evidence

Installed projects/documentation.md:36-46 and198-213 defines project display gates in PROJECT scope with FROM country, and country outputs in COUNTRY scope with FROM project.
Its SHA-256 is 16879504bc72aa357f1d3c0f1093e94a3946f8c35e7942f65ac9a5d3bcd6c643.
Installed triggers_documentation.md:6228-6256 defines exact research/completion queries, and7482-7501 defines temporary-variable trigger operations.
Its SHA-256 is 7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29.
Offline Decision modding:44-78 describes category and decision structure, revision7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162.
Installed common/decisions/_documentation.md:1-46 describes decision evaluation and COUNTRY scope, revision5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019.
The existing family Prototype controls and the exact installed Rocketry project definitions supply the source and AI-policy precedents.
The core, integrated decision and probability handoffs record their separate evidence and unresolved inputs.
The Electronics continuation is recorded in 016_native_electronics_core_2026-10-03.md, 016_native_electronics_integration_2026-10-03.md and 016_native_electronics_ai_2026-10-03.md.
The parent independently reran the actual-source driver, including conservative temporary lifetime, paid-receipt preservation, exact-source provenance, integrated feedback and Cloning bridge-gate cases.
Engine queries, provider lifecycle, dynamic modifier refresh and full operational package payloads remain declared fixture inputs or stubs in those cases.
Its installed Radar precedent retains every native field, equipment module, facility effect, technology grant and reward after removing only the two owned country hooks.
That preservation comparison is source evidence, not native research or live-log acceptance.
The nine fixed-source continuation is recorded in `016_fixed_native_provider_sources_2026-10-07.md` and its core and integration handoffs.
Its source driver covers 10,953 scenarios, and the maintained adapter audit covers 4,911 assertions with their declared engine boundaries.

## Remaining lifecycle proof

Native start/cancel synchronization, automatic matching-cancellation cleanup, and immutable release/reselection callback generations remain unresolved under the full completion contract.
The selection layer does not waive them or represent explicit withdrawal as a substitute.
A synchronous native output can also be emitted by scripted completion, so fresh output is an exact witnessed transaction and does not independently prove native payment.
The overloaded MCP route retries and current domain evidence limits remain explicit in the handoffs.
Source scenario reasoning does not establish live callback timing, research continuation, or engine refresh.
The full Event016 goal remains incomplete until all fifteen families, lifecycle cases, AI/domain evidence, assets, UI, documentation, and catalog requirements are closed.
Future work should retain exact source identity while completing those lifecycle seams, without adding another public board or replacing native research with a provider clock.
