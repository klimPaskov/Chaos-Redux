# Generic detention activation: exact-cost reconciliation

Disposition: implemented in current package source and bounded source tests; native cost tooltip, AI eligibility and click/debit behavior remain unresolved.

The retained `generic_activate_detention_network` order quotes 35 political power through the native decision field and 5,000 manpower, 10 command power and 180 support equipment through its custom-cost row.
Before this correction, the custom-cost trigger, decision availability, Ledger action and AI site-cap flag used strict `>` for at least one of those three resources, rejecting stock exactly equal to a debit.
The shared `camp_rework_generic_activation_resources_ready` trigger now uses inclusive `NOT (< quote)` checks for those three resources.
Both decision gates and the Ledger action call that helper; the AI site-cap calculation uses the matching inclusive manpower threshold, leaving the decision to check its command and support requirements.
The existing activation effect still debits those same three constants once after an accepted action; this patch adds no purchase or resource grant.
The legacy Ledger activation quote now colors only an insufficient resource red at equality boundaries, and the native decision's blocked custom-cost row uses the same three resource-specific getters rather than coloring every cost red.
The custom-cost hover key states the current four-part quote, controlled-location requirement and ongoing consequences without adding a persistent price grid.
The separate evidence action retains its previous manpower status getter, so the activation color change does not misdescribe that different gate.

## Source identities and test scope

- Frozen pre-edit decision, effects and trigger copies are in `ai_evidence/generic_activation_decisions_before_2026-09-27.txt`, `generic_activation_effects_before_2026-09-27.txt` and `generic_activation_triggers_before_2026-09-27.txt`, with raw SHA-256 values `a40e04371b4b90817e8ca6ecdbaaec656798a6e9ae5b3cf5f38d2a688e830704`, `d0e09a73da864f651be7515cd7b8e6f46fa9296cdd4cde3b50ca0938be613f33` and `45dc4f5633e3166cb11da295a216fee920c463dd90649a640c5321aa3aeb1100`.
- Current direct decision `common/decisions/camp_repression_generic_decisions.txt` has raw SHA-256 `fe36f6e1081c3f01c6bc7de548d2050aa6697860a827a060610bb9e476eec7e1` after a subsequent AI cap-weight ordering edit; the exact-cost comparison audited its earlier post-cost hash `6d201ec4c075a3c321195e56322024845239d006a069edc59f6f195ee2d58601`.
- Current Ledger and AI-cap effects `common/scripted_effects/camp_repression_rework_effects.txt` have raw SHA-256 `123e0be345a8aa9ce03f8d2f12f0e355477b3e4c8c854e0be6cde2ba091b89ec`.
- Current shared trigger `common/scripted_triggers/camp_repression_rework_triggers.txt` has raw SHA-256 `8670e2237c7dbe8ea5b2502379a8e972f9d8bce39f83a99ae8d9aa5f04141ae8`.
- Current scripted UI cost text `common/scripted_localisation/camp_repression_ui_scripted_localisation.txt` has raw SHA-256 `65d26746107cc0b383132e8673abe9120d9da9b2d01f4b880ff8f28cef6c0409`; the English UI and decision strings have raw SHA-256 `22f6e9a0eb6450e65fe8a4541de1efecf668c5d97a35a9ed2f93b0072d296e65` and `7cf51585b05b5fd75a245621fa9d75ef0c63492895447fe6c1e0e453be2161c9`.

The 34-group foundation source suite executes the actual shared trigger in a restricted evaluator: all three resources at their exact quotes pass, and one unit short in each fails.
It also checks that the direct decision, Ledger action and AI-cap source use the corrected gates, and evaluates each activation display getter at exact and one-short stocks.
The touched Clausewitz files parse under the package parser, and the scoped localisation audit found the current quote, red/yellow equality behavior, texticons and tooltip key aligned, with both edited English files retaining UTF-8 BOM and no missing or duplicate scoped keys.
These are source and mocked-primitive checks, not a live HOI4 decision or scripted GUI transaction.

## References and remaining evidence

The root's connected `hoi4.reference_context`, `reference_search`, `reference_read` and `source_lookup` routes were not exposed, so pertinent local sections were read directly.
Offline `Decision modding - Hearts of Iron 4 Wiki.md` lines 305–325, SHA-256 `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, documents custom-cost normal, blocked and hover localisation keys.
Installed `common/decisions/_documentation.md` lines 1–46, SHA-256 `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, documents decision availability and targeted-scope refresh.
Installed vanilla `common/decisions/AUS.txt` lines 1638–1646, SHA-256 `619f5e7d922c7900c2cfe31b54dc37d32b7583dedae9f33336a430d753362ef0`, uses a native political-power cost with a custom equipment cost trigger and text.
The baseline weighted inspection/evaluation for `generic_activate_detention_network` used four synthetic AFG wartime equality/above-cost scenarios under hash `a595fea8331a48c074d3348c67b4168e7ba14953817fad15496b49c14e6fb2f2` and returned partial, score-only evidence with 52 unresolved items.
A [matched post-edit probability comparison](ai_evidence/generic_activation_exact_cost_probability_2026-09-27.md) returned no modeled score changes but partial eligibility with 53 unresolved items in the same four synthetic cases; neither that result nor a raw willingness score is an exact AI click probability.
The subsequent zero-factor source-order correction has its separate [under/over-cap comparison](ai_evidence/generic_activation_cap_order_2026-09-27.md), which remained partial and did not resolve a numeric raw-score delta.
The scoped read-only decision inspection returned `DECISION_ANALYZED_PARTIAL` for two declared scenarios at revision prefix `e7b497fc`, [artifact](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7dd6f5ba4c616a490600741b5e06b8920680b72b0b8ec2d4300648dc647fa0bb/3839a77953fc74935b132e8abed0695298802e7b798dd4365135b55c7b85769a/decision-f751b93fd7d90434ff92c054.json); it did not establish runtime equality behavior.
The related [GUI inspection](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8a498dad670253600f91c6d129ea07c480774318ee9eae811fcd7cd48c39ce01/755ade6a2da0901cd2d991023f63d8e94fb2e2a38c7419af444780c9cb60d88b/gui-inspect.0bb5cbe1b4468bd0.json) used a generated default `repression_ledger_window` scenario with resource primitives but no explicit panel, cost consumer or route state; it is rejected as visual proof for the legacy activation cost.
The matching render did not complete within the bounded attempt, so the native blocked-cost row's visual fit remains unverified.
