# Soviet Collapse Focus Endpoint Identity Patch Handoff

Date: 2026-05-29
Agent: Chaos Redux focus-tree audit/patch subagent
Scope:
- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`

The worktree was already dirty when this audit began. I did not revert unrelated/current-state edits. The changed focus files include broader pre-existing modifications in `git diff`; the identifiers below are the small patch surface I intentionally changed in this pass.

## References Read

- `AGENTS.md`
- `.agents/skills/hoi4-focus-trees/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-improvement-loop/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, AI modding, On actions, Event modding, Decision modding, Idea modding, National focus modding
- Vanilla docs: `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`
- Vanilla focus precedents for `create_wargoal`, `add_state_claim`, `add_core_of`, `division_template`, `create_unit`, dockyard, supply, and railway rewards
- Spec reference: `docs/specs/005_soviet_collapse_specs/005_soviet_union_collapse_final_clean_merged_part_5_focus_trees.md`

## Route Coverage Table

| Tree | Focuses | Current route depth | Main remaining gap |
| --- | ---: | --- | --- |
| `soviet_collapse_ukraine_focus_tree` | 83 | Broad bespoke republic tree with politics, industry, military, diplomacy | Still helper-heavy; more direct decision hooks and postwar expansion handling needed |
| `soviet_collapse_breakaway_focus_tree` | 36 | Generic breakaway coverage | Shallow by design; needs stronger identity splits or replacement for long-lived tags |
| `soviet_collapse_internal_republic_focus_tree` | 62 | Internal republic politics/industry/military | Rewards still rely on generic helpers; expansion and decision integration thin |
| `soviet_collapse_baltic_focus_tree` | 42 | Regional political/industry/security lines | Needs clearer distinct diplomatic and expansion payoffs |
| `soviet_collapse_caucasus_focus_tree` | 40 | Regional authority and survival lines | Needs deeper route-specific wars, border claims, and postwar hooks |
| `soviet_collapse_central_asia_focus_tree` | 45 | Regional congress and southern shield lines | Claims exist, but decision/postwar integration remains light |
| `soviet_collapse_moldova_focus_tree` | 48 | Regional state/river/crossing lines | Needs deeper expansion/diplomatic decision hooks |
| `soviet_collapse_belarus_focus_tree` | 53 | Regional state/security/industry lines | Needs stronger identity-specific endpoint rewards |
| `soviet_collapse_kazakhstan_focus_tree` | 92 | Deepest republic tree; multiple politics/resource/foreign branches | Layout cleaned further; still needs more direct mechanics and fewer generic helper rewards |
| `FTH_soviet_collapse_focus_tree` | 47 | Full custom splinter template with identity names | Still template-heavy; needs more Free Territory-specific decision/mechanic hooks |
| `PRA_soviet_collapse_focus_tree` | 22 | Railway authority crisis tree | Endpoint strengthened this pass; whole tree still shallow |
| `TSC_soviet_collapse_focus_tree` | 18 | Tunguska crisis tree | Endpoint strengthened this pass; needs real political/industry/military branches |
| `RMC_soviet_collapse_focus_tree` | 18 | Romanov/martyr crisis tree | Endpoint strengthened this pass; needs broader political and restoration mechanics |
| `DSC_soviet_collapse_focus_tree` | 18 | Dead soldiers congress crisis tree | Endpoint strengthened this pass; needs recruitment/cores/aggression branch depth |
| `NRF_soviet_collapse_focus_tree` | 18 | Northern revenant fleet crisis tree | Endpoint strengthened this pass; needs naval/dockyard/raiding branch depth |
| `ICD_soviet_collapse_focus_tree` | 18 | Immortal commissariat crisis tree | Endpoint strengthened this pass; needs commissariat-specific control mechanics |
| `BSC_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `TNC_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `ALA_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `BBH_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `KRS_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `UDC_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `SDZ_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `GAC_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `DHC_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `KHC_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `FEV_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `SZA_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `UWD_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `MRC_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `IUL_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `BAC_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Needs stronger local identity and direct mechanics |
| `ARD_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Layout line cleaned this pass; needs stronger Arctic naval/convoy identity |
| `NLC_soviet_collapse_focus_tree` | 47 | Full custom splinter template | Layout lines cleaned this pass; needs stronger polar-city industrial/survival identity |
| `CFR_soviet_collapse_focus_tree` | 47 | Factory successor construction authority | Civilian industry payoff strengthened this pass |
| `OGB_soviet_collapse_focus_tree` | 23 | Factory successor bureaucracy tree | Still shallow; needs a full political/industry/security branch pass |
| `MFR_soviet_collapse_focus_tree` | 58 | Military factory/arsenal authority | Duplicate-style equipment reward cleaned this pass; still needs stronger unit/doctrine identity |

## Patched Focus IDs

### Endpoint aggression and identity mechanics

- `PRA_rails_over_capitals`
  - Before: high-chaos/military helper plus pale railway endgame completion, but weak actual railway/expansion payoff.
  - After: adds railway authority reward, extra railway construction, SOV annex wargoal when valid, existing custom splinter expansion claims, assault-column spawn helper, and SOV conquer/antagonize AI strategy in hidden effect.

- `TSC_starfall_mandate`
  - Before: high-chaos helper and air XP.
  - After: adds SOV annex wargoal when valid, custom splinter expansion claims, assault-column spawn helper, and SOV conquer/antagonize AI strategy.

- `RMC_resurrection_without_state`
  - Before: high-chaos/legal recognition endpoint.
  - After: adds SOV annex wargoal when valid, custom splinter expansion claims, assault-column spawn helper, and SOV conquer/antagonize AI strategy.

- `DSC_congress_of_the_dead_army`
  - Before: high-chaos/military endpoint with limited aggression.
  - After: adds SOV annex wargoal when valid, custom splinter expansion claims, assault-column spawn helper, and SOV conquer/antagonize AI strategy.

- `NRF_northern_revenant_fleet`
  - Before: high-chaos/navy XP endpoint with limited naval infrastructure payoff.
  - After: adds a dockyard/shared slot in a controlled state, SOV annex wargoal when valid, custom splinter expansion claims, assault-column spawn helper, and SOV conquer/antagonize AI strategy.

- `ICD_commissariat_without_end`
  - Before: high-chaos/political endpoint.
  - After: adds SOV annex wargoal when valid, custom splinter expansion claims, assault-column spawn helper, and SOV conquer/antagonize AI strategy.

### Factory successor payoff cleanup

- `CFR_the_state_that_builds`
  - Before: construction authority focus leaned on variables/helpers without a major direct civilian industry payoff.
  - After: adds offsite civilian factory industry through `add_offsite_building = { type = industrial_complex level = constant:soviet_collapse_factory_ancient.medium_mandate_gain }`.

- `MFR_workers_own_the_arsenal`
  - Before: repeated support-equipment stockpile style reward.
  - After: second support-equipment reward changed to artillery equipment to make the arsenal payoff more military-specific and less spammy.

### Layout-only cleanup

- `ARD_extreme_path`: moved from `x = 5` to `x = 4` to remove a connector crossing through `ARD_winter_convoy_columns`.
- `NLC_winter_guarantees`: moved from `x = 14, y = 9` to `x = 16, y = 10` to remove connector crossings.
- `NLC_heated_workshop_contracts`: moved from `x = 12, y = 10` to `x = 13, y = 11` to remove connector crossings.
- `kaz_soviet_collapse_emergency_oil_boards`: moved from the current-state location to `x = 10, y = 8` to remove an exact connector-line hit without creating duplicate coordinates.

## Localisation and Icon Changes

- No focus IDs were changed.
- No new icon IDs were added.
- No localisation files were edited.
- Existing tooltip reused: `soviet_collapse_custom_splinter_route_identity_reward_tt`.
- Full English localisation scan found `0` missing focus name/description keys for the scoped files.
- Mod plus vanilla `.gfx` scan found `0` unresolved focus icon sprite names for the scoped files.

## Reward and Localisation Mismatch Findings

- Direct idea spam is no longer present in these three focus files: `add_ideas = 0`, `swap_ideas = 0`.
- Exact repeated equipment-stockpile rewards inside one focus: `0` after the `MFR_workers_own_the_arsenal` cleanup.
- Many 47-focus custom splinter trees still have reward text that implies unique identity while the gameplay remains generic helper cadence. The biggest examples are the template-heavy trees from `BSC` through `NLC`.
- The six short crisis trees now have stronger endpoints, but the middle routes remain shallow and do not yet fully match their strong lore claims.
- `OGB_soviet_collapse_focus_tree` remains the clearest factory successor mismatch: it is only 23 focuses and does not yet deliver a distinct political/industry/security identity.

## AI Behavior Gaps

- Mechanical scan found `0` focuses missing `ai_will_do`.
- The six patched crisis endpoints now add hidden SOV conquer/antagonize AI strategy when SOV exists.
- Remaining AI weakness is qualitative: most custom splinter and factory successor trees still use flat/local focus weights rather than route-aware AI strategies for political, industrial, naval, rail, and expansion identity.
- No persistent AI cleanup was added in this pass; the patch stays within endpoint focus effects and existing helper calls.

## Icon Coverage Table

| Check | Result |
| --- | ---: |
| Focuses scanned | 1634 |
| Focuses missing `icon` | 0 |
| Unresolved icon sprite references, mod plus vanilla scan | 0 |
| Icon IDs changed in this pass | 0 |
| New icons required by this pass | 0 |

Repeated generic icon usage still exists in template-heavy custom splinter trees, but no missing or broken icon references were found.

## Missing or Simplified Content

- `PRA`, `TSC`, `RMC`, `DSC`, `NRF`, and `ICD` still need full branch deepening. This patch strengthened endpoints only; it did not create new political/industry/military route families.
- `OGB_soviet_collapse_focus_tree` needs the largest factory-successor pass: expand to distinct bureaucracy/political control, files-and-records industry, internal security, and diplomatic/expansion payoffs.
- The 47-focus custom splinter trees from `BSC` through `NLC` remain too template-like. Each needs at least a small identity pass that swaps generic helper cadence for direct mechanics tied to the tag's name/lore.
- Republic trees are mechanically broad but still need more direct Soviet Collapse decision hooks, postwar handling, and route-aware expansion decisions.
- Focus-decision integration remains mostly indirect outside Ukraine and existing helper systems.
- No full redesign was attempted in this subtask by request; broad rewrites are queued as remaining work.

## High-Priority Follow-Up

1. Deepen `OGB_soviet_collapse_focus_tree` first; it is short and least distinct.
2. Expand the six short crisis trees into real political, industrial, and military/expansion branches:
   - `PRA`: rail authority, supply nodes, railway seizure, junction city decisions.
   - `DSC`: dead-soldier congress recruitment, cores/claims, aggressive war goals, manpower.
   - `NRF`: dockyards, naval raiding, Arctic ports, ship/naval modifiers.
   - `TSC`: observatory/impact-zone science, air/rocket/chaos identity, Siberian war aims.
   - `RMC`: restoration legitimacy, imperial cores/claims, officer corps.
   - `ICD`: commissariat control, ideological policing, industrial command.
3. Replace remaining generic helper cadence in full custom splinter trees with identity-specific direct rewards.
4. Add route-aware AI strategies for endpoint aggression, naval play, railway play, industry play, and defensive republic survival.
5. Add or reuse decision unlock flags from focuses where the focus text promises ongoing mechanics.

## Validation

Commands/checks run:

- `git diff --check -- common/national_focus/005_soviet_collapse_republics.txt common/national_focus/005_soviet_collapse_custom_splinters.txt common/national_focus/005_soviet_collapse_factory_successors.txt`
  - Passed.
- Brace depth script over all three scoped focus files.
  - `final_depth=0`, no early closes.
- Unsupported operator scan:
  - `rg -n "<=|>="` over all three scoped focus files returned no matches.
- Focus audit parser over all three scoped focus files:
  - Trees: `37`
  - Focuses: `1634`
  - Missing `ai_will_do`: `0`
  - Missing focus icons: `0`
  - Unresolved focus icons: `0`
  - Missing English focus name/description localisation keys: `0`
  - Direct `add_ideas`: `0`
  - Direct `swap_ideas`: `0`
  - Exact duplicate equipment stockpile reward focuses: `0`
  - Duplicate focus coordinates: `0`
  - Exact connector-line path hits: `0`
  - Direct wargoal effects: `10`
  - Custom splinter expansion helper calls: `6`
  - Custom splinter assault-column helper calls: `6`

Skipped validation:
- No in-game load test was run.
- No full mod validator was run because this is a subagent handoff in a dirty concurrent worktree.

## Changed Files

- `common/national_focus/005_soviet_collapse_republics.txt`
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `common/national_focus/005_soviet_collapse_factory_successors.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_endpoint_identity_patch_handoff.md`

No commit was created from this subagent pass because the worktree contains unrelated/concurrent dirty changes and this handoff is intended for parent integration.
