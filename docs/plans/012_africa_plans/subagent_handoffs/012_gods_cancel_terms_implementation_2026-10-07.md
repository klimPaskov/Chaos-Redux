# Event 012 cancellation of temporary contract terms

Date: 2026-10-07.
Acceptance basis: the active full-Gods goal requires host loss and participant cancellation to close current demands, punishment and live participant authority while retaining the accepted historical ledger.
Disposition: source repair implemented and independently reviewed; the parent publishes only this bounded change through the shared-index workflow.

## Defect and source repair

`gods_of_africa_cancel_participant` retired its contract and removed its authority fields, but did not call the agreement, diplomatic-term or instalment-term cleanup helpers already used by ordinary demand closure.
Signed instalment schedules and frozen state/enemy terms therefore survived cancellation as private residual state.
Its mission removal also depended on a private demand flag, leaving an orphan native mission untouched when that flag was absent.
This is a source cleanup defect; no post-loss native transfer or punishment was observed or inferred from those residual fields.

The parent adds the three existing cleanup calls after interrupted-contract retirement and frozen original-host slot release.
Cancellation also clears the private burden/ease flags, armour quotes, payment credit and capacity requirements that ordinary demand closure already clears.
It tests `has_active_mission` independently of the private demand flag, then removes any remaining native mission without invoking its completion or timeout effects.
The actual mission-state guard follows vanilla cleanup and avoids assuming the engine's behavior for removing an absent mission.
The existing historical contribution totals, terminal contract receipts, Wrath, opt-out memory, settlement/victor receipts and recovery ownership are unchanged.
No cooldown, material payment, punishment, price, weight, public value or periodic scan is added.

Changed gameplay owner: `common/scripted_effects/012_africa_gods_effects.txt`, `gods_of_africa_cancel_participant` only.
The helper contract is documented in `common/scripted_effects/012_africa_gods_contract_effects.md`.
Existing localisation already promises cancellation, so no player text or asset change is needed.

## Source identities

The immutable before copy is `C:/Users/klimp/AppData/Local/Temp/gods_cancel_terms_before_20261007/012_africa_gods_effects.txt`.
Before SHA-256: `f9fcb0d37264ebe6b10e64ca8b774226c17804170fae194bf616f4155aa00d51`.
Final after SHA-256: `720f1cb91a1c36e73254954f08b08bd5e2b241770b022d310aaea16b8b6d9332`.
Independent review caught a mission-guard edit landing in the similar archival body during refinement.
The parent restored that body to its baseline and applied the native mission-presence guard specifically inside `gods_of_africa_cancel_participant`; the final whole-file diff is confined to that helper.
Only the cancellation helper changes; the ordinary payment, defiance, punishment, recovery and final-settlement owners retain their existing bodies.

## Reference and validation evidence

The live reference context returned installed and offline sources with no omitted required sources.
The targeted search/read calls read installed `documentation/effects_documentation.md:6083–6092` for `remove_mission` and `2773–2782` for `clear_variable`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:1916`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, confirms country-scoped mission removal.
Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:565`, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, documents clearing an ordinary variable from memory.
Vanilla precedent: `common/scripted_effects/SWI_scripted_effects.txt:1877–1901`, `SWI_outgoing_president_cleanup`, read through source lookup and the underlying file; SHA-256 `1db766b3da05ca60c44b8708d20225eef780137c4fbf21572215f22a9395f939`.
Installed `documentation/triggers_documentation.md:3022–3030`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, documents `has_active_mission` in COUNTRY scope and was read for the final presence guard.

The added helper bodies were explicitly expanded into 28 native statements and checked as COUNTRY effects by `hoi4.script_validate`.
It returned `SCRIPT_CHECKED`, `valid=true`, 28 checked commands, zero unresolved commands and zero unchecked argument blocks.
Its check set is syntax, command kind and declared scope; `parametersChecked=false` remains explicit.
Seven supported findings omitted from the first inline result were checked in a separate seven-statement call, also `SCRIPT_CHECKED`, with no omitted findings.
The final `if` / `has_active_mission` / `remove_mission` block was checked separately as a COUNTRY effect and returned `SCRIPT_CHECKED`, three supported commands, no unresolved commands, no omitted findings and no unchecked argument blocks.
The documentation inventory revision is `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
These checks do not execute native missions, recovery or material transactions.

The bounded `.607` event trace and terminals render returned partial artifacts at revision `8f4a82aa5d847df22b40a90e209f8bd0e27f3d6ebe79d13e4fb3dbaf45dc33b0`, with helper expansion disabled.
They retain one aggregate blocking diagnostic and 10,444 unresolved nodes; the terminals view selected zero nodes and supplies no cleanup-closure evidence.
Trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c671ca0aea13db685fb20fe79df395935de6367372b3eae3a4549132b9bac305/7576aa68fd36248c870d4efc75071c5e6b4dc4b9f903a74d52d3109be25db160/event-trace-8f4a82aa5d84.json`.
Render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86794d5ed9f95d89208e3fbbf6647b369d5ab96f39c0c055afd147589c6bfdd3/0a72f4725f69c4dffd5fe795fcb649bd6ce3e706aa833e6d66afc5a1bbf7aeae/event-terminals-8f4a82aa5d84-manifest.json`.
No current-to-current comparison or native behavior is inferred from those projections.

The one-node `.602` options render succeeded as a partial source projection and its complete JSON artifact was read through the exposed artifact resource template.
It identifies the existing triggered COUNTRY demand notice at `events/012_africa_gods_of_africa.txt:42–57`, with the current title and description keys, but the one-node bound contains no option edges and no helper closure.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f60c3b3d08ceeafbb42aec161849c91bf5f6b33aa6d6156e8e79bfa7f141970/40654e1003107a2e2cbb69e0788f4725498d0f2fc8ff84c5e9e18e5a41dd1d48/event-options-8f4a82aa5d84.json`.
The live `hoi4-agent://server/status` resource reports version 3.10.0 and a responding current stdio process on October 7.
Client native-task negotiation was not established, so no job/helper-expansion route was assumed.
The old baseline probability artifact could not be recovered: resource read returned `Artifact provenance manifest is unavailable` for `probability-e8e4c7c626fb350f6c52e89c.json`.
The missing raw probability fixture therefore remains an explicit evidence gap, not a numeric comparison result.

No simplification is introduced.
The independent review in `012_gods_cancel_terms_review_2026-10-07.md` verifies the final `720f1cb9` file, confines the diff to cancellation, and finds no blocking source regression.
Its source matrix covers signed support, frozen diplomatic terms, already closed receipts, historical report preservation, orphan missions, repeated cleanup and recovery enrollment.
Separate participant archival/capitulation owners retain their existing bodies and are not represented as callers of this patched helper.
The full Gods objective remains open at native acceptance, weighted-evidence and separately owned asset/UI boundaries.
Skills used: events, decisions/missions, subagents and shared Git commit; the maintenance sidecar used the official skill-creator guidance.
The decisions/missions skill receives only a generic lifecycle paragraph covering cleanup parity, actual native mission presence and preservation of durable receipts.
Its exact bounded hunk and documentation-only validation are in `012_gods_cleanup_skill_handoff_2026-10-07.md`.
