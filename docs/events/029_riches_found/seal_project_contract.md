# Riches Found evolution sealing projects

This contract covers `decision_riches_found_gold_seal_depths` and `decision_riches_found_demons_permanent_seal`.
The acceptance basis is the human Event 029 implementation goal, Part 3's sealing cost profiles, and Part 4's localized Gold Disease containment and demonic sealing and military-purge routes.
The package remains incomplete; this bounded repair is not acceptance of the full sealing, dynamic-cost, AI, or achievement system.

## Costs and delayed results

| Project | Discrete payment | Capacity commitment | Output consequence |
| --- | --- | --- | --- |
| Gold Disease deep-section seal | 300 manpower and 150 support equipment | Two civilian factories for 60 days | Lower workings remain sealed; stable, controlled upper workings can contribute |
| Demonic permanent seal | 600 manpower and 150 support equipment | Two civilian factories for 90 days | Ordinary mine output ends permanently |

Shared constants own prices and durations.
The file-local capacity alias supplies the native static factory modifier.
The same composite affordability helper is used by availability and the custom cost gate; resource-specific predicates also colour the displayed quote.
Each inline row shows three values, and its full tooltip states the duration and output consequence.
Neither project spends political power or trucks, refunds them, or declares a political-power saving hint.
Counting foregone output, each profile uses four cost types.

Both projects exclude terminal mines at selection.
The delayed result checks the original payer's control, registration, and nonterminal status again.
Gold sealing also rechecks the Gold Disease layer, restricted-access route, and absence of an already completed gold seal.
Demonic sealing also rechecks the demonic layer, cleared district, and absence of an active concession, occupation, or completed demonic seal.
A failed delayed check returns exactly the manpower and support equipment charged by that project, without an output change or a second sealing reward.
Elapsed native factory commitment is opportunity time, not escrowed equipment or buildings, and is not refunded.
These checks do not establish generation-safe callback identity after controller cycling or atomic native factory reservation after a stale click.

## Evacuation, military clearance, and harm

The district-cleared predicate permits either completed evacuation or military purge.
Military clearance is not an evacuation receipt.
The demonic seal reads `riches_found_record_entombment_harm` before terminal mine cleanup, mirroring the ordinary permanent seal.
The existing predicate identifies trapped crews during severe collapse or supernatural crisis when the deposit is not exhausted and neither district nor workforce evacuation is recorded.
Its mine-owned receipt prevents the same entombment from applying twice.
The shared harm transaction requests up to 220 civilian deaths, records deliberate mine violence in Deaths and public responsibility in Condemnation, lowers Local Order by 15 and Revenue Legitimacy by 20, and marks workforce entombment.
The Last Shift's existing eligibility predicate and timer disqualifiers reject entombment and military purge independently.
An exhausted deposit or a completed evacuation does not satisfy the entombment predicate.
The demonic tooltip includes the ordinary seal's explicit human consequences and states that a purge does not evacuate trapped crews.
The demonic AI block mirrors the ordinary permanent seal's existing safety modifiers: `low_factor` for an entombment risk and `never_factor` for that risk under democratic government.
These are configured willingness modifiers, not observed click probabilities or a measured ranking against evacuation and assistance.
The immutable baseline and identical named scenarios are retained for the required probability comparison; an empty adapter result cannot establish balance acceptance.

Gold sealing remains a localized-source containment action rather than an emergency-only action.
Part 4 permits sealing the strongest incident areas while preserving upper workings.
No new minimum-integrity number is inferred from that prose.
Its existing one-time partial-seal guard remains intact, and its tooltip promises production only from stable upper workings, not unrestricted reopening.

## Source and reference evidence

The pre-safety decision bytes are retained at `docs/plans/029_riches_found_plans/evidence/2026_10_08_seal_safety_parent_before/common__decisions__029_riches_found_decisions.txt`, SHA-256 `ae8c42a480a71ccd41ab2553dc324815daadf6496a406f8b530123b5e2ade7b9`.
That snapshot already contains the proposed physical recipes and another owner's wartime-denial gate; it is not the original cost baseline.
The original recipes remain in `evidence/2026_10_07_seal_cost_before/`.
Sibling-file replacement revalidated the target hash and preserved every byte outside the two owned decision blocks and the two owned effect-tooltip lines.

Offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:337-356`, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, distinguishes selection effects, delayed removal, cancellation, and timed modifiers.
Installed `common/decisions/_documentation.md:1-46`, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, documents acting-country and targeted-state scopes.
Installed `documentation/triggers_documentation.md:4827-4842`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, and offline `Triggers - Hearts of Iron 4 Wiki.md:1837`, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, document state flags.
Installed `documentation/effects_documentation.md:1252-1266` and `3320-3326`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, document equipment debit/refund and custom effect tooltips.
Vanilla `common/decisions/AST.txt:2-42`, `AST_union_strike`, is the native timed civilian-factory precedent.
Chaos Redux's ordinary permanent seal is the direct precedent for conditional entombment before terminal cleanup.
`hoi4.source_lookup` read the actual entombment helper at `common/scripted_effects/029_riches_found_harm_effects.txt:193-210`, source-index revision `2bbc7c7345d4a1ccc1eb1444198b552f266bdcf8cf8d99fb78f3e41ac12501c2`, with one complete definition and references deliberately excluded.

The scoped MCP removal snippet returned `SCRIPT_CHECK_PARTIAL`, `valid = null`: native command kinds and declared scopes were checked, six scripted-helper calls remained unresolved, and the equipment argument block was unchecked.
The parent read those helpers and the installed equipment syntax; this does not turn partial static validation into engine evidence.
The previous sealing-cost probability workflow returned `JOB_WORKER_EXIT` for decision comparison and `PROBABILITY_SURFACE_EMPTY` for decision AI; neither establishes eligibility, ranking, or click probability.
The safety follow-up retained exact before/after bytes and the same thirteen scenario IDs, then submitted five probability comparisons, including narrower requests and a logical gameplay path pinned to the snapshots.
None produced a terminal comparison result; neither a score delta nor a comparison pass is claimed.
The typed fixture's `manpower_k = 500` means 500,000 people, not a shortage against the 600-person seal cost; this unit error was corrected in the audit without changing the frozen gameplay source or scenario inputs.
Current bounded decision and probability follow-up evidence belongs in the dated sealing safety handoffs.
The postpatch decision review found no P1 regression in the two decision blocks and traced invalid-result refunds, safe evacuation/exhaustion, purge without evacuation, repeated harm, and Last Shift disqualification.
Its typed Gold scenario resolved the three affordability predicates at two free civilian factories, 0.3k manpower, and 150 support equipment, while actor control, selected-mine scope, the category, and manual payment execution remained unresolved.
The parent treats those funded factories, crews, and tools as the existing concrete engineering-capacity inputs, not an absent resource that should be replaced by a new engineer currency or arbitrary permission flag.
State-specific entrance access, supply, resistance, and native execution of the reservation remain separate requirements.
The review's requests using the category ID as a GUI window produced no native-list visual evidence; they do not establish that a dedicated Event 029 window exists or is required.
No agent launched Hearts of Iron IV.

## Presentation and remaining integration

Consumers remain the ordinary mine-management category, existing deep-section and permanent-seal decision sprites in `interface/029_riches_found.gfx`, and existing civilian-factory, manpower, and support-equipment texticons.
No dedicated GUI, portrait, animation, unit, or new asset family is introduced.
The ongoing visual repair must approve the exact ordinary decision icons independently.

Control of shaft entrances, integrity-dependent success, affected-group resistance, time-scaled evacuation quality, the complete dynamic quote, native callback identity, and current live consumer evidence remain separate acceptance requirements.
The existing `riches_found_state_can_control_access` cannot simply substitute for a closure-project gate because it requires an active mine and excludes closed or collapsed containment targets.
Future integration must preserve severe-collapse sealing and the explicitly harmful alternative, not silently omit either route or relabel a military purge as safe evacuation.
