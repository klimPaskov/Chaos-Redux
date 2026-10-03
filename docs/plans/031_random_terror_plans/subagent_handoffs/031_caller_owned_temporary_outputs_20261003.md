# Event 31 caller-owned temporary outputs

## Disposition and accepted scope

Implemented as a bounded helper-contract hardening within the accepted multi-country wave and manual CXT extension workflow.
The user authorized those systems through the Event 31 coding prompt and AGENTS.md.
No live failure is inferred from this source-level risk, and this repair does not prove the full wave or country-selection transaction.

## Source rule and precedents

The offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, Variable types, lines 435–445, warns that a temporary variable created inside a scripted effect may not survive its return, whereas a value declared before the call can be modified by the helper and retained by its caller.
The wiki SHA-256 revision is `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Installed `documentation/effects_documentation.md`, lines 7820–7840, defines `set_temp_variable`, its any-scope support and value/variable/math-expression forms.
The installed documentation SHA-256 revision is `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Installed vanilla `common/scripted_effects/00_scripted_effects.txt` contains temporary-variable use; the exact caller-owned return-lifetime constraint comes from the cited wiki section, not an invented vanilla guarantee.
The existing Chaos Redux registration helper at `common/scripted_effects/chaosx_test_country_effects.txt`, lines 349–373, explicitly writes a zero/one registration-added output.
The Event 31 wrapper calls that helper and the existing daily fallback then reads its output.

## Changed caller contracts

`random_terror_run_global_wave` now declares `random_terror_wave_target_count` before calling its nested resolver.
The resolver still chooses the configured baseline/evolution count or the existing scenario override, and the loop consumes that caller-owned result.
Configured counts remain 3, 5, 7, 10, 15 and 20.
No ticket weight, selection eligibility, evolution threshold, scenario intensity or pacing callback is changed.

The initialized-country branch of `on_daily_CXT` now declares `chaosx_test_country_extension_registration_added` before calling the Event 31 wrapper and shared registration helper.
A first registration returns one and marks manual synchronization pending; repeat registration returns zero without a new pending write.
An uninitialized CXT does not enter this branch.
This hook grants no content and introduces no whole-world iteration.
The existing startup registration has no output consumer and needs no extra receipt declaration.

## Review and validation limits

The parent reviewed both exact diffs, the single wave-resolver caller, the nested CXT wrapper/helper and the downstream receipt condition.
A source-contract check confirmed all six configured count branches remain present, both declarations precede their respective calls, and the CXT threshold remains greater than zero.
`random_terror_actor_created` is consumed within its own spawning helper, not returned to its callers; no caller declaration was added for that internal scratch value.
These checks are source evidence and do not establish actual affected-country counts, state validity or observed pending-decision behavior.
A narrow installed-documentation reference search for `set_temp_variable` and a reduced event-root lint request were issued; exact outcomes and artifacts belong in the MCP evidence ledger when delivered.
The event lint disables helper expansion, so even a successful result would not cover this helper contract by itself.
Other shared helper outputs, including adjusted target-ticket weights, require their own owner review and probability baseline/comparison before any weighted correction.

## Remaining work

Global multi-country scope correctness, protected-identity paired scenarios, state targeting, pacing evidence, carrier availability and full CXT manual lifecycle remain open.
The permanent resume/disposition documents must keep this bounded hardening separate from complete-system acceptance.
