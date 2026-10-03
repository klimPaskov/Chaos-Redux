# Bounded reusable skill maintenance

Disposition: implemented skill guidance, parent-reviewed for the three authored clarifications.
Acceptance basis: the explicit bounded maintenance request to capture three reusable source-contract lessons without event-specific skill content.
The parent owns the shared-tree commit and the parent feature's completion claim.

## Exact files changed

- `.agents\skills\chaos-redux-events\SKILL.md`: two short paragraphs after the existing country activation, actor/receipt identity, and callback coalescing guidance.
- `.agents\skills\chaos-redux-decisions-missions\SKILL.md`: three sentences extending the existing custom-cost affordability and payment paragraph.
- `docs\plans\029_riches_found_plans\subagent_handoffs\skill_maintenance_2026_10_03.md`: this handoff.

No new skill or supporting reference was needed.
The events skill already owns callback scope and actor/receipt validation, while the decisions skill already owns shared inclusive affordability, payment, and display precision.
Those existing rules were retained rather than restated.
The skill-creator and chaos-redux-subagents contracts were used and left unchanged.
No routing changed, so the parent needs no AGENTS.md or subagent-skill routing update.

## Reusable changes and inspected precedent

The event guidance makes independent state review/growth dates authoritative when bounded country callbacks service state-owned records.
Controller cycling and duplicate callbacks cannot count as extra elapsed time.
Source precedent: `common\scripted_effects\029_riches_found_effects.txt`, lines 278-279 initialize both dates, `common\scripted_effects\029_riches_found_exposure_effects.txt`, lines 11-19 gate exposure by its state date, and `common\scripted_effects\029_riches_found_maintenance_effects.txt`, lines 40-47 gate pressure growth separately.
These are inspected source control-flow contracts, not executed engine results.

The second event paragraph covers terminal records whose maintenance ends before delayed outcome verification is due.
It requires an owner-scoped one-time callback, a persistent due date, consumption of the pending receipt before verification, preservation of the original date across narrow controller changes, and record/actor revalidation with existing personal-route invalidation preserved.
Source precedent: `common\scripted_effects\029_riches_found_effects.txt`, lines 2114-2127 schedule the verification and lines 2257-2269 preserve the date and reschedule the remaining delay.
`events\029_riches_found_verification.txt`, lines 16-30 guard delivery by registration, pending receipt, due date, and controller existence, then consume the receipt before refreshing verification.
`common\scripted_effects\029_riches_found_achievement_effects.txt`, lines 173-198 and 224-247 check the recorded actor against the controller and the route-specific deadline.
The guidance adds no periodic world scan.

The payment clarification requires per-resource display/colour selectors to call the same authoritative inclusive components used by availability and the native custom-cost gate, preserving payer, quote, units, and equipment-token identity.
Source precedent: `common\scripted_triggers\029_riches_found_cost_triggers.txt`, lines 15-85 define inclusive resource predicates and lines 89-93 compose the survey gate.
`common\decisions\029_riches_found_decisions.txt`, lines 47-49 and 71-73 invoke that same composite from availability and custom cost.
`common\scripted_localisation\029_riches_found_scripted_localisation.txt`, lines 332-335 call the same manpower component for the colour selection.
The added boundary-review rule covers reserves below, equal to, and above the quote without duplicating resource predicates.

## Validation and limits

Both updated skills passed the official skill-creator `quick_validate.py` check.
The decisions-skill check initially hit the Windows default cp1252 decoder, then passed with `python -X utf8`.
Comparing the final skill text with the captured pre-edit text after removing only these additions showed all prior text preserved, including other agents' existing changes.
A later reread found a concurrent Script Constants guidance insertion in the events skill, which was preserved and is outside this handoff's authored delta.
The added guidance comprises two event paragraphs and one extension to an existing payment paragraph, with no Event 029 identifiers, tuning, design, or task history in the additions.

No gameplay scenario, source interpreter test, MCP inspection/render/comparison, or native engine execution was run for this documentation-only patch.
The exposed reference routes were identified, but service health and evidence delivery were not tested.
The inspected source logically supports the reusable contracts, while delayed callback delivery, event-target lifetime, date arithmetic, persistence, and native display behavior retain the parent's engine-proof limits.
The parent-reported engine-proof blocker remains unresolved, and this handoff does not claim an MCP capture or clear that blocker.

No gameplay, assets, localisation, workbook, Git index, or commit was changed by this maintenance work.
No game was launched.
No simplifications or omissions were made within the bounded skill request.
The parent should review these three additions, retain its existing engine blocker in the feature report, and include only the approved skill delta in its shared-tree commit.
