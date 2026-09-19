# Event 006 Transcaucasus cost-localisation compaction — 2026-09-19

## Disposition

Implemented a narrow player-facing localisation repair for the three four-resource Transcaucasus security projects. Mechanics, affordability predicates, payment effects, AI hints, decision IDs, and the absolute no-pre-event gate are unchanged. This is not a whole-event completion claim.

## Changed surface

`localisation/english/006_independence_wave_transcaucasus_l_english.yml` now keeps the normal inline rows for `independence_wave_cost_iw070_garrison`, `independence_wave_cost_iw071_command`, and `independence_wave_cost_iw072_oil` to three visible resource groups: command power, infantry equipment, and support equipment. The manpower charge remains explicit in each `_tooltip` row, which now expands the complete four-group payment. The `_blocked` rows show all four groups in red so an unaffordable manpower, infantry, or support requirement cannot disappear from the blocked state.

The four-group payment remains sourced from the existing constants and helpers. IW-070 still pays the standard security manpower/infantry/support bundle plus its ARM-specific command-power, infantry, and support additions; IW-071 and IW-072 retain their existing corresponding bundles. No cost was removed, merged mechanically, or retuned.

## Evidence and limits

- Vanilla Decision modding documentation confirms that `custom_cost_text` selects the normal key, `_blocked` when the shared `custom_cost_trigger` fails, and `_tooltip` on hover.
- The inspected decision definitions continue to use the shared inclusive affordability triggers at `common/decisions/006_independence_wave_transcaucasus_decisions.txt:69-215`.
- Payment effects remain in `common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt:221-297`; no gameplay file changed.
- The normal rows now contain three cost groups, while each tooltip and blocked row contains all four paid groups with the matching texticons.
- No native decision-row render route is exposed in the current HOI4 MCP surface, so native pixel-fit and hover rendering remain unclaimed. The source contract is documented and parser/static checks are the available evidence.

## Remaining blockers

The broader Event 006 route-cost audit still has unresolved native-render evidence for other cost families and the owner-level IW-093/IW-098 100-PP contract. Event 006 remains HOLD / PARTIAL at the current 32 content-attested packages, 29 reservation groups, 40 adapters, and 161 unattested selectable rows.

No fallback, hidden payment, speculative resource merge, or pre-event decision/category surface was introduced.
