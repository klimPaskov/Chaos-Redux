# Event 014 completion resume audit, 2026-10-03

Status: **INCOMPLETE**.
This is a read-only completion audit of current Event 014 integration and owner contracts, not implementation or live-game acceptance.
The audit writes only this handoff and makes no commit.
The shared checkout HEAD at initial inspection was `01bc85ee3c9f25be8bda48dbdd7dc4d0ed1f98fe`.
Concurrent parent corrections are identified separately below.

## Authorized scope and authority

The user explicitly resumed Event 014 within the events 1 through 40 completion effort.
Current authorization is three origins, nine gameplay families, seven installed bespoke model packages, Bone Riders on vanilla `sprite = cavalry`, Network Cadre on vanilla `sprite = infantry`, separate vanilla `elephantry`, and no animation toggle.
The two vanilla reuse decisions are approved simplifications, not unresolved model tasks.
No model production was reopened.
Other events and their agents' changes were not edited.
The parent owns detailed model/entity/audio/counter review and the user or orchestrator owns live-game acceptance.
No HOI4 launch, runtime-log request, or runtime-log search was performed.

Required authority read: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-event-planning`, `chaos-redux-improvement-loop`, `chaos-redux-subagents`, relevant event-assets, super-event, scripted-GUI, decisions/missions, and 3D handoff guidance.
Event-specific authority includes `resume_packet.md`, `documentation_state.md`, the spec README and acceptance criteria, the current event overview, current identity surface matrix, the August 26 improvement disposition, and relevant current specialist handoffs.
Old closure reports were read as historical evidence and were not promoted into current completion proof.

## Current implementation defect

### E014-COMP-01: Provider 523 builds an invalid division layout and records the same invalid coordinates

**Status: open implementation defect.**
Owner: Event 014 parent in coordination with the Event 019 consumer owner.
Evidence: `common/scripted_effects/014_cannibalism_effects.txt:19658-19702`.

The provider template puts `cannibal_island_reavers` at `x = 0 y = 5` on line 19672.
Installed `MAX_DIVISION_BRIGADE_HEIGHT = 5` permits zero-based rows 0 through 4.
The same column contains infantry-group families and `cannibal_bone_riders` at `x = 0 y = 4` on line 19671.
Bone Riders is `group = mobile` at `common/units/014_cannibalism_irregular_infantry.txt:520`, while the other families are infantry-group definitions.
The offline Division modding reference states that a column cannot change group.

The component ledger also appends row 5 at lines 19694-19695 and records Bone Riders in the same infantry column.
Fixing only the template text would leave the Event 019 transaction ledger out of agreement with the actual template.

Recommended owner patch: retain all nine bodies in one provider lot, arrange the eight infantry bodies within valid infantry columns, give Bone Riders its own mobile column, and update every appended component coordinate to match.
No gameplay-family removal, model replacement, or new provider family is required.
After the patch, verify template-to-ledger equality, all nine consumers, and the provider spawn/sustainment transaction.

Meaningful read-only validation found nine provider body tokens, exact equality with the nine installed Event 014 definitions, one out-of-range coordinate, and mixed infantry/mobile groups in column 0.
The intended totals are correct: 7,350 manpower, 990 infantry equipment, and 35 motorized equipment.
Those totals match `common/script_constants/014_cannibalism_constants.txt:3649-3652` and the provider obligation callbacks at `014_cannibalism_effects.txt:19709-19724`.
There is no demonstrated resource-total defect.
The CXT formations already separate Bone Riders from the mixed infantry muster at `common/scripted_effects/014_cannibalism_cxt_test_effects.txt:84-117`.
This source diagnosis does not assert how the engine handles the invalid template.

## Parent correction reviewed

### E014-COMP-02: Scavenger Warband mesh object binding corrected

**Status: implemented by parent and reviewed at the source/receipt boundary.**
Before: `gfx/entities/014_cannibalism_units.gfx:156` registered `mesh_node.001`.
After: the same line registers `mesh.001`, stream index 0.
The reviewed Git diff changes that one scalar and preserves the mesh path, eight action references, shader, and three material texture bindings.
The Scavenger v2 runtime handoff line 29 now records the exported `mesh.001` object and stream index 0.
The parent's completed repair handoff is `subagent_handoffs/2026-10-03_material_binding_repair.md`.
It records selected-source SHA-256 `32797fd2487009d0f25b64546b5842d7e687ac9aedf5c71c7c17c75be851f19b` and installed derivative SHA-256 `72532f027fd58a7d2f7ef0151a192140b1698a5193df0130132ee390023af308`, with the decoded difference limited to three material texture basenames.
The source and runtime files are therefore distinct documented derivatives, not byte-identical copies.

The parent-owned receipts are:
- `docs/plans/014_cannibalism_plans/evidence/2026-10-03_runtime_unit_bindings_before.json`, SHA-256 `2d09adcbaa71291cfd885de7a41b99a9174e2699da264b98d3dc9e3e0022fbe9`.
- `docs/plans/014_cannibalism_plans/evidence/2026-10-03_runtime_unit_bindings_after.json`, SHA-256 `a9dc4753057922ff00d1c06c0658625a8c79b75a90d8325a394555f91c0ebb76`.

Their summaries cover seven meshes, 56 actions, 21 material textures, and 86 registered state audio cues.
The before receipt has one material-node mismatch and the after receipt has zero findings.
The parent reported that all 24 action bone names match each mesh and no entity sound time exceeds its last animation sample.
This auditor reviewed the receipt summaries and source diff and did not rerun the detailed binary audit.
The after receipt explicitly excludes live or visual role/contact acceptance and does not infer authorship, rights, or provider/reimport provenance.
No geometry, animation, or material bitmap change is represented by this correction.

## Documentation and asset completion gaps

### E014-COMP-03: Five current model manifest links are absent

**Status: open documentation/receipt gap, not missing runtime models.**
The current `docs/assets/014_cannibalism/models_3d/family_jobs.json` names absent root `manifest.json` files for Feast Guard at line 36, Feast Cohort at line 44, Bone Guard at line 52, Siege Eaters at line 68, and March Predation Column at line 76.
The Scavenger and Island Reavers root manifests exist.
This was confirmed by direct path existence checks and is also retained in the parent's after receipt.

Recommended owner action: recover the actual surviving package manifests or correct each ledger link to a real authoritative handoff with an explicit archival-manifest disposition.
Do not fabricate provider receipts or turn the new installed-byte receipt into missing authorship/reimport evidence.
Keep production closed and record remaining provenance limits explicitly.

### E014-COMP-04: The resume documentation's super-event image-registration queue is stale

**Status: source image registration finished, documentation stale, presentation acceptance open.**
`interface/chaosx_super_events.gfx:188-201` registers all four Event 014 sprites.
`common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:250-253` maps slots 49, 50, 52, and 53 to their correct distinct sprites.
All four runtime DDS files exist, have DDS headers and 457 by 328 dimensions, and have distinct SHA-256 hashes.
All four emitters at `014_cannibalism_effects.txt:11412-11499` require public reveal before dispatch.

The image files and hashes are:
- Reveal: `50b4f7a95818845bede3892a6545fc428277c9482349a80e1f7d37c6ab606e38`.
- Ordinary terminal: `cf5173a65873cfdd548e6b5c3334c1013572c5c3bc725ee81edfd481e5551ca8`.
- Global defeat: `cf57406a51693ffc07363027337b65b331ff403876bd5ca3a5a336b05796571e`.
- Wendigo terminal: `597c31ef0e1726402fc157a27e89f6d202341b9fb7b6583feb7ffc8e62170fe1`.

Recommended documentation patch: retire the missing-registration claim in `resume_packet.md` and `documentation_state.md` while retaining visual action-composition and live-presentation review as separate evidence gates.
DDS presence, dimensions, and different bytes do not prove composition quality or in-game presentation.

### E014-COMP-05: Current portrait placeholders remain incomplete finals

**Status: explicit asset blocker, not absent portrait-worker handoff.**
The later `subagent_handoffs/event014_portrait_completion_2026-08-26.md:9-11` records 56 distinct source-placeholder packages and explicitly states that every replacement remains pending.
Lines 31-43 distinguish sourced reference coverage from the 56-of-56 blocked final redistribution gate.
A current portrait-worker handoff exists, so an older missing-worker-receipt claim must not be repeated without checking what receipt it specifically means.
The requested HOI4-style finals and their authorized replacement/provenance evidence remain unresolved.
The parent must retain this blocker and must not infer finished portraits from 56 installed DDS files.
No portrait production or RunPod operation was attempted here.

### E014-COMP-06: GUI specialist evidence remains incomplete

**Status: current completion-evidence gap.**
The named Event 014 windows have ownership proof and worker handoffs, including `event014_gui_completion_2026-08-26.md:11-27`.
That handoff's lines 5-7 expressly leave visual completion blocked.
The August 25 GUI handoff records absent attributable cropped/annotated/hierarchy/click-region evidence and unresolved state/resolution comparisons at lines 225-257.
Optional `gui_rewrite` was not required for a read-only pass that found no attributable patch.
The missing visual evidence must not be recast as a source defect or as a missing worker.
This bounded completion audit did not redo the GUI worker's layout review or request work on shared Event Details, settings, or super-event frameworks.

## Source surfaces checked with no demonstrated current defect

| Surface | Current status | Source evidence and limit |
| --- | --- | --- |
| Event root and classification | Implemented in source, engine coverage partial | `events/014_cannibalism.txt:18-25`, fire-once registration at `chaosx_logic_effects.txt:251`, availability checks at lines 726-745. |
| Prefire preparation and actor mapping | Implemented in reviewed source | Shared preparation at `chaosx_settings_effects.txt:4140-4148`, `014_cannibalism_effects.txt:3562-3624`, and default actor mapping at `chaosx_events_log_effects.txt:311-324`. No fresh full transaction proof. |
| Startup safety | Registration only in inspected startup path | `014_cannibalism_on_actions.txt:17-25` calls provider/CXT registration in one existing-country scope. Provider registration writes registry metadata, not event activation or unit grants. |
| CXT daily fallback | Safe, initial grant finding withdrawn | `014_cannibalism_on_actions.txt:29-40` calls the shared wrapper. `chaosx_test_country_effects.txt:442-444` sets only pending. Actual application is the separate `_apply` effect at line 449 and initial setup calls it at line 425. No patch is needed. |
| Nine-family CXT coverage | Implemented in source | One modifier-free carrier, matching setup token, all nine subunit registrations, and infantry/mobile formations. Current token cross-check found no missing Event 014 definition. |
| Pulse lifecycle | Substantial implementation, validation incomplete | Ticket ownership at `014_cannibalism_triggers.txt:2594-2607`, scheduling at effects lines 1708-1782, retired-callback quarantine and rehoming at 1784-1850, pulse dispatch at 3217-3257. No full MCP lifecycle sign-off. |
| Global victory and cleanup | Implemented in inspected source, evidence open | Resolver and cleanup at `014_cannibalism_effects.txt:2490-2617`, residue trigger at `014_cannibalism_triggers.txt:2610-2632`. Release, callback draining, and final residue scenarios remain required. |
| Reveal secrecy | Sampled source gates present, no proven current leak | Ordinary reveal flag precedes CBL public creation at effects lines 12406-12424. Named GUI windows require reveal at scripted-GUI lines 184-217. Evolution III title selectors require reveal at shared localisation lines 2222, 3357, and 6966. Named event triggers require reveal. This is not a full visual secrecy audit. |
| Four super-event image consumers | Registered and file-backed | Four sprite definitions, four selector mappings, four valid-size distinct DDS containers. Live presentation remains open. |
| Models, audio, counters | Parent-reviewed runtime wiring, acceptance bounded | The parent owns the exact-byte bindings and detailed seven-model audit. This handoff does not duplicate or replace it. Five archival model manifests are still absent. |
| Focuses, country packages, missions, achievements | Existing specialist implementation records, not reaccepted by this bounded pass | Old zero-defect counts are frozen-scope history. No new full focus/decision/country/achievement audit or live acceptance was performed here. |
| Catalog | Completion status unpromoted | Resume docs retain `Events!N15` and `Scenarios!F10` as Needs Testing. The workbook was not edited or independently reaudit-tested in this pass. |

A read-only literal helper-call inventory found no undefined `cannibalism_*` calls across current common/event text definitions.
That check cannot resolve meta dispatch, parameter semantics, engine execution, or the focused MCP helper catalog.

## Accepted-plan disposition

The user message supplies current acceptance for three origins, nine gameplay families, seven bespoke packages, two named vanilla visual reuses, and no animation toggle.
The August 26 improvement addendum records the accepted elite Rider, elephant, Bone Guard sequence as promoted into spec parts 4, 6, and 12.
Older accepted focus/technology-union/icon addenda have recorded implemented/promoted dispositions in the spec README and the August 26 disposition table.
This pass does not turn those recorded dispositions into new runtime acceptance.

Optional cross-origin joint operations, route-aware recovery case files, and inspection-access compacts are explicitly queued but unaccepted and nonblocking.
No broad improvement expansion is recommended.
The current provider-layout defect is a bounded correction to the accepted implementation, not a reason to reopen model production or add another origin.
Final lifecycle, probability, GUI, portrait, provenance, and live-consumer evidence remains open.

## Live MCP evidence and exact limits

Connected schemas expose `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, and the reference/source routes.
No confirmed server-health/version route or client task-negotiation evidence was available in this audit, so helper-expansion and native job routes were not used.

- The initial root trace requested `chaosx.nr14.1`, downstream depth 2, 20 nodes, 35 edges, helpers off, refresh true.
  It did not yield a completed result during the prolonged wait and its client wait was stopped.
- A narrower root lint retry used depth 1, one node, one edge, helpers off, full workspace ID.
  It exceeded an explicit 55,000 ms client audit deadline with no result or artifact.
- A further cached root trace with depth 1, two nodes, two edges also exceeded that client deadline.
  These are client nonresponse limits, not invented server timeout codes.
- The options render for `chaosx.nr14.2`, depth 1, four nodes, helpers off, returned `EVENT_RENDERED_PARTIAL`, status ok.
  Revision: `e9e470262f1ea057b06851d06c768e7e69517688395c2427a2d534af5005edff`.
  Graph hash: `f1f3fe2750c44bb62d31407f7e92684b9092d34dcec5e9be3f77666ccae16663`.
  Analysis mode: focused.
  The full resource has `complete = false`, four selected nodes, three option edges, 42,950 omitted workspace nodes, and a 386-source hash inventory.
  Indexed helpers are zero and whole-workspace helper/lifecycle analysis is deferred.
  The three option helpers are `EVENT_HELPER_UNRESOLVED` in that active focused catalog, even though current source definitions exist at effects lines 3640, 3668, and 3693.
  These are missing MCP coverage, not missing source implementations.
  The full JSON was read using byte-range resources and the PNG was visually inspected.
- An initial comparison invocation was rejected because documentation_state.md line 75 records a 65-character revision, which fails the live 64-hex revision contract.
  The corrected old-artifact baseline request with a one-node boundary exceeded the 55-second client deadline.
  Independently reading the old lint artifact's provenance manifest returned `-32603: Artifact provenance manifest is unavailable`.
  No comparison artifact or before/after engine conclusion was obtained.
  The malformed historical revision should be corrected from an authentic surviving receipt, never guessed.
- `hoi4.source_lookup` for the exact provider-template helper, one definition, no references, 45 lines, exceeded the 55-second client deadline.
  Direct source reading supplies file evidence only.
- Event reference context/search succeeded, but context omitted six topics.
  The targeted reference-read/search continuation did not finish during the audit and its client wait was stopped.
  Relevant local sections were read directly below.
  No full core reference coverage is claimed.

Current render artifacts:
- event-options-e9e470262f1e-manifest.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14a78a1b86d8b198f8f114b46e3a1de759d168ca20e65fa70ab88f330f658f11/da172f3888e1a55affb51b92ed3bac9dcb9bd24895c434c737c6b228760fb55f/event-options-e9e470262f1e-manifest.json`, SHA-256 `14a78a1b86d8b198f8f114b46e3a1de759d168ca20e65fa70ab88f330f658f11`.
- event-options-e9e470262f1e.json: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ae8ead00069b0cf3a7e1feec3dbe0eadee6d6b3b8ff20d6b1770512e2910fd7/3f9337a50a39ed05c32664a63a63348570bcbf1a59ff550cd8bc335112303033/event-options-e9e470262f1e.json`, SHA-256 `8ae8ead00069b0cf3a7e1feec3dbe0eadee6d6b3b8ff20d6b1770512e2910fd7`.
- event-options-e9e470262f1e.svg: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7b89efa7776de7912ad26bb290247eba78be6067b00365fa7a8db7f6e3fbf44e/bcec37c14156407635145e396287aa74b0c11ffdd0186a34b53462f29d59f64d/event-options-e9e470262f1e.svg`, SHA-256 `7b89efa7776de7912ad26bb290247eba78be6067b00365fa7a8db7f6e3fbf44e`.
- event-options-e9e470262f1e.png: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90afba928c9a814ab3da851c65de584478426de4eb086c565739b2d6cf2cba3a/a137cd979f7a5d392d7a8166c86b831cf3bad217f5e08f90d0850befea3986c6/event-options-e9e470262f1e.png`, SHA-256 `90afba928c9a814ab3da851c65de584478426de4eb086c565739b2d6cf2cba3a`.

## Reference evidence

- Offline wiki `paradox_wiki/Division modding - Hearts of Iron 4 Wiki.md:51-72`, column groups and zero-based template limits, SHA-256 `19b8349a2e1a7da45d138c0807119d1ab5e24c391a8182099ff59ff18d8be147`.
- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\defines\00_defines.lua:859-863`, template limits, SHA-256 `405a24ce579815443cafe052cff1361e20c712ca8182e3f10ccbf45330dd4be4`.
- Installed effects documentation `documentation/effects_documentation.md:3625-3632`, country scope for `division_template`, revision/SHA-256 `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Installed precedent `history/units/GER_1936.txt:4-40`, legal template coordinates and separate regiment columns, SHA-256 `bdf33f60d8e1d972f8fd56c92e550c53d2af9140776e708d28f4952f2e806b17`.
- Installed `common/on_actions/00_on_actions.txt:931-932,1615-1616,1633-1634,4911-4914`, capitulation/annex/startup/war-relation scope comments, source hash from the fresh render `52a751456f1774ad5001c86d41d4e46494f751d79b6c224b6cd4c0eebb615eb9`.
- Offline `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`, corresponding war-relation/capitulation/annex sections.
- Current CXT contract `docs/testing/chaosx_test_country.md:87,105`, registration/pending only for daily hooks.

The context response identified installed on-action documentation revision `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4` and offline Event modding revision `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d`.
Its headers/context bundle are discovery evidence and do not prove the detailed rules were read through MCP.

## Weighted-surface routing

A fully self-contained, no-inherited-context, read-only `chaosx_ai_probability_auditor` was spawned as `01a10109-440d-74d2-8bec-a2ccc0860c92`.
It was assigned current event option/random/helper discovery and scenario evidence, with all previous August probability reports explicitly treated as baseline/limits.
No weights were changed and this auditor chose no balance targets.
The specialist returned its full inline handoff before final delivery: **current probability sign-off is blocked**, with no confirmed current weighted implementation defect.
Its corrected file-source `probability_inspect` request received no result in an approximately five-minute client wait, and its narrower `.2` identifier retry received no result in an approximately two-and-a-half-minute client wait.
Both client waits were stopped without a returned status, artifact, source revision, candidate list, or scenario hash.
No current evaluate, sweep, render, simulation, sequence, or probability comparison result was obtained.
The specialist reviewed the same current event/effects/constants raw hashes recorded here.
It identified 32 explicit `ai_chance` blocks across nine current event pools: `.2` at lines 38-65, `.20` at 110-136, `.21` at 173-202, `.30` at 226-236, `.60` at 289-333, `.61` at 373-404, `.71` at 475-545, `.80` at 717-796, and `.81` at 826-864.
The nested `.80.d` list at lines 772-781 has source weights 85 and 15, conditional on that option's own gate.
The effects file has seven regional name pools, one personality pool, and three dynamic outcome pools, which remain source observations rather than current normalized probabilities.
Host/state selectors at effects lines 1328-1364 and 1451-1491 use score arrays and `find_highest_in_array`, so they are deterministic score selection rather than probability-proportional pools.
The specialist found no current evidence that justifies a weight patch, a dominance/starvation claim, or a rank/timing conclusion.
The `.30` human-switch zero is the documented player-safety branch, not a newly discovered starvation defect.
Prior `E014_POLICY_BASELINE_2026_08_26`, `E014_POLICY_DEMO_2026_08_26`, player-safety, capture-outcome, regional-name, personality, forensic, and missing-burial scenarios remain historical fixtures.
Current external gate/candidate completeness is unresolved, particularly route and integrity states for `.20`/`.21`, alignment/player-safety inputs for `.71`, valid captured targets and anti-decapitation states for `.80`, and reveal/terminal-lock conditions for `.81`.
Aggregate event, decision/mission, focus, MTTH score, country-scorer, and dynamic provider probabilities remain unaccepted until the specialist provides exact scenario and coverage evidence.
Any future weighted patch needs owner-applied changes and the specialist's matching-scenario probability comparison.

## Source identity at audit cut

| File | SHA-256 |
| --- | --- |
| `events/014_cannibalism.txt` | `9d547737d176a96bc359ba9c3b1cb2422fd6e399448f4453c551c9c6059e14f9` |
| `common/on_actions/014_cannibalism_on_actions.txt` | `7c6009b52f8e85735c65a13842201ff30d0d50ba89b6f39fd12e2c48822561a1` |
| `common/scripted_effects/014_cannibalism_effects.txt` | `ed6a485ca3fc49f92e45088fbe58acf8e63e15a73c2412438dcb1895b2143f97` |
| `common/scripted_effects/chaosx_test_country_effects.txt` | `fb9b483db5d1a70b4f0900135b22815c612989ae0b3a4d50bca05072b22c39c3` |
| `common/script_constants/014_cannibalism_constants.txt` | `6972f5972ac0021854a4b2354c52eedb0fbd0ff65806546528b81f02f3608abe` |
| `common/units/014_cannibalism_irregular_infantry.txt` | `db9abb73d642c3fe218543d8444d609a5141e843fc7478cbba875701d5253623` |
| `interface/chaosx_super_events.gfx` | `b7448b72d30498b6372e771a53dc1683d479de38912b33c14387e287e3a2ccda` |
| `gfx/entities/014_cannibalism_units.gfx`, parent-corrected | `c5f3155fcd1fa57a44774b5a263db52158447f7d3d2c69eba2ca15bdee00a3d8` |
| `docs/assets/014_cannibalism/models_3d/family_jobs.json` | `6db6fd9882f5ceef7be6cc5a481917e4db3f0ecc658f387b55fe4ddce886e18a` |

## Recommended owner continuation

1. Correct provider 523's native template and matching component ledger, then recheck all nine tokens and unchanged obligations.
2. Retain the reviewed Scavenger binding correction and parent exact-byte receipts.
3. Repair the five manifest links and reconcile stale super-event image and portrait-receipt claims.
4. Obtain current event inspect/helper/lifecycle and graph-bearing comparison evidence without claiming that the focused render covers those systems.
5. Finish the specialist probability pass, required GUI scenario evidence, portrait finals/provenance, and parent/user live-consumer gates.
6. Update completion/catalog status and commit only the parent's finished authorized changes when their own completion requirements are satisfied.

No new simplification was introduced by this audit.
The two approved vanilla visual simplifications remain explicit.
The event must not be marked complete from old zero-defect audits, installed assets alone, a partial render, or the corrected Scavenger binding alone.
