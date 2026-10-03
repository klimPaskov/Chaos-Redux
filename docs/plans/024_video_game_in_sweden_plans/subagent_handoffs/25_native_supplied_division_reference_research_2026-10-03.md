# Repo Explorer Handoff

## Scope read
- Parent task: bounded, read-only search for an actual native per-division supply-satisfaction reader usable in division or state scope, to resolve Event 24's exact supplied-unit proof blocker.
- Explicit constraints: Event 24 specs remain accepted; no simplification, unsupported fallback, invented native command, gameplay edit, balance choice, HOI4 launch, index operation, commit, service restart, or work on another agent's changes. The parent owns Event 24 implementation and current runtime repairs.
- Files or ids requested: prior audit `20_helper_lifetime_and_proof_audit_2026-10-03.md`; approved Workshop IDs `1521695605`, `2265420196`, and `1458561226`.
- Skills or docs read: `AGENTS.md`; complete `.agents/skills/chaos-redux-subagents/SKILL.md`, `chaos-redux-events/SKILL.md`, and `chaos-redux-decisions-missions/SKILL.md`; the named audit 20 handoff. No Paradox wiki web access.

## Primary findings
- No exact per-division supplied-satisfaction reader was found in the installed reference-mod sources that were present and searched. The findings do not establish that no engine-internal accessor exists elsewhere; the supported reader remains unverified and Event 24's exact proof remains blocked.
- Kaiserreich's two closest named triggers inspect state-owner countries for Guangzhou and Dali. They do not inspect divisions or supply delivery.
- Old World Blues' `change_mot_supply` is an explicit mod-defined country-variable system (`mot_supply` / `mot_army_supply`), not evidence of a native division reader. Other supply-name hits are local variables, modifiers, technology, or custom resource names.
- The approved directory for Workshop ID `1458561226` is absent at the requested path, so that reference could not be inspected.
- No source write is proposed. No gameplay dry-run, review, apply, post-validation, rollback, or recovery action was performed or is proposed by this research.

## Relevant files

| Path | Why it matters | Evidence / source revision |
| --- | --- | --- |
| `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1521695605/common/scripted_triggers/CHI triggers (Left Kuomintang).txt` | `CHI_support_INC_guangzhou_supply_base_trigger` at 479-486 and `CHI_support_INC_dali_supply_base_trigger` at 488-495 each enter a state's `owner` (`var:592`, `var:816`) and test `tag = CHI` / `is_subject_of = CHI`. No division scope or satisfaction read. | SHA-256 `46F558933B2DA89C15073D7FBCA500441E2C3C91D00E7E301AC350210CE92766` |
| `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1521695605/events/CHI events (Left Kuomintang).txt` | Calls the two state-owner triggers at 4014-15, 4027-28, 4049-50, and 4102-03 as event-option conditions. | SHA-256 `31B017A1F5C8CEE94B9D8A2E179163C204BA66FA3A2874504A9D581864EB2323` |
| `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2265420196/common/scripted_effects/MOT_scripted_effects.txt` | `calculate_state_damage` uses state-control-scaled `mot_supply_change` at 2-34; `change_mot_supply` at 116-143 changes country variable `mot_supply` and derives `mot_army_supply`. The code comment says to call it in MOT scope. This is a custom pool and writer, not a division reader. | SHA-256 `D49338AC3FFBA12E7225984D0BF9A105DE2CDE5DA57766B13C29A8FB7D293569` |
| `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2265420196/events/nf_mot.txt` | Event `nf_mot.6` initializes `mot_supply` and `mot_army_supply` at 171-172; options call the custom effect at 663-664 and 819-820. | SHA-256 `6416BDCA8EAE8E937CD8BB3FB8D6821C1CC6746E0954FA1C9F7CE08DB91A4EF9` |
| `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2265420196/common/scripted_effects/VER_scripted_effects.txt` | `ver_issues_supply_consumption` at 126-136 is a mod variable adjusted and compared inside an effect, not a native supply predicate. | SHA-256 `82092D24760BA4B17CFFDF2FA5D0640217FEAEA607352295FF51B6EA3382F5D6` |
| `docs/plans/024_video_game_in_sweden_plans/subagent_handoffs/20_helper_lifetime_and_proof_audit_2026-10-03.md` | Prior Event 24 audit states the exact gap at 127-149 and 285-293, records earlier source/document search scope, native citations, and MCP blockers at 345-368. | Prior audit's cited source revisions are copied below; this pass did not re-run those documentation inspections. |

## Existing patterns

The closest Kaiserreich pattern is territorial ownership/subject qualification for named supply-base locations. It proves a location's owner identity only. The Old World Blues pattern explicitly mutates a country-scoped custom stock (`mot_supply`) and a scaled variable (`mot_army_supply`). Its `army_supply` name does not make it an engine reader. Search hits such as `local_supplies`, `sla_supplies`, `ver_issues_supply_consumption`, `basic_supply_transport_tech`, and `COS_supply_rebels_array` are likewise variable, modifier, technology, or custom-array tokens, not a per-division satisfaction result.

## Vanilla or reference precedents

No qualifying native reader precedent was found in the searched files. The exact search covered `.txt` and `.md` files in each present Workshop root's `common/scripted_triggers`, `common/scripted_effects`, `events`, `docs`, and `documentation` directories. The last two directories were absent in IDs `1521695605` and `2265420196`; the entire `1458561226` root was absent.

The bounded identifier/operator search was:

```text
^\s*(?!#).*\b[A-Za-z_][A-Za-z0-9_]*(?:supply|suppl)[A-Za-z0-9_]*\s*(?:=|>|<)|^\s*(?!#).*\b(?:supply|supplied)\s*(?:=|>|<)
```

The division/supply cross-reference search was:

```text
division.{0,80}(supply|suppl)|(supply|suppl).{0,80}division|(?:is|has|any|every|num|unit|state)[A-Za-z0-9_]*supply[A-Za-z0-9_]*\s*=|supply[A-Za-z0-9_]*(?:unit|status|ratio|satisfaction)\s*=
```

The `suppl` substring also caught the unrelated `Supplementary Reserve` template in `2265420196/common/scripted_effects/dynamic_rebellion_scripted_effects.txt:446,528`; it is a lexical false positive, not a supply reader.

Audit 20's installed evidence is from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`, SHA-256 `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` (`divisions_in_state` 2648-2661, `unit_strength` / `unit_organization` 7686-7702, supply-vehicle totals 2979-2992), and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`, SHA-256 `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` (`num_armies_in_state` 526-533). The offline source is `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, SHA-256 `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` (division quantity rows 1276-1282 and division trigger table 2217-2225). Audit 20 records that these mechanisms do not establish delivered supply to a division and that no exact reader was found in its bounded installed/offline search.

## Likely edit order for the parent

No edit order is proposed from this evidence-only pass. Keep exact supplied-division proof unresolved under the accepted Event 24 requirements until an authoritative native reader is identified and its division/state scope is verified. Do not promote stockpiles, railway connectivity, readiness, strength, or organization into supplied-satisfaction evidence.

## Validation checks

- Read-only `rg` searches used the exact patterns above over the listed directories and only `.txt` / `.md` files; the matching definitions and consumers above were opened with line context and hashed.
- Live tool registry exposure included `mcp__hoi4_agent_tools__hoi4_reference_context`, `mcp__hoi4_agent_tools__hoi4_reference_search`, `mcp__hoi4_agent_tools__hoi4_reference_read`, and `mcp__hoi4_agent_tools__hoi4_source_lookup`; it did not include `mcp__hoi4_agent_tools__hoi4_script_validate`. Tool exposure alone does not verify reference-service health. No MCP inspection was attempted in this pass because the source search yielded no candidate to validate. Audit 20 records earlier reference calls timing out after 600 seconds and bounded retries timing out after 40 seconds; see its lines 345-368.
- No game, test suite, service, map, rewrite tool, index, or commit was used.

## Risks and blockers

- Confirmed blocker: no supported per-division supply-satisfaction reader is established by this bounded research or the cited audit 20 documentation search.
- Confirmed package gap: Workshop reference root `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1458561226` does not exist in this installation.
- MCP validation blocker: `mcp__hoi4_agent_tools__hoi4_script_validate` is not exposed in the connected registry. Reference-route exposure was observed, but service health was not established by this pass. Prior timeout evidence remains in audit 20.
- No fallback, source implementation, or balance target is proposed or approved here.

## Recommended next action

The parent should carry the exact native supplied-reader gap as unresolved in Event 24 review. Any newly found candidate needs an authoritative installed/offline syntax and scope citation and, if available, live MCP validation before it can support the accepted requirement.
