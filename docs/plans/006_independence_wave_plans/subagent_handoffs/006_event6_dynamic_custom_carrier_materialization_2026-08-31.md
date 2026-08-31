# Event 006 dynamic custom-carrier materialization

Date: 2026-08-31 (Europe/Kyiv).

Owner: `/root`.

## Scope and disposition

The standalone Event 006 execution path now materializes the nine centrally admitted custom X-tag carriers (`AFX`, `AGX`, `AJX`, `ARX`, `ASX`, `AXX`, `BAX`, `BBX`, and `HBX`) when their frozen plan selects an absent tag. These carriers use shared country definitions but have no historical state cores, so the ordinary `release = PREV` path can leave the selected country absent and the later state-transfer and package-setup passes with no live target. This was the source-level failure behind the reported event-triggered no-country result.

The fix is limited to `independence_wave_release_one_frozen_country`. Inside the exact `every_possible_country` absent-candidate scope, each custom carrier uses the documented `create_dynamic_country` template path with a literal `original_tag`, `copy_tag = THIS`, and `reserve_dynamic_country = yes`, then saves the resulting live scope as `independence_wave_execution_country`. Vanilla carriers retain the existing former-host `release = PREV` and autonomy cleanup path, with an in-scope target rebind after release. A second frozen-plan core pass runs after materialization so dynamic carriers receive the exact planned cores before masked-core restoration and state transfer.

No admission, reservation, automatic count ladder, package attestation, pre-event category, pressure, mission, queue, or decision-cost surface changed. Dormant startup shells continue through their existing state-transfer formation path.

## Changed source

`common/scripted_effects/006_independence_wave_execution_effects.txt` in `independence_wave_release_one_frozen_country`:

- Added explicit dynamic-country branches for the nine custom carriers listed above.
- Kept the supported candidate-scope/former-host `release = PREV` fallback for vanilla carriers.
- Added the post-materialization frozen-plan core restoration pass.

The Fallout fracture implementation in `common/scripted_effects/fallout_consolidated_effects.txt` uses the same literal-tag, `copy_tag = THIS`, reserved dynamic-country pattern. The offline wiki and installed vanilla documentation confirm that `release` only cores states already associated with the released tag, while `create_dynamic_country` creates a dynamic country from an existing country template and can be used from a country scope.

## Validation and evidence

Focused validators pass on the current source:

- `python -B .tools/audit_event6_allocator.py --strict`
- `python -B .tools/audit_event6_country_api.py --strict`
- `python -B .tools/audit_event6_flags.py --strict`

The callable Event MCP inspect route returned a source-linked partial lint artifact with `MCP_INLINE_FILES_TRUNCATED`; it did not provide helper-level execution or live save/load evidence. No Hearts of Iron IV process was launched, so this handoff does not claim live event semantics.

## Remaining limits

The broader Event 006 package boundary remains HOLD / PARTIAL at 32 content attestations, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows. Central package admission, typed probability comparison, and live release/save-load receipts remain separate acceptance work. The Event 021 adapter registry still contains its own raw release branches and was not widened by this execution-only repair.

No unapproved fallback or simplification was introduced.
