# Event 006 character handoff refactor v50

Date: `2026-08-01`

Status: `package_effects_patched_parent_event_branch_ready`

## Scope and result

The two remaining Event 006 package-effect files no longer call `recruit_character` directly.

Each package surface now invokes the existing hidden synchronous event `chaosx.nr6.15` before the existing role and promotion effects continue.

No new event ID was added and `events/006_independence_wave.txt` was not edited by this subagent.

## Files changed

- `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt`
- `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt`
- this handoff

## Exact call sites and behavior

- `independence_wave_apply_iw043_institutional_surface` calls `chaosx.nr6.15` under its existing exact IW-043 active-country/package/origin guard.
- `independence_wave_apply_iw058_institutional_surface` calls `chaosx.nr6.15` under its existing exact IW-058 active-country/package/origin guard.
- `independence_wave_prepare_iw093_leadership` and `independence_wave_prepare_iw093_command_roster` call `chaosx.nr6.15` only under `is_independence_wave_iw093_prepared_scope`.
- `independence_wave_prepare_iw098_date_appropriate_leadership` calls `chaosx.nr6.15` only under the existing prepared-scope, Event 012 safety, and post-cutover date guard.
- `independence_wave_prepare_iw098_command_roster` calls `chaosx.nr6.15` only under the existing prepared-scope and Event 012 safety guard, so the command roster remains available before the cutover date.

The IW-093 and IW-098 helpers retain separate guarded calls because they are separate package-owned entry points. The hidden event is idempotent through `NOT = { has_character = ... }` checks, so the normal setup pass may invoke it twice per package without changing roster or role semantics.

All existing `add_country_leader_role`, `promote_character`, role flags, and date-attestation effects remain in their original scripted helpers and execute after the synchronous handoff.

## Parent-owned event branch contract

The parent has added these branches to `chaosx.nr6.15` in `events/006_independence_wave.txt`.

- `is_independence_wave_iw043_country`: recruit `CHU_independence_wave_middle_volga_congress` and `CHU_independence_wave_federal_presidium` always. Recruit `CHU_independence_wave_bolgar_civic_presidium` only for `independence_wave_iw043_route_restoration` or `independence_wave_route_traditional_restoration`. Recruit `CHU_independence_wave_river_security_directorate` only for `independence_wave_iw043_route_emergency_guard` or `independence_wave_route_emergency_military`.
- `is_independence_wave_iw058_country`: recruit `ASY_independence_wave_provisional_national_council` and `ASY_independence_wave_concordat_council` always. Recruit `ASY_independence_wave_civic_national_assembly` for `independence_wave_iw058_route_civic_assembly`, `independence_wave_route_constitutional_republic`, or `independence_wave_route_popular_council`. Recruit `ASY_independence_wave_levies_guardianship` for `independence_wave_iw058_route_levies_guardianship` or `independence_wave_route_emergency_military`.
- `is_independence_wave_iw093_prepared_scope`: recruit `DOX_prempeh_ii`, `DOX_kwame_frimpong`, and `DOX_kwaku_ntim`.
- `is_independence_wave_iw098_prepared_scope` plus `is_independence_wave_iw098_event012_state_safe`: recruit `SOK_muhammad_dikko` and `SOK_bello_rabah` on every admitted date, and recruit `SOK_siddiq_abubakar` only when `is_independence_wave_iw098_post_cutover` is true.

These branch conditions reproduce the removed direct-recruit limits. Parent-owned Pacific FIJ/FSM branches remain separate.

## Validation

- `rg -n "recruit_character"` over both changed package-effect files returned no matches.
- `rg -n "country_event = { id = chaosx.nr6.15 }"` found six intended call sites, with four in IW-093/IW-098 prepared helpers and one each in the IW-043/IW-058 institutional surfaces.
- Source inspection confirmed every original role setup, promotion, route flag, and date-attestation block remains after the handoff call.
- Read-only `hoi4.event_inspect` was run for `chaosx.nr6.15`. The MCP returned partial workspace analysis with no blockers and linked artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b79609b3ea67023929eadddbdc548a169aa865b9ef864eea885b22ef9299a902/0d976d71b2cde81b487ef082fa2615f3721153df05fe989ee4783f3060c63dcc/event-trace-54c80fc8baf0.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dfa71916050db40acfb0d93d34512f5b1fd9b660726e5584663b421128cdcbca/9779e51ae43247acc4a630d4e66c3ecc87e9a8e8a2406b900323e5a1c8ec5e07/event-lint-54c80fc8baf0.json`. The report deferred workspace-wide helper projections, so it is evidence of source reachability rather than a clean whole-workspace lint pass.

## Remaining risks and parent follow-up

- The parent must keep the `chaosx.nr6.15` branches aligned with the exact route and date guards above while merging the parent-owned FIJ/FSM work.
- No live game or consumer validation was run because agents must not launch Hearts of Iron IV. The parent owns final source review and user-owned live validation.
- No empty helper blocks remain. Each formerly recruitment-only IW-093/IW-098 helper now has a guarded synchronous event call.
- No localisation, asset, attestation, balance, cleanup, or unrelated event changes were made.
