# Event 006 FORM-24 / FORM-25 linkage architecture handoff

**Date:** 2026-07-19

**Scope:** IW-093 Asante (`DOX`) and IW-098 Sokoto (`SOK`) formable linkage

**Disposition:** design and blocker report only. No gameplay source was changed.

## Result

The accepted material defines package-local preparation, but it does not yet
define an executable FORM-24 or FORM-25 family contract. The family matrix
names broad member directions and territorial themes only. It does not name
the exact carrier policy, member tags and package ids, anchor states, capital
alternatives, consent policy, or integration policy needed by an adapter.

The current generic registry has profile rows for family ids 24 and 25, but
its readiness, carrier, member, commit, and cleanup dispatch paths have no
FORM-24 or FORM-25 branches. The task scope also excludes edits to the general
registry files. Adding inert helpers without a caller would violate the
repository helper rule, while setting any generic readiness flag would break
the accepted fail-closed contract. The safe result is therefore this
implementation-ready plan and an explicit blocker, with package-local
preparation left unchanged.

## Evidence inspected

Accepted source-of-truth surfaces:

- `docs/specs/006_independence_wave_specs/matrices/006_formable_family_registry.csv`
  lists FORM-24 as West African Federation with broad directions for Asante,
  Fante, Dahomey, Benin, Oyo, and compatible republics, and lists
  member-capital plus rail or port links as the territorial direction. It
  lists FORM-25 as Sahel Confederation with broad directions for Sokoto,
  Kanem-Bornu, Hausa, Darfur, Wadai, and compatible packages, and regional
  capitals plus caravan corridors as the territorial direction. No exact
  tags, package ids, states, or consent rows are provided.
- `docs/systems/006_independence_wave_iw093_iw098_signature_packages.md`
  explicitly limits IW-093 and IW-098 to package-local preparation. It
  requires three active members, three unique anchors, and three explicit
  consents before a shared family can commit, and leaves identity, territory,
  flags, and member-policy audits as separate blockers.
- `docs/plans/006_independence_wave_plans/006_iw093_iw098_signature_packages_improvement_addendum_2026_07_18.md`
  repeats that `WFX` and `SFX` are only collision-free candidates, not
  admitted identities, and that no assumed Fante, Hausa, Darfur, Wadai,
  Benin, Oyo, or Kanem-Bornu member may be materialized from a name.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw093_iw098_scripted_system_architecture_handoff_2026-07-18.md`
  already records the intended family adapter names and confirms that the
  generic router must remain the only dispatch router.

Current source surfaces:

- `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt`
  has the package gates `can_prepare_independence_wave_form24_from_iw093`
  and `can_prepare_independence_wave_form25_from_iw098`. They validate the
  accepted package route and values only. The current FORM-25 gate allows
  Sultanic Federal or Northern Constitution and intentionally excludes
  Frontier Command. Broaden it only after an explicit package-spec decision.
- `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt`
  selects family ids 24 and 25 during the reviewed focus setup and does not
  set generic readiness or commit flags.
- `common/decisions/006_independence_wave_iw093_iw098_decisions.txt` and
  `common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.txt`
  own the paid 90-day preparation decisions and the generation-local
  `independence_wave_iw093_form24_preparation_complete` and
  `independence_wave_iw098_form25_preparation_complete` receipts. They do not
  mutate the map, invite members, set a cosmetic tag, or commit a family.
- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`
  has readiness and commit branches for FORM-01 through FORM-05, FORM-48,
  FORM-12, FORM-13, and FORM-18, but no FORM-24 or FORM-25 branch.
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`
  already dispatches `independence_wave_formable_identity_adapter_[ID]` and
  `independence_wave_formable_integration_adapter_[ID]` through meta effects,
  but its generic readiness and cleanup paths cannot reach family 24 or 25
  until their family branches are added by the general-registry owner.
- `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`
  is the closest admitted precedent for keyed identity adapters, frozen-row
  member iteration, sovereign-member handling, and family cleanup. It uses
  exact package predicates and fixed state mappings. Those details cannot be
  copied for FORM-24 or FORM-25 because the accepted sources do not provide
  equivalent mappings.

## Proposed helper map

The following is the narrow adapter contract to implement after the missing
family decisions are accepted. Names are proposed to match the existing
keyed-adapter and package-prefix conventions. No helper in this table was
added in this tranche.

| Helper | Scope and inputs | Output and side effects | Intended call sites |
| --- | --- | --- | --- |
| `is_independence_wave_iw093_form24_carrier` | Country. Requires active IW-093 `DOX`, setup completion, family 24 selection/profile snapshot, constitutional/federal route, and the package preparation receipt. | Boolean only. Must reject terminal sovereignty and stale generations. | Generic carrier eligibility branch in the formable registry. |
| `is_independence_wave_iw098_form25_carrier` | Country. Requires active IW-098 `SOK`, setup completion, family 25 selection/profile snapshot, an explicitly approved route/method policy, and the package preparation receipt. | Boolean only. Must preserve the Event-012 exclusion and reject terminal sovereignty. | Generic carrier eligibility branch in the formable registry. |
| `has_independence_wave_form24_exact_carrier_anchor` | Carrier country plus the frozen Event-006 anchor target. Requires state 274 ownership/control and the family-specific territory proof once exact states are supplied. | Boolean only. No state transfer or capital mutation. | Carrier trigger, pre-congress ledger pass, and strict commit preconditions. |
| `has_independence_wave_form25_exact_carrier_anchor` | Carrier country plus the frozen Event-006 anchor target. Requires state 902 ownership/control and the family-specific territory proof once exact states are supplied. | Boolean only. No state transfer or capital mutation. | Carrier trigger, pre-congress ledger pass, and strict commit preconditions. |
| `is_independence_wave_form24_member_candidate` | Candidate country with ROOT as carrier. Requires a named active Event-006 origin/package row, sovereign status, current generation, a nonzero owned and controlled anchor, no war or formable transaction, and family-specific route/consent compatibility. | Boolean only. Must reject assumed or placeholder members. | Frozen member-ledger builder, founding invitation validation, and reply validation. |
| `is_independence_wave_form25_member_candidate` | Same inputs as FORM-24, with an exact Sahel package row and family-specific route, religious or defensive policy once accepted. | Boolean only. Must reject Event-012-only membership and stale SOK origins. | Frozen member-ledger builder, founding invitation validation, and reply validation. |
| `has_independence_wave_form24_method_policy` | Carrier country. Reads the selected generic method and the accepted IW-093 route receipt. | Boolean only. Does not infer a method from a route label. | Discovery, congress preparation, and commit preconditions. |
| `has_independence_wave_form25_method_policy` | Carrier country. Reads the selected generic method and the accepted IW-098 religious, federal, or defensive route policy. | Boolean only. Must not silently map religious union to dynastic, negotiated, or military method without a written decision. | Discovery, congress preparation, and commit preconditions. |
| `independence_wave_iw093_form24_register_readiness` | Carrier country after exact identity, flag, territory, and member-policy audits. | Sets the selected-family snapshot and family readiness attestation only when all receipts exist. It must never create a tag or infer a territory. | A future branch in `independence_wave_formable_register_selected_family_readiness`. |
| `independence_wave_iw098_form25_register_readiness` | Same as FORM-24, including date-appropriate IW-098 role and Event-012-safe package proofs. | Same fail-closed readiness behavior. | A future branch in `independence_wave_formable_register_selected_family_readiness`. |
| `independence_wave_formable_identity_adapter_24` | Carrier plus frozen family id, generation, exact readiness flags, and the audited `WFX` reservation. | Applies `set_cosmetic_tag = WFX` only after strict prevalidation, writes the family identity receipt, and never overwrites a living country or creates a SOK tag. | Existing generic meta-effect identity dispatcher. |
| `independence_wave_formable_identity_adapter_25` | Carrier plus frozen family id, generation, exact readiness flags, and the audited `SFX` reservation. | Applies `set_cosmetic_tag = SFX` only after strict prevalidation and writes the family identity receipt. | Existing generic meta-effect identity dispatcher. |
| `independence_wave_formable_integration_adapter_24` | Carrier plus frozen member-country, generation, anchor, and consent arrays. | Iterates frozen rows only. Applies the accepted sovereignty or integration policy, writes bounded integration-state entries, and sets the integration receipt only after every required row passes. | Existing generic meta-effect integration dispatcher. |
| `independence_wave_formable_integration_adapter_25` | Same as FORM-24 with the exact Sahel member policy. | Same frozen-row and no-world-scan contract. | Existing generic meta-effect integration dispatcher. |
| `has_independence_wave_form24_runtime_commit_proof` | Carrier. Checks family, generation, package preparation, member and anchor counts, consent receipts, exact territory, identity, flags, integration, and member-policy proofs. | Boolean only. | Generic `can_independence_wave_commit_selected_formable` branch. |
| `has_independence_wave_form25_runtime_commit_proof` | Same as FORM-24 with date-aware role and Event-012-safe checks. | Boolean only. | Generic `can_independence_wave_commit_selected_formable` branch. |
| `independence_wave_form24_cleanup_runtime` / `independence_wave_form25_cleanup_runtime` | Carrier or frozen member country with matching family and generation. | Clears only family-owned receipts, staged member rows, reservations, and generation-bound variables. It must preserve a committed cosmetic tag and any Event-012 state. | Generic formable cleanup and transaction failure cleanup, once general branches are admitted. |

The adapter names deliberately use the existing numeric meta-effect contract.
No second router or package-specific replacement for the generic registry is
proposed.

## Constants and tuning table plan

Existing constants are sufficient for package preparation and the initial
family profile:

| Existing constant | Use |
| --- | --- |
| `constant:independence_wave_formable_family.west_african_federation` | FORM-24 family id 24 |
| `constant:independence_wave_formable_family.sahel_confederation` | FORM-25 family id 25 |
| `constant:independence_wave_formable_registry.west_african_federation` | Region 9, method mask 5, 3 members, 3 consents, 3 anchors, AI/risk tiers |
| `constant:independence_wave_formable_registry.sahel_confederation` | Region 9, method mask 11, 3 members, 3 consents, 3 anchors, AI/risk tiers |
| `constant:independence_wave_iw093.anchor_state` | IW-093 anchor state 274 |
| `constant:independence_wave_iw098.anchor_state` | IW-098 anchor state 902 |
| `constant:independence_wave_iw093.form24_*` | Accepted IW-093 package thresholds 70, 65, and 50 |
| `constant:independence_wave_iw098.form25_*` | Accepted IW-098 package thresholds 70, 65, and 60 |

Do not duplicate these profile counts or package thresholds. Once the family
contract is resolved, add only values that are genuinely new to
`common/script_constants/006_independence_wave_iw093_iw098_constants.txt` or
the shared signature table owned by the parent. The missing values that need
an explicit decision are:

- exact package id and original-tag rows for every FORM-24/25 member;
- exact anchor-state list and any capital alternatives for each member;
- the method-policy mapping for FORM-25 religious, federal, and defensive
  routes, including whether the existing Frontier Command exclusion remains;
- member sovereignty versus full integration receipts and post-formation
  integration stages;
- final identity and cosmetic-tag reservations. `WFX` and `SFX` are
  collision-free candidates only, not approved identities.

No political-power store, free-unit loop, free equipment grant, or hardcoded
territorial reward belongs in these helpers.

## Event-target and cleanup plan

- Reuse the existing regular targets `independence_wave_formable_proposer`,
  `independence_wave_formable_member_to_end`, and the frozen setup anchor and
  former-host targets. Regular targets are appropriate for the current effect
  chain and clear automatically after the chain completes.
- Keep carrier, member, generation, anchor, consent, and proposal-sequence
  data in the existing aligned arrays and variables. Do not introduce a
  family-wide world scan or a new periodic on-action.
- Do not add a global family target. If a future post-formation system truly
  needs one, it must use a uniquely named target and an explicit
  `clear_global_event_target` on every success, failure, and generation reset.
- Before generic cleanup clears the selected profile, clear only IW-093 or
  IW-098 preparation receipts and any future family adapter receipts whose
  stored generation equals the ending generation.
- On failed or cancelled congress, remove provisional identity reservations
  and staged member receipts without dropping a pre-existing cosmetic tag.
  On successful commit, preserve the committed `WFX` or `SFX` cosmetic tag
  and clean only transient proposal and ledger state.
- IW-098 cleanup must not clear `africa_priority_member_package_active`,
  `africa_priority_member_focus_tree_loaded`, Event-012 role receipts, or
  vanilla SOK state. Existing package cleanup already follows this boundary.

## Migration from current package preparation

1. Keep the current paid decisions and focus preparation exactly as they are.
   Their receipts remain the only package-local proof currently available.
2. After an accepted family contract exists, add the carrier, member, anchor,
   method-policy, and runtime-proof triggers to the IW-093/IW-098 package
   trigger surface. Each trigger must use exact package rows and frozen
   anchors, not regional name matching.
3. Add the keyed identity, integration, readiness, and cleanup effects to the
   IW-093/IW-098 package effect surface. The effects must be inert unless the
   strict family proof passes.
4. The parent or general-registry owner must then add the FORM-24/25 branches
   to the existing generic readiness, carrier, member, commit, and cleanup
   paths. The existing meta-effect dispatch names remain unchanged.
5. Replace any future family-specific member loop with the shared frozen
   arrays. Do not scan all countries or states from a decision, focus, or
   adapter.
6. Add a family-specific audit receipt and final content attestation only
   after identity, flags, territory, member policy, country surfaces, and
   visual audits pass. Package preparation alone must continue to expose no
   formation transaction.
7. Add decisions or missions for post-formation integration only after the
   family policy specifies whether members remain sovereign, which staged
   values move, and what failure means. Do not create a generic integration
   substitute in this tranche.

## Blockers and unsupported or unresolved fields

1. **Exact members are missing.** The family matrix provides names and broad
   regional direction, not exact original tags, package ids, or generation
   bindings. A member predicate cannot be safely written.
2. **Exact territory is missing.** “Member capitals, rail or port links” and
   “regional capitals and caravan corridors” do not identify state ids,
   ownership versus control rules, exclusions, or capital alternatives.
3. **Carrier scope is incomplete.** DOX and SOK are package carriers, but the
   accepted sources do not say whether other fully attested region-09 packages
   may carry FORM-24 or FORM-25. Do not broaden carrier eligibility.
4. **FORM-25 method mapping is incomplete.** The profile mask allows methods
   1, 2, and 8, while the package language says religious, federal, or
   defensive. The existing package trigger excludes Frontier Command. This
   needs an explicit decision before a method-policy trigger is authored.
5. **Identity packages are absent.** `WFX` and `SFX` were only collision-audit
   candidates. No final country/cosmetic identity, flags, localisation, or
   reviewed identity adapter is admitted.
6. **Member policy is absent.** The generic registry requires a separate
   member-policy audit. The broad post-formation descriptions do not authorize
   annexation, subject creation, blanket cores, or origin ending. No adapter
   should guess whether any consenting member is autonomous or fully
   integrated.
7. **General-registry wiring is out of scope here.** The task explicitly
   excludes edits to `006_independence_wave_formable_registry_effects.txt` and
   `006_independence_wave_formable_registry_triggers.txt`. Without those
   branches, package-local helpers cannot be an executable end-to-end path.
8. **Static-token fields remain constrained.** `set_cosmetic_tag` requires a
   concrete token. It cannot be made dynamic with a numeric script constant.
   If a future identity adapter needs dynamic injection, use the existing
   meta-effect pattern only after the final tag is approved.

## Read-only inspection and validation

Required offline wiki pages were loaded before source inspection, including
Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On
actions, Event modding, Decision modding, Idea modding, AI modding, Country
creation, and Cosmetic tag modding. Vanilla documentation was loaded for
script constants, effects, triggers, modifiers, and script concepts. The
relevant event-target, cosmetic-tag, transfer-state, meta-effect, and
scripted-trigger sections were checked against the existing adapters.

Read-only HOI4 MCP inspection was performed:

- Map inspection for states 274 and 902 completed with valid map, state,
  network, adjacency, and locator checks. Artifact:
  `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e55b5ed5963bbd66de536f7cdd5a17bbdc79c4322a63791b0339935e84f7e57a/2b4b287734074d67f657b79725e94b52ec49b73dfe73c08bcc3274e20fd3b820/map-inspect.fdb4a1d43f524be4.json`
- Focus inspection of the shared Event-006 tree completed. The current MCP
  source inventory still reports the pre-existing 176-node tree and omits
  the standalone IW-093/IW-098 focus source, so no layout or node-coverage
  claim is made for this package. Artifact:
  `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/392f4e1c787a3482a16375f86427e6e068e8d67f6ffadcba5538105428b77813/27601de4e1866694338f3b5a92c45d086b4b7976b59d79ce0955d28e20819e/focus-inspect.13528ac5e5caabc7.json`

No source patch, game load, save scenario, formable transaction, or runtime
commit validation was run because the accepted contract is incomplete and no
safe executable linkage can be wired inside the assigned file boundary.

## Parent follow-up required

Before implementation, promote an exact FORM-24/25 contract into the accepted
specs. It must list carrier eligibility, every member tag and package id,
anchor states and control rules, method and consent policy, final X-ending
identity tags, flags, member sovereignty or integration behavior, capital and
core policy, and cleanup receipts. Then the parent can add the general-registry
branches and request a second, patch-capable architecture pass for the
package-local helpers described above.

No simplification was introduced. The packages remain fail-closed as required.
