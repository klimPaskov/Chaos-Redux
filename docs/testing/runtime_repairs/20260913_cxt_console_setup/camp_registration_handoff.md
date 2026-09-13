# Camp registration repair handoff

Disposition: implemented, pending parent review within the authorized CXT console crash repair.
Ownership: only `camp_rework_register_active_site` in `common/scripted_effects/camp_repression_rework_effects.txt` and this handoff.
No staging or commit was performed.

## Finding and change

The supplied 269-line attachment contains two `invalid event target: var:genocide_responsible_country` messages at original source line 634.
The helper initialized an absent responsible-country variable from `ROOT` without first checking that ROOT named an existing country, then immediately entered the variable as a country trigger scope.
A present variable was also treated as a usable country pointer without an existence check.

The repair adds `country_exists = ROOT` to the missing-pointer default.
It requires `has_variable = genocide_responsible_country` and `country_exists = var:genocide_responsible_country` before the first country-pointer scope.
It checks the migration flag before the ordinary equality branch and adds a ROOT country-existence guard inside that branch.
It also guards the later ROOT-dependent state-pool classification.
Eligibility, ROOT equality, the migration bypass, and every registration write remain in place.
An unusable saved pointer is rejected without replacement, clearing, or assigning responsibility to the state owner or controller.

## Helper contract

| Field | Contract |
| --- | --- |
| Name | `camp_rework_register_active_site` |
| Current scope | State, as required by its existing state flags and state profile effects |
| Responsible-country input | Existing state variable `genocide_responsible_country`, or missing variable defaulted from an existing country ROOT |
| Other input | Temporary `camp_register_site_type`, unchanged |
| Migration input | Existing global `camp_rework_migration_in_progress` flag and a caller-supplied responsible-country pointer |
| Accepted registration | Existing, eligible responsible country matching ROOT, or existing, eligible responsible country during migration |
| Outputs | Existing flags, site profile, state and country registries, evidence registration, administrative initialization/reopening, achievements, and country recalculation |
| Rejected registration | Registration payload does not execute, and the existing final temporary site-type reset still executes |
| Side effects | Unchanged valid registration payload and guarded initialization of an absent pointer |

No helper was extracted or added.
No constants, tuning values, AI scores, weights, flags, event targets, or cleanup hooks were added or changed.
No call site was changed.

## Caller review

`camp_rework_run_versioned_migration` supplies the pointer from PREV inside its existing country/control-state traversal before registration.
The historical detention and gulag activators in `common/scripted_effects/genocide_crisis_effects.txt` likewise supply `genocide_responsible_country = PREV` before invoking the helper.
Ordinary action callers in the camp effects file retain their existing country ROOT contract.
`genocide_track_state_for_monthly_pulse` delegates directly to this helper.
The repair preserves the public ROOT default and does not introduce a PREV, owner, or controller fallback.

## Meaningful source validation

The saved baseline SHA256 is `fe25763cefe8c6b50f0b92e259551b486ab1b1b6416f04d547b71260b8bea028`, matching `baseline_inventory.json`.
A direct normalized comparison against that saved baseline shows only the helper comment, the guarded default, the registration-entry guards, the guarded equality branch, and the classification guard.
All source outside this helper is unchanged relative to the saved baseline.
The entire registration payload after its first state write is identical after removing the single added classification guard.
The extracted registration write sequence contains the same 16 writes before and after, with SHA256 `c53a1fbb1cfa86dc2104244df52ae95d756240b0c4d16305b5076305c71b69f6`.
The patched source SHA256 at handoff creation is `8e41639c785e610c2180b935ca3431d5a594f3fa0631553456aef720c51e6d26`.

| Source scenario | Expected guard behavior |
| --- | --- |
| Missing pointer, existing country ROOT | Pointer defaults to ROOT, then original eligibility and equality apply |
| Missing pointer, None ROOT | Country default is rejected, and the presence guard prevents the variable-scope block |
| Missing pointer, State ROOT | Country default is rejected under the documented country-target contract |
| Present stale pointer to a country that no longer exists | Pointer is preserved and registration is rejected before country-pointer scoping |
| Present valid eligible pointer equal to country ROOT | Original registration payload executes |
| Present valid eligible pointer unequal to ROOT, migration off | Original equality restriction rejects registration |
| Present valid eligible pointer, migration on, None or State ROOT | Migration can admit registration without evaluating ordinary ROOT equality, and ROOT-dependent classification is guarded |
| Present special-chaos-country pointer | Existing eligibility trigger still rejects registration |

These are source and documentation deductions, not live-engine scenario results.
Installed documentation does not expose a general `is_country` or `is_state` scope-type trigger.
The guard uses the documented any-scope `country_exists` trigger with a country scope or variable target.
The exact engine treatment of a malformed variable containing a non-country scope has not been independently demonstrated by the available helper analysis.

## Required references consulted

Read `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.
Opened all eleven required offline core wiki pages and read the relevant invalid-target, variable-scope, ROOT, presence-trigger, and country-existence sections.
Read installed vanilla trigger documentation for `country_exists`, `exists`, `scope_exists`, `has_variable`, and `tag`, and effect documentation for `if`, `set_variable`, and saved event targets.
Consulted the installed script-concept documentation and existing shared dynamic-effect source and markdown.
The installed `scope_exists` documentation explicitly states that variable scopes are always valid, so that trigger cannot validate the saved country pointer.
Vanilla `SOV_scripted_triggers.txt` provides the existence-before-country-scoping precedent in `SOV_basic_pressure_government_triggers` and neighboring diplomatic triggers.
Existing Chaos Redux faction and cannibalism helpers provide the explicit `country_exists = var:<country_pointer>` pattern.

## MCP evidence and limitation

Used read-only `hoi4.event_inspect` trace and `hoi4.event_render` scope with the source selector `{ kind: "source", sourcePath: "common/scripted_effects/camp_repression_rework_effects.txt", line: 627 }`, `expandHelpers = true`, `maxDepth = 1`, and `maxNodes = 12`.
The trace also used `maxEdges = 20`.
The service returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL` at revision `964dd033660ad33876b6a25b579f70b5972852d29ed02fed266aabb47bd4e399`.
Both responses reported `analysisMode = focused`, `helpers = 0`, and failed analysis validation with the exact message: `Large workspace analysis deferred workspace-wide helper projections and lifecycle passes; direct evidence is linked`.
The tool used its indexed workspace inventory despite the bounded source request.
No broad scan or source-analysis escalation was requested.
This partial event graph does not validate helper scope resolution or country-pointer lifecycle, and no engine-equivalent helper validation is claimed.

- Trace artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39d601bce158f976d2cae0380b2209e02dfdf9b3750c992a6b52fc0c107d76d7/a9b84f72f79ef0dc9f98ea8f69a06e1b9ce91e87fa03f33bb9981e4184576e95/event-trace-964dd033660a.json`
- Scope render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6f6d8c480b90118cd53d2955b904474d1bfe8eb869549ba6682e82524239c1d7/323ce7d61765a725382ce9761346331d50138e0dbc8bc658dc8ddf8d1bba3792/event-scope-964dd033660a-manifest.json`
- Scope render data: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a52149414fa8d0b87c0a5b1784c6c1d7b5831ad5a0d9c722f7a886d8e6be16fd/41d33a01b7614c52cbb524f06f6c27e4a0873bc1514fc25bf9484ebf8c3a71e6/event-scope-964dd033660a.json`
- Scope render image: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c795d38fe147b9232400143e549875659fcb005e8534d577021380f19992a388/5da7f794190f0002f1fb168145240042f9921263ccd9cc991237b37ba386853c/event-scope-964dd033660a.png`

## Simplifications, omissions, and blockers

No gameplay simplifications or replacement behavior were introduced.
The patch does not establish that the two camp messages caused the reported crash, and the parent owns the separate CXT command and ROOT repair.
Live-engine evaluation was not performed because game execution and console control are outside this task.
The focused MCP route omitted helper projections and lifecycle analysis, so exact runtime guard behavior remains unverified by that route.
The parent must review the bounded diff and carry this limitation into the complete repair report.
