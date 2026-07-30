# Event 012 W2-W4 runtime integration handoff

Status: implementation-ready runtime wiring completed on 2026-07-30.

Scope: shared constants, package polity decisions, grounded sponsorship actions and missions, bounded on-actions, and the existing package installer/cleanup call sites. The isolated W2, W3, and W4 effect, trigger, event, and localisation files remain the source of truth for their protocol kernels.

## Files changed

- `common/script_constants/012_africa_world_order_constants.txt`
- `common/decisions/012_africa_decisions.txt`
- `common/on_actions/012_africa_world_order_on_actions.txt`
- `common/scripted_effects/012_africa_world_order_effects.txt`

No localisation, event, focus, country, tag, model, or asset files were edited.

## Runtime integration

### W2 package polity boards

The existing `africa_world_polity_actions_category` now exposes the six Crossroads and Europe boards, three Asia boards, three North America boards, three South America boards, and three Oceania boards. Each board uses its handoff's package/opening flags, action locks, exact helper, protocol cost, and AI weight. South America and Oceania use normal decision costs without the missing `africa_world_package_action_cost` custom-cost key; their scripted effects still own the action lock and effect tooltip.

### W3 sponsorship modes

`africa_world_order_actions_category` now contains four grounded host offer actions with custom-cost checks, four mode fulfil actions, four mode missions, and bounded renegotiation/refusal review actions. The generic sponsorship action and mission are hidden from grounded mode packages and remain migration-only. The package installer activates only the matching grounded mission (`diplomatic`, `material`, `military`, or `ideological`) and falls back to the legacy mission only when no grounded mode is present.

### W4 union, war, and terminal surfaces

The polity category now exposes the bilateral union opener and clause sequence, three explicit continental-war goal variants, bounded registered-war ledger actions, defeated-package review, and terminal unanimous/last-standing proof and handoff actions. Goal variants reuse the existing parent decision localisation while retaining distinct IDs and call their corresponding prepare helper. Successor, exile, and breakup decisions now call the W4 wrappers so the accepted `africa_world_commit_package_successor` transfer remains the sole state-transfer implementation.

### On-actions and cleanup

`on_war_relation_added` has a bounded military sponsorship hook and an explicit W4 registered-pair witness that checks attacker/defender event-target equality without scanning. `on_capitulation` opens the W4 defeated review once for a registered defender package actor. `on_peace` checks the registered pair and only emits `.734` or calls war cleanup after the attacker and defender are no longer at war. No recurring world iteration was added.

The existing package loss, exile, breakup, and terminal-resolution helpers call `africa_world_sponsorship_cleanup_active_state` when active sponsorship state is present. Cleanup therefore removes active mode decisions, bounded host-array membership, and a military guarantee only when its guarantee flag exists.

## Constants added

`africa_world_package_protocol` now contains routine/negotiated/intervention/major/crisis/ratification/lifecycle costs, union/war/terminal costs, timing aliases, and voluntary quorum bands. The new `africa_world_sponsorship_mode` category contains grounded enum values, offer costs, mode gains/losses, AI tuning, and the 180-day obligation. Nested `africa_world_union_protocol`, `africa_world_war_protocol`, and `africa_world_terminal_protocol` categories provide the status, approval, goal, strain, support, and terminal-proof values consumed by the isolated W4 files.

## Validation

- Balanced braces match in all four changed script files.
- New constants referenced by W2/W3/W4 decisions and isolated effect/trigger files were cross-checked against the shared constants file.
- New decision helper and trigger identifiers were cross-checked against the corresponding scripted effect/trigger definitions.
- New and reused decision localisation keys and custom tooltip/cost keys were checked against the W2/W3/W4 localisation files.
- No unsupported `<=` or `>=` operators were introduced.
- Read-only `hoi4.event_inspect` scan of `africa_world_package.700` completed with no blocking diagnostic; the workspace-wide projection remained partial with deferred diagnostics.

## Risks and limitations

- The W4 `on_war_relation_added` branch marks the already-registered attacker/defender pair active; it deliberately does not call the war opener or re-dispatch partner events, avoiding duplicate declarations when the callback follows `declare_war_on`.
- The new W4 goal variants share `africa_world_prepare_continental_war` name/description localisation because no variant-specific decision keys were supplied. Their IDs and effects remain distinct.
- Live Hearts of Iron IV execution and consumer validation were not run, per repository policy.
- No fallback mechanics, world scans, identity changes, super-event readiness setters, or duplicated stockpile effects were added.
