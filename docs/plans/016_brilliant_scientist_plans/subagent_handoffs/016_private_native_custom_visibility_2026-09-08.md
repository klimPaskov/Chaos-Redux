# Event 016 private native custom-project visibility audit

Date: 2026-09-08

Status: read-only source audit complete; no gameplay, weights, KRG maturation, GUI, localisation, or special-project files were changed.

Scope: trace the seven Event 016 custom families named in the request through their native project definitions, private `can_research_mengele_*` visibility triggers, native project-output callback, private native authentication, and operational adapter. This audit does not rely on stubbed test counts as proof of runtime wiring.

## Executive finding

Six of the seven Event 016 custom native project definitions already consume their corresponding private provider trigger in both `visible` and `available`. The only source-proven visibility gap is cloning: `brilliant_scientist_can_research_mengele_cloning_prototype` is defined at `common/scripted_triggers/016_mengele_project_bridge_triggers.txt:100-109`, but has no consumer outside its definition, while `sp_brilliant_scientist_cloning` remains host-only at `common/special_projects/projects/016_brilliant_scientist_projects.txt:385-389`.

The cloning downstream path is otherwise present: its native output calls `brilliant_scientist_record_new_project_prototype`, generic private callback routing accepts the cloning family, exact native authentication checks `sp_brilliant_scientist_cloning`, and the seven-family operational adapter already maps cloning to the neutral clone family. The minimal intended adapter is therefore to add the existing private trigger to the cloning project’s `visible` and `available` OR blocks, matching the six already-wired peers.

`sp_mengele_cloning` is a separate Germany/Mengele-chain project and is a deliberate exception, not the missing Event 016 adapter. It uses `camp_rework_germany_cloning_project_currently_available`, outputs `germany_mengele_complete_cloning_project`, and must not be retargeted to the Event 016 private trigger or callback.

## Seven-family consumer matrix

| Family | Native project and definition gates | Private provider trigger and consumer status | Native output callback | Private authentication and adapter status |
|---|---|---|---|---|
| Teleportation | `sp_brilliant_scientist_quantum_transit`, `specialization_nuclear`, `allowed = { }`, and `visible`/`available` OR host/private at `016_brilliant_scientist_projects.txt:315-319` | `brilliant_scientist_can_research_mengele_teleportation_prototype` is defined at `016_mengele_project_bridge_triggers.txt:88-97` and consumed by the native project at `016_brilliant_scientist_projects.txt:318-319` | `project_output` sets family `teleportation` and calls `brilliant_scientist_record_new_project_prototype` at `016_brilliant_scientist_projects.txt:341` | `brilliant_scientist_mengele_teleportation_native_output_is_authentic` at `016_mengele_project_stage_triggers.txt:1445-1453` checks strict provider, matching Theory, and `sp_brilliant_scientist_quantum_transit`; generic auth includes it at `:1574`; operational adapter maps it to `chaosx_custom_technology_family.portal` at `016_mengele_project_bridge_effects.txt:21-29` |
| Cloning | `sp_brilliant_scientist_cloning`, `specialization_biowarfare`, `allowed = { }`, but host-only `visible`/`available` at `016_brilliant_scientist_projects.txt:385-389` | `brilliant_scientist_can_research_mengele_cloning_prototype` is defined at `016_mengele_project_bridge_triggers.txt:100-109`; a repository search found no consumer outside that definition | `project_output` sets family `cloning` and calls `brilliant_scientist_record_new_project_prototype` at `016_brilliant_scientist_projects.txt:410` | `brilliant_scientist_mengele_cloning_native_output_is_authentic` at `016_mengele_project_stage_triggers.txt:1455-1463` checks strict provider, matching Theory, and `sp_brilliant_scientist_cloning`; generic auth includes it at `:1575`; operational adapter maps it to `chaosx_custom_technology_family.clone` at `016_mengele_project_bridge_effects.txt:31-39` |
| Robotics | `sp_brilliant_scientist_autonomous_cognition`, `specialization_land`, `allowed = { }`, and visible/available OR host/private at `016_brilliant_scientist_projects.txt:454-458` | `brilliant_scientist_can_research_mengele_robotics_prototype` is defined at `016_mengele_project_bridge_triggers.txt:112-121` and consumed at `016_brilliant_scientist_projects.txt:457-458` | `project_output` sets family `robotics` and calls `brilliant_scientist_record_new_project_prototype` at `016_brilliant_scientist_projects.txt:480` | `brilliant_scientist_mengele_robotics_native_output_is_authentic` at `016_mengele_project_stage_triggers.txt:1465-1473` checks `sp_brilliant_scientist_autonomous_cognition`; generic auth includes it at `:1576`; operational adapter maps it to `chaosx_custom_technology_family.robot` at `016_mengele_project_bridge_effects.txt:41-49` |
| Paleogenetics | `sp_brilliant_scientist_paleogenetics`, `specialization_biowarfare`, `allowed = { }`, and visible/available OR host/private at `016_brilliant_scientist_projects.txt:524-528` | `brilliant_scientist_can_research_mengele_paleogenetics_prototype` is defined at `016_mengele_project_bridge_triggers.txt:124-133` and consumed at `016_brilliant_scientist_projects.txt:527-528` | `project_output` sets family `paleogenetics` and calls `brilliant_scientist_record_new_project_prototype` at `016_brilliant_scientist_projects.txt:550` | `brilliant_scientist_mengele_paleogenetics_native_output_is_authentic` at `016_mengele_project_stage_triggers.txt:1475-1483` checks `sp_brilliant_scientist_paleogenetics`; generic auth includes it at `:1577`; operational adapter maps it to `chaosx_custom_technology_family.paleogenetic` at `016_mengele_project_bridge_effects.txt:51-59` |
| Xenobiological Synthesis | `sp_brilliant_scientist_xenobiological_synthesis`, `specialization_biowarfare`, `allowed = { }`, and visible/available OR host/private at `016_brilliant_scientist_projects.txt:594-598` | `brilliant_scientist_can_research_mengele_xenobiological_synthesis_prototype` is defined at `016_mengele_project_bridge_triggers.txt:136-145` and consumed at `016_brilliant_scientist_projects.txt:597-598` | `project_output` sets family `xenobiological_synthesis` and calls `brilliant_scientist_record_new_project_prototype` at `016_brilliant_scientist_projects.txt:620` | `brilliant_scientist_mengele_xenobiological_synthesis_native_output_is_authentic` at `016_mengele_project_stage_triggers.txt:1485-1493` checks `sp_brilliant_scientist_xenobiological_synthesis`; generic auth includes it at `:1578`; operational adapter maps it to `chaosx_custom_technology_family.xenobiological` at `016_mengele_project_bridge_effects.txt:61-69` |
| Alien Arms | `sp_brilliant_scientist_alien_arms`, `specialization_nuclear`, `allowed = { }`, and visible/available OR host/private at `016_brilliant_scientist_projects.txt:664-668` | `brilliant_scientist_can_research_mengele_alien_arms_prototype` is defined at `016_mengele_project_bridge_triggers.txt:169-178` and consumed at `016_brilliant_scientist_projects.txt:667-668` | `project_output` sets family `alien_arms` and calls `brilliant_scientist_record_new_project_prototype` at `016_brilliant_scientist_projects.txt:690` | `brilliant_scientist_mengele_alien_arms_native_output_is_authentic` at `016_mengele_project_stage_triggers.txt:1510-1518` checks `sp_brilliant_scientist_alien_arms`; generic auth includes it at `:1580`; operational adapter maps it to `chaosx_custom_technology_family.alien_infantry` at `016_mengele_project_bridge_effects.txt:71-79` |
| Temporal Mechanics | `sp_brilliant_scientist_temporal_mechanics`, `specialization_nuclear`, `allowed = { }`, and visible/available OR host/private at `016_brilliant_scientist_projects.txt:734-738` | `brilliant_scientist_can_research_mengele_temporal_prototype` is defined at `016_mengele_project_bridge_triggers.txt:181-190` and consumed at `016_brilliant_scientist_projects.txt:737-738` | `project_output` sets family `temporal` and calls `brilliant_scientist_record_new_project_prototype` at `016_brilliant_scientist_projects.txt:760` | `brilliant_scientist_mengele_temporal_native_output_is_authentic` at `016_mengele_project_stage_triggers.txt:1520-1528` checks `sp_brilliant_scientist_temporal_mechanics`; generic auth includes it at `:1581`; operational adapter maps it to `chaosx_custom_technology_family.temporal` at `016_mengele_project_bridge_effects.txt:81-89` |

## Shared callback path

- Every listed custom native project calls `brilliant_scientist_record_new_project_prototype` from its `project_output` block.
- `brilliant_scientist_record_new_project_prototype` at `common/scripted_effects/016_brilliant_scientist_project_effects.txt:1294-1308` selects the private path when `brilliant_scientist_mengele_project_stage_provider_is_valid = yes` and otherwise selects the current Kruger host path.
- `brilliant_scientist_record_mengele_project_prototype` at `common/scripted_effects/016_mengele_project_bridge_effects.txt:97-123` copies the public family into `mengele_event016_project_family`, calls `brilliant_scientist_mengele_record_native_project_prototype`, and invokes the seven-family operational adapter after a successful native record.
- `brilliant_scientist_mengele_record_native_project_prototype` at `common/scripted_effects/016_mengele_project_stage_effects.txt:1372-1398` routes non-Singularity families through `brilliant_scientist_mengele_sync_native_project_prototypes`.
- `brilliant_scientist_mengele_sync_native_project_prototypes` at `common/scripted_effects/016_mengele_project_stage_effects.txt:1358-1370` requires `brilliant_scientist_mengele_project_native_output_is_authentic`, applies the family Prototype output, and clears stage selectors.
- `brilliant_scientist_mengele_project_native_output_is_authentic` at `common/scripted_triggers/016_mengele_project_stage_triggers.txt:1566-1583` includes all seven family-specific authenticators, including cloning despite its missing visibility consumer.

## Deliberate `sp_mengele_cloning` exception

- The separate project is `sp_mengele_cloning` at `common/special_projects/projects/mengele_cloning_projects.txt:17-73`.
- Its `visible` and `available` blocks call `camp_rework_germany_cloning_project_currently_available` at `:23-32`, not an Event 016 private trigger.
- Its output calls `germany_mengele_complete_cloning_project` at `:68-72`, which sets `germany_mengele_cloning_project_completed`, `directorate_special_project_cloning_completed`, and Germany-specific clone production/revolt behavior in `common/scripted_effects/germany_mengele_effects.txt:104-119`.
- The test-country helper’s `complete_special_project = sp:sp_mengele_cloning` at `common/scripted_effects/chaosx_test_country_special_project_effects.txt:60` is a separate Germany-chain fixture and does not prove Event 016 native visibility.
- Event 016’s private cloning authenticator checks `sp:sp_brilliant_scientist_cloning`, not `sp:sp_mengele_cloning`, so replacing or redirecting it would conflate two histories and output contracts.

## Exact gap and safe minimal adapter proposal

### Source-proven gap

`brilliant_scientist_can_research_mengele_cloning_prototype` is a live scripted trigger definition with private provider, Theory, incomplete Prototype, incomplete public completion, incomplete native completion, and availability-flag gates at `common/scripted_triggers/016_mengele_project_bridge_triggers.txt:100-109`. A repository-wide source search found zero consumers outside that definition.

The only missing consumer is the native Event 016 project presentation gate at `common/special_projects/projects/016_brilliant_scientist_projects.txt:388-389`, where both `visible` and `available` call only `brilliant_scientist_can_research_cloning_prototype`.

### Minimal intended connection under the accepted full-portfolio plan

If the parent accepts native private presentation for the full seven-family portfolio, the narrow source change is to expand only those two cloning blocks to the existing peer pattern:

```text
visible = { FROM = { OR = { brilliant_scientist_can_research_cloning_prototype = yes brilliant_scientist_can_research_mengele_cloning_prototype = yes } } }
available = { FROM = { OR = { brilliant_scientist_can_research_cloning_prototype = yes brilliant_scientist_can_research_mengele_cloning_prototype = yes } } }
```

No new trigger, effect, project, category, family, history flag, cost, adapter, or authentication branch is needed because the existing private trigger, generic callback, exact authenticator, and operational adapter are already present.

This proposal is documentation only in this audit; no source patch was applied.

## Severity and lifecycle notes

### Medium: private cloning native presentation is unreachable

The missing `visible`/`available` consumer prevents the private provider from selecting `sp_brilliant_scientist_cloning` through the native project interface, even though the callback and authentication pipeline is complete.

### Low: unused trigger discoverability

The six wired private triggers are consumed directly by native project definitions, while the cloning trigger is currently a zero-consumer stub from the source graph perspective. The trigger should remain as the canonical provider gate because the accepted adapter proposal uses it.

### No callback or authentication gap found

The cloning output callback, generic private route, exact native completion authenticator, and neutral operational grant mapping are all present. Do not add duplicate cloning callbacks or weaken authentication.

### No `sp_mengele_cloning` migration

The Germany/Mengele-chain project remains separate and should not be used as the Event 016 private native presentation surface.

## Validation and evidence limits

- Direct source inspection covered the seven project definitions, private bridge triggers, project output blocks, generic callback, private native record/sync effects, individual authenticators, generic authenticator, operational adapter, and separate `sp_mengele_cloning` project.
- A targeted `rg` search confirmed private trigger consumers; six trigger names occur in their corresponding native project’s `visible` and `available` blocks, while cloning occurs only in its defining trigger file.
- Offline Paradox wiki core pages and installed vanilla special-project documentation were consulted for special-project visibility/availability semantics.
- No stubbed test count was used as evidence for consumer wiring, and no gameplay/weights/KRG source was changed.
- No narrow special-project MCP route is exposed by the installed HOI4 tool surface, so this is a source audit only; no runtime engine visibility claim is made.
- No GUI or project-board render was needed for this source-only visibility-consumer audit.

Initial audit disposition: one precise source gap identified (`sp_brilliant_scientist_cloning` private visibility/availability consumer); all other six custom families were already wired end-to-end; parent review was required before applying the two-line cloning visibility adapter.

## Parent acceptance and post-application verification

Parent acceptance recorded 2026-09-08: the minimal full-portfolio adapter was accepted and applied to `sp_brilliant_scientist_cloning` only, with no reward, cost, weight, authentication, `sp_mengele_cloning`, or KRG-maturation changes in that adapter hunk.

The current source now has the expected two-line peer pattern at `common/special_projects/projects/016_brilliant_scientist_projects.txt:388-389`:

```text
visible = { FROM = { OR = { brilliant_scientist_can_research_cloning_prototype = yes brilliant_scientist_can_research_mengele_cloning_prototype = yes } } }
available = { FROM = { OR = { brilliant_scientist_can_research_cloning_prototype = yes brilliant_scientist_can_research_mengele_cloning_prototype = yes } } }
```

A fresh targeted consumer search now returns exactly the two native project consumers at lines `388-389` plus the trigger definition at `016_mengele_project_bridge_triggers.txt:100`; there is no additional consumer or duplicate adapter.

The focused diff confirms the cloning hunk changes only those two visibility lines. The same project file contains unrelated concurrent materials and biomedical reward edits outside this adapter hunk; they were preserved and are not attributed to this audit.

The source-level disposition is now `implemented`: all seven custom families have private native visibility consumers, output callbacks, exact private authenticators, and operational adapter branches. This does not claim native engine presentation, probability, or balance completion.

The native special-project MCP/probability adapter was unavailable to the auditor, and the baseline weighted auditor’s earlier pre-adapter description was returned for correction; this handoff makes no weighted or engine-runtime completion claim.
