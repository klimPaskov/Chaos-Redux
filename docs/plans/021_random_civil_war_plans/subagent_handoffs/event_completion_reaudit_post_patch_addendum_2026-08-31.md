# Event 021 Completion Re-audit — Post-patch Addendum

Date: 2026-08-31

Scope: bounded source verification of the Event 006 adapter’s actor-force receipt and opening-log call flow only.

## Verdict

**Verified fixed in current source.**

In `common/scripted_effects/021_random_civil_war_parent_effects.txt`:

- The Event 006 actor captures its post-creation force receipt in actor scope through `event021_parent_capture_actual_actor_force_receipt` at line 2797.
- The adapter now invokes `event021_parent_record_system_log` exactly once, still in actor scope, at line 2816. The former host-scope log invocation is absent.
- Inside `event021_parent_record_system_log`, the actor-owned receipt values are read at lines 1768–1770.
- The helper stores the snapshot on its current actor scope at line 1812 and mirrors that same snapshot to the crisis host or host-country scope at lines 1813–1820.
- The helper performs one immutable Event 021 snapshot append and one shared system-history append at lines 1832–1833.

Therefore the previously reported Event 006 duplicate immutable opening-row defect is corrected at source level: one opening is recorded once from actor scope after actual receipt capture, while the helper mirrors the resulting snapshot to the host.

This bounded verification does not add live HOI4 evidence or alter the other tooling, probability, specialist, catalog, or user-owned acceptance blockers recorded in the final re-audit.
