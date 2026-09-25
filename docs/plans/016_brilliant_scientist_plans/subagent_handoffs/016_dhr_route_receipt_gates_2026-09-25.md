# Event 016 D’Rhondan route receipt gates

Date: 2026-09-25.

Disposition: implemented as a bounded owner tranche under the accepted Event 016 final completion contract. This does not close the remaining D’Rhondan diplomatic rewards or whole-event acceptance.

## Behavior and files

`common/scripted_triggers/016_dhrondan_country_triggers.txt` defines `dhrondan_integration_route_contract_is_ready` from the three existing regime focus receipts. The existing timed integration completion guard consumes it, and the `.49` compact response guard rechecks the Covenant ratification receipt before any diplomatic effect can commit.

`common/decisions/016_dhrondan_country_decisions.txt` requires the integration contract at targeted-decision discovery and availability, while its existing cancellation and completion paths reuse the strengthened completion guard. The Two-World Compact root now requires Covenant ratification at discovery. The two decisions retain their existing targets, costs, duration, AI weights, icons, and effects.

`localisation/english/016_dhrondan_country_l_english.yml` describes the added requirements and provides the integration route tooltip. `docs/events/016_brilliant_scientist/systems/dhrondan_country.md` records the effective decision lifecycle.

The three mandate flags are produced by `DHR_the_subject_world_protocol`, `DHR_administer_the_optimal_order`, and `DHR_invite_the_enclave_congress`; ratification is produced by `DHR_ratify_the_two_world_covenant`. The 88-focus source and layout were not changed.

## Source review and MCP evidence

The decision syntax and target-scope structure were checked against the offline Decision modding wiki snapshot, installed vanilla `common/decisions/_documentation.md`, and the vanilla African Union targeted decisions. The existing DHR decision category and receipt helpers were the implementation precedent. `git diff --check` passed for the gameplay, localisation, and system-documentation files; the localisation retains its UTF-8 BOM.

The narrow Event MCP trace for `chaosx.nr16.49` returned `EVENT_INSPECTED_PARTIAL`, revision `77b92aa19c709d2481f6335577b7c93ccd92b1ed2c5daf64211e57f83890e64a`, zero blocking diagnostics, and source artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/26d3d7c0d5c9036736535da9a664ce7a42f0e4e292073b445f2fb7a7b6960716/11b31fa91670a020ff923dbd652872819c0bd03c76169cf2f91bd36758781a4f/event-trace-77b92aa19c70.json`. The bounded options render returned `EVENT_RENDERED_PARTIAL` at the same revision with manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/309bdd201ba2db4f51e5f5165998139f09f1476a1178c6bc44ff95023c0ba797/9e1a16b732bce8e3fd62211c121cae82e4965eae61651179bedfd2f43525cde7/event-options-77b92aa19c70-manifest.json`. Both views defer workspace-wide helper and lifecycle projections. A comparison against retained revision `18bf807c8be35655138be368b38a6ff43f90d4c9ac0a1470ca1d9d44f43afd8f` returned `EVENT_REVISION_NOT_CACHED`, no comparison artifact, and failed validation.

`hoi4.probability_inspect` on the two affected targeted decisions returned `PROBABILITY_SOURCE_INSPECTED` through the discovered `mission_ai_will_do` adapter, but `poolComplete=false`, one discovered candidate, one unresolved input, and zero available candidates. Its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4fbf80ad5f4179a5857e0b37edb3e642fa9e03a93063fca238f8c00b209a320f/546d1f3748b2e6812d7b86aad872ce48a7c601c8226ccfdd18b82395f63a9334/probability-inspect-60d7fb4e8076.json`. The `decision_ai_will_do` probe was incomplete as well. A four-scenario before/after comparison using the committed decision source as inline before and the edited path as after timed out after 180 seconds. The missing candidate and timeout leave AI eligibility comparison unresolved. The unchanged source weights are not a substitute for it.

## Scope and remaining work

This tranche does not implement the separate paid terrestrial partner accord or decide its Synod no-DLC effect. The partner accord remains queued in `016_final_dhr_diplomatic_rewards_plan_2026-09-02.md`. Its no-DLC alternative still requires the recorded user choice. The existing map-exchange receipt remains the Covenant compact's prerequisite.

The Event 016 final contract still requires the other gameplay, model, GUI, focus, asset, audit, MCP, and catalog gates. This tranche makes no claim of in-game acceptance.
