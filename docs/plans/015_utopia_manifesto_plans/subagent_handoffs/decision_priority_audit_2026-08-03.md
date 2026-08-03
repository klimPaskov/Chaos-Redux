# Event 015 Decision Priority Audit Handoff

## Scope

Audited `common/decisions/categories/015_utopia_manifesto_categories.txt`, `common/decisions/015_utopia_manifesto_decisions.txt`, the Event 015 decision constants, and Event 015 decision localisation after the category-priority update.

## Changed files

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/decision_priority_audit_2026-08-03.md`

## Changed identifiers

- `decision_utopia_repeal_the_founding_charter`
- `decision_utopia_add_a_sunset_clause`

## Before and after behavior

The two decisions' custom-cost gates used `check_variable` with `var = stability`.

`check_variable` is documented for script variables, while `has_stability` is the documented country-stability trigger.

Both gates now use `NOT = { has_stability < constant:utopia_manifesto_decision_cost.stability_* }`.

The repeal action therefore requires at least 5% Stability before it can spend the localized 5% Stability cost, 100 Support Equipment, and 10 Trains.

The sunset-clause action therefore requires at least 2% Stability before it can spend the localized 2% Stability cost.

No duration, outcome, AI, cleanup, priority, helper, or localisation identifier was renamed.

## Audit evidence

- The centralized nine-entry file-scoped priority table assigns 1100 through 1092 in display order, and every Event 015 category consumes exactly one table entry.
- The highest resolved priority in every other category file is 1000 in `common/decisions/categories/chaosx_decisions_categories.txt`, leaving Event 015's lowest category 92 points above it.
- The 145 direct Event 015 decision blocks include 40 missions across all nine categories.
- All 40 missions have dynamic timeout variables, `activation`, `available`, `cancel_trigger`, `cancel_effect`, and `timeout_effect` branches.
- The mission lifecycle calls reference 62 named Event 015 helpers, all defined in Event 015 scripted-effect files.
- No mission uses a literal timeout, and the system uses 20 duration variables backed by the decision-duration constants and preparation helpers.
- All 105 non-mission decision blocks with a completion action have `ai_will_do` coverage.
- Every one of the 54 targeted decision or mission blocks has a `target_trigger`, and none enables `target_non_existing`.
- All nine categories have ledger and phase or route visibility gates.
- All 145 decision and mission title and description keys resolve across the nine Event 015 localisation files.
- All 84 custom-cost keys have title, blocked, and tooltip variants, and all 144 custom-effect tooltips resolve.

## MCP evidence

- `hoi4.probability_inspect` found 105 Event 015 decision AI surfaces with no diagnostics or unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1c6fbfe4b06de912f14fb03e8d73c0bc428ea525a46a9378065bd8ad7516adc/c30f296581fef41dd3181245ccd96dcf474095d023a69d701fa554f174022330/probability-inspect-ad71fa077045.json`.
- `hoi4.gui_inspect` and `hoi4.gui_render` covered the ledger category window `utopia_manifesto_ledger_container` under the default scenario. The rendered comparison reports no source-presentation delta. GUI artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e1cee3de4321065991f357f1af9c56fbb4363d42c1bfef08870c38274fa7114a/10e0510272dc23b3a5ced320bbed3b6d0af063c8ef02f5f4f3c31a7107293d45/utopia_manifesto_ledger_container-full.png`.

## Validation not performed

No live game session was launched.

The AI inspector is structural rather than a campaign-state evaluation, so its candidate pool is incomplete for a full balance ranking.

The GUI tool reported global repository diagnostics and unresolved offline-fidelity elements, but none was attributed to the Event 015 category-priority change. No GUI source was changed in this audit.

## Remaining risks

The Event 015 priority table uses file-scoped macros because the category priority field is static. It is centralized and complete within the file, but any future category inserted above or between these categories must be added to the same table intentionally.

No broad design gap or plan handoff was created.
