---
description: Use when creating, editing, auditing, or scripting Chaos Redux ideas, national spirits, hidden ideas and test-country carriers, laws, advisor or designer ideas, dynamic modifiers, static or custom modifiers, timed ideas, the cost-modifier framework, Chaos Meter tier scaling, or modifier tooltips and localisation.
---

### In Chaos Redux Ideas and Modifiers

Before authoring reusable scripted effects or triggers, read and follow the [helper argument contract](../chaos-redux-events/references/scripted-systems-and-country-integration.md#duration-fields-and-constants) and [caller-owned temporary-output contract](../chaos-redux-events/references/scripted-systems-and-country-integration.md#helper-output-lifetime), including supported variable/token inputs, meta substitutions, and output initialization at each call boundary.

### In Contents

- Chaos Redux specifics

### In Dynamic modifiers

Chaos Redux wording differs from the kit:

```
add_dynamic_modifier = { modifier = my_dynamic_modifier }
add_dynamic_modifier = { modifier = my_dynamic_modifier days = 30 }                  # temporary, may be a variable
add_dynamic_modifier = { modifier = my_dynamic_modifier scope = POL }                # applied here, bound to POL; see state-beneficiary rule below
remove_dynamic_modifier = { modifier = my_dynamic_modifier }                          # repeat scope = if used on add
force_update_dynamic_modifier = yes                                                   # refresh now
has_dynamic_modifier = my_dynamic_modifier                                            # or { modifier = x scope = GER }
```

- Daily refresh: at the start of each day every variable-valued modifier resets to 0, then dynamic modifiers evaluate in the order they were added, each treated as 0 until its variables resolve. Changes take effect at most one day later unless you call `force_update_dynamic_modifier = yes` in the same scope. Re-adding an existing binding with the same holder, id, and optional scope updates its timer instead of stacking a second copy. (Chaos Redux wording differs from the kit)

- A state-side `add_dynamic_modifier = { modifier = my_dynamic_modifier scope = GER }` restricts the beneficiary to GER; it does not move the holder off the state (`GAME/documentation/effects_documentation.md`, lines 1153–1173).
  For country-bound views of state data, anchor values to `ROOT.my_state_variable` and state conditions in `enable` / `remove_trigger` to `ROOT = { ... }`, since the optional scope changes the default variable base while `ROOT` remains the containing effect scope (`GAME/common/dynamic_modifiers/0_dynamic_modifiers.txt`, lines 19–26; `WIKI/Modifiers`, lines 149–181).
  Compute severity and duration once in the source state, then bind eligible country views to those results; do not repeat the arithmetic for each beneficiary.
- Match holder, modifier id, and optional `scope` in every add, presence check, and removal (`GAME/documentation/triggers_documentation.md`, lines 3775–3794; `effects_documentation.md`, lines 5978–5991).
  The documented targeting supports intended keying by distinct bound scopes; source review alone does not establish that same-id bindings coexist in the running engine.
  Keep that distinction in the handoff without making user game testing a completion gate.
- Binding lifecycle includes country creation, release, retirement, and changes of eligibility, as well as state cleanup and expiry; register newly eligible countries through the owning lifecycle path and remove stale bindings with the original scope.
  When registration uses a country flag receipt, set and test `my_flag_@THIS` in that country's scope so a copied receipt for another tag does not suppress registration of a released or cloned tag (`WIKI/Data structures`, line 125, targeted flags).

### In Chaos Redux specifics

The `CLAUDE.md` coding, constants, dynamic-effect, and localisation rules apply and are not repeated here, and no world-iterating hook may refresh ideas or modifiers; refresh from the effect that changes the underlying variable. (Chaos Redux wording differs from the kit)

**Where Chaos Redux ideas and modifiers live**

- `common/ideas/<owner>_ideas.txt` and `common/dynamic_modifiers/<owner>_*modifiers.txt` hold one file per event or system. Timed response ideas such as the condemnation responses (`common/ideas/condemnation_sanctions_ideas.txt`) pair with scalable dynamic modifiers (`common/dynamic_modifiers/condemnation_sanctions_dynamic_modifiers.txt`).
- Chaos dynamic modifiers read their tuning with `constant:category.key` in the modifier fields (see `famine_state_modifiers.txt`), carry an `icon = GFX_...` sprite registered in an `interface/*.gfx` file, and switch on a flag through `enable` with a matching `remove_trigger`. Idea `modifier` blocks accept literals, so a tunable idea value either becomes a dynamic modifier fed from a constant or repeats a literal documented once in the file header.
- State modifier families (`famine_state_*`, `migration_state_*`) are removed together and re-added by the refresh effect, so a stage change or cleanup never leaves a stale family.

**Rules that recur**

1. Hidden-idea carriers for test-country registration are modifier-free `hidden_ideas` entries whose id equals the package setup effect name before `_apply` (`common/ideas/012_africa_gods_cxt_extension_ideas.txt` is the pattern). They are tokens, never added to a country, and need no modifiers, localisation, or icon. Registration is in `docs/testing/chaosx_test_country.md`.
2. Chaos scaling reads the Chaos Meter tier constants (`constant:chaos_meter_tier_range.tier_0` through `tier_final`, ids in `chaos_meter_tier_id`) from `common/script_constants/chaos_meter_constants.txt`; do not hardcode a tier boundary. Grants go through `add_chaos_meter_value` with the temporary `chaos_change` and a history reason from `chaos_meter_history_reason`.
3. A price change on an ordinary payable cost goes through the universal discounted-cost framework (`universal_cost_quote_exact` and the register, pay, record, refund, settle helpers) so the displayed price, paid price, and refund agree; do not approximate it with a cost modifier idea (`docs/systems/universal_cost_modifier.md`).
4. Equipment bonuses carried by ideas name ids that must exist in `script_enum_equipment_bonus_type` (`chaos-redux-equipment`).
5. MTTH values that feed a modifier come from `chaos-redux-mtth`; a decision that grants or swaps an idea follows `chaos-redux-decisions-missions`. (Chaos Redux wording differs from the kit)
