---
name: chaos-redux-mtth
description: Define and use HOI4 MTTH variables safely (base/modifiers, file-scoped constants, and mtth:entry usage in set_variable/set_temp_variable) with guidance for minimizing ai_will_do clutter.
---

# Chaos Redux MTTH Variables

## Scope and references

Use MTTH variables to compute a value from a base plus modifiers, then inject that value into other logic.

Read first to see how Chaos Redux already implements them:

- `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/mtth/chaosx_mtth_variables.txt`

## Defining an MTTH entry

Create entries in `common/mtth/*.txt`:

```
example_mtth_value = {
	base = 50

	modifier = {
		factor = 0.8
		tag = GER
	}
	modifier = {
		add = 25
		has_war = yes
	}
}
```

Notes:

- `base` is the starting value.
- `modifier` blocks use `factor` or `add` and standard triggers.

## Using an MTTH entry

Vanilla example pattern:

```
set_variable = { my_value = mtth:example_mtth_value }
```

Typical usage:

- `set_variable` or `set_temp_variable` to store the computed MTTH value.
- Use the variable later (`add = temp`, `check_variable = { temp > 1 }`, etc.).

## AI weights with MTTH

To reduce `ai_will_do` clutter, compute the full weight in MTTH and inject it:

```
ai_will_do = {
	factor = 0
	modifier = {
		set_temp_variable = { temp = mtth:chem_ai_weight }
		add = temp
	}
}
```

## Scenario analysis

Route MTTH timing and MTTH-backed AI-weight audits through `chaosx_ai_probability_auditor` for one bounded pass. Prefer `hoi4.probability_inspect` and targeted evaluation/comparison when supported; after the AGENTS.md retry limit, read real MTTH entries, modifiers, helpers, constants, and eligibility and evaluate named representative source scenarios. Preserve before/after source and matching scenarios when weights change. Use sweeps or simulation only for an actual threshold or uncertain-input question. Supply scheduled state changes for timing questions; claim cumulative timing only from a verified game-version adapter, label exact/bounded/sampled/score-only conclusions, and report unsupported timing as a limitation without blocking documented implementation. The auditor remains read-only and does not choose balance targets.
