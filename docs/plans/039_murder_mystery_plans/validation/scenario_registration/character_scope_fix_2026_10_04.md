# SCN-019 character registration scope repair

## Implemented correction

The parent orchestrator reported the maximum-intensity launch error at `common/scripted_effects/039_murder_mystery_runtime_effects.txt:442` on 2026-10-03 at 16:15.
The installed engine rejected `exists = yes` in a CHARACTER scope.
Both named-target and opening-leader registration branches require the saved character target and check its exact identity inside the registering country's `any_character` roster.
This proves recruitment by the recorded owner without applying a country-only trigger to a character.
Generic-office and protected dispositions, registry payloads, retirement effects, scenario IDs, intensity, and launch routing are unchanged by this isolated repair.
No new helper or unfinished capture transaction is included in the repair commit.

## Required source evidence

`hoi4.reference_context(surface=event, limit=2)` identified the installed documentation and offline wiki, with additional topics omitted by that limit.
Targeted searches and revision-bound reads covered the three native triggers and the offline roster semantics relevant to this repair.

| Source | Read lines | Revision or SHA-256 | Rule |
| --- | --- | --- | --- |
| Installed `documentation/triggers_documentation.md` | 1272-1280 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` | `any_character` accepts COUNTRY scope |
| Installed `documentation/triggers_documentation.md` | 2708-2716 | same revision | `exists` accepts COUNTRY scope only |
| Installed `documentation/triggers_documentation.md` | 5345-5353 | same revision | `is_character` accepts CHARACTER scope and compares identity |
| Offline `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | 399-404 | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` | `any_character` checks characters recruited by the current country |
| Vanilla `common/national_focus/germany.txt` | 8088-8105 | `4cfd72972e19bcc560684dfc2f170e62ce786153ee01cf06ee7acc9609996095` | Native `is_character = PREV.PREV` compares a scope pointer |
| Approved Kaiserreich `events/FNG events (Fengtian).txt` | 6829-6872 | `f17ddf705b71abd94b6b30be765065e42b12d966e46ac38d5c4290a208381f2f` | `is_character = event_target:leaker` compares a saved character pointer |

The installed game root is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
The approved reference-mod root is `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1521695605/`.

## Validation limits

`hoi4.source_lookup` read the repaired registration branches at lines 432-456, source revision `eeda58a404cf7c981ad1f97cfd593ffaa6b6f05639ca30c4adb9dd321c46d063`.
The read shows both roster checks and the unchanged generic and protected disposition alternatives.
The narrow `event_inspect` trace and `event_render(view=scope)` returned focused partial analysis at revision `f2b8bdff77c9db689497266f8e35cb0795c11751b02e0188f6533efbece85fd5`, with zero indexed helpers and zero selected render nodes.
These outputs do not establish registration-helper or lifecycle coverage.
The trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/afa0966f1ad59137bef9294ffd055d1c24cdf34bdae9616071b2efefc36d9e79/04a280af6526a27a472bd7d1a09294708ef3148daa03043ff81062b8ee11fc7e/event-trace-f2b8bdff77c9.json`.
The scope render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93fcad0938b072f6e10bb1e5036b35e2a7e422ea347e77df12f2c080128611ea/23bf61baf08bd52a9f2cbd11381c6c8fb66c2a76a4fbb82c1b9109a3161e9486/event-scope-f2b8bdff77c9-manifest.json`.
The matching `event_compare` attempt returned `EVENT_REVISION_NOT_CACHED`, because that focused report revision is not retained as a graph baseline.
No comparison success is claimed.
The generic MCP resource route rejected server name `hoi4-agent-tools` as unknown, so the linked artifacts were not read through that route.
Native `script_validate` is not exposed by this connection.

The isolated staged source is checked against its parent blob for exactly two replacements, with the remainder byte-identical.
The working-tree character source-contract check remains a source-only check of broader unfinished work and is not runtime evidence.
The separate scenario-registration checker currently fails its workbook `Scenarios!E14` equality assertion against the four runtime warning strings.
That documentation reconciliation remains queued in the broader goal and is outside this isolated runtime-scope correction.
The orchestrator's evidence confirms the SCN-019 list entry and launch on the preceding committed build, and identifies this specific failure.
Post-fix live execution, a clean full error log, and the complete Event 039 Part 18 matrix remain unverified.
No gameplay simplification or asset substitution is introduced by this repair.
Event 039 as a whole remains incomplete.
Skills used for this repair are `chaos-redux-events` and `chaos-redux-shared-git-commit`.
