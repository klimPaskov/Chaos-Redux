---
description: Define and use HOI4 MTTH variables safely (base/modifiers, file-scoped constants, and mtth:entry usage in set_variable/set_temp_variable) with guidance for minimizing ai_will_do clutter.
---

### In Chaos Redux MTTH Variables

Section heading: Chaos Redux MTTH Variables (Chaos Redux wording differs from the kit)

### In Scope and references

Read first to see how Chaos Redux already implements them:

- `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/common/mtth/chaosx_mtth_variables.txt`

### In Scenario analysis

Route every MTTH timing or MTTH-backed AI-weight audit through `chaosx_ai_probability_auditor`. Begin with `hoi4.probability_inspect` to identify the MTTH entry, modifiers, helpers, and scenario inputs before evaluating timing. Use `hoi4.probability_inspect` for named world states, `hoi4.probability_analyze` (`analysis = sweep`) for thresholds and timing reversals, `hoi4.probability_analyze` (`analysis = simulate`) for declared uncertain inputs, and `hoi4.probability_analyze` (`analysis = compare`) after a patch. Use `hoi4.probability_analyze` (`analysis = render`) for timing-survival, sensitivity, comparison, and unresolved views when visual evidence is clearer. Supply scheduled state changes when conditions vary across the horizon. Accept cumulative timing only from the verified game-version MTTH adapter, and keep exact, bounded, sampled, and unresolved results distinct. The auditor supplies evidence and never chooses the intended timing or writes source. (Chaos Redux wording differs from the kit)
 Apply the AGENTS.md retry limit to unavailable or inconclusive tool checks; keep direct calculations distinct from unsupported game-execution or cumulative-timing claims.
