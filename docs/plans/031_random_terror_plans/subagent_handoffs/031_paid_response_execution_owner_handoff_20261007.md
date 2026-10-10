# Event 31 paid response execution preflight

## Disposition and acceptance

Applied owner repair under the explicit full Event 31 implementation request and the accepted decision/mission matrix and dedicated prompt.
Independent transaction review and same-fixture probability comparison remain in progress.
The repair covers Security Surge and Targeted Raid rather than claiming completion of all Event 31 actions or the full goal.

## Current source and change

`common/scripted_triggers/031_random_terror_triggers.txt` adds two read-only country-scope helpers, `random_terror_can_execute_security_surge` and `random_terror_can_execute_targeted_raid`.
ROOT is the payer and FROM is the exact state selected by the native targeted decision.
The helpers combine the existing inclusive affordability check, current government-response eligibility, nonterminal phase, current controller, exact response target and the existing normal or emergency branch.
The occupied-slot emergency exception still applies only to the responding government's own hostage or uprising receipt.
Foreign ownership does not block a state currently controlled by the responding government.

`common/decisions/031_random_terror_decisions.txt` uses that same helper inside each existing localized availability tooltip and before every effect in the cost-bearing callback.
Rejected stale clicks cannot debit command power, fuel, support equipment or army experience, save an action target, write an action receipt or invoke an outcome helper through this callback.
Valid actions retain their original inner dispatch, costs, outcome handlers, AI recipe and native cooldown expression.
The requirement tooltip now includes the accepted emergency hostage or uprising route beside the normal active/entrenched organization route.
No asset, mission, country, focus or unit definition was changed by this owner patch.

Current decision SHA-256 is `47E92D500BC5E0D4A8EBEB7D9292437638C89F718F6004010C35A676C3E4FA2E`.
Current trigger SHA-256 is `179DD12823D4580A14A1D753F6BF7C7ED6154D2392F1D69FFE156174025B54A7`.
The canonical event overview documents the shared preflight and its engine limits.
The unrelated dirty attack-foiling effects and English localisation hunks remain outside this patch and commit scope.
The one owned localisation hunk is `random_terror_targeted_raid_requirements_tt`.
Its direct edit returned `Failed to write file`, so the reviewed source was patched into a unique sibling through `apply_patch` and atomically promoted after both resolved paths and the unchanged target hash were verified.
Byte comparison proved that only the owned line changed while the BOM, line endings and unrelated edits were retained.

## Baseline and probability evidence

The read-only auditor deposited six byte-identical before sources under `evidence/hostage_response_before_20261007/` and the named scenario fixture `evidence/031_hostage_response_probability_scenarios_20261007.json` before this patch.
Fixture SHA-256 is `4E7C90BB68B3C7E54686CC7A82D9E3BB81C71A50245486FA8C1964AC938EE6DE`.
The baseline handoff is `031_hostage_response_probability_baseline_20261007.md`.

The parent live `probability_inspect` accepted the logical engine path, archived `snapshotPath` and expected copied-byte SHA-256 together and found both baseline decisions with `poolComplete=true`.
Canonical source hash is `81a09dc1f9433f9323e146ddda6b0d81c8f3ebd27943b0d3fa7b77b85021b672`, revision `958c6f3d9eb8b65ab876c2c40f402d22599c52d5e2dd66ed20d93b58797f03e1`.
Inspect artifact SHA-256 is `b25f95e89c00d4ce2facc18c0a07f74e239d5eae557c4c6c60cae67433e96386`, size 25,827 bytes.
The two-definition pool is complete only for the named pair, not for all government decisions or target-level campaign eligibility.
Required inputs include the actor, reserves, FROM, owned-state scopes, equipment scopes, classifier state and response legitimacy.
No conditional score or normalized click probability follows from that discovery result.
The reviewer attempted the matching full-pair before/after call using the unchanged fixture and verified snapshot selector, but the RPC timed out after 600 seconds without an analysis or comparison ID.
The parent issued a narrower Security Surge-only retry with the same fixture after that confirmed timeout and preserves its pending handle rather than inferring a result.

## Reference and scope evidence

Successful installed reference read: `common/decisions/_documentation.md:16-46`, ID `c8ba2a44d708fd3048c019dfb9e36f3ecf59ff754f7cb4ea3bb7c4704deb5c58`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
Successful offline reference reads: Decision modding cost lines 308-336, ID `0a37b9f1ad43a16c2d85d25b307d261fcc9e60292b4e164c335c03816535e4d8`, and targeted decisions lines 513-518, ID `09d5949e5fe45735721cecc1a56ee07a277873591c4a5289b66d184e7658ce96`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`.
These document the independent visibility/availability update cadence, manual custom-cost payment, payer ROOT and target FROM.
The bounded context bundle also omitted Scopes, so its presence alone was not treated as full rule coverage.
The detailed targeted-decision section supplies the pertinent ROOT/FROM rule directly.

Live source lookup navigated `random_terror_security_surge` through `view=structure` and `keyPath=[{key:complete_effect, occurrence:0}]`.
The initial expected revision became stale during concurrent work and the parent refreshed the definition rather than treating it as engine failure.
The returned callback at lines 472-500 had no complete transaction preflight, confirming the baseline gap.
Definition source revision was `3389508995053682572ca8b72b766542ef175b88bee638164052b8d8f85cdd48`.
The exact native precedent inspected is `AFG_cross_border_target_state` in installed `common/decisions/AFG.txt:458-512`, SHA-256 `DABC91C3F7FB1810D64D91D07147E827068D42540326CE10554A0752EE48D7A7`.
It demonstrates targeted state ROOT/FROM handling and manual command-power payment, not execution of this mod's rejection path.

## Validation and remaining limits

The connected `script_validate` route is exposed in this runtime.
It rejected explicit ROOT bindings as reserved, then checked both proposed trigger bodies under country scope with FROM bound to state.
Both returned `SCRIPT_CHECK_PARTIAL`, `valid=null`, with syntax, native command kind and declared-scope checks performed.
Seven existing scripted helper calls remained unresolved and parameter blocks were not fully checked.
The parent inspected the referenced helper definitions and retained those limits instead of treating the partial result as native engine validation.

The independent transaction reviewer found no source-level preflight defect and confirmed the shared payer/target/cost contract.
Its requirement-tooltip omission finding is repaired by the one owned English hunk described above.
The review's scenario inspection produced no returned result and is not treated as successful native execution.
Native re-enable timing after a rejected stale click is not established by the source guard and remains an engine evidence limit.
Current hostage partial outcomes and emergency access already existed and were not duplicated.
The full accepted dynamic-cost, unit commitment, country, focus, asset, achievement, terminal and other scenario contracts remain separate completion requirements.
No fallback or weakened substitute was introduced by this transaction preflight.
No game was launched and no logs were requested or searched.
