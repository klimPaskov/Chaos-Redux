# Dynamic building damage helper handoff

Status: helper implemented under the parent-accepted parser-fix scope.
Parent owns migration of the twelve Acid Rain calls and native verification.
No commit or game launch was performed.

## Files and contract

Changed `common/scripted_effects/chaosx_dynamic_effects.txt` and its matching `.md` only, plus this handoff and byte backups under `pre_patch_dynamic_building_damage19/`.
Added `damage_state_building_dynamic`, a state-scope neutral wrapper that executes one native building-damage effect through `meta_effect`.
The required inputs are `dynamic_building_damage_type`, a caller-set temporary building token, and `dynamic_building_damage_amount`, a caller-set temporary number.
The helper only reads these inputs and generates no output variable.
Both inputs must be initialized within the calling effect chain, with no absence sentinel or fallback value.
The amount may be assigned before a bounded call group if no intervening effect modifies it.

```txt
set_temp_variable = { dynamic_building_damage_amount = acid_rain_damage_one }
set_temp_variable = { dynamic_building_damage_type = token:infrastructure }
damage_state_building_dynamic = yes
```

The parent accepted this supported caller-set temporary-variable contract after source research rejected an unverified direct parameter-block proposal.
No `$PARAM$` syntax was installed.

## Behavior, tuning, and cleanup

Building type comes from `GetTokenKey` and damage comes from the same unformatted numeric interpolation used by `damage_buildings_in_random_states`.
The current Acid Rain damage amount of one remains one.
There is no explicit arithmetic rounding, clamp, scale, random choice, scope change, repair modifier, target reassignment, input mutation, persistent variable, flag, event target, or on-action hook.
The underlying native state/province-building lookup is preserved, including the native first matching province-building search.
No new constants or tuning table are necessary because the owning Acid Rain constant remains authoritative.
No persistent cleanup is necessary because inputs are temporary.
An independent caller must initialize its own values before reuse.

## Evidence and checks

Read AGENTS.md, events and subagents skills, all eleven required core offline wiki pages, the Effects meta/scripted-effect and damage-building references, Data structures variable/token references, Localisation token references, vanilla effect documentation for `damage_building` and `meta_effect`, and vanilla script-constant documentation.
Vanilla `common/scripted_effects/00_scripted_effects.txt` contains `SF_PARA_sabotage_effect` with same-state direct building damage.
Vanilla `CZE_scripted_effects.txt` uses numeric-variable localisation in `meta_effect`.
Existing `013_natural_disasters_effects.txt` effect `natural_disaster_damage_selected_building` supplies building type through `GetTokenKey` and numerical damage through meta text.
The shared registry's `damage_buildings_in_random_states` supplies damage through raw numerical interpolation.

Reviewed exact source and documentation differences against immediate full-byte backups, with hash guards before writing.
The helper body contains only one `meta_effect`, one `damage_building`, and two read-only interpolation inputs, which permits the parent's group-level amount initializer.
Native parser and runtime verification remain parent-owned.
Exact default-formatter serialization of arbitrary fractional or large values is unresolved and must not be claimed lossless.
This limitation does not change the current exact amount of one.

MCP Event 33 inspection and render used selector `{kind: event, eventId: chaosx.nr33.1}`, depth 1, node bound 12, without helper expansion.
Inspection returned `EVENT_INSPECTED_PARTIAL` and render returned `EVENT_RENDERED_PARTIAL` at revision `410c82bea077b36a7e01b4ed11eb4927d40357359aad54622f2b2adf58fea5cb`.
The service explicitly deferred helper projection and lifecycle passes, reported zero indexed helpers in focused mode, and marked its event-analysis check false.
These artifacts establish bounded event-surface inspection only and do not prove helper parsing or execution.

- Trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c28ff76eb8d289764c92ee6694a02d3ff03ffbc0f59b55700cc6e55c274bd2c2/e3aa93492d85b46f7b8a73eefc40fa43b8472ba5853c2e517b1d1f312605a9ff/event-trace-410c82bea077.json`
- Render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0856f5e8cb42337fd95808e5101dd271acf046bce2735f1667609e569f34caf4/c18129b3de90b0fb8ee35206fc83c751ab9917e69e0a073835c35c196b2dbc8d/event-neighborhood-410c82bea077.svg`

MCP comparison against the inspection revision returned `EVENT_REVISION_NOT_CACHED` with the exact blocker `Requested event graph revision is not cached`.
No event comparison or helper execution proof is claimed from that failed route.

## Simplifications, omissions, and blockers

No gameplay simplifications were introduced.
No probability, focus, GUI, or map surface changed.
Call-site migration and native validation are explicitly assigned to the parent, so this helper handoff does not claim overall repair completion.
No skill was created or changed.

## Byte identities

- `chaosx_dynamic_effects.txt` before: `e6fac3fa6a6b2bc180c2bdadba97a82c711142c016e33f01b42736526b1855bb`, after: `e767552e990aaa091afde7fa7528dcb99fdab5ee455adbe72f3a077c561b857e`.
- `chaosx_dynamic_effects.md` before: `692bb9837d20de6a3c7260a94be181480c6d53e99f910eb2f043fa7a37b0820a`, after: `b7475054088b28e61bb3abdc1d1af559064c7b28c53e8df0fdcca25f0b991f71`.
