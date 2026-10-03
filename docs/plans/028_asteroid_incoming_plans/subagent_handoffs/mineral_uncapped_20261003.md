# Event 028 uncapped mineral armour handoff

Disposition: implemented in owned source with the parent runtime wrapper, shared achievement count call, transition callbacks, legacy marker label, helper contract document, and owner index row integrated.
The bounded source tranche is ready for parent review and an isolated commit, while native acceptance remains unresolved.
Acceptance basis: the explicit user-authorized full Event 028 package and this parent's bounded instruction correct the existing Part 5 requirement for current-controller plus 100 percent main-crater armour and uncapped plus 20 percent per controlled fragment.
The subsequent parent-owner decision authorizes the exact six-guard shared predicate and country count helper, replacing only the existing weaker achievement recount without another monthly country refresh.
No stat value, normal fragment generation count, AI weight, cost, branch, identity, or map is redesigned.
The parent owns runtime/history source, legacy English marker labels, host/control/annex callbacks, final integration, and commits.
The worker does not launch the game or commit.
Skills read fully for this implementation: `chaos-redux-events` and `chaos-redux-subagents`.

## Owned files and identifiers

- New `common\scripted_effects\028_asteroid_incoming_mineral_effects.txt` provides the uncapped refresher, country recomputation, shared country count, explicit annex/dead-recipient cleanup, first-migration legacy dead-controller cleanup, and existing-alias presentation adapter.
- New `common\scripted_triggers\028_asteroid_incoming_mineral_triggers.txt` provides the STATE-scoped `asteroid_incoming_is_processed_mineral_fragment` predicate with exactly six current physical-site validity guards.
- New `common\dynamic_modifiers\028_asteroid_incoming_mineral_dynamic_modifiers.txt` defines `asteroid_incoming_fragment_crater_armour`, binding only `armor_factor` to the recipient's normal `asteroid_incoming_fragment_armour_bonus` variable.
- Existing `common\ideas\028_asteroid_incoming_ideas.txt` changes only the modifier bodies/comments of fragment_material_1 through fragment_material_6.
- New BOM English file `localisation\english\028_asteroid_incoming_mineral_dynamic_modifiers_l_english.yml` defines only the new dynamic modifier's name and description keys.
- This new handoff contains contracts, baseline evidence, references, integration limits, and executable actual-source scenarios.

No new constants file is needed.
The existing `constant:asteroid_incoming_mineral.fragment_site_armour_factor = 0.20` is reused.
The main idea's file-local factor remains `@ASTEROID_MAIN_CRATER_ARMOUR = 1.00` and its entire definition is preserved.
The old fragment file-local factor remains unchanged outside the permitted modifier bodies and is no longer a bonus consumer.
Fragment_material_1 is a visible modifier-free marker for any country with positive valid fragment count, preserving the existing AI idea predicate source.
Fragments 2 through 6 are modifier-free retired identifiers and are removed by the new refresh path.
One dynamic modifier implements all fragment stat bonuses, so the marker cannot double the bonus.

## Helper contracts

| Helper | Scope, inputs, and call sites | Outputs and side effects |
| --- | --- | --- |
| `asteroid_incoming_refresh_uncapped_mineral_control` | ANY scope, called by the parent-owned legacy refresh wrapper. Reads active-minerals flag, main-state target, fragment registry, prior recipient ledger, and existing fragment state aliases. | One existing-country pass, bounded former/dead recipient cleanup, current controller targets, overwritten country counts/bonuses, modifier lifecycle, cleared scratch array. |
| `asteroid_incoming_recompute_mineral_country` | Existing COUNTRY, called from the refresher's every_country. | Normal `asteroid_incoming_country_controlled_fragment_count` and `asteroid_incoming_fragment_armour_bonus`. Maintains main idea, marker 1, one dynamic modifier, and current recipient ledger. |
| `asteroid_incoming_count_controlled_mineral_fragments` | COUNTRY, called once by country recomputation and by the parent's existing achievement-country loop. | Overwrites the normal public count from current controlled states and the shared predicate, or zero when inactive. Does not create scratch, mutate bonus/ideas/modifier, or iterate countries. |
| `asteroid_incoming_is_processed_mineral_fragment` | STATE trigger, reads registry membership and five additional physical-site conditions. | Read-only true for a registered, flagged, applied non-main fragment center. Shared by count and presentation collection. |
| `asteroid_incoming_clear_dead_mineral_recipient` | COUNTRY, explicitly selected as annexed FROM by the callback or as exists=no by recorded-recipient cleanup callers. No internal existence guard. | Zeros count/bonus, removes main and all legacy fragment ideas, removes the owned dynamic modifier. No grant, including transitional exists=yes. |
| `asteroid_incoming_cleanup_legacy_dead_mineral_controllers` | ANY scope, first call inside refresher before replacing old targets. | Cleans dead countries still named by the previous implementation's main and six controller aliases, including first deployment before a new recipient ledger exists. |
| `asteroid_incoming_publish_mineral_fragment_controllers` | ANY scope after country recomputation. Uses the typed, unique scratch states and existing six named state aliases. | Republishes only their actual existing controllers for current-control localisation. It does not count or grant a bonus and contains no array-ordinal branch. |

No temporary output is consumed across a helper return.
Persistent outputs are normal COUNTRY variables and global arrays/targets.
The source tests use conservative helper-frame cleanup of any first-created temporary storage.
Public invocation is `= yes`, without named parameter blocks or placeholder parameters.

## Counting, validity, and lifecycle

Each existing country's every_controlled_state iterates real controlled state objects once and checks membership in `global.asteroid_incoming_fragment_site_states`.
Repeated registry values therefore cannot duplicate a bonus, and a non-state/stale registry entry is never entered as a state scope.
The shared predicate's exact six guards are registry membership, fragment_site, mineral_site, state_transaction_applied, NOT main_crater, and actual state_profile equal to the existing fragment_center constant of 50.
Ring-only, unprocessed planned, missing-marker, unregistered, or wrong-profile states grant nothing.
The predicate does not require ownership, cores, an overlord, population, or normal target eligibility.
The current controller owns the benefit even when it is a subject or an occupier.

The main target is accepted by its actual main_crater flag and an existing CONTROLLER.
Its zero population and wasteland category do not invalidate the main benefit.
The main idea is added only when needed and retained on an unchanged actual controller, giving one preserved 1.00 contribution.
The country fragment bonus is overwritten as exact count multiplied by the existing 0.20 constant, with no clamp, six-slot condition, or accumulating old bonus.
An existing owned dynamic modifier is force-updated rather than removed/re-added during positive-to-positive refresh.
Zero count or inactive minerals removes the dynamic modifier and marker and leaves the normal bonus variables at zero.
Normal generation of three through six centers is untouched.

`global.asteroid_incoming_mineral_recipient_countries` stores only current real beneficiaries, once per existing-country pass.
Before rebuilding it, the refresher cleans recorded countries that have ceased to exist.
Living former controllers are included in the normal country pass and lose benefits if they control no qualifying site.
The first-migration alias cleanup also catches an annexed legacy beneficiary before the new ledger has ever been filled.
`global.asteroid_incoming_mineral_refresh_fragment_states` is a transient, typed, unique scratch registry built from valid controlled state objects and cleared at entry/exit.
It supports old state-alias presentation without tying gameplay to six slots.
Country recomputation calls the shared count helper once and separately collects valid controlled states into that existing scratch array.
The count helper itself creates no scratch and adds no world scan.
No new periodic hook or every_possible_country scan is introduced.
Dead-country pointer cleanup uses retained COUNTRY objects, and native post-annex object behavior remains separately unverified.

## Parent integration order and applied source

The parent integrated the runtime wrapper at `028_asteroid_incoming_runtime_effects.txt:1826-1828` as exactly `asteroid_incoming_refresh_uncapped_mineral_control = yes`.
The old six-slot stat assignments are absent from that wrapper.
The appendix imports that actual runtime wrapper and invokes it for all 33 scenarios, instead of invoking the owned entry point directly.
Commit the owned idea-body change together with the new helpers, trigger, modifier, localisation, and reviewed parent integration, because legacy ideas no longer carry fragment stats.

Keep the initial impact refresh after physical footprint processing and final active-minerals selection.
The new processed-site guard prevents a planned fragment from granting armour before its physical receipt is applied.
The parent retained the bounded state-control callback and its final legacy refresh call at runtime line 2004.
The actual on_annex source at lines 38-44 refreshes current controllers first, then clears FROM last and unconditionally inside the active-minerals gate, even if FROM still reports exists=yes.
Gated legacy refresh calls are present in on_release_as_free, on_release_as_puppet, on_liberate, and on_civil_war_end at callback lines 50-71.
The shared monthly host still calls `asteroid_incoming_update_achievements` at line 112.
The actual achievement-country loop now calls the shared count helper at runtime line 1879 and contains no direct weaker state recount or separate public-count reset.
The only source writers of that public variable are the owned count helper and explicit recipient cleanup.
The dynamic armour binding reads the separate overwritten bonus variable, and the count-only achievement helper does not alter that bonus.
No second monthly every_country mineral refresh or new host scan is added.
The parent renamed the existing marker 1 name to `Fragment Crater Material` in the legacy English file at line 274.
Its existing description remains present, and this worker did not edit that file or create duplicate legacy keys.
No GUI, new asset family, or generic router is introduced.
The parent wrote `common/scripted_effects/028_asteroid_incoming_mineral_effects.md` and only the owner index row in the mixed `chaosx_dynamic_effects.md`.
Those parent-owned documents were reviewed read-only and not edited by this worker.

## Armour scope and presentation

The only new modifier field is installed `armor_factor`, categorised army/defensive.
Installed vanilla `common\unit_medals\00_default.txt:2224-2226` provides a concrete land-unit armor_factor precedent.
The installed dynamic-modifier documentation example at `common\dynamic_modifiers\0_dynamic_modifiers.txt:1-28` binds a plain variable name and documents daily versus forced updates.
Its actual SOV national-spirit definition around 1103-1111 binds an army factor to a plain normal variable.
The existing Event 028 country dust modifier follows the same variable-binding structure.
There is no explicit scope override to read the owner, overlord, or original ROOT's bonus variable.
No piercing, hardness, flat armour, aircraft, naval, or equipment modifier is added.
The source model checks the additive stat contribution and zero-base arithmetic but does not prove combat-engine application.

Both the visible compatibility idea and the dynamic modifier reuse `GFX_idea_asteroid_incoming_minerals` from `interface\028_asteroid_incoming.gfx:68-69`.
Its existing `gfx\interface\ideas\028_asteroid_incoming\asteroid_fragment_material.dds` header is 64 by 64.
The new description exposes the normal controlled-site count and fragment armour percentage.
No existing localisation key is duplicated and no art is produced.

## Baseline, tuning, AI, and MCP limits

Stage zero captured the exact physical ideas bytes before any owned stat edit.
Before ideas SHA256: `2C253144B328C0E7A663DAF2FAE30A28A8DD5B157E007F1B493D49467B59261B`, retained byte-for-byte below.
The clean before ideas Git blob was `ec021ac38ee415abe72a83d72aba709f226f27ee` at parent HEAD `e9264c9fef18092103dce3d205209eca49e6f525` when captured.
Before AI trigger file SHA256: `D591180EDE589C319D6077028736EDAFC184DECB86F62E2D48BFEC3F8AF81A4B`.
Existing ratios/constants file SHA256: `E81036C0CFFA3D9830B220AA4BA7E311F14165D40599B990D316F77E470FE157`.
The owned idea bodies contain gameplay armour fields and no AI probability, MTTH, target-selection, or cost tuning edit.
The unchanged actual AI predicate is evaluated against refreshed marker/main identities as a logical truth test, not a probability or balance comparison.
No probability-bearing tuning field was changed, so the parent's stop-and-notify condition for such a field was not triggered.

During the initial implementation pass, five narrow MCP requests were attempted before helper design: idea reference context, add_dynamic_modifier search, old refresh source lookup, Event 028.4 trace, and probability inspection of the ideas file.
All five returned `timed out awaiting tools/call after 600s` with `isError = true`.
No new reference citation, event graph, candidate/adapter report, probability comparison, or artifact URI was returned.
Those are historical initial-pass blockers, not a claim that all routes remain unavailable after the parent resume.
`hoi4.script_validate` is absent from the exposed inventory.
Local installed and offline references were read directly, and this source evidence is not substituted for native or probability acceptance.
No unsupported source field is claimed as engine-tested.

Relevant local sections: installed effects add_dynamic_modifier 1153-1174, remove_dynamic_modifier 5978-5991, force_update_dynamic_modifier 4372-4381, every_controlled_state 3800-3818, for_each_scope_loop 4296-4310, and trigger has_dynamic_modifier 3775-3792.
Installed modifiers_documentation armor_factor 1752-1755 identifies its army/defensive category.
Offline Modifiers lines 108-180 explain plain variable binding, icon visibility, enable/removal triggers, scope binding, and forced updates.
Offline Scopes every_controlled_state at 536 and PREV explanation around 813-823 establishes controller-country attribution.

Captured reference revisions: effects documentation `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF`, modifiers documentation `00A0ECA6D2B3A70CE4B8A0D38997DD609AA0C9349DDCD04C8CAC92849425BE7E`, vanilla dynamic source `34832A23502C23CC02988A0DA899123A4D9891102913901B733C39C789B8469E`, vanilla medals `AC8F6FD131ADE8FBB3752541119D154C0B770BE71B1877F672B3F206E5275325`, offline Modifiers `FE41A26F2B8D3B8E78A9B0DEA9CE1A55F001D1E27886807A0A3FB2D2F535F14F`.

## Actual-source validation

The appendix executes actual owned helper ASTs, including helper calls and scopes, every controlled-state/country iteration, variable arithmetic, idea lifecycle, registry mutation, controller target publication, and dynamic add/remove/update operations.
Unknown commands fail instead of being treated as completed work.
Dynamic modifier enable/remove triggers and the actual armour variable binding are evaluated as source models.
Native cached-stat refresh, dormant-country effect execution, combat, tooltip rendering, and callback timing remain engine evidence pending.
The six idea-body-only edits are validated by reconstructing the exact before AST and comparing all other content, including the full main/dust/preparedness definitions.
The unchanged AI source hash, actual idea predicate truth, new-key uniqueness, and source-only idempotence are checked.
All 33 actual-source scenarios passed, including the 22 combinations of count zero through ten with/without the main and eleven control/lifecycle/invalid-data cases.
The final 2026-10-04 rerun imports the new predicate and executes the shared count helper through the integrated actual runtime wrapper.
Nine additional actual-source callback/count probes passed: two declared annex/control orders, five inactive gated callback paths, the retained inactive state-control zero-cleanup path, and the actual achievement count call against duplicate/unprocessed/wrong-profile/missing-marker/unregistered states.
The appendix asserts the applied clear-FROM-last ordering and exact active gate from the real callback AST.
The callback fixtures have no original-target flag or recovery project/mission and use a fragment change, so unrelated recovery cancellation and main-capture achievement branches are outside execution coverage.
Entering the unmodelled recovery cancellation fails explicitly, rather than accepting an invented effect result.
Every matrix case includes three additional stable refreshes.
The source checks confirm that positive-to-positive repeats retain the same dynamic identity, that main-only and fragment-only contributions do not duplicate, and that scratch state is cleared.
The unknown-command sentinel is rejected by the static evaluator before execution.

| Controlled fragment sites | Fragment armor_factor | With main armor_factor contribution | Source arithmetic on a declared base armour of 100 |
| --- | --- | --- | --- |
| 0 | 0.00 | 1.00 | 200 with main |
| 7 | 1.40 | 2.40 | 240 without main, 340 with main |
| 9 | 1.80 | 2.80 | 280 without main, 380 with main |
| 10 | 2.00 | 3.00 | 300 without main, 400 with main |

These arithmetic results are declared source-model results, not measured division combat statistics.
No new probability analysis, engine stat/render output, or native callback observation is claimed.

Owned source SHA256 values after validation:

| File | SHA256 |
| --- | --- |
| `028_asteroid_incoming_mineral_effects.txt` | `78ABFAD2E724EE1D33BE4B16605033AFFC65CAD749A06CE2262B291E235C5E68` |
| `028_asteroid_incoming_mineral_triggers.txt` | `8441F5EF8692B36FC3B3F62642A1E18E34A1EA895D6F4D402DDAC9E77D3D2688` |
| `028_asteroid_incoming_mineral_dynamic_modifiers.txt` | `D94D7EAFE08D51B65364FA260584ECDEB48E19C1F9F6A8359EF3EEDD8F055DC8` |
| `028_asteroid_incoming_ideas.txt` | `F961B1B38772008D095E6B10EA9C7FB67540E111EC0AB384ED71C04C259EDEA1` |
| `028_asteroid_incoming_mineral_dynamic_modifiers_l_english.yml` | `41D1B3541090CE96912FE2B2D030A32B26AFC61C70B6825FDF36F6F6D08BE722` |

No gameplay simplification or unapproved fallback is introduced.
The bounded source implementation and parent wiring are integrated and ready for the parent's isolated tranche commit.
This does not claim Event 028 completion, native acceptance, or an engine-proven modifier lifecycle.

## Parent resume and callback evidence, 2026-10-04

This follow-up changes only the owned effects TXT, new mineral trigger TXT, and this handoff/appendix.
Runtime, old English, hooks, ideas, modifier definitions, new localisation, and the parent's helper contract/index documents remain untouched by this worker during the follow-up.
The effects header explicitly describes both recorded dead-recipient callers and unconditional annex-FROM cleanup without assuming a native existence transition guarantee.
Final caller runtime SHA256 is `276CBAF89FFCB4071A077DAA6948E787D6BA723FD08D2342332E023F14EB2564`.
Final event-owned callback source SHA256 is `631C0F3A96AAC023F5DD67190A34A103D531647D29A87B490E258765BE97B4CD`, and the shared host source remains `F6DACD9CBB5E49574CD43E48AB63DD3D486B72812018EB2056E47CCB9BAD08B8`.
Earlier wrapper-only runtime identity `7AFCE31FCDAFA6E918E365C04FBEF51EEA9E4ABC7C00B80671B56DE89F3C99B8` and pre-transition callback identity `A3030B946719966CBD7329DEC2786D7F40FFE984E5BF88BA6732CADDBC614CDA` are historical checkpoints, not the final tested caller sources.
The renamed legacy English source SHA256 is `0BB95D686742C33A6951F67AF72D596562E08D75D2B88A51DF5E1D51967E2256`.

The current event-owned on_annex block includes the applied gated refresh followed by unconditional FROM cleanup last.
Its earlier FROM block retains the annexed country's recovery/achievement cleanup.
The on_state_control_changed block enters FROM.FROM for the changed state and invokes `asteroid_incoming_on_state_control_changed`, whose retained final call invokes the integrated legacy mineral wrapper.
The native ROOT remains the new controller during that state-scope entry.
The mineral helper derives actors from actual state control and scoped country iteration, rather than using callback ROOT as every recipient.
The shared monthly source still shows the achievement update at line 112, and the actual runtime achievement writer uses the shared processed-site count helper.
The source model executes both declared annex timing snapshots with FROM.exists=yes, rather than treating existence as an engine ordering fact.
If control has already transferred, refresh awards the actual winner and final FROM cleanup cannot regrant the loser.
If the annex refresh still sees FROM as controller, it can recompute that old snapshot before the final explicit cleanup removes FROM's bonuses.
The winner receives no guessed territory or bonus in that snapshot and is awarded only after the fixture transfers actual control and executes the existing state-control refresh.
The recipient ledger/controller targets can likewise reflect the transitional old-control snapshot until the next actual refresh.
Whether native callback ordering delivers that later refresh after all transfers remains unresolved, with later state-control or country-transition-end refresh intended to reconcile actual control.
No new scan, fallback, branch, or synthetic balance is introduced to cover that native gap.
The source model verifies applied wrapper/callback/count code under declared inputs, not native callback timing or delivery.

Healthy reference context returned no missing or omitted sources at limit twelve.
Its bundle identifies sections but is not treated as having read the detailed scope rules.
Installed reference read citation `d4991c2652842822b5ce7b8bb85f13474953eb23cd99cb86730bac127088afed` read `common\on_actions\_documentation.md:30-49`, revision `876be96cab02a3eaa9a133891bea5f963f8980aa4a794f759c1b30f87d2663c4`.
It lists the diplomacy callback names without specifying all ROOT/FROM bindings.
The underlying installed `common\on_actions\00_on_actions.txt:1615-1617` explicitly states ROOT is the winner and FROM is annexed, and lines 5075-5085 state ROOT is new controller, FROM old controller, and FROM.FROM the state.
That installed source revision is `52A751456F1774AD5001C86D41D4E46494F751D79B6C224B6CD4C0EEBB615EB9`.
Offline reference reads corroborated the scope contracts in `On actions - Hearts of Iron 4 Wiki.md:244-287` and 446-483, revision `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`.
Their citation IDs are `63c5b25db9ca264cff04d287a0eedea6dd50afc24a8dc62c49e140dacab8bb27` and `29a59ae162a696b51d2f1c1acd96319e5728623f991118cc650720ee76789e7e`.
Only the relevant callback rows were needed, so the remaining annex section continuation was not consumed.

Healthy source_lookup confirmed the one actual wrapper definition at runtime lines 1826-1828, with complete=true, skippedSourceCount=0, no override/shadow, references deliberately disabled, and revision `50bfd8987f4aebf69c52f6b126fab4753d5f122c4f0d02e3f29180a21e0bb152`.
It is definition evidence and does not certify all callers.
The Event 028.4 trace returned `EVENT_INSPECTED_PARTIAL`, analysisMode=focused, helpers=0, depth one, eight-node and ten-edge bounds, and helper expansion disabled.
It explicitly deferred whole-workspace helper projections/lifecycle passes and returned an inline inventory limited to 64 of 388 paths.
Its revision is `828ca59a9a1fa1a44d0bf5a12bce75e5cb65e717d2d055388d5ac1994d71fe92`, graphHash `db36826f88e04b62673db3f3908a3ef1dbcc2e27abf44c1047338abd9c5ad351`.
Returned trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0355dce0eef2ec1605c068d0661d484174aff0d63f2ec874d225b6f20e55e9d4/a567328e9c3faa68b08f186e7e6304287e3d5dfb25797bba8e5136044de9b7d8/event-trace-828ca59a9a1f.json`.
A bounded resource read at offset zero, length 12288 failed with exact error `Mcp error: -32603: Artifact provenance manifest is unavailable`.
No complete artifact retrieval, source inventory coverage, helper lifecycle validation, native armour/stat acceptance, or probability comparison is claimed from that trace.

Fresh healthy idea-reference context also returned no missing or omitted sources.
Installed `modifiers_documentation.md:1752-1756` was read through citation `5274fa8bc11dd7b23f0c0416bfd36b28489164fda49d6a043104238a2f97601f`, revision `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e`, identifying armor_factor as army/defensive.
The introduction at lines 1-8 was separately read through citation `3b0913c29e4c72d37f3ae14618299e26d3e632e328ae3ebe34afe82b15504b59` at the same revision.
It cautions that recognized modifiers are not necessarily used and that documented decimal places describe display, so those entries do not establish zero-base division arithmetic or exclusive land-only application in native combat.
The offline dynamic-addition section at `Modifiers - Hearts of Iron 4 Wiki.md:149-181` was read through citation `c70dc2f900c7a24176cc5d6e243831c57a47919ba98bebd34a92a01ff57c05c5`, revision `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f`.
It confirms attachment-scope variable binding when no override is supplied and explains that variable-backed bonuses are absent from the add-effect tooltip even when the applied modifier works.
Healthy source lookup returned one unshadowed main-material idea definition at lines 239-247 with its static 1.00 factor, complete=true and skippedSourceCount=0, revision `84691547e1efd4265b3dfe44b17dd2551179ab9e4ab2a3e5353a6bcaf3a355c0`.
The new dynamic modifier's kind-filtered lookup and unfiltered retry returned zero indexed definitions despite its verified physical source file.
The unfiltered result was complete=true, skippedSourceCount=0, revision `6aab7b8c64eea657685bbc8489cedc27be8d49da126e5d8616eaf33d19b6bcc1`.
This is a narrow index/source-coverage gap, not proof that the engine rejected the definition or proof of native armor_factor support for that modifier.
The direct installed dynamic-variable example, actual vanilla army-factor precedent, owned AST execution, and physical source hash are retained separately from that unresolved lookup coverage.

Final boundary: after the final 33 plus 9 actual-source rerun, the worker freezes owned sources and this handoff until the parent commit.
The parent retains final integration, acceptance, and commit ownership.

## Reproducible actual-source appendix

Parent isolated-tranche review: the proposed committed runtime wrapper and complete achievement-update AST match the actual bodies used by the 33 plus 9 source-model cases exactly.
Only those two mineral/count bodies are selected from the mixed runtime file, together with the one marker label and one owner-documentation index row from their mixed files.
The captured whole-runtime and legacy-English hashes above describe the tested working-tree snapshot, which also contains pending physical-receipt and other presentation work; they are not claims about the complete blob in the isolated mineral commit.
The source model executes the mineral/count/callback bodies and does not execute or certify those excluded physical changes.
The other agents' staged or unstaged work is preserved by the shared-tree commit workflow.

```powershell
python -c "from pathlib import Path; p=Path('docs/plans/028_asteroid_incoming_plans/subagent_handoffs/mineral_uncapped_20261003.md'); t=p.read_text(encoding='utf-8'); exec(t.rsplit('<!-- mineral-source-model -->',1)[1].split(chr(96)*3+'python')[1].split(chr(96)*3)[0])"
```

<!-- mineral-source-model -->
```python
from pathlib import Path
import base64
import copy
from decimal import Decimal as D
import hashlib
import json
import re
import runpy

root = Path.cwd()
parse = runpy.run_path(str(root / '.tools/validation/validate_028_availability.py'))['parse_source']
before_ideas_bytes = base64.b64decode('IyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiMgQ0hBT1MgUkVEVVggLSBFVkVOVCAwMjggQVNURVJPSUQgSU5DT01JTkcgSURFQVMKIyA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09CiMgQ291bnRyeSBpZGVhcyBmb3IgdGhlIGJvdW5kZWQgRXZlbnQgMDI4IGxpZmVjeWNsZS4gVGhlIGltcGFjdCBzdGFnZSBpZGVhcwojIGFyZSByZXBsYWNlZCBhcyB0aGUgZ2xvYmFsIER1c3QgTG9hZCBjaGFuZ2VzOyBwcm90ZWN0aW9uIGlkZWFzIHJlcGxhY2Ugb25lCiMgYW5vdGhlciBhbmQgZW5kIHdoZW4gdGhlIGR1c3QgbGVkZ2VyIHJlYWNoZXMgemVyby4gUHJlcGFyZWRuZXNzIGlkZWFzIGFyZQojIHNob3J0LWxpdmVkIHByZS1pbXBhY3QgY29tbWl0bWVudHMsIHdoaWxlIHRoZSBwb3N0LWltcGFjdCBkaXNsb2NhdGlvbiBhbmQKIyByZWNvdmVyeSBpZGVhcyBhcmUgdGltZWQgYnkgdGhlIGV2ZW50LW93bmVkIGVmZmVjdHMuCiMKIyBJZGVhIG1vZGlmaWVyIGZpZWxkcyBkbyBub3QgYWNjZXB0IHRoZSBzaGFyZWQgc2NyaXB0LWNvbnN0YW50IG5hbWVzcGFjZSBpbgojIHRoaXMgZ2FtZSB2ZXJzaW9uLiBUaGVzZSBmaWxlLXNjb3BlZCB2YWx1ZXMgdGhlcmVmb3JlIG1pcnJvciB0aGUgYWNjZXB0ZWQKIyBFdmVudCAwMjggdHVuaW5nIG1hdHJpeCBhbmQga2VlcCBldmVyeSByZXBlYXRlZCBpZGVhIHZhbHVlIGNlbnRyYWxpemVkIGluCiMgdGhpcyBmaWxlLgojID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0KCkBBU1RFUk9JRF9QUkVQQVJFRF9DT01NQU5EX1NUQUJJTElUWSA9IDAuMDMKQEFTVEVST0lEX1BSRVBBUkVEX0NPTU1BTkRfUE9XRVIgPSAwLjA1CkBBU1RFUk9JRF9QUkVQQVJFRF9DT01NQU5EX09SRyA9IDAuMDMKQEFTVEVST0lEX1BSRVBBUkVEX1RSQU5TUE9SVF9TVVBQTFkgPSAtMC4wMwpAQVNURVJPSURfUFJFUEFSRURfVFJBTlNQT1JUX1NQRUVEID0gLTAuMDIKQEFTVEVST0lEX1BSRVBBUkVEX01FRElDQUxfU1RBQklMSVRZID0gMC4wMgpAQVNURVJPSURfUFJFUEFSRURfTUVESUNBTF9TVVBQTFkgPSAtMC4wMgoKQEFTVEVST0lEX0RJU0xPQ0FUSU9OX1NUQUJJTElUWSA9IC0wLjA1CkBBU1RFUk9JRF9ESVNMT0NBVElPTl9QT0xJVElDQUxfUE9XRVIgPSAtMC4xMApAQVNURVJPSURfRElTTE9DQVRJT05fQ09OU1RSVUNUSU9OID0gLTAuMDUKQEFTVEVST0lEX0RJU0xPQ0FUSU9OX09SRyA9IC0wLjAzCkBBU1RFUk9JRF9ESVNMT0NBVElPTl9QUkVQQVJFRF9TVEFCSUxJVFkgPSAtMC4wMgpAQVNURVJPSURfRElTTE9DQVRJT05fUFJFUEFSRURfUE9MSVRJQ0FMX1BPV0VSID0gLTAuMDQKQEFTVEVST0lEX0RJU0xPQ0FUSU9OX1BSRVBBUkVEX0NPTlNUUlVDVElPTiA9IC0wLjAyCkBBU1RFUk9JRF9ESVNMT0NBVElPTl9QUkVQQVJFRF9PUkcgPSAtMC4wMQoKQEFTVEVST0lEX0RVU1RfUkVTSURVQUxfRkFDVE9SWSA9IC0wLjAzCkBBU1RFUk9JRF9EVVNUX1JFU0lEVUFMX0NPTlNUUlVDVElPTiA9IC0wLjAyCkBBU1RFUk9JRF9EVVNUX1JFU0lEVUFMX0VGRklDSUVOQ1kgPSAwLjAwCkBBU1RFUk9JRF9EVVNUX1JFU0lEVUFMX1NVUFBMWSA9IDAuMDIKQEFTVEVST0lEX0RVU1RfUkVTSURVQUxfQUlSID0gLTAuMDEKQEFTVEVST0lEX0RVU1RfVkVJTF9GQUNUT1JZID0gLTAuMDcKQEFTVEVST0lEX0RVU1RfVkVJTF9DT05TVFJVQ1RJT04gPSAtMC4wNQpAQVNURVJPSURfRFVTVF9WRUlMX0VGRklDSUVOQ1kgPSAtMC4wMwpAQVNURVJPSURfRFVTVF9WRUlMX1NVUFBMWSA9IDAuMDUKQEFTVEVST0lEX0RVU1RfVkVJTF9BSVIgPSAtMC4wMwpAQVNURVJPSURfRFVTVF9XSU5URVJfRkFDVE9SWSA9IC0wLjEyCkBBU1RFUk9JRF9EVVNUX1dJTlRFUl9DT05TVFJVQ1RJT04gPSAtMC4xMApAQVNURVJPSURfRFVTVF9XSU5URVJfRUZGSUNJRU5DWSA9IC0wLjA4CkBBU1RFUk9JRF9EVVNUX1dJTlRFUl9TVVBQTFkgPSAwLjEwCkBBU1RFUk9JRF9EVVNUX1dJTlRFUl9BSVIgPSAtMC4wNQpAQVNURVJPSURfRFVTVF9TRVZFUkVfRkFDVE9SWSA9IC0wLjIwCkBBU1RFUk9JRF9EVVNUX1NFVkVSRV9DT05TVFJVQ1RJT04gPSAtMC4xNQpAQVNURVJPSURfRFVTVF9TRVZFUkVfRUZGSUNJRU5DWSA9IC0wLjEyCkBBU1RFUk9JRF9EVVNUX1NFVkVSRV9TVVBQTFkgPSAwLjE1CkBBU1RFUk9JRF9EVVNUX1NFVkVSRV9BSVIgPSAtMC4xMAoKQEFTVEVST0lEX1JFQ09WRVJZX0JVUkRFTl9GQUNUT1JZID0gLTAuMDUKQEFTVEVST0lEX1JFQ09WRVJZX0JVUkRFTl9TVVBQTFkgPSAwLjA1CkBBU1RFUk9JRF9SRUNPVkVSWV9CVVJERU5fQ09OU1VNRVJfR09PRFMgPSAwLjA1CkBBU1RFUk9JRF9SRUNPVkVSWV9CVVJERU5fU1RBQklMSVRZID0gLTAuMDIKQEFTVEVST0lEX1JFQ09WRVJZX0xFR0FDWV9SRVBBSVIgPSAwLjA1CkBBU1RFUk9JRF9SRUNPVkVSWV9MRUdBQ1lfQ09OU1RSVUNUSU9OID0gMC4wMwpAQVNURVJPSURfUkVDT1ZFUllfTEVHQUNZX1NUQUJJTElUWSA9IDAuMDIKCkBBU1RFUk9JRF9EVVNUX1JFU0lEVUFMX1dFQVRIRVIgPSAwLjAwCkBBU1RFUk9JRF9EVVNUX1ZFSUxfV0VBVEhFUiA9IDAuMDMKQEFTVEVST0lEX0RVU1RfV0lOVEVSX1dFQVRIRVIgPSAwLjA1CkBBU1RFUk9JRF9EVVNUX1NFVkVSRV9XRUFUSEVSID0gMC4xMApAQVNURVJPSURfTUFJTl9DUkFURVJfQVJNT1VSID0gMS4wMApAQVNURVJPSURfRlJBR01FTlRfU0lURV9BUk1PVVIgPSAwLjIwCgppZGVhcyA9IHsKCWNvdW50cnkgPSB7CgkJYXN0ZXJvaWRfaW5jb21pbmdfY29tbWFuZF9jb250aW51aXR5ID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfcHJlcGFyZWRuZXNzCgkJCWFsbG93ZWQgPSB7IGFsd2F5cyA9IHllcyB9CgkJCWFsbG93ZWRfY2l2aWxfd2FyID0geyBhbHdheXMgPSB5ZXMgfQoJCQlyZW1vdmFsX2Nvc3QgPSAtMQoJCQltb2RpZmllciA9IHsKCQkJCXN0YWJpbGl0eV9mYWN0b3IgPSBAQVNURVJPSURfUFJFUEFSRURfQ09NTUFORF9TVEFCSUxJVFkKCQkJCXBvbGl0aWNhbF9wb3dlcl9nYWluID0gQEFTVEVST0lEX1BSRVBBUkVEX0NPTU1BTkRfUE9XRVIKCQkJCWFybXlfb3JnX2ZhY3RvciA9IEBBU1RFUk9JRF9QUkVQQVJFRF9DT01NQU5EX09SRwoJCQl9CgkJfQoKCQlhc3Rlcm9pZF9pbmNvbWluZ190cmFuc3BvcnRfZGlzcGVyc2lvbiA9IHsKCQkJcGljdHVyZSA9IEdGWF9pZGVhX2FzdGVyb2lkX2luY29taW5nX3ByZXBhcmVkbmVzcwoJCQlhbGxvd2VkID0geyBhbHdheXMgPSB5ZXMgfQoJCQlhbGxvd2VkX2NpdmlsX3dhciA9IHsgYWx3YXlzID0geWVzIH0KCQkJcmVtb3ZhbF9jb3N0ID0gLTEKCQkJbW9kaWZpZXIgPSB7CgkJCQlzdXBwbHlfY29uc3VtcHRpb25fZmFjdG9yID0gQEFTVEVST0lEX1BSRVBBUkVEX1RSQU5TUE9SVF9TVVBQTFkKCQkJCWFybXlfc3BlZWRfZmFjdG9yID0gQEFTVEVST0lEX1BSRVBBUkVEX1RSQU5TUE9SVF9TUEVFRAoJCQl9CgkJfQoKCQlhc3Rlcm9pZF9pbmNvbWluZ19tZWRpY2FsX21vYmlsaXphdGlvbiA9IHsKCQkJcGljdHVyZSA9IEdGWF9pZGVhX2FzdGVyb2lkX2luY29taW5nX3ByZXBhcmVkbmVzcwoJCQlhbGxvd2VkID0geyBhbHdheXMgPSB5ZXMgfQoJCQlhbGxvd2VkX2NpdmlsX3dhciA9IHsgYWx3YXlzID0geWVzIH0KCQkJcmVtb3ZhbF9jb3N0ID0gLTEKCQkJbW9kaWZpZXIgPSB7CgkJCQlzdGFiaWxpdHlfZmFjdG9yID0gQEFTVEVST0lEX1BSRVBBUkVEX01FRElDQUxfU1RBQklMSVRZCgkJCQlzdXBwbHlfY29uc3VtcHRpb25fZmFjdG9yID0gQEFTVEVST0lEX1BSRVBBUkVEX01FRElDQUxfU1VQUExZCgkJCX0KCQl9CgoJCWFzdGVyb2lkX2luY29taW5nX2dvdmVybm1lbnRfZGlzbG9jYXRpb24gPSB7CgkJCXBpY3R1cmUgPSBHRlhfaWRlYV9hc3Rlcm9pZF9pbmNvbWluZ19yZWNvdmVyeV9idXJkZW4KCQkJYWxsb3dlZCA9IHsgYWx3YXlzID0geWVzIH0KCQkJYWxsb3dlZF9jaXZpbF93YXIgPSB7IGFsd2F5cyA9IHllcyB9CgkJCXJlbW92YWxfY29zdCA9IC0xCgkJCW1vZGlmaWVyID0gewoJCQkJc3RhYmlsaXR5X2ZhY3RvciA9IEBBU1RFUk9JRF9ESVNMT0NBVElPTl9TVEFCSUxJVFkKCQkJCXBvbGl0aWNhbF9wb3dlcl9nYWluID0gQEFTVEVST0lEX0RJU0xPQ0FUSU9OX1BPTElUSUNBTF9QT1dFUgoJCQkJcHJvZHVjdGlvbl9zcGVlZF9idWlsZGluZ3NfZmFjdG9yID0gQEFTVEVST0lEX0RJU0xPQ0FUSU9OX0NPTlNUUlVDVElPTgoJCQkJYXJteV9vcmdfZmFjdG9yID0gQEFTVEVST0lEX0RJU0xPQ0FUSU9OX09SRwoJCQl9CgkJfQoKCQlhc3Rlcm9pZF9pbmNvbWluZ19nb3Zlcm5tZW50X2Rpc2xvY2F0aW9uX3ByZXBhcmVkID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfcHJlcGFyZWRuZXNzCgkJCWFsbG93ZWQgPSB7IGFsd2F5cyA9IHllcyB9CgkJCWFsbG93ZWRfY2l2aWxfd2FyID0geyBhbHdheXMgPSB5ZXMgfQoJCQlyZW1vdmFsX2Nvc3QgPSAtMQoJCQltb2RpZmllciA9IHsKCQkJCXN0YWJpbGl0eV9mYWN0b3IgPSBAQVNURVJPSURfRElTTE9DQVRJT05fUFJFUEFSRURfU1RBQklMSVRZCgkJCQlwb2xpdGljYWxfcG93ZXJfZ2FpbiA9IEBBU1RFUk9JRF9ESVNMT0NBVElPTl9QUkVQQVJFRF9QT0xJVElDQUxfUE9XRVIKCQkJCXByb2R1Y3Rpb25fc3BlZWRfYnVpbGRpbmdzX2ZhY3RvciA9IEBBU1RFUk9JRF9ESVNMT0NBVElPTl9QUkVQQVJFRF9DT05TVFJVQ1RJT04KCQkJCWFybXlfb3JnX2ZhY3RvciA9IEBBU1RFUk9JRF9ESVNMT0NBVElPTl9QUkVQQVJFRF9PUkcKCQkJfQoJCX0KCgkJYXN0ZXJvaWRfaW5jb21pbmdfcmVzaWR1YWxfaGF6ZSA9IHsKCQkJcGljdHVyZSA9IEdGWF9pZGVhX2FzdGVyb2lkX2luY29taW5nX3Jlc2lkdWFsX2hhemUKCQkJYWxsb3dlZCA9IHsgYWx3YXlzID0geWVzIH0KCQkJYWxsb3dlZF9jaXZpbF93YXIgPSB7IGFsd2F5cyA9IHllcyB9CgkJCXJlbW92YWxfY29zdCA9IC0xCgkJCW1vZGlmaWVyID0gewoJCQkJaW5kdXN0cmlhbF9jYXBhY2l0eV9mYWN0b3J5ID0gQEFTVEVST0lEX0RVU1RfUkVTSURVQUxfRkFDVE9SWQoJCQkJcHJvZHVjdGlvbl9zcGVlZF9idWlsZGluZ3NfZmFjdG9yID0gQEFTVEVST0lEX0RVU1RfUkVTSURVQUxfQ09OU1RSVUNUSU9OCgkJCQlwcm9kdWN0aW9uX2ZhY3RvcnlfZWZmaWNpZW5jeV9nYWluX2ZhY3RvciA9IEBBU1RFUk9JRF9EVVNUX1JFU0lEVUFMX0VGRklDSUVOQ1kKCQkJCXN1cHBseV9jb25zdW1wdGlvbl9mYWN0b3IgPSBAQVNURVJPSURfRFVTVF9SRVNJRFVBTF9TVVBQTFkKCQkJCWFpcl9taXNzaW9uX2VmZmljaWVuY3kgPSBAQVNURVJPSURfRFVTVF9SRVNJRFVBTF9BSVIKCQkJCWFpcl93ZWF0aGVyX3BlbmFsdHkgPSBAQVNURVJPSURfRFVTVF9SRVNJRFVBTF9XRUFUSEVSCgkJCX0KCQl9CgoJCWFzdGVyb2lkX2luY29taW5nX2dsb2JhbF9kdXN0X3ZlaWwgPSB7CgkJCXBpY3R1cmUgPSBHRlhfaWRlYV9hc3Rlcm9pZF9pbmNvbWluZ19nbG9iYWxfZHVzdF92ZWlsCgkJCWFsbG93ZWQgPSB7IGFsd2F5cyA9IHllcyB9CgkJCWFsbG93ZWRfY2l2aWxfd2FyID0geyBhbHdheXMgPSB5ZXMgfQoJCQlyZW1vdmFsX2Nvc3QgPSAtMQoJCQltb2RpZmllciA9IHsKCQkJCWluZHVzdHJpYWxfY2FwYWNpdHlfZmFjdG9yeSA9IEBBU1RFUk9JRF9EVVNUX1ZFSUxfRkFDVE9SWQoJCQkJcHJvZHVjdGlvbl9zcGVlZF9idWlsZGluZ3NfZmFjdG9yID0gQEFTVEVST0lEX0RVU1RfVkVJTF9DT05TVFJVQ1RJT04KCQkJCXByb2R1Y3Rpb25fZmFjdG9yeV9lZmZpY2llbmN5X2dhaW5fZmFjdG9yID0gQEFTVEVST0lEX0RVU1RfVkVJTF9FRkZJQ0lFTkNZCgkJCQlzdXBwbHlfY29uc3VtcHRpb25fZmFjdG9yID0gQEFTVEVST0lEX0RVU1RfVkVJTF9TVVBQTFkKCQkJCWFpcl9taXNzaW9uX2VmZmljaWVuY3kgPSBAQVNURVJPSURfRFVTVF9WRUlMX0FJUgoJCQkJYWlyX3dlYXRoZXJfcGVuYWx0eSA9IEBBU1RFUk9JRF9EVVNUX1ZFSUxfV0VBVEhFUgoJCQl9CgkJfQoKCQlhc3Rlcm9pZF9pbmNvbWluZ19pbXBhY3Rfd2ludGVyID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfaW1wYWN0X3dpbnRlcgoJCQlhbGxvd2VkID0geyBhbHdheXMgPSB5ZXMgfQoJCQlhbGxvd2VkX2NpdmlsX3dhciA9IHsgYWx3YXlzID0geWVzIH0KCQkJcmVtb3ZhbF9jb3N0ID0gLTEKCQkJbW9kaWZpZXIgPSB7CgkJCQlpbmR1c3RyaWFsX2NhcGFjaXR5X2ZhY3RvcnkgPSBAQVNURVJPSURfRFVTVF9XSU5URVJfRkFDVE9SWQoJCQkJcHJvZHVjdGlvbl9zcGVlZF9idWlsZGluZ3NfZmFjdG9yID0gQEFTVEVST0lEX0RVU1RfV0lOVEVSX0NPTlNUUlVDVElPTgoJCQkJcHJvZHVjdGlvbl9mYWN0b3J5X2VmZmljaWVuY3lfZ2Fpbl9mYWN0b3IgPSBAQVNURVJPSURfRFVTVF9XSU5URVJfRUZGSUNJRU5DWQoJCQkJc3VwcGx5X2NvbnN1bXB0aW9uX2ZhY3RvciA9IEBBU1RFUk9JRF9EVVNUX1dJTlRFUl9TVVBQTFkKCQkJCWFpcl9taXNzaW9uX2VmZmljaWVuY3kgPSBAQVNURVJPSURfRFVTVF9XSU5URVJfQUlSCgkJCQlhaXJfd2VhdGhlcl9wZW5hbHR5ID0gQEFTVEVST0lEX0RVU1RfV0lOVEVSX1dFQVRIRVIKCQkJfQoJCX0KCgkJYXN0ZXJvaWRfaW5jb21pbmdfc2V2ZXJlX2ltcGFjdF93aW50ZXIgPSB7CgkJCXBpY3R1cmUgPSBHRlhfaWRlYV9hc3Rlcm9pZF9pbmNvbWluZ19zZXZlcmVfaW1wYWN0X3dpbnRlcgoJCQlhbGxvd2VkID0geyBhbHdheXMgPSB5ZXMgfQoJCQlhbGxvd2VkX2NpdmlsX3dhciA9IHsgYWx3YXlzID0geWVzIH0KCQkJcmVtb3ZhbF9jb3N0ID0gLTEKCQkJbW9kaWZpZXIgPSB7CgkJCQlpbmR1c3RyaWFsX2NhcGFjaXR5X2ZhY3RvcnkgPSBAQVNURVJPSURfRFVTVF9TRVZFUkVfRkFDVE9SWQoJCQkJcHJvZHVjdGlvbl9zcGVlZF9idWlsZGluZ3NfZmFjdG9yID0gQEFTVEVST0lEX0RVU1RfU0VWRVJFX0NPTlNUUlVDVElPTgoJCQkJcHJvZHVjdGlvbl9mYWN0b3J5X2VmZmljaWVuY3lfZ2Fpbl9mYWN0b3IgPSBAQVNURVJPSURfRFVTVF9TRVZFUkVfRUZGSUNJRU5DWQoJCQkJc3VwcGx5X2NvbnN1bXB0aW9uX2ZhY3RvciA9IEBBU1RFUk9JRF9EVVNUX1NFVkVSRV9TVVBQTFkKCQkJCWFpcl9taXNzaW9uX2VmZmljaWVuY3kgPSBAQVNURVJPSURfRFVTVF9TRVZFUkVfQUlSCgkJCQlhaXJfd2VhdGhlcl9wZW5hbHR5ID0gQEFTVEVST0lEX0RVU1RfU0VWRVJFX1dFQVRIRVIKCQkJfQoJCX0KCgkJYXN0ZXJvaWRfaW5jb21pbmdfcmVjb3ZlcnlfYnVyZGVuID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfcmVjb3ZlcnlfYnVyZGVuCgkJCWFsbG93ZWQgPSB7IGFsd2F5cyA9IHllcyB9CgkJCWFsbG93ZWRfY2l2aWxfd2FyID0geyBhbHdheXMgPSB5ZXMgfQoJCQlyZW1vdmFsX2Nvc3QgPSAtMQoJCQltb2RpZmllciA9IHsKCQkJCWluZHVzdHJpYWxfY2FwYWNpdHlfZmFjdG9yeSA9IEBBU1RFUk9JRF9SRUNPVkVSWV9CVVJERU5fRkFDVE9SWQoJCQkJc3VwcGx5X2NvbnN1bXB0aW9uX2ZhY3RvciA9IEBBU1RFUk9JRF9SRUNPVkVSWV9CVVJERU5fU1VQUExZCgkJCQljb25zdW1lcl9nb29kc19mYWN0b3IgPSBAQVNURVJPSURfUkVDT1ZFUllfQlVSREVOX0NPTlNVTUVSX0dPT0RTCgkJCQlzdGFiaWxpdHlfZmFjdG9yID0gQEFTVEVST0lEX1JFQ09WRVJZX0JVUkRFTl9TVEFCSUxJVFkKCQkJfQoJCX0KCgkJYXN0ZXJvaWRfaW5jb21pbmdfcmVjb3ZlcnlfbGVnYWN5ID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfcmVjb3ZlcnlfYnVyZGVuCgkJCWFsbG93ZWQgPSB7IGFsd2F5cyA9IHllcyB9CgkJCWFsbG93ZWRfY2l2aWxfd2FyID0geyBhbHdheXMgPSB5ZXMgfQoJCQlyZW1vdmFsX2Nvc3QgPSAtMQoJCQltb2RpZmllciA9IHsKCQkJCXJlcGFpcl9zcGVlZF9mYWN0b3IgPSBAQVNURVJPSURfUkVDT1ZFUllfTEVHQUNZX1JFUEFJUgoJCQkJcHJvZHVjdGlvbl9zcGVlZF9idWlsZGluZ3NfZmFjdG9yID0gQEFTVEVST0lEX1JFQ09WRVJZX0xFR0FDWV9DT05TVFJVQ1RJT04KCQkJCXN0YWJpbGl0eV9mYWN0b3IgPSBAQVNURVJPSURfUkVDT1ZFUllfTEVHQUNZX1NUQUJJTElUWQoJCQl9CgkJfQoKCQlhc3Rlcm9pZF9pbmNvbWluZ19kdXN0X3Byb3RlY3Rpb25fYmFzaWMgPSB7CgkJCXBpY3R1cmUgPSBHRlhfaWRlYV9hc3Rlcm9pZF9pbmNvbWluZ19kdXN0X3Byb3RlY3Rpb24KCQkJYWxsb3dlZCA9IHsgYWx3YXlzID0geWVzIH0KCQkJYWxsb3dlZF9jaXZpbF93YXIgPSB7IGFsd2F5cyA9IHllcyB9CgkJCXJlbW92YWxfY29zdCA9IC0xCgkJCSMgU3RhZ2Utc2NhbGVkIGNvbXBlbnNhdGlvbiBiZWxvbmdzIHRvIHRoZSBoaWRkZW4gY291bnRyeSBkeW5hbWljCgkJCSMgbW9kaWZpZXIuIFRoaXMgaWRlYSBpcyB0aGUgdmlzaWJsZSBwcm90ZWN0aW9uLWxldmVsIGlkZW50aXR5LgoJCX0KCgkJYXN0ZXJvaWRfaW5jb21pbmdfZHVzdF9wcm90ZWN0aW9uX29yZ2FuaXplZCA9IHsKCQkJcGljdHVyZSA9IEdGWF9pZGVhX2FzdGVyb2lkX2luY29taW5nX2R1c3RfcHJvdGVjdGlvbgoJCQlhbGxvd2VkID0geyBhbHdheXMgPSB5ZXMgfQoJCQlhbGxvd2VkX2NpdmlsX3dhciA9IHsgYWx3YXlzID0geWVzIH0KCQkJcmVtb3ZhbF9jb3N0ID0gLTEKCQl9CgoJCWFzdGVyb2lkX2luY29taW5nX2R1c3RfcHJvdGVjdGlvbl9oYXJkZW5lZCA9IHsKCQkJcGljdHVyZSA9IEdGWF9pZGVhX2FzdGVyb2lkX2luY29taW5nX2R1c3RfcHJvdGVjdGlvbgoJCQlhbGxvd2VkID0geyBhbHdheXMgPSB5ZXMgfQoJCQlhbGxvd2VkX2NpdmlsX3dhciA9IHsgYWx3YXlzID0geWVzIH0KCQkJcmVtb3ZhbF9jb3N0ID0gLTEKCQl9CgoJCWFzdGVyb2lkX2luY29taW5nX21haW5fY3JhdGVyX21hdGVyaWFsID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfbWFpbl9jcmF0ZXJfbWF0ZXJpYWwKCQkJYWxsb3dlZCA9IHsgYWx3YXlzID0geWVzIH0KCQkJYWxsb3dlZF9jaXZpbF93YXIgPSB7IGFsd2F5cyA9IHllcyB9CgkJCXJlbW92YWxfY29zdCA9IC0xCgkJCW1vZGlmaWVyID0gewoJCQkJYXJtb3JfZmFjdG9yID0gQEFTVEVST0lEX01BSU5fQ1JBVEVSX0FSTU9VUgoJCQl9CgkJfQoKCQlhc3Rlcm9pZF9pbmNvbWluZ19mcmFnbWVudF9tYXRlcmlhbF8xID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfbWluZXJhbHMKCQkJYWxsb3dlZCA9IHsgYWx3YXlzID0geWVzIH0KCQkJYWxsb3dlZF9jaXZpbF93YXIgPSB7IGFsd2F5cyA9IHllcyB9CgkJCXJlbW92YWxfY29zdCA9IC0xCgkJCW1vZGlmaWVyID0geyBhcm1vcl9mYWN0b3IgPSBAQVNURVJPSURfRlJBR01FTlRfU0lURV9BUk1PVVIgfQoJCX0KCQlhc3Rlcm9pZF9pbmNvbWluZ19mcmFnbWVudF9tYXRlcmlhbF8yID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfbWluZXJhbHMKCQkJYWxsb3dlZCA9IHsgYWx3YXlzID0geWVzIH0KCQkJYWxsb3dlZF9jaXZpbF93YXIgPSB7IGFsd2F5cyA9IHllcyB9CgkJCXJlbW92YWxfY29zdCA9IC0xCgkJCW1vZGlmaWVyID0geyBhcm1vcl9mYWN0b3IgPSBAQVNURVJPSURfRlJBR01FTlRfU0lURV9BUk1PVVIgfQoJCX0KCQlhc3Rlcm9pZF9pbmNvbWluZ19mcmFnbWVudF9tYXRlcmlhbF8zID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfbWluZXJhbHMKCQkJYWxsb3dlZCA9IHsgYWx3YXlzID0geWVzIH0KCQkJYWxsb3dlZF9jaXZpbF93YXIgPSB7IGFsd2F5cyA9IHllcyB9CgkJCXJlbW92YWxfY29zdCA9IC0xCgkJCW1vZGlmaWVyID0geyBhcm1vcl9mYWN0b3IgPSBAQVNURVJPSURfRlJBR01FTlRfU0lURV9BUk1PVVIgfQoJCX0KCQlhc3Rlcm9pZF9pbmNvbWluZ19mcmFnbWVudF9tYXRlcmlhbF80ID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfbWluZXJhbHMKCQkJYWxsb3dlZCA9IHsgYWx3YXlzID0geWVzIH0KCQkJYWxsb3dlZF9jaXZpbF93YXIgPSB7IGFsd2F5cyA9IHllcyB9CgkJCXJlbW92YWxfY29zdCA9IC0xCgkJCW1vZGlmaWVyID0geyBhcm1vcl9mYWN0b3IgPSBAQVNURVJPSURfRlJBR01FTlRfU0lURV9BUk1PVVIgfQoJCX0KCQlhc3Rlcm9pZF9pbmNvbWluZ19mcmFnbWVudF9tYXRlcmlhbF81ID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfbWluZXJhbHMKCQkJYWxsb3dlZCA9IHsgYWx3YXlzID0geWVzIH0KCQkJYWxsb3dlZF9jaXZpbF93YXIgPSB7IGFsd2F5cyA9IHllcyB9CgkJCXJlbW92YWxfY29zdCA9IC0xCgkJCW1vZGlmaWVyID0geyBhcm1vcl9mYWN0b3IgPSBAQVNURVJPSURfRlJBR01FTlRfU0lURV9BUk1PVVIgfQoJCX0KCQlhc3Rlcm9pZF9pbmNvbWluZ19mcmFnbWVudF9tYXRlcmlhbF82ID0gewoJCQlwaWN0dXJlID0gR0ZYX2lkZWFfYXN0ZXJvaWRfaW5jb21pbmdfbWluZXJhbHMKCQkJYWxsb3dlZCA9IHsgYWx3YXlzID0geWVzIH0KCQkJYWxsb3dlZF9jaXZpbF93YXIgPSB7IGFsd2F5cyA9IHllcyB9CgkJCXJlbW92YWxfY29zdCA9IC0xCgkJCW1vZGlmaWVyID0geyBhcm1vcl9mYWN0b3IgPSBAQVNURVJPSURfRlJBR01FTlRfU0lURV9BUk1PVVIgfQoJCX0KCX0KfQo=')
assert hashlib.sha256(before_ideas_bytes).hexdigest().upper() == '2C253144B328C0E7A663DAF2FAE30A28A8DD5B157E007F1B493D49467B59261B'
class BeforeIdeas:
    def read_text(self, encoding): return before_ideas_bytes.decode(encoding)
before_ideas = parse(BeforeIdeas())
ideas = parse(root / 'common/ideas/028_asteroid_incoming_ideas.txt')
defs = parse(root / 'common/scripted_effects/028_asteroid_incoming_mineral_effects.txt')
runtime_path = root / 'common/scripted_effects/028_asteroid_incoming_runtime_effects.txt'
runtime = parse(runtime_path)
WRAPPER = 'asteroid_incoming_refresh_mineral_control'
assert runtime[WRAPPER] == [('asteroid_incoming_refresh_uncapped_mineral_control', '=', 'yes')], 'parent wrapper differs from the accepted entry point'
defs[WRAPPER] = runtime[WRAPPER]
CONTROL_HELPER = 'asteroid_incoming_on_state_control_changed'
defs[CONTROL_HELPER] = runtime[CONTROL_HELPER]
dmods = parse(root / 'common/dynamic_modifiers/028_asteroid_incoming_mineral_dynamic_modifiers.txt')
constants = parse(root / 'common/script_constants/028_asteroid_incoming_constants.txt')
trigger_path = root / 'common/scripted_triggers/028_asteroid_incoming_triggers.txt'
triggers = parse(trigger_path)
achievement_trigger_path = root / 'common/scripted_triggers/028_asteroid_incoming_achievement_triggers.txt'
triggers.update(parse(achievement_trigger_path))
mineral_trigger_path = root / 'common/scripted_triggers/028_asteroid_incoming_mineral_triggers.txt'
mineral_triggers = parse(mineral_trigger_path)
triggers.update(mineral_triggers)
PREDICATE = 'asteroid_incoming_is_processed_mineral_fragment'
COUNT_HELPER = 'asteroid_incoming_count_controlled_mineral_fragments'
assert hashlib.sha256(trigger_path.read_bytes()).hexdigest().upper() == 'D591180EDE589C319D6077028736EDAFC184DECB86F62E2D48BFEC3F8AF81A4B'
def fields(rows): return dict((k, v) for k, _, v in rows)
assert fields(mineral_triggers[PREDICATE])['hidden_trigger'] == [
    ('is_in_array', '=', [('array', '=', 'global.asteroid_incoming_fragment_site_states'), ('value', '=', 'THIS')]),
    ('has_state_flag', '=', 'asteroid_incoming_fragment_site'),
    ('has_state_flag', '=', 'asteroid_incoming_mineral_site'),
    ('has_state_flag', '=', 'asteroid_incoming_state_transaction_applied'),
    ('NOT', '=', [('has_state_flag', '=', 'asteroid_incoming_main_crater')]),
    ('check_variable', '=', [('var', '=', 'asteroid_incoming_state_profile'), ('value', '=', 'constant:asteroid_incoming_profile.fragment_center'), ('compare', '=', 'equals')])
], 'exact six processed identity guards changed'
idea_defs = fields(fields(ideas['ideas'])['country'])
restored = copy.deepcopy(ideas)
restored_country = fields(restored['ideas'])['country']
for i in range(1, 7):
    name = 'asteroid_incoming_fragment_material_' + str(i)
    assert 'modifier' not in fields(idea_defs[name])
    for key, _, body in restored_country:
        if key == name: body.append(('modifier', '=', [('armor_factor', '=', '@ASTEROID_FRAGMENT_SITE_ARMOUR')]))
assert restored == before_ideas, 'an unowned idea field or definition changed'
MOD = 'asteroid_incoming_fragment_crater_armour'
MARKER = 'asteroid_incoming_fragment_material_1'
MAIN = 'asteroid_incoming_main_crater_material'
COUNT = 'asteroid_incoming_country_controlled_fragment_count'
BONUS = 'asteroid_incoming_fragment_armour_bonus'
REGISTRY = 'global.asteroid_incoming_fragment_site_states'
RECIPIENTS = 'global.asteroid_incoming_mineral_recipient_countries'
SCRATCH = 'global.asteroid_incoming_mineral_refresh_fragment_states'
ACTIVE = 'asteroid_incoming_minerals_active'
DM = fields(dmods[MOD])
assert set(DM) == {'icon', 'enable', 'remove_trigger', 'armor_factor'} and DM['armor_factor'] == BONUS
main_factor = fields(fields(idea_defs[MAIN])['modifier'])['armor_factor']
assert D(ideas[main_factor]) == D('1.00')

def country(name, alive=True, **extras):
    return dict(key=('country', name), kind='country', exists=alive, vars={}, ideas=set(), dynamic={}, flags=set(), missions=set(), **extras)
def state(number, owner='A', controller='A', profile=50, processed=True, mineral=True, fragment=True, main=False):
    flags = set()
    if processed: flags.add('asteroid_incoming_state_transaction_applied')
    if mineral: flags.add('asteroid_incoming_mineral_site')
    if fragment: flags.add('asteroid_incoming_fragment_site')
    if main: flags.add('asteroid_incoming_main_crater')
    return dict(key=('state', number), kind='state', owner=('country', owner), controller=('country', controller) if controller is not None else None, flags=flags, vars={'asteroid_incoming_state_profile': D(str(profile))}, population=0 if main else 10000, category='wasteland' if main else 'town')

class Model:
    def __init__(self, countries, states, registry, main_state=None, active=True, root_scope=('country', 'HOST'), from_scope=None, from_from_scope=None):
        self.objects = {o['key']: copy.deepcopy(o) for o in countries + states}
        self.root = root_scope
        self.from_scope, self.from_from_scope = from_scope, from_from_scope
        self.stack = [root_scope]
        self.flags = {ACTIVE} if active else set()
        self.arrays = {REGISTRY: list(registry)}
        self.targets = {}
        if main_state is not None: self.targets['asteroid_incoming_main_crater_state'] = main_state
        for i, key in enumerate(registry[:6], 1):
            if key in self.objects and key[0] == 'state': self.targets[f'asteroid_incoming_fragment_{i}_state'] = key
        self.temp, self.calls, self.ops = {}, [], []
    def obj(self): return self.objects[self.stack[-1]]
    def scope(self, token):
        if token == 'THIS': return self.stack[-1]
        if token == 'PREV': return self.stack[-2]
        if token == 'ROOT': return self.root
        if token == 'FROM': return self.from_scope
        if token == 'FROM.FROM': return self.from_from_scope
        if token == 'CONTROLLER':
            assert self.obj()['kind'] == 'state'
            key = self.obj()['controller']
            # A missing controller has no executable child scope.
            return key if key in self.objects else None
        if token.startswith('event_target:'): return self.targets.get(token.split(':', 1)[1])
        raise AssertionError(('unknown scope', token))
    def value(self, token):
        if token.startswith('constant:'):
            category, key = token[9:].split('.')
            return D(fields(constants[category])[key])
        if token in ('THIS', 'PREV', 'ROOT') or token.startswith('event_target:'): return self.scope(token)
        if token in self.arrays: return self.arrays[token]
        if token.startswith('global.'): return self.arrays.get(token, [])
        if token.startswith('PREV.'):
            return self.objects[self.scope('PREV')]['vars'].get(token[5:], D(0))
        try: return D(token)
        except Exception: return self.temp.get(token, self.obj()['vars'].get(token, D(0)))
    def conditions(self, rows): return all(self.node(k, op, v) for k, op, v in rows)
    def node(self, key, op, value):
        assert op == '='
        if key in ('AND', 'hidden_trigger'): return self.conditions(value)
        if key == 'OR': return any(self.node(*r) for r in value)
        if key == 'NOT': return not any(self.node(*r) for r in value)
        if key in triggers:
            return self.conditions(triggers[key]) == (value == 'yes')
        if key == 'exists':
            assert self.obj()['kind'] == 'country', 'COUNTRY exists used in a non-country scope'
            return self.obj()['exists'] == (value == 'yes')
        if key == 'has_state_flag':
            assert self.obj()['kind'] == 'state'
            return value in self.obj()['flags']
        if key == 'has_global_flag': return value in self.flags
        if key == 'has_country_flag':
            assert self.obj()['kind'] == 'country'
            return value in self.obj()['flags']
        if key == 'has_variable': return value in self.obj()['vars']
        if key == 'has_active_mission':
            assert self.obj()['kind'] == 'country'
            return value in self.obj()['missions']
        if key == 'has_war_with':
            assert self.obj()['kind'] == 'country'
            return self.scope(value) in self.obj().get('wars', set())
        if key == 'has_event_target': return value in self.targets
        if key == 'has_idea': return value in self.obj()['ideas']
        if key == 'has_dynamic_modifier': return value in self.obj()['dynamic']
        if key == 'tag': return self.stack[-1] == self.value(value)
        if key == 'check_variable':
            args = fields(value)
            a, b = self.value(args['var']), self.value(args['value'])
            comparators = {'equals': lambda: a == b, 'greater_than': lambda: a > b, 'less_than': lambda: a < b}
            assert args['compare'] in comparators
            return comparators[args['compare']]()
        if key == 'is_in_array':
            args = fields(value)
            return self.value(args['value']) in self.arrays.get(args['array'], [])
        if key in ('CONTROLLER', 'ROOT', 'FROM', 'FROM.FROM') or key.startswith('event_target:'):
            target = self.scope(key)
            if target is None: return False
            self.stack.append(target)
            try: return self.conditions(value)
            finally: self.stack.pop()
        raise AssertionError(('unmodelled trigger', key))
    def assign(self, key, value):
        target = self.stack[-1]
        if key.startswith('PREV.'): target, key = self.scope('PREV'), key[5:]
        self.objects[target]['vars'][key] = value
    def invoke(self, name):
        assert name in defs
        preexisting_temp = set(self.temp)
        self.calls.append((name, self.stack[-1]))
        self.run(defs[name])
        # Conservative helper lifetime: discard first-created temporary outputs.
        for key in set(self.temp) - preexisting_temp: self.temp.pop(key)
    def run(self, rows):
        chain = False
        for key, op, value in rows:
            assert op == '='
            if key in ('if', 'else_if', 'else'):
                if key == 'if': chain = False
                limit = next((v for k, _, v in value if k == 'limit'), [])
                if not chain and self.conditions(limit):
                    self.run([r for r in value if r[0] != 'limit'])
                    chain = True
            elif key in defs:
                assert value == 'yes'
                self.invoke(key)
            elif key in ('every_country', 'every_controlled_state', 'for_each_scope_loop'):
                body = [r for r in value if r[0] != 'array']
                if key == 'every_country': pool = [o['key'] for o in self.objects.values() if o['kind'] == 'country' and o['exists']]
                elif key == 'every_controlled_state':
                    assert self.obj()['kind'] == 'country'
                    pool = [o['key'] for o in self.objects.values() if o['kind'] == 'state' and o['controller'] == self.stack[-1]]
                else: pool = list(self.arrays.get(fields(value)['array'], []))
                for target in pool:
                    assert target in self.objects, ('invalid iterator input', target)
                    self.stack.append(target)
                    try:
                        limit = next((v for k, _, v in body if k == 'limit'), [])
                        if self.conditions(limit): self.run([r for r in body if r[0] != 'limit'])
                    finally: self.stack.pop()
            elif key in ('set_variable', 'add_to_variable', 'multiply_variable'):
                name, operator, token = value[0]
                assert len(value) == 1 and operator == '='
                val = self.value(token)
                if key == 'add_to_variable': val = self.value(name) + val
                if key == 'multiply_variable': val = self.value(name) * val
                self.assign(name, val)
            elif key == 'add_to_array':
                args = fields(value)
                self.arrays.setdefault(args['array'], []).append(self.value(args['value']))
            elif key == 'clear_array': self.arrays[value] = []
            elif key == 'clear_variable': self.obj()['vars'].pop(value, None)
            elif key == 'set_global_flag': self.flags.add(value)
            elif key in ('set_country_flag', 'clr_country_flag'):
                assert self.obj()['kind'] == 'country'
                if key == 'set_country_flag': self.obj()['flags'].add(value)
                else: self.obj()['flags'].discard(value)
            elif key == 'clear_global_event_target': self.targets.pop(value, None)
            elif key == 'save_global_event_target_as': self.targets[value] = self.stack[-1]
            elif key in ('CONTROLLER', 'ROOT', 'FROM', 'FROM.FROM') or key.startswith('event_target:'):
                target = self.scope(key)
                assert target is not None, ('invalid effect scope', key)
                self.stack.append(target)
                try: self.run(value)
                finally: self.stack.pop()
            elif key in ('add_ideas', 'remove_ideas'):
                assert self.obj()['kind'] == 'country'
                self.ops.append((key, self.stack[-1], value))
                if key == 'add_ideas': self.obj()['ideas'].add(value)
                else: self.obj()['ideas'].discard(value)
            elif key in ('add_dynamic_modifier', 'remove_dynamic_modifier'):
                assert self.obj()['kind'] == 'country'
                name = fields(value)['modifier']
                assert name == MOD and set(fields(value)) == {'modifier'}
                self.ops.append((key, self.stack[-1], name))
                if key == 'add_dynamic_modifier':
                    assert name not in self.obj()['dynamic'], 'duplicate dynamic add'
                    self.obj()['dynamic'][name] = D(0)
                else: self.obj()['dynamic'].pop(name, None)
            elif key == 'force_update_dynamic_modifier':
                assert value == 'yes' and self.obj()['kind'] == 'country'
                self.ops.append((key, self.stack[-1], MOD))
                if MOD in self.obj()['dynamic']:
                    if self.conditions(DM['remove_trigger']): self.obj()['dynamic'].pop(MOD)
                    elif self.conditions(DM['enable']): self.obj()['dynamic'][MOD] = self.value(DM['armor_factor'])
                    else: self.obj()['dynamic'][MOD] = D(0)
            elif key == 'asteroid_incoming_cancel_recovery_runtime':
                raise AssertionError('callback fixture unexpectedly entered unmodelled recovery cancellation')
            else: raise AssertionError(('unmodelled effect', key))
    def refresh(self): self.invoke(WRAPPER)
    def stats(self, actor):
        o = self.objects[('country', actor)]
        return (o['vars'].get(COUNT, D(0)), o['vars'].get(BONUS, D(0)), D('1.00') if MAIN in o['ideas'] else D(0), o['dynamic'].get(MOD, D(0)), MARKER in o['ideas'])
    def verify(self, expected):
        for actor, (number, main) in expected.items():
            count, bonus, main_bonus, applied, marker = self.stats(actor)
            assert (count, bonus, main_bonus, applied, marker) == (D(number), D(number) * D('0.20'), D(main), D(number) * D('0.20'), number > 0), (actor, self.stats(actor), number, main)
            o = self.objects[('country', actor)]
            assert all('asteroid_incoming_fragment_material_' + str(i) not in o['ideas'] for i in range(2, 7))
            assert (MOD in o['dynamic']) == (number > 0)
            self.stack.append(o['key'])
            try: assert self.conditions(triggers['asteroid_incoming_ai_chooser_holds_mineral_advantage']) == bool(number or main)
            finally: self.stack.pop()
            total = bonus + main_bonus
            assert D(0) * (D(1) + total) == 0
            assert D(100) * (D(1) + total) == D(100) + D(100) * total
        assert not self.arrays.get(SCRATCH), 'scratch leaked'
        recipients = self.arrays.get(RECIPIENTS, [])
        assert len(recipients) == len(set(recipients))
    def stable_repeat(self, expected):
        before_state = copy.deepcopy((self.objects, self.arrays, self.targets))
        self.ops.clear()
        self.refresh()
        self.verify(expected)
        assert (self.objects, self.arrays, self.targets) == before_state, 'refresh drift'
        assert not any(k == 'add_dynamic_modifier' or k == 'remove_dynamic_modifier' for k, _, _ in self.ops), 'stable refresh replaced dynamic identity'

def validate_owned(rows, trigger=False):
    effect_keys = {'if', 'else_if', 'else', 'every_country', 'every_controlled_state', 'for_each_scope_loop', 'set_variable', 'add_to_variable', 'multiply_variable', 'add_to_array', 'clear_array', 'clear_variable', 'set_global_flag', 'set_country_flag', 'clr_country_flag', 'clear_global_event_target', 'save_global_event_target_as', 'add_ideas', 'remove_ideas', 'add_dynamic_modifier', 'remove_dynamic_modifier', 'force_update_dynamic_modifier', 'asteroid_incoming_cancel_recovery_runtime'}
    trigger_keys = {'AND', 'OR', 'NOT', 'hidden_trigger', 'exists', 'has_state_flag', 'has_global_flag', 'has_country_flag', 'has_variable', 'has_active_mission', 'has_war_with', 'has_event_target', 'has_idea', 'has_dynamic_modifier', 'tag', 'check_variable', 'is_in_array'}
    for key, op, value in rows:
        assert op == '=', ('unsupported operator', key, op)
        if key in ('CONTROLLER', 'ROOT', 'FROM', 'FROM.FROM') or key.startswith('event_target:'): validate_owned(value, trigger)
        elif trigger and key in triggers:
            assert value == 'yes'
        elif trigger:
            assert key in trigger_keys, ('unknown owned trigger', key)
            if key in ('AND', 'OR', 'NOT', 'hidden_trigger'): validate_owned(value, True)
        elif key in defs:
            assert value == 'yes'
        else:
            assert key in effect_keys, ('unknown owned effect', key)
            if key in ('if', 'else_if', 'else', 'every_country', 'every_controlled_state', 'for_each_scope_loop'):
                for k, _, v in value:
                    if k == 'limit': validate_owned(v, True)
                validate_owned([r for r in value if r[0] not in ('limit', 'array')])
for body in defs.values(): validate_owned(body)
validate_owned(mineral_triggers[PREDICATE], True)
validate_owned(DM['enable'], True); validate_owned(DM['remove_trigger'], True)
try: validate_owned([('unmodelled_mineral_command', '=', 'yes')])
except AssertionError: pass
else: raise AssertionError('unknown command sentinel accepted')

actors = [country('A'), country('B'), country('HOST'), country('DEAD', False)]
cases_run = 0
for number in range(11):
    for main in (False, True):
        states = [state(i) for i in range(1, number + 1)]
        registry = [s['key'] for s in states]
        if main: states.append(state(1000, profile=70, fragment=False, main=True))
        m = Model(actors, states, registry, ('state', 1000) if main else None)
        m.refresh()
        m.verify({'A': (number, int(main)), 'B': (0, 0), 'HOST': (0, 0)})
        for _ in range(3): m.stable_repeat({'A': (number, int(main)), 'B': (0, 0), 'HOST': (0, 0)})
        cases_run += 1
        print(f'MINERAL_COUNT_{number}_MAIN_{int(main)}: count={number}, fragments={D(number)*D("0.20")}, main={int(main)}, repeated stable')

m = Model(actors, [state(1, owner='A', controller='B')], [('state', 1)])
m.objects[('country', 'B')]['subject_of'] = ('country', 'A')
m.refresh(); m.verify({'A': (0, 0), 'B': (1, 0), 'HOST': (0, 0)})
cases_run += 1; print('MINERAL_SUBJECT_ACTUAL_CONTROLLER: subject B receives bonus, owner/overlord A does not')

m = Model(actors, [state(1, owner='A', controller='B'), state(1000, owner='A', controller='B', profile=70, fragment=False, main=True)], [('state', 1)], ('state', 1000))
m.objects[('country', 'B')]['subject_of'] = ('country', 'A')
m.refresh(); m.verify({'A': (0, 0), 'B': (1, 1)})
cases_run += 1; print('MINERAL_SUBJECT_MAIN_AND_FRAGMENT: actual subject controller receives both, without overlord transfer')

m = Model(actors, [state(1), state(1000, profile=0, processed=False, mineral=False, fragment=False, main=True)], [('state', 1)], ('state', 1000), root_scope=('state', 1000))
m.refresh(); m.verify({'A': (1, 1), 'B': (0, 0)})
m.stable_repeat({'A': (1, 1), 'B': (0, 0)})
cases_run += 1; print('MINERAL_ANY_STATE_SCOPE_MAIN_FLAG: zero-pop wasteland main flag is authoritative, independent of fragment receipts')

m = Model(actors, [state(1000, controller='DEAD', profile=70, fragment=False, main=True)], [], ('state', 1000))
m.objects[('country', 'A')]['ideas'].add(MAIN)
m.refresh(); m.verify({'A': (0, 0), 'B': (0, 0)})
assert 'asteroid_incoming_main_crater_controller' not in m.targets
cases_run += 1; print('MINERAL_INVALID_MAIN_CONTROLLER: dead controller grants nothing and clears stale live main recipient')

states = [state(1), state(2, fragment=False), state(3, profile=30), state(4, processed=False), state(5, mineral=False), state(6, controller='DEAD'), state(7, controller=None), state(8), state(9, main=True, profile=70)]
registry = [('state', 1), ('state', 1), ('state', 2), ('state', 3), ('state', 4), ('state', 5), ('state', 6), ('state', 7), ('state', 9), ('state', 99999), ('country', 'A')]
m = Model(actors, states, registry)
m.refresh(); m.verify({'A': (1, 0), 'B': (0, 0), 'HOST': (0, 0), 'DEAD': (0, 0)})
m.stable_repeat({'A': (1, 0), 'B': (0, 0), 'HOST': (0, 0)})
cases_run += 1; print('MINERAL_DUPLICATE_STALE_RING_UNPROCESSED: only one valid registered center contributes')

states = [state(i) for i in range(1, 8)] + [state(1000, profile=70, fragment=False, main=True)]
m = Model(actors, states, [('state', i) for i in range(1, 8)], ('state', 1000))
m.refresh(); m.verify({'A': (7, 1), 'B': (0, 0)})
for s in m.objects.values():
    if s['kind'] == 'state': s['controller'] = ('country', 'B')
m.refresh(); m.verify({'A': (0, 0), 'B': (7, 1)})
m.stable_repeat({'A': (0, 0), 'B': (7, 1)})
cases_run += 1; print('MINERAL_TRANSFER: former A loses both bonuses, new B receives them once')

m.objects[('country', 'B')]['exists'] = False
for s in m.objects.values():
    if s['kind'] == 'state': s['controller'] = ('country', 'A')
m.refresh(); m.verify({'A': (7, 1), 'B': (0, 0)})
m.stable_repeat({'A': (7, 1)})
cases_run += 1; print('MINERAL_ANNEX: dead recorded recipient cleared, annexer gains current-control bonuses')

m.flags.clear(); m.refresh(); m.verify({'A': (0, 0), 'B': (0, 0)})
m.stable_repeat({'A': (0, 0)})
cases_run += 1; print('MINERAL_EVOLUTION_OFF: zeroed variables and no material/dynamic bonuses')

m = Model(actors, [state(1, controller='B')], [('state', 1)])
m.objects[('country', 'A')]['exists'] = False
m.objects[('country', 'A')]['ideas'].update({MAIN, 'asteroid_incoming_fragment_material_4'})
m.objects[('country', 'A')]['vars'].update({COUNT: D(4), BONUS: D('0.80')})
m.objects[('country', 'A')]['dynamic'][MOD] = D('0.80')
m.targets['asteroid_incoming_main_crater_controller'] = ('country', 'A')
m.targets['asteroid_incoming_fragment_4_controller'] = ('country', 'A')
m.refresh(); m.verify({'A': (0, 0), 'B': (1, 0)})
cases_run += 1; print('MINERAL_FIRST_MIGRATION_DEAD: old aliases clean dead beneficiary before recipient ledger exists')

m = Model(actors, [state(1), state(2)], [('state', 1), ('state', 2), ('state', 1)])
m.objects[('country', 'A')]['ideas'].update({MAIN} | {'asteroid_incoming_fragment_material_' + str(i) for i in range(1, 7)})
m.objects[('country', 'A')]['vars'].update({COUNT: D(999), BONUS: D('9.99')})
m.objects[('country', 'A')]['dynamic'][MOD] = D('9.99')
m.refresh(); m.verify({'A': (2, 0), 'B': (0, 0)})
assert not any(k in ('add_dynamic_modifier', 'remove_dynamic_modifier') and actor == ('country', 'A') for k, actor, _ in m.ops)
m.stable_repeat({'A': (2, 0), 'B': (0, 0)})
cases_run += 1; print('MINERAL_LEGACY_LIVE_MIGRATION: removes old identities and overwrites inflated variables without replacing a positive dynamic identity')

m = Model(actors, [state(1)], [('state', 1)])
m.refresh(); m.objects[('country', 'A')]['vars'][COUNT] = D(999)
m.refresh(); m.verify({'A': (1, 0)})
cases_run += 1; print('MINERAL_COUNT_WRITER_RECONCILIATION: refresh overwrites a conflicting public count from actual registry control')

hook_path = root / 'common/on_actions/028_asteroid_incoming_on_actions.txt'
hooks = fields(parse(hook_path)['on_actions'])
annex_effect = fields(hooks['on_annex'])['effect']
annex_mineral_branch = next(v for k, _, v in annex_effect if k == 'if' and (WRAPPER, '=', 'yes') in v)
assert fields(annex_mineral_branch)['limit'] == [('has_global_flag', '=', ACTIVE)]
annex_mineral_body = [r for r in annex_mineral_branch if r[0] != 'limit']
clear_from = ('FROM', '=', [('asteroid_incoming_clear_dead_mineral_recipient', '=', 'yes')])
assert annex_mineral_body[-1] == clear_from and (WRAPPER, '=', 'yes') in annex_mineral_body[:-1], 'annex must clear FROM last without an exists gate'
control_effect = fields(hooks['on_state_control_changed'])['effect']
validate_owned(annex_effect); validate_owned(control_effect)
achievement_country = next(v for k, _, v in runtime['asteroid_incoming_update_achievements'] if k == 'every_country')
count_call = next(r for r in achievement_country if r == (COUNT_HELPER, '=', 'yes'))
assert not any(k == 'every_controlled_state' for k, _, _ in achievement_country), 'weak achievement recount remains'
assert not any(k == 'set_variable' and any(var == COUNT for var, _, _ in v) for k, _, v in achievement_country), 'achievement count reset remains outside shared helper'

def execute_callback(model, effect):
    model.run(effect)

callback_probes = 0
for timing in ('state_control_before_annex', 'annex_before_state_control'):
    states = [state(i) for i in range(1, 8)] + [state(1000, profile=70, fragment=False, main=True)]
    m = Model(actors, states, [('state', i) for i in range(1, 8)], ('state', 1000), root_scope=('country', 'B'), from_scope=('country', 'A'), from_from_scope=('state', 1))
    m.refresh(); m.verify({'A': (7, 1), 'B': (0, 0)})
    # Fixtures declare no recovery project or active mission. The actual
    # recovery trigger is evaluated, and its cancellation branch must not run.
    if timing == 'state_control_before_annex':
        for s in m.objects.values():
            if s['kind'] == 'state': s['controller'] = ('country', 'B')
        execute_callback(m, control_effect)
        m.verify({'A': (0, 0), 'B': (7, 1)})
    # FROM intentionally still reports exists=yes in both annex snapshots.
    execute_callback(m, annex_effect)
    assert m.stats('A') == (D(0), D(0), D(0), D(0), False), timing
    if timing == 'annex_before_state_control':
        m.verify({'A': (0, 0), 'B': (0, 0)})
        for s in m.objects.values():
            if s['kind'] == 'state': s['controller'] = ('country', 'B')
        m.objects[('country', 'A')]['exists'] = False
        execute_callback(m, control_effect)
    m.verify({'A': (0, 0), 'B': (7, 1)})
    callback_probes += 1
    print(f'MINERAL_CALLBACK_{timing.upper()}: transient FROM cleared last, current B receives final snapshot bonuses')

for hook_name in ('on_annex', 'on_release_as_free', 'on_release_as_puppet', 'on_liberate', 'on_civil_war_end'):
    m = Model(actors, [state(1)], [('state', 1)], active=False, root_scope=('country', 'B'), from_scope=('country', 'A'))
    # A declared stale field must be left alone by the inactive gated callback,
    # not treated as a native active bonus. The owned modifier enable is false.
    m.objects[('country', 'A')]['vars'].update({COUNT: D(99), BONUS: D('9.99')})
    m.objects[('country', 'A')]['ideas'].add(MARKER)
    before_state = copy.deepcopy((m.objects, m.arrays, m.targets))
    effect = fields(hooks[hook_name])['effect']
    validate_owned(effect)
    execute_callback(m, effect)
    assert (m.objects, m.arrays, m.targets) == before_state and not m.calls, hook_name
    callback_probes += 1
    print(f'MINERAL_CALLBACK_INACTIVE_{hook_name.upper()}: gated mineral path is a no-op')

m = Model(actors, [state(1, controller='B')], [('state', 1)], active=False, root_scope=('country', 'B'), from_scope=('country', 'A'), from_from_scope=('state', 1))
m.objects[('country', 'B')]['ideas'].add(MARKER)
m.objects[('country', 'B')]['vars'].update({COUNT: D(99), BONUS: D('9.99')})
m.objects[('country', 'B')]['dynamic'][MOD] = D('9.99')
execute_callback(m, control_effect)
m.verify({'A': (0, 0), 'B': (0, 0)})
assert any(name == WRAPPER for name, _ in m.calls)
callback_probes += 1; print('MINERAL_CALLBACK_INACTIVE_STATE_CONTROL: retained ungated refresh performs zero-bonus cleanup')

m = Model(actors, [state(1), state(2, profile=30), state(3, processed=False), state(4, mineral=False), state(5, controller='B'), state(6)], [('state', 1), ('state', 1), ('state', 2), ('state', 3), ('state', 4), ('state', 5)])
m.refresh(); m.verify({'A': (1, 0), 'B': (1, 0)})
snapshot = copy.deepcopy((m.arrays, m.targets, m.objects[('country', 'A')]['dynamic'], m.objects[('country', 'A')]['ideas'], m.objects[('country', 'A')]['vars'][BONUS]))
m.objects[('country', 'A')]['vars'][COUNT] = D(999)
m.stack.append(('country', 'A'))
try: m.run([count_call])
finally: m.stack.pop()
assert m.objects[('country', 'A')]['vars'][COUNT] == 1
assert (m.arrays, m.targets, m.objects[('country', 'A')]['dynamic'], m.objects[('country', 'A')]['ideas'], m.objects[('country', 'A')]['vars'][BONUS]) == snapshot, 'count-only helper mutated scratch, ledger, bonus, or bonus identity'
callback_probes += 1; print('MINERAL_ACHIEVEMENT_ACTUAL_COUNT_CALL: processed registered current count, no scratch duplication or bonus mutation')

owned_paths = ['common/scripted_effects/028_asteroid_incoming_mineral_effects.txt', 'common/scripted_triggers/028_asteroid_incoming_mineral_triggers.txt', 'common/dynamic_modifiers/028_asteroid_incoming_mineral_dynamic_modifiers.txt', 'common/ideas/028_asteroid_incoming_ideas.txt', 'localisation/english/028_asteroid_incoming_mineral_dynamic_modifiers_l_english.yml']
loc_bytes = (root / owned_paths[-1]).read_bytes()
assert loc_bytes.startswith(bytes([239, 187, 191]))
for key in (MOD, MOD + '_desc'):
    matches = []
    for path in (root / 'localisation/english').glob('*.yml'):
        if re.search(r'^' + re.escape(key) + r':', path.read_text(encoding='utf-8-sig'), re.M): matches.append(path.name)
    assert matches == [Path(owned_paths[-1]).name], (key, matches)
assert not any('ai_will_do' in str(body) or 'ai_chance' in str(body) for name, body in defs.items())
assert cases_run == 33 and callback_probes == 9, 'expected scenario coverage changed'
print(f'{cases_run} actual-source scenarios passed. Main/dust/preparedness ideas preserved, no caps or bonus drift, AI predicate source unchanged. Native acceptance pending.')
print(f'{callback_probes} additional actual-source callback/count probes passed. Declared timing snapshots only, not observed engine ordering.')
for path in owned_paths: print(path, hashlib.sha256((root/path).read_bytes()).hexdigest())
print('Integrated runtime caller SHA256:', hashlib.sha256(runtime_path.read_bytes()).hexdigest())
print('Actual callback source SHA256:', hashlib.sha256(hook_path.read_bytes()).hexdigest())
```
