# Event 006 absent-release target rebind

Date: 2026-08-31 (Europe/Kyiv).

Owner: `/root`.

## Scope and disposition

The Event 006 execution path now rebinds `independence_wave_execution_country` to the current `every_possible_country` candidate immediately after an absent carrier is released. The selected tag is saved before release from the frozen plan, so the later transfer, capital, package setup, final-validation, and instantiated-count checks could otherwise continue through a stale absent-tag target in engines that do not refresh an event-target pointer when the country is created.

The patch is narrow and keeps the accepted vanilla release shape intact: the current candidate is limited to `exists = no` and the exact frozen tag, the former host performs `release = PREV`, and the current candidate then saves itself back to the existing regular event target. Existing dormant shells still skip the no-op release branch and are unaffected.

## Changed source

`common/scripted_effects/006_independence_wave_execution_effects.txt` in `independence_wave_release_one_frozen_country`:

```text
save_event_target_as = independence_wave_execution_country
```

The effect is executed only inside the absent-tag `every_possible_country` branch, after the host release and autonomy cleanup. No package admission, roster fallback, capital-scope use, pre-event surface, count ladder, or central attestation changed.

## Evidence and validation

The offline Paradox wiki and installed vanilla documentation confirm that `every_possible_country` evaluates absent country tags, `release` accepts `PREV`, and `save_event_target_as` saves the current scope for the remainder of the effect chain. The vanilla `13_goe_on_actions.txt` release precedent uses the same candidate-scope/former-host release shape.

Focused Event 006 static validators passed after the patch:

- `python -B .tools/audit_event6_allocator.py`
- `python -B .tools/audit_event6_country_api.py`
- `python -B .tools/audit_event6_flags.py --strict`
- `python -B .tools/audit_event6_form16.py`
- `python -B .tools/audit_event6_scenario_matrix.py`

The maintained result remains 149 publishers, 126 automatic/high-chaos candidates, 138 SCN-008 ranked candidates, 40 runtime adapters, 32 content attestations, 29 compatible groups, exact `3/4/5/7/10` counts, and a retired pre-event surface.

## Remaining limits

The installed callable Event MCP route has only returned source-linked partial graphs for this workspace, and no live Hearts of Iron IV process was launched. Therefore this patch does not claim a live standalone release, save/load success, or engine proof that the event target refresh is required; it isolates the source-level stale-target risk reported by the missing-country symptom without changing the accepted release semantics.

Event 006 remains HOLD / PARTIAL for the broader package boundary. No simplification or unapproved fallback was introduced.
