# Event 019 registry and isolation specialist re-audit

> **Historical provider-contract notice (2026-08-09):** This re-audit's
> three-provider and eight-callback counts predate the expanded 18-ID provider
> census and the management-cost display/profile-cache callback. Retain its
> isolation findings as historical evidence only; use `source_of_truth_map.md`,
> `docs/events/019_infantry_spawn/systems/unit_family_coverage.md`, and
> `.tmp/event19_docs_curator_current.md` for current contract status.

> Registry-extension supersession notice: the dated statement that every
> future provider must be added to the sole Event 19 registry file predates the
> accepted external-provider contract. The three initial integrations remain
> consolidated there, but a future family defines one registration and its
> callbacks in its own existing integration surface and adds one parent startup
> call. It requires no Event 19 registry-file, list, name-map, or picture-map
> edit. Other findings below remain historical audit evidence.

Date: 2026-07-16  
Mode: live-source read-only specialist audit; this handoff is the only file written  
Gameplay ownership: parent agent

## Verdict

The one-file Event 019 registry ownership correction, ordinary unit registry, shared family registration rows, provider dispatch, local-token use, source-parent isolation, dynamic derivative identity, transaction ledgers, and lifecycle containment are sound in the audited live source. The expected sole registry hash matches exactly.

One P1 contract defect and one P2 documentation defect remain. The concurrently strengthened duplicate-family registration guard is complete and closes the duplicate-row metadata lead.

| Severity | Count | Disposition |
| --- | ---: | --- |
| P0 | 0 | No corrupting registry or isolation defect was found. |
| P1 | 1 | The advertised provider cleanup callback and cleanup-profile contract is dead: callbacks exist, but generic dispatch never invokes them and no runtime path consumes the profile. |
| P2 | 1 | The shared registry documentation names the wrong provider payment-success temporary variable. |

The two owner-approval engine contracts are reported separately below. They remain global Event 019 completion blockers, but they are not reclassified as registry/isolation defects.

## Required registry ownership invariant

The audited source satisfies the invariant:

- the sole Event 019 registry implementation file is `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`;
- its SHA-256 is `CF847800E89D6B38E484338EC0B9C21DC48D07AC505C80040109BB6670E7C934`;
- Event 019 registry constants remain in `common/script_constants/019_infantry_spawn_constants.txt`;
- Event 019 registry predicates remain in `common/scripted_triggers/019_infantry_spawn_triggers.txt`;
- no other gameplay file has an Event 019 registry filename, and no obsolete split-registry reference remains;
- `common/on_actions/002_zombie_outbreak_on_actions.txt` calls `chaos_unit_family_provider_501_register` exactly once from its existing `on_startup` block;
- `common/on_actions/010_death_on_actions.txt` calls `chaos_unit_family_provider_502_register` exactly once from its existing `on_startup` block;
- `common/on_actions/005_soviet_collapse_on_actions.txt` calls `chaos_unit_family_provider_503_register` exactly once from its existing `on_startup` block.

The future-family ownership rule is exact: complete provider entry goes in sole Event19 registry file; only startup call goes in existing parent on-action; no Event19 family-list edit.

## Finding REG-019-P1-001 — cleanup is a dead provider contract

### Evidence

Each installed provider supplies all nine advertised Event 019 callbacks, including:

- `chaos_unit_family_provider_501_event19_cleanup`;
- `chaos_unit_family_provider_502_event19_cleanup`;
- `chaos_unit_family_provider_503_event19_cleanup`.

All three callbacks call `infantry_spawn_cleanup_current_family_lot`. The shared registry document lists `chaos_unit_family_provider_N_event19_cleanup` as a required provider callback. Nevertheless:

- no meta-effect or direct runtime caller dispatches any provider `event19_cleanup` callback;
- `infantry_spawn_cleanup_current_family_lot` occurs only at its definition and inside those three otherwise-dead callbacks;
- `global.chaos_unit_family_cleanup_profile_entries` is appended, alignment-checked, duplicate-checked, and populated, but is never consumed by lifecycle logic.

The other eight provider callback families have live generic dispatchers across generation, Muster Control, derivative management, and scenario creation. Cleanup is the sole callback exception.

### Impact

This is not a current zombie/ghost/golem unit leak. Current annex, defeat, derivative, and scenario cleanup use exact generic unit/lot/template ledgers, proof-gated deletion, teardown, and retry finalization. Those paths cover providers 501–503 independently of the dead callback.

It is still P1 because the published extension contract is false: a future family can provide the required cleanup callback and cleanup profile exactly as documented, yet Event 019 will never execute either. That breaks the provider-only extension promise at a lifecycle boundary where silent leakage would be costly.

### Recommended narrow correction

The safest narrow correction for the current design is to make the contract match the already-authoritative generic exact-ledger cleanup:

1. retire `event19_cleanup` as a required live provider callback;
2. remove the three dead callback definitions;
3. document `cleanup_profile` explicitly as reserved/audit metadata until a real consumer exists, or remove that field consistently if it has no planned use;
4. keep generic exact-ledger cleanup authoritative.

Do not simply dispatch `infantry_spawn_cleanup_current_family_lot` during annex cleanup. Annex/final cleanup may span defeated-country and annexer scopes after engine ownership changes, so a provider call requires an explicit proof-safe lifecycle boundary and idempotence contract. If custom family cleanup is required, define that boundary first and add one generic provider-ID dispatcher there.

## Finding REG-019-P2-001 — payment result token is stale in documentation

`docs/systems/cbrn_warfare/chaos_unit_family_registry.md` says `event19_pay_management_action` must set `infantry_spawn_family_management_payment_success`. That token does not occur in gameplay source.

All three providers and all derivative/Muster consumers consistently use:

`infantry_spawn_family_provider_payment_succeeded`

Update the shared registry document to name the live token. This matters for future provider implementations because the documented spelling would cause the generic transaction to treat a successful debit as failure.

## Closed lead — duplicate family metadata conflict detection

The live `chaos_unit_family_register_current_provider` implementation now treats a repeated family ID as idempotent only when the complete registered row matches. It compares:

- provider ID;
- source event ID;
- availability mode;
- Event 019 lot policy;
- derivative, sustainment, containment, AI, visual, cleanup, and parent-isolation profiles;
- spawn weight;
- contract version.

Any mismatch routes to the global registry invariant failure. The registered family ID is the lookup key, and an exact repeated registration remains harmless. This closes the earlier duplicate-row metadata ambiguity.

## Ordinary registry and generic dispatch evidence

- The ordinary registry builds 15 aligned temporary arrays with 87 entries apiece: row, token, provider, gate-provider, slot-kind, group, equipment, quality, compatibility, mobility, supply, finite-risk, and three support ledgers.
- Row, token-provider, gate-provider, and obligation-provider ID sets align exactly. There are 87 distinct live rows, matching `registered_rows`; row IDs 31 and 37 remain intentionally unregistered constants rather than ghost rows.
- All 87 local token providers and 87 gate providers exist. Obligation providers resolve across the sole registry and generation effect files without an unresolved ID.
- Template materialization is manifest-gated, ledger-aligned, and transaction-scoped. It stamps exact unit, lot, template, and family identity; failure rolls back or marks failure instead of substituting a different unit.
- Static unit tokens are loaded through provider-local token keys. No cross-event unit alias or static-token fallback was found.

## Family behavior, saturation, and transactions

### Train versus spawn

- Provider 501 uses the base `zombies` token and is `trainable_and_spawnable`.
- Provider 502 uses the weak `death_weak_ghost_host` token and is `spawn_only`.
- Provider 503 uses the base `coal_golem` token and is `spawn_only`.
- Ghost and golem templates are locked and non-recruitable. Generic Muster authorization only enables recruiting for a trainable provider. No advanced zombie/ghost variant is smuggled into the family registry.

### Saturation, containment, and reinforcement

- Pressure/saturation is rebuilt from aligned live unit, lot, family, claimant, and management records and is bounded by the configured clamps.
- Containment, cantonment, and restricted management reduce pressure; sustainment increases it through the provider profile.
- Paid family reinforcement evaluates eligibility, debits provider costs, snapshots the request, builds/spawns, and calls the matching refund callback on proven failure. Shared and provider-owned costs remain separated.
- Derivative and scenario creation use private exact ledgers and proof-before-finalization. A failed create does not silently substitute another family, template, owner, or tag.

## Isolation and lifecycle evidence

- Shared classification keeps all Event 019 derivatives under `is_special_chaos_country`, while only flagged nonhuman derivatives enter `is_actual_nonhuman_country`; human claimant breakaways are not mislabeled nonhuman.
- Provider and derivative eligibility reject the original zombie/Death parents and the relevant source-event parent-state flags. KMB-specific source mechanics remain tag-keyed and are not inherited by a dynamically created actor.
- Event 019 derivative/scenario code reads safety gates such as world-end state but does not mutate source event counts, stages, evolution flags, super-event state, or world-end state.
- Dynamic actors use `create_dynamic_country` with the source owner as `original_tag`; no fixed derivative tag or release-tag fallback exists.
- Defeat handling is idempotent across capitulation and annex. War-win accounting is performed only on the derivative victory path. Ghost civilian deaths have one dedicated mutation path. Selected states are transferred once from a deduplicated selection array.
- Annex, derivative, and scenario cleanup operate on exact recorded unit/lot/template/cohort identities, require positive proof before finalization, and retain retry records when proof is incomplete.
- The natural derivative preflight stops before ownership mutation because the engine exposes no exact division-scoped owner transfer. It does not fall through to a whole-army, ratio, fixed-tag, or recreate/delete substitute.

## Claimant-pool evidence

The claimant selector first samples a compatible profile and then performs a deterministic scan across region-compatible profiles if the random sample fails. The deterministic pass closes a sampling gap without selecting a mismatched portrait/profile.

No `every_country`, `any_country`, `random_country`, `always = yes`, global profile, or catch-all claimant exists in the claimant identity file. The twentieth Australasia profile remains region-bound; it is not a disguised global fallback.

## Approval blockers — separate from audit findings

### B-019-001 — exact natural loyal-formation ownership transfer

Natural pressure-driven derivative release freezes the exact candidate, region, unit, template, lot, generation, and claimant/family records, then deliberately stops before ownership mutation. Installed engine documentation provides whole-army or country-ratio transfer, not an exact division-scoped transfer effect. Recreate-prove-delete would lose live formation state and is an explicit fallback requiring owner approval. It was not implemented by this audit.

### B-019-002 — four exact same-battle achievement awards

The available combat callback surface does not atomically provide the exact Event 019 division, victory, duration, enemy-strength ratio, and casualties for the same battle. The four achievements therefore remain hidden and fail closed. A controlled-trial/proxy battle path would be a fallback requiring owner approval. It was not implemented by this audit.

These two blockers still prevent a global Event 019 completion claim even though they do not reopen a registry/isolation P0, P1, or P2.

## References consulted

Repository skills read and followed:

- `chaos-redux-subagents`;
- `chaos-redux-events`.

Required offline wiki pages consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Division modding, and Unit modding.

Vanilla authority consulted included `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, relevant effect/trigger documentation for arrays, event targets, dynamic countries, unit creation/deletion, and vanilla `create_unit` and `on_startup` precedents.

## Files changed, simplifications, and remaining risk

- Changed only this handoff: `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_registry_isolation_specialist_reaudit_2026_07_16.md`.
- No gameplay, localisation, registry, constant, trigger, on-action, specification, asset, or workbook file was edited.
- No fallback, fixed tag, global claimant catch-all, weaker battle proxy, or ownership-transfer substitute was introduced.
- No audit criterion was omitted. The P1 cleanup contract and P2 documentation token remain for the parent to resolve; the two approval-gated engine contracts remain deliberately unresolved.
- No files were staged and no commit was created.

## Remediation re-audit: 2026-07-16 10:00 +03:00

This section records the read-only audit of the parent's cleanup-contract remediation. It supersedes the initial P1 and P2 disposition above and the earlier statement that those findings remained open.

### Final severity disposition

| Severity | Open count | Result |
| --- | ---: | --- |
| P0 | 0 | No registry or isolation regression was found. |
| P1 | 0 | REG-019-P1-001 is closed. |
| P2 | 0 | REG-019-P2-001 is closed, and the residual definition-only cleanup helper found during this re-audit was removed before the final source snapshot. |

The two owner-approval engine contracts B-019-001 and B-019-002 remain unchanged. They are still separate global Event 019 completion blockers and are not registry or isolation severity findings.

### REG-019-P1-001 closure

The three provider `event19_cleanup` definitions are absent. The required provider callback list no longer advertises a cleanup callback. `cleanup_profile` is documented as reserved audit and migration metadata, while Event 19 remains responsible for exact lot, unit, template, claimant, annex, and derivative-defeat teardown through frozen evidence and absence proofs.

The first remediation snapshot left `infantry_spawn_cleanup_current_family_lot` and its old provider-hook comment as definition-only residue. The parent removed that helper and comment before this final audit. Neither the helper nor a provider cleanup callback definition remains in live gameplay source.

### REG-019-P2-001 closure

The shared registry document now names the live payment result token:

`infantry_spawn_family_provider_payment_succeeded`

The obsolete `infantry_spawn_family_management_payment_success` token has no occurrence in gameplay, the shared registry document, or Event 019 specifications.

### Remaining callback coverage

Each provider has exactly eight callback definitions, for 24 definitions across providers 501, 502, and 503. The definition set is:

- `build_template`
- `evaluate_eligibility`
- `evaluate_management`
- `pay_management_action`
- `reconcile_sustainment`
- `refund_management_action`
- `setup_derivative`
- `spawn_unit`

The generic meta-dispatch set matches this definition set exactly. The documented required callback set also matches it exactly. There is no defined callback without a generic dispatcher and no generic dispatcher without a provider definition.

### Sole-file registry compliance

The post-remediation SHA-256 of `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt` is:

`F5582496605395431EF38AF798D6C56D05DD2CF91B7CF8C89D57A42F87C3D90A`

The earlier `CF847800E89D6B38E484338EC0B9C21DC48D07AC505C80040109BB6670E7C934` hash identifies the pre-remediation audit snapshot. The hash changed only because the approved remediation removed the three callback blocks from the sole registry file.

The ownership constraint remains exact:

- `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt` is the only Event 019 registry gameplay filename.
- Registry constants remain in `common/script_constants/019_infantry_spawn_constants.txt`.
- Registry predicates remain in `common/scripted_triggers/019_infantry_spawn_triggers.txt`.
- Event 002 calls provider 501 once from its existing parent `on_startup` block.
- Event 010 calls provider 502 once from its existing parent `on_startup` block.
- Event 005 calls provider 503 once from its existing parent `on_startup` block.
- No alternate registry file, family-list row, or obsolete split-registry reference was introduced.

The 15 ordinary registry ledgers still contain 87 aligned entries each. The provider callback removal did not alter ordinary rows, local tokens, gate providers, family registration rows, payment and refund behavior, source-parent isolation, claimant selection, dynamic actor identity, or exact teardown paths.

### Final remediation verdict

The cleanup callback contract is retired cleanly, the payment-result documentation is correct, all remaining provider callbacks are live-dispatched, and the sole-file registry ownership rule remains intact. No new P0, P1, or P2 registry or isolation finding exists in the final audited source.

This re-audit appended only this closure section. The auditor made no gameplay, shared documentation, specification, localisation, asset, or workbook edit and did not stage or commit any file.
