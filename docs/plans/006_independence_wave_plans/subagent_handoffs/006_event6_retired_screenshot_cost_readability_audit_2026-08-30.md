# Event 006 retired screenshot cost readability audit

Date: 2026-08-30

Mode: bounded localisation audit with no runtime localisation change

## Outcome

The decision shown in the user screenshot belongs to the retired pre-event Independence Wave crisis surface. No current category, mission, decision, cost key, queue, pressure label, or history row consumes that presentation. The screenshot therefore does not identify a live localisation key that can be shortened safely.

The current post-event cost consumers were traced instead. The active shared security-standard cost already uses two compact lines in both normal and blocked states. Its four resource tokens remain manpower, army experience, infantry equipment, and support equipment. The current diplomatic transport selector continues to display one payable convoy-or-train alternative and does not present both transport types as cumulative charges.

No further localisation rewrite was applied. Changing another live cost family based only on a retired screenshot would risk hiding a real payment, a factory reservation, a staged payment, or an alternate transport condition.

## Retired surface evidence

- `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md` defines an intentionally empty pre-event state and forbids calls to the old crisis category, mission, cost, queue, and history keys.
- `common/scripted_triggers/006_independence_wave_compatibility_triggers.txt` retains only hard-disabled parser-compatibility crisis helpers.
- `common/scripted_effects/006_independence_wave_compatibility_effects.txt` retains inert cleanup stubs only.
- `events/006_independence_wave.txt` clears stale crisis flags in the retired callback and does not open a player-facing pre-event surface.
- `.tools/audit_event6_allocator.py` reports the pre-event crisis surface retired with no category, mission, cost, or queue.

## Active cost readability review

### Missing keys

None. The current Event 006 decision sources contain 699 `custom_cost_text` consumers using 192 unique cost keys. Every consumer resolves its base, `_tooltip`, and `_blocked` keys.

### Duplicate keys

None. The 37 dedicated Event 006 English localisation files contain 8,813 unique parsed keys.

### Scripted localisation issues

None in the inspected decision-cost path. The normal and blocked diplomatic-standard transport selectors retain matching convoy, train, and either-resource branches. A repository-wide selector-result check also resolves the four shared scenario intensity labels in `localisation/english/chaosx_gui_l_english.yml`.

### Dynamic text opportunities

No safe opportunity follows from the screenshot. The active transport selector is already dynamic. The provisional-capital cost selector already distinguishes force tier and supplied or isolated capitals. The staged patron-balance cost must retain separate starting and later payments.

### Cross-surface mismatch notes

The screenshot surface is historical and has no current consumer. The active `independence_wave_cost_security_standard` and blocked counterpart preserve the same four resources across their two-line layouts. No trigger, payment effect, reservation, category gate, decision identifier, or AI weight changed in this audit.

Three previously documented cost-budget defects remain outside a readability-only repair. `independence_wave_cost_security_standard_factory` displays five spendable types, while `independence_wave_formable_commit_cost_revolutionary` and `independence_wave_formable_commit_cost_military` each display seven. Localisation must not conceal those payments. The decision owner must simplify the underlying payment designs before their cost strings can meet the four-cost contract.

### File encoding concerns

None. All 37 dedicated Event 006 English localisation files retain UTF-8 BOM.

## Prose-quality findings

- Vagueness: the retired screenshot cannot be mapped to a live key, so no speculative replacement wording was invented.
- Bloat: the active security-standard cost already uses a compact two-line amount-and-icon layout. No additional filler remains on that shared row.
- Obvious explanation: no live cost row tied to the screenshot repeats its decision title or narrates the visible icons.
- Repetition: the active shared normal, tooltip, and blocked cost families retain their established aliases and parity.
- Overcomplication: the remaining five-cost and seven-cost strings reflect gameplay design defects that wording alone cannot repair safely.
- Style-rule repair: no player-facing prose changed. No em dash, sentence semicolon, staged contrast, or implementation-history wording was introduced.

## Sourced quotations

No quote-bearing surface was changed. The Event 006 super-event quotations and all dynamic tokens remain untouched.

## Meaningful validation

- The focused localisation scan found 699 cost consumers, 192 unique cost keys, zero missing cost triplets, zero duplicate Event 006 keys, and zero BOM failures.
- `python -B .tools/audit_event6_allocator.py` passed and confirmed that the retired pre-event crisis exposes no category, mission, cost, or queue.
- `hoi4.event_inspect` lint for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` at revision `269d5c7882f38258729f70240fd9f5547bd66b98751888b3a9ca0e91ca8dc44e`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/245a8e84a526413409877b8ab331e1800c2f0753b97523d09ac2472438323405/8f212383b0751d5a9c1139952f236632f0918fdb1360bd73625c93db7e6b14a5/event-lint-269d5c7882f3.json`.
- `hoi4.event_render` produced a partial Event 006 options manifest at the same revision. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f79d0699403bd048f7269925fb0333070a2cbf547df30b15ae8b34239689a07/98e69d64715a82425535a56aafa40c7aaf9fb74dcb3f1c494d7bb07acc0e422e/event-options-269d5c7882f3-manifest.json`.

The MCP results defer workspace-wide helper and lifecycle projections. They do not render ordinary decision cost rows and are not treated as visual fit evidence.

## Skipped meaningful validation

The installed MCP package exposes no ordinary decision-list or `custom_cost_text` production renderer. Decision-row wrapping, clipping, and overflow therefore remain unverified. Source token checks are not equivalent visual evidence.

No live HOI4 claim is made.

## Changed files and keys

No runtime localisation, scripted localisation, decision, trigger, effect, GUI, asset, workbook, or specification file changed. This handoff is the only added file. No localisation key changed, and no dynamic localisation was added or fixed.

## Unresolved decisions

- A current screenshot or exact live decision identifier is required before another layout rewrite can be tied to a visible defect.
- The five-cost and seven-cost gameplay families require decision-owner simplification rather than a localisation workaround.

## Simplifications, omissions, and blockers

No cost, resource, alternate transport route, reservation, blocked-state token, dynamic value, quotation, or gameplay requirement was simplified or omitted. The only blocker is the absence of a live key for the retired screenshot and the lack of an ordinary decision-cost renderer.
