# Event 006 achievement completion audit handoff

Date: 2026-07-17

Mode: audit with approved small local fixes

Scope owner: `event6_achievement_audit`

## Documentation reconciliation note (2026-07-18)

This 2026-07-17 achievement audit is preserved as historical evidence for the
fourteen non-signature achievements and its lifecycle cautions. Its IW-043
and IW-058 blocker verdict is superseded by the exact signature tranche:
`CHU` and `ASY` are admitted, the two IW-043 route writers and three IW-058
settlement writers are operational, and the Assyria icon triplet is complete.
The signature achievements remain hidden when their route, survival, or
terminal proof predicates fail. A parent-wide sixteen-achievement completion
audit is still required; do not repeat the old “no writers/no assets” work.

## Result

The registration, localisation, constants, historical ledgers, and runtime wiring for all sixteen Event 006 achievements were reviewed. Fourteen achievements have reachable proof chains after the fixes in this handoff. Two package-specific achievements remain deliberately fail-closed:

- `Bolgar's Modern Heirs` (`IW-043` / `CHU`) is absent from the exact compile-time content-attestation registry and has no writers for either signature route-completion flag.
- `The Council Between Two Rivers` (`IW-058` / `ASY`) is absent from the exact compile-time content-attestation registry, has no writers for its three signature proof flags, and is missing its complete runtime achievement icon triplet.

Both packages have regional readiness shells, but neither is runtime-admitted: `has_independence_wave_runtime_package_content_attestation_for_execution_id` omits both immutable package IDs. The exact compile-time registry remains the admission authority. The overall sixteen-achievement feature is therefore not content-complete even though every definition is registered safely.

## Sources consulted

- Repository `AGENTS.md`.
- `chaos-redux-subagents` and `chaos-redux-events` repository skills.
- Offline wiki: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Achievement modding.
- Vanilla documentation: script concepts and script constants, triggers, effects, and `common/on_actions/_documentation.md`.
- Vanilla achievement and on-action precedents, including war, peace, state-control, subject, release, and annexation scopes.
- Event 006 achievement definitions, constants, triggers, effects, on-actions, localisation, decisions, scenario application, super-event witnesses, formable families, and package selectors.

## Achievement-by-achievement verdict

| Achievement | Verdict | Main proof path or blocker |
| --- | --- | --- |
| Seal of a Sovereign Decade | Reachable | Exact Event 006 anchor opening, sovereign-history guard, public-value thresholds, and ten-year origin date are connected. |
| Sovereignty Without Strings | Reachable | Recognition/security proof and patron/client/subject disqualifiers are connected. |
| Five Quiet Years | Reachable | DM-25/DM-26 plus recognized separation establish the negotiated-peace date; forced recognition and former-host war invalidate it. |
| The Tower Never Fell | Reachable after fix | Former-host declaration, exact anchor control changes, thirty-day grace, and qualifying peace now form one bounded reconquest proof. |
| Five Signatures at the Table | Reachable after fix | Natural formal proclamation marks exact founders; a global provenance marker blocks every member of a scenario-preformed Common Congress, including later joiners. |
| Four Regions, One Charter | Reachable after fix | Maintained member/region arrays and cohesion transactions drive the two-year clock; the same global provenance marker prevents a preformed-congress leak. |
| The Smallest Capital Saved | Reachable | DM-44 success records the actor/target relationship after mission completion; one-year target survival and voluntary-reunion failure are connected. |
| A Union Beyond Proclamation | Reachable after fix | FORM01/02/04 and FORM05 already wrote exact receipts. FORM03 now writes both generic receipts only on full ratification and clears them at start/cleanup. |
| Bolgar's Modern Heirs | Fail-closed blocker | IW-043 has a regional readiness shell but no exact compile-time content attestation; `independence_wave_volga_bulgaria_restoration_route_complete` and `...federal_route_complete` also have no writers. The icon triplet is complete. |
| The Council Between Two Rivers | Fail-closed blocker | IW-058 has a regional readiness shell but no exact compile-time content attestation; its population, settlement, and host-conflict proof flags have no writers, and all three achievement DDS files are missing. |
| Institutions Before Empire | Reachable | One-state opening, institutional-major history, professional army, and successful league-goal receipt are connected. |
| The Open-Border Reckoning | Reachable after fix | Dangerous-milestone publication qualifies the actor; the first external containment attack now begins the one-year clock. Scenario-forced qualification remains excluded. |
| The Long Roll Call | Reachable | Only Low, non-Common-Congress SCN-008 plans start the exact committed-country ledger; origin end, subject changes, and annexation update it without a world scan. |
| Three Patrons, No Master | Reachable | Distinct major-aid patrons are array-backed; dependency history, client routes, and concessions are connected. |
| Five Lines, No Shots | Reachable | Leadership terms reset correctly; DM-43 increments the current leader; member war and DM-51 invalidate the term. The expulsion disqualifier is dormant because Event 006 has no separate expulsion transaction. |
| One Capital, Ten Years | Reachable after fix | Candidate initialization now records current subject/war state; any war clears the continuous peace attempt; full peace starts a new date; subject status and former-host reconquest remain permanent failures. |

## Fixes applied

### Radical containment timing

`independence_wave_achievement_begin_radical_containment` now records qualification without starting the survival date. `independence_wave_achievement_record_war` writes the date only for the first qualifying non-member attack on the league. Duplicate milestone witnesses do not reset an existing proof. The English tooltip now says that the year begins when the containment war begins.

### Host-remnant continuous peace

Added `independence_wave_achievement_refresh_host_remnant_peace` and wired it to candidate initialization, peace resolution, and subject/free on-actions. Candidate initialization detects an already-subject host. War declarations explicitly clear the date for either participant when it is a host-remnant candidate, independent of the precise point at which the engine exposes `has_war`. A later full peace starts a fresh date only if permanent subject/reconquest disqualifiers are absent. A separate former-host transaction now records annexation, voluntary reabsorption, or subordination of an Event 006 breakaway as permanent host reconquest history.

### Former-host anchor grace

Anchor-loss tracking now requires an active war against the release's living former host. A former-host declaration seeds the grace date immediately when the anchor is already uncontrolled. Recovery or the qualifying peace evaluates and closes the current clock. Unrelated wars and pre-reconquest occupation can no longer contaminate this achievement.

### Scenario-preformed league provenance

Common Congress application sets `independence_wave_achievement_scenario_preformed_league` before league-member registration. The marker gates founder receipt creation, the founding final trigger, the cross-regional clock, and its final trigger. It is cleared at first network initialization, league dissolution, or successful natural consultative/formal proclamation. This blocks later natural joiners to the preformed league without permanently locking future league generations.

### FORM03 integration receipts

FORM03 post-charter start and cleanup clear both generic achievement receipts. Exact full confederal ratification writes both receipts. Compromise and failure paths remain non-qualifying.

### Documentation and localisation

- Reconciled IW-043/IW-058 against the exact compile-time admission registry; regional readiness shells do not constitute runtime admission.
- Documented the revised clock, grace, provenance, and FORM03 receipt lifecycles.
- Clarified the radical achievement's one-year timing.
- Replaced the government-specific phrase “durable republic” with “durable state”; the proof accepts any qualifying government route.

## Files changed by this audit

- `common/scripted_effects/006_independence_wave_achievement_effects.txt`
- `common/scripted_triggers/006_independence_wave_achievement_triggers.txt`
- `common/on_actions/006_independence_wave_achievement_on_actions.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/006_independence_wave_scenario_effects.txt`
- `common/scripted_effects/006_independence_wave_form03_effects.txt`
- `localisation/english/006_independence_wave_achievements_l_english.yml`
- `docs/systems/006_independence_wave_achievements.md`
- this handoff

The achievement definition file and achievement constants were audited but not edited by this subagent. No FORM48 or Pacific file was touched. Existing unrelated dirty-worktree changes were preserved. No commit was created.

## Evidence and validation

- Exactly sixteen `chaosx_006_*` achievement definitions are registered under the existing unique achievement group.
- All sixteen use start-safe `possible = { ... always = yes }` blocks and map to one exact final scripted trigger.
- The English file contains 50 unique keys with no duplicates and retains UTF-8 BOM encoding.
- Numerical tooltip claims match the centralized achievement constants.
- Forty-five of forty-eight expected DDS files exist and decode as 64 by 64; the only missing files are the three Assyria variants listed below.
- No daily, weekly, monthly, or global-country achievement scan exists. Iteration stays bounded to the frozen host, league-member, or scenario-country arrays.
- FORM03's exact decision and timeout success paths both call the patched full-ratification transaction.
- Touched script files have balanced braces. The tracked-file diff check reported no whitespace errors.

The HOI4 MCP event inspector was attempted with event, namespace, and exact-file selectors. Each accepted query returned `INTERNAL_ERROR` for workspace `mod_chaos_redux_ea3b2d67c2c0` without an artifact or diagnostic payload. No MCP-based event graph can therefore be cited for this audit; the source-level and vanilla-reference review above remains the available evidence.

## Simplifications, omissions, and blockers

No gameplay fallback or simplified substitute was introduced by these fixes.

The feature remains incomplete for these exact reasons:

1. IW-043 needs implementation of the accepted restoration/federal route design, exact writers for its two route-completion flags, independent package audits, and exact compile-time admission.
2. IW-058 needs implementation of the accepted Assyrian route design, exact writers for population protection, Mesopotamian settlement, and host-conflict survival, independent package audits, and exact compile-time admission.
3. IW-058 also needs approved Assyrian symbol research and these final assets; they must not be improvised:
   - `gfx/achievements/chaosx_006_assyria_survives.dds`
   - `gfx/achievements/chaosx_006_assyria_survives_grey.dds`
   - `gfx/achievements/chaosx_006_assyria_survives_not_eligible.dds`
4. Event 006 has no explicit member-expulsion action. The arbitration achievement already checks a future expulsion-history flag, but nothing currently writes it because there is no corresponding gameplay transaction.
