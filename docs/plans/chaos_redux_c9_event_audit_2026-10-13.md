# C9 event rewards and tooltip audit, 13 October 2026

Status: implemented source repairs and completed static audit within C9.
Acceptance basis: the user's restore plan C9 authorises the all-event reward, internal-tooltip and duplicate-idea audit.
The parent accepted maintained protection as Event 11's grant condition, the existing wartime condition for the Bulgarian and Mongol spirits, and display-only isolation of private flag predicates while preserving real requirements, native costs and existing text.
The parent retains C10 opener randomisation, C6 human-system guards, A5 pictures, and the shared restore-plan annotation.

## Published source changes

- `f63ab274b16410e1b50643d07ab27570b8ca8f88`: 4,646 scalar private flag predicates isolated with `hidden_trigger`, across 301 actually changed files.
- `77d24f47c3d23d7e191486261790c48d5ce80c28`: maintained protection for Hardened Networks, paid-opening helper privacy, Bulgarian/Mongol wartime conditions, one requirement key in the existing shared ideas localisation, and the existing Event 11 overview.
- `d0fbe01a8927c65fb2f3fdde3c0536268399d959`: three private structured flag predicates isolated, and the public `chaos_tier` labelled through its existing localisation owner.

The flag preparation initially tracked 302 paths.
Preserving the already-localised vanilla `form_nordic_nation_flag` left its owning file unchanged, so the published scalar commit changes 301 paths.
The two `SOV_paranoia_system_active_flag` checks and `INS_revolution_has_started` also retain their existing vanilla labels.
The scalar leaves are attributable to 241 human-visible event definitions, with unions over conditional helper paths rather than observed game displays.
The final structured pass preserves 226 public tier checks with the label `Chaos Meter tier` and suppresses only three private checks.

## Reward findings, history and current cases

### Event 11

`secret_alliance_recalculate_preparedness` originally granted `secret_alliance_hardened_networks` whenever global Preparedness was positive.
Baseline Preparedness is 4, so an ordinary opening investigation could activate +14% planning speed, +18% entrenchment speed and -6% supply consumption without paying for protection.
The exact offending introduction is `d1d641122f2ed7b86654e035965bd33cba827290`.
Its parent lacks this helper, and the later inspected versions retain the positive-Preparedness grant.
There is no correct earlier implementation to restore for this grant, so the accepted fix changes only its condition and phase ownership.

```diff
- limit = { check_variable = { global.secret_alliance_preparedness > 0 } }
+ limit = { secret_alliance_is_concealed = yes }
+ if = {
+     limit = { check_variable = { secret_alliance_active_protections > 0 } }
+     add_ideas = secret_alliance_hardened_networks
+ }
+ else = { remove_ideas = secret_alliance_hardened_networks }
```

The ordinary paid protection package starts from 24 Command Power, 15 Army Experience and 300 support equipment, with the existing dynamic scaling and discounts retained.
The protection cap is one.
The staff project lasts 300 days and carries -6% planning speed while active, giving a net +8% planning benefit alongside the original entrenchment/supply bonuses.
Existing expiry callbacks release the protection slot and recalculate.
Baseline and known-plan contributions remain in Preparedness and all outcome calculations, but no longer grant the spirit by themselves.
Public reveal still clears interference/protection spirits and selects one known-plan tier and one defense tier through the existing mutually exclusive ladders.
The concealed refresh cannot replace a public defense tier when an old project callback runs.
Final cleanup still removes the spirit families.

| Current source case | Hardened Networks outcome |
| --- | --- |
| Baseline 4, no protection | No grant |
| Baseline plus known plans, no protection | No grant |
| One paid active protection | Original full bonuses, with the existing project burden |
| Project expires while concealed | Removed on recalculation |
| Public reveal, defense score above 85 | Existing high defense tier remains |
| Public reveal, medium defense tier | No concealed refresh adds the high tier |

`chaosx.nr11.3.b` retains its dynamic Command Power payment and original wording.
Only `secret_alliance_add_known_plans_component` and `secret_alliance_select_operation_suspect` are placed inside `hidden_effect` at that call site.
The first helper contains a private timed-component flag and expiry bookkeeping.
The second selects true or innocent suspects through private membership/evidence filters.
Their original call-site introduction is also `d1d641122`, and the current root `.1` C10 hunk is preserved.

### Old Great Bulgaria and Mongols Rise

The original definitions in `f93ad0644` already contain the full numeric strengths without a continuing condition.
`5f00dbea7a44080a981f47d71eec9e52245fc36d` moves them from `common/ideas/chaosx_ideas.txt` into the event-owned files without lowering those values or adding a war requirement.
No earlier lower/conditional version was established in that inspected history.
Accepting the origins permits a country to remain at peace with substantial construction, efficiency, resources, political-power and manpower advantages.
The parent accepted `do_effect = { has_war = yes }` as the minimal ongoing commitment, retaining all historical strengths and the existing country/unit/war-goal mechanics.

| Spirit | Peace after accepting | War after accepting |
| --- | --- | --- |
| `old_great_bulgaria` | Its modifiers do not apply | Original +50% construction, +50% maximum efficiency, -25% consumer goods, +30% core attack and other original values |
| `legacy_of_khan` | Its modifiers do not apply | Original +25% construction, +100% resources, +2,500 weekly manpower, cavalry bonuses and other original values |

For the Mongol manpower component, 52 active wartime weeks give 130,000 manpower from this spirit, versus zero during peace.
This is a source-derived case, not an engine measurement or a new target.
The spirits remain present and survive civil war under their original rules.
They resume their original modifiers when war begins again.

### Strong candidates retained after source review

- Space Race: the launch requires advanced rocket engines and advanced computing, plus advanced fire control with the relevant DLC combination, and pays the existing dynamic 50-PP price.
  The active race category disappears when launch clears `space_race`, and the launcher explicitly loses `leading_space_race`.
  Other leadership spirits have the existing cancellation rule when the race ends.
  `secrets_of_the_universe` is a single permanent idea, with no `on_add` material grant, and is the core completion reward rather than an incidental report bonus.
  Its +50% research/construction/maximum-efficiency and +200% resources are already present in `f93ad0644` and survive the `5f00dbea7` split.
  Retention is based on the real technology accomplishment and the parent's acceptance of that distinction, not merely on historical existence.
- Industrial Boom: +35% output and construction belong to the boom itself.
  Output is reduced by the existing band shares: 0.67 at Strained, 0.33 at Dangerous and 0.25 during cooling, before other mapped components.
  These give 23.45%, 11.55% and 8.75% from the base output component.
  Dangerous/cooling construction shares halve that component to 17.5%.
  Existing exhaustion imposes -15% output/construction for the mapped rough/forced periods, and overheating/crash connects the benefit to consequences.
- Riches Found: factory output comes from registered mine contribution scores at 0.0012 per score and is capped at 0.12 across the existing aggregate refresh.
  Scores 25 and 250 illustrate 3% and a capped 12% component.
  The refresh removes predecessor revenue ideas and chooses one aggregate stage.
- Time Traveler: institutional spirits clear all predecessor stages before applying one profile/stage spirit.
  Military consultations award the original 25-XP component and a 120-day window scaled by reward share, industrial windows use 180 days, and emergency authority is timed for 180 days with the existing stability penalty/divergence consequences.
  These are conditional consultation/route rewards, not free permanent additions to ordinary incident acknowledgements.
- Brilliant Scientist: the +25% world-threat project-state output is conditional on `brilliant_scientist_world_threat_active` and removed otherwise.
  Shared helper reachability from another event does not establish that an ordinary technology/resource report creates that condition.
- Zombie, Rat King, Wendigo, Holy Realm, successor-state and other origin/transformation strengths were distinguished from ordinary human response gifts.
  They were not blanket-nerfed or redesigned.
- Explicit reward events retain their core premise and visible native grants: Event 84 gives 100 Political Power, Event 85 gives one selected 100-XP branch, Event 58 adds one civilian factory and slot per owned state, and Event 55 builds infrastructure for its selected country.
  For Event 58, five and fifty owned states mean five and fifty factories, which is deliberately state-scaled reward content rather than a hidden extra attached to an unrelated response.

## Internal tooltip coverage and history

The initial direct-variable diagnosis was corrected after reading the offline Data structures section.
Ordinary variable operations do not have a tooltip by default.
The 701 draft variable wrappers were removed through a checked inverse patch and were never published.
The installed documentation also permits an explicit `tooltip` on `check_variable`, unlike the older wiki wording, so explicit tooltip strings were inspected separately.

The final traversal starts from human-visible event choices and follows literal scripted-effect and scripted-trigger callees.
It excludes hidden effects/triggers, option visibility tests, AI-only resolution pages, AI chance blocks, and random-list weight modifiers.
It resolves flag labels against both mod and installed vanilla English localisation, including vanilla indentation.
It preserves public/localised predicates, native costs/stat/state requirements, existing custom tooltips, complete flag argument blocks, scope links, values, meta bindings and boolean nesting.

History evidence distinguishes introductions from regressions.
`git log -S` checks the exact flag-check signatures rather than treating a flag setter as the offending check.
The corresponding per-token introduction data and source-linked diff excerpts are in the task evidence.
`git log -G 'hidden_trigger|hidden_effect'` was also checked across all 302 original candidate paths.
Thirty-one deletion-bearing revisions were compared by current owning root and flag masking.
No matching current-root visibility regression was established.
The apparent removals include indentation changes, moved/paginated event bodies, deleted older implementations and refactors.
Selected flag localisation deletions were also checked since 1 June 2026, covering the recent sweep/refactor period, with no matching deletion found.
These results justify narrow authorised display fixes, not claims that introduction hashes prove unwanted removals or that every historical caller arrangement was reconstructed.

The structured follow-up retains the public tier requirement through `chaos_tier: "Chaos Meter tier"` in `localisation/english/chaosx_chaos_meter_l_english.yml`.
No earlier standalone key was found for restoration.
The two private zombie-tier checks are raw in their `b45c83d41` introduction.
The evolution-toggle check keeps its complete meta-generated flag name and all three replacement bindings.

## Explicit custom tooltip prose dispositions

The reachable explicit-key closure contains 3,283 keys, including referenced keys, scripted-localisation results, vanilla keys and indented definitions.
No missing literal referenced tooltip key was found after recognising formatters and internal replacement placeholders.
Formatting/texticon tokens and dynamic substitutions are not classified as raw implementation identifiers.
The eight concrete prose candidates below were read and retained without rewriting the restored wording.

| Key | Disposition |
| --- | --- |
| `soviet_collapse_custom_splinter_irregular_front_tt` | Black-flag columns and hidden depots describe military behaviour, not boolean flags or a secret route |
| `soviet_collapse_regional_charter_joint_staff_tt` | Internal tension is a public league-state consequence |
| `soviet_collapse_regional_charter_patron_channels_tt` | The same public tension/foreign-pressure consequence, with no implementation identifier |
| `utopia_manifesto_accept_tree_warning_tt` | Base flag means the country's displayed flag and warns of the real focus-tree replacement |
| `chaosx.nr19.105.b.tt` | Internal autonomy is the formation's negotiated political status and the numeric consequences are public mechanic values |
| `event021_posture_constitutional_tt` | Internal division means civil conflict within the country |
| `chaosx.nr21.9.amnesty.tt` | Public settlement obligations and their authority/idea consequences |
| `chaosx.nr21.9.harsh.tt` | Public repression/grievance consequences, not a disclosed hidden route identifier |

No exact private Secret Alliance Cohesion, Readiness or member-count value reference was found in the reachable tooltip wording.
Its existing suspect wording does not equate a visible suspect with true hidden membership.
No confirmed inappropriate explicit custom disclosure was hidden or rewritten.

## Duplicate ideas and localisation handoff

No duplicate idea definition ID was found, and no directly repeated immediate-plus-option idea grant was found.
Equal-name/equal-modifier groups exist among separate BSK/BYA/KHA origin packages: Fragmented Frontier Mandate, Frontier Workers' Council, Emergency Frontier Command and Traditional Land Compact.
The Bashkir route installer clears predecessor route ideas before adding its government spirit, and its compact refresh replaces provisional/stable compact stages.
The corresponding Siberian package helpers maintain their own country-specific families.
Time Traveler clears predecessor institutional spirits, Riches Found clears aggregate revenue stages, and Secret Alliance reveal uses mutually exclusive tiers with cleanup.
No confirmed same-country duplicate stack was invented or patched.

Changed localisation keys:

- `wartime_event_bonus_tt`: `These bonuses apply while at war.` in the existing shared ideas file.
- `chaos_tier`: `Chaos Meter tier` in the existing Chaos Meter file.

No dynamic-localisation helper was added or changed.
No existing dynamic token, cost, name, sourced quotation or attribution was altered.
No encoding concern was found in the scoped writes.
The optional narrative `_desc` entries for the two legacy Bulgarian/Mongol spirits and their empty report descriptions remain as supplied by history, with their existing names and the explicit wartime requirement retained.
No new lore was invented under the restore-only wording constraint.
The parent confirmed that Event 11's catalogue premise remains aligned and does not promise a fixed opener/free bonus, so no workbook or export edit is required.

Prose-quality changes are limited to two concise requirement/label additions and the existing overview's protection prerequisite.
Vagueness is repaired by stating the exact ongoing condition.
No bloat, obvious explanation, repetition, overcomplication or style-only rewrite was introduced into the restored event/tooltip text.
All actual sourced quotations were preserved because their existing values were untouched.

## Validation and limits

- Complete before/after canonical AST comparison across the scalar proposal and isolated commit tree, stripping only `hidden_trigger`, retains all original expressions, commands, scopes, values and weighted blocks.
- Captured-index reconciliation was compared against the captured index rather than the proposed tree, preserving unrelated staged content and modes.
- A concurrently committed Random Terror file was rebuilt only after its current source was proved canonical-equal to the reviewed working baseline.
- Complete structured-predicate argument/meta-binding and reconciliation equivalence was checked separately.
- All Bulgarian/Mongol numeric modifier entries match their original values.
- Maintained-protection baseline, known-plan, paid-project, expiry and public-reveal cases were checked against current source.
- The final scalar-and-structured player-path scan has no remaining unlocalised flag leaf in the analysed closure.
- The final duplicate-definition/direct-grant and explicit-key checks were rerun.
- Every source publication used a temporary index, reviewed intended diff, captured-index reconciliation, immediate-before-CAS entry checks and path-specific real-index reconciliation.

The MCP grant snippet returned partial coverage: native command/scope checks ran, while the helper and argument semantics required source/reference review.
It is not reported as a full validator pass.
No GUI render, live game, engine timing measurement, save or unsolicited error log was used.
Counts refer to source paths, not observed rendered leaks.
Conditional unions may include paths that do not execute in the same state, and dynamically generated helper destinations are not a claimed complete runtime graph.
Those limits do not change the known literal flag/requirement repairs.
No balance weights, probabilities or new numerical targets were changed.

There are no gameplay design simplifications or reduced requested mechanics in this C9 patch.
Verification remains static, and broader prose additions to the preserved legacy empty descriptions are outside the accepted C9 wording scope.
No unresolved wording decision remains for the changed keys, and no expansion plan was written.

## References and task evidence

- Offline Data structures, `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, flags lines 119-121 and variable tooltips lines 526-529, reference revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
- Offline Effects tooltip manipulation, lines 4572-4616, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
- Offline Triggers `hidden_trigger`, line 344, revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`, describes tooltip suppression and AND semantics.
- Installed effects documentation `add_timed_idea`, lines 2244-2268, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Installed triggers documentation `check_variable`, lines 2110-2135, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- Offline Idea modding line 247 documents the condition's modifier suspension without removing the spirit.
- Installed vanilla `common/ideas/andalusia.txt`, lines 17-21, supplies the `do_effect` trigger-block precedent.
- MCP source lookup located the original preparedness helper at lines 4713-4756, source index revision `25ed430b0d9892f85e6a1cff4eda0b489c53fa1a4743e96238fd553ca19e9686`.

Task-specific evidence is retained under `.tmp/c9/`: final `inventory.json`, `flag_paths.json`, `flag_history.json`, `flag_history_excerpts.json`, `visibility_history.json`, `visibility_classification.json`, `flag_loc_history.json`, `custom_tooltip_inventory.json`, `custom_tooltip_candidates.json`, owned before/after snapshots, and the isolated commit state/review patches.
It is temporary recovery/review evidence, not maintained tooling.
The following tables retain the durable per-file grant and changed-path coverage.

Skills used: canonical events, ideas/modifiers, subagents and shared Git commit, plus the event text-formatting reference.
The parent captured the reusable default-variable-tooltip and visibility-history guidance in `8ae0339e6`, updating the canonical event skill and its text-formatting reference.
This audit does not duplicate those instructions into another skill.

## Final per-event-file grant coverage

The final working-source inventory contains 183 event files and 4337 event definitions, with 5885 unique grant-command source locations across events and literal helper expansions.
The early 4,342-definition inventory preceded concurrent C3 retirements and is not used as the final count.
The table inventories grant paths rather than adding mutually exclusive effects into one hypothetical reward.

| Event source | Definitions | Unique grant sites in helper union | Grant kinds |
| --- | ---: | ---: | --- |
| `events\000_chaosx_events.txt` | 0 | 0 | None |
| `events\001_communism_spread.txt` | 0 | 0 | None |
| `events\002_zombie_outbreak.txt` | 0 | 0 | None |
| `events\003_the_holy_realm.txt` | 0 | 0 | None |
| `events\004_random_war.txt` | 0 | 0 | None |
| `events\005_soviet_collapse.txt` | 0 | 0 | None |
| `events\006_independence_wave.txt` | 0 | 0 | None |
| `events\006_independence_wave_foreign_reaction_events.txt` | 0 | 0 | None |
| `events\006_independence_wave_host_response_events.txt` | 0 | 0 | None |
| `events\006_independence_wave_iw098_succession_events.txt` | 0 | 0 | None |
| `events\006_independence_wave_milestone_events.txt` | 0 | 0 | None |
| `events\006_independence_wave_package_incident_events.txt` | 0 | 0 | None |
| `events\006_independence_wave_ready_formable_contracts_events.txt` | 0 | 0 | None |
| `events\006_independence_wave_statehood_incident_events.txt` | 0 | 0 | None |
| `events\006_independence_wave_support_events.txt` | 0 | 0 | None |
| `events\007_fury.txt` | 0 | 0 | None |
| `events\008_tensions_rising.txt` | 0 | 0 | None |
| `events\009_white_peace.txt` | 0 | 0 | None |
| `events\010_death.txt` | 0 | 0 | None |
| `events\011_secret_alliance.txt` | 0 | 0 | None |
| `events\012_africa_diaspora_protocol.txt` | 0 | 0 | None |
| `events\012_africa_evolutions.txt` | 0 | 0 | None |
| `events\012_africa_gods_of_africa.txt` | 0 | 0 | None |
| `events\012_africa_priority_member_events.txt` | 0 | 0 | None |
| `events\012_africa_promoted_tiera_events.txt` | 0 | 0 | None |
| `events\012_africa_rsa.txt` | 0 | 0 | None |
| `events\012_africa_world_order.txt` | 0 | 0 | None |
| `events\012_africa_world_package.txt` | 0 | 0 | None |
| `events\012_africa_world_package_asia_north_america.txt` | 0 | 0 | None |
| `events\012_africa_world_package_crossroads_europe.txt` | 0 | 0 | None |
| `events\012_africa_world_package_south_america_oceania.txt` | 0 | 0 | None |
| `events\012_africa_world_package_sponsorship.txt` | 0 | 0 | None |
| `events\012_africa_world_package_union_war.txt` | 0 | 0 | None |
| `events\012_african_union.txt` | 0 | 0 | None |
| `events\013_natural_disasters.txt` | 0 | 0 | None |
| `events\014_cannibalism.txt` | 0 | 0 | None |
| `events\015_utopia_manifesto.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_aftermath_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_biological_raid_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_containment_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_context_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_dhrondan_contact_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_directorate_outcomes.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_evolutions.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_foreign_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_host_reaction_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_kruger_state_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_news_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_project_incident_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_super_events.txt` | 0 | 0 | None |
| `events\016_brilliant_scientist_synthesis_events.txt` | 0 | 0 | None |
| `events\016_dhrondan_country_events.txt` | 0 | 0 | None |
| `events\017_join_faction.txt` | 0 | 0 | None |
| `events\018_random_resource.txt` | 0 | 0 | None |
| `events\019_infantry_spawn.txt` | 0 | 0 | None |
| `events\019_infantry_spawn_scenario.txt` | 0 | 0 | None |
| `events\020_black_death.txt` | 0 | 0 | None |
| `events\020_black_plague_weaponization.txt` | 0 | 0 | None |
| `events\021_random_civil_war.txt` | 0 | 0 | None |
| `events\021_random_civil_war_adaptation_events.txt` | 0 | 0 | None |
| `events\021_random_civil_war_external_war_events.txt` | 0 | 0 | None |
| `events\022_concentration_camps.txt` | 0 | 0 | None |
| `events\023_sov_nuclear_bombs_closure.txt` | 0 | 0 | None |
| `events\023_soviet_nukes.txt` | 0 | 0 | None |
| `events\024_hearts_of_iron.txt` | 0 | 0 | None |
| `events\025_alien_technology_in_antarctica.txt` | 0 | 0 | None |
| `events\026_black_friday.txt` | 0 | 0 | None |
| `events\027_doctrine_research.txt` | 0 | 0 | None |
| `events\028_asteroid_impact.txt` | 0 | 0 | None |
| `events\029_riches_found.txt` | 0 | 0 | None |
| `events\029_riches_found_verification.txt` | 0 | 0 | None |
| `events\030_time_traveler.txt` | 0 | 0 | None |
| `events\030_time_traveler_evolutions.txt` | 0 | 0 | None |
| `events\030_time_traveler_figures.txt` | 0 | 0 | None |
| `events\031_terrorist_attack.txt` | 0 | 0 | None |
| `events\032_missile_crisis.txt` | 0 | 0 | None |
| `events\032_missiles_evolution_events.txt` | 0 | 0 | None |
| `events\033_acid_rain.txt` | 0 | 0 | None |
| `events\034_industrial_boom.txt` | 0 | 0 | None |
| `events\035_great_depression.txt` | 0 | 0 | None |
| `events\036_chemical_and_biological_weapons_convention.txt` | 0 | 0 | None |
| `events\037_mysterious_population.txt` | 0 | 0 | None |
| `events\038_malta_crusaders.txt` | 0 | 0 | None |
| `events\039_murder_mystery.txt` | 0 | 0 | None |
| `events\040_lawrence_of_arabia.txt` | 0 | 0 | None |
| `events\040_lawrence_of_arabia_evolutions.txt` | 0 | 0 | None |
| `events\040_lawrence_of_arabia_federation.txt` | 0 | 0 | None |
| `events\041_disease_in_divisions.txt` | 0 | 0 | None |
| `events\042_equipment_from_heavens.txt` | 0 | 0 | None |
| `events\043_massive_flood.txt` | 0 | 0 | None |
| `events\044_space_race.txt` | 0 | 0 | None |
| `events\045_third_balkan_war.txt` | 0 | 0 | None |
| `events\046_placeholder.txt` | 0 | 0 | None |
| `events\047_boom.txt` | 0 | 0 | None |
| `events\048_old_great_bulgaria.txt` | 0 | 0 | None |
| `events\049_mass_panic.txt` | 0 | 0 | None |
| `events\050_the_great_embargo.txt` | 0 | 0 | None |
| `events\051_heat_wave.txt` | 0 | 0 | None |
| `events\052_intelligence_leak.txt` | 0 | 0 | None |
| `events\053_mysterious_man.txt` | 0 | 0 | None |
| `events\054_random_tech.txt` | 0 | 0 | None |
| `events\055_great_infrastructure_project.txt` | 0 | 0 | None |
| `events\056_navy.txt` | 0 | 0 | None |
| `events\057_radars.txt` | 0 | 0 | None |
| `events\058_free_civs.txt` | 0 | 0 | None |
| `events\059_ai_focus_aggressive.txt` | 0 | 0 | None |
| `events\060_research_failure.txt` | 0 | 0 | None |
| `events\061_mils_into_civs.txt` | 0 | 0 | None |
| `events\062_allies_backstab.txt` | 0 | 0 | None |
| `events\063_subject_independence.txt` | 0 | 0 | None |
| `events\064_border_forts.txt` | 0 | 0 | None |
| `events\065_random_trait.txt` | 0 | 0 | None |
| `events\066_cic.txt` | 0 | 0 | None |
| `events\067_generalissimo.txt` | 0 | 0 | None |
| `events\068_zin.txt` | 0 | 0 | None |
| `events\069_boxer_rebellion.txt` | 0 | 0 | None |
| `events\071_persian_empire.txt` | 0 | 0 | None |
| `events\072_ireland_reclaims_north.txt` | 0 | 0 | None |
| `events\073_mongols_rise.txt` | 0 | 0 | None |
| `events\074_japan_california.txt` | 0 | 0 | None |
| `events\075_tannu_tuva_joins_allies.txt` | 0 | 0 | None |
| `events\076_usa_tests_weapons.txt` | 0 | 0 | None |
| `events\077_send_eq.txt` | 0 | 0 | None |
| `events\078_border_war.txt` | 0 | 0 | None |
| `events\079_the_master.txt` | 0 | 0 | None |
| `events\080_airship.txt` | 0 | 0 | None |
| `events\081_england_tax.txt` | 0 | 0 | None |
| `events\082_law_upgrade.txt` | 0 | 0 | None |
| `events\083_agency_upgrade.txt` | 0 | 0 | None |
| `events\084_pp.txt` | 0 | 0 | None |
| `events\085_xp.txt` | 0 | 0 | None |
| `events\086_world_claims.txt` | 0 | 0 | None |
| `events\087_ww1.txt` | 0 | 0 | None |
| `events\088_mines.txt` | 0 | 0 | None |
| `events\089_tech_sharing_group.txt` | 0 | 0 | None |
| `events\090_kamikaze.txt` | 0 | 0 | None |
| `events\091_the_great_revolution.txt` | 0 | 0 | None |
| `events\092_greenland_sale.txt` | 0 | 0 | None |
| `events\093_portugal_galicia.txt` | 0 | 0 | None |
| `events\094_half_gone.txt` | 0 | 0 | None |
| `events\095_occupation_revolt.txt` | 0 | 0 | None |
| `events\096_divisions_lock.txt` | 0 | 0 | None |
| `events\097_collaboration.txt` | 0 | 0 | None |
| `events\098_new_ore.txt` | 0 | 0 | None |
| `events\099_desert_storm.txt` | 0 | 0 | None |
| `events\100_unknown.txt` | 0 | 0 | None |
| `events\_chaosx_easter_eggs.txt` | 0 | 0 | None |
| `events\_chaosx_news.txt` | 0 | 0 | None |
| `events\biological_countermeasure_events.txt` | 0 | 0 | None |
| `events\biological_facility_capture_events.txt` | 0 | 0 | None |
| `events\biological_lifecycle_events.txt` | 0 | 0 | None |
| `events\biological_native_raid_bridge_events.txt` | 0 | 0 | None |
| `events\biological_stockpile_safety_events.txt` | 0 | 0 | None |
| `events\biowarfare_events.txt` | 0 | 0 | None |
| `events\camp_administration_country_events.txt` | 0 | 0 | None |
| `events\camp_occ_partner_events.txt` | 0 | 0 | None |
| `events\cbrn_chemical_air_bridge_events.txt` | 0 | 0 | None |
| `events\cbrn_chemical_delivery_events.txt` | 0 | 0 | None |
| `events\cbrn_doomsday_raid_bridge.txt` | 0 | 0 | None |
| `events\cbrn_hq_events.txt` | 0 | 0 | None |
| `events\cbrn_land_raid_bridge_events.txt` | 0 | 0 | None |
| `events\cbrn_occupation_events.txt` | 0 | 0 | None |
| `events\cbrn_protection_events.txt` | 0 | 0 | None |
| `events\cbw_doom_news_events.txt` | 0 | 0 | None |
| `events\chaosx_activation.txt` | 0 | 0 | None |
| `events\chaosx_event_clusters.txt` | 0 | 0 | None |
| `events\chaosx_forced_event_feedback.txt` | 0 | 0 | None |
| `events\chaosx_test_country.txt` | 0 | 0 | None |
| `events\chaosx_triggerable_scenarios.txt` | 0 | 0 | None |
| `events\chemical_air_bomb_events.txt` | 0 | 0 | None |
| `events\chemical_warfare_events.txt` | 0 | 0 | None |
| `events\condemnation_sanctions_events.txt` | 0 | 0 | None |
| `events\fallout_manual_launch_notice_events.txt` | 0 | 0 | None |
| `events\fallout_treaty_cleanup_events.txt` | 0 | 0 | None |
| `events\fallout_world_end_events.txt` | 0 | 0 | None |
| `events\genocide_crisis_events.txt` | 0 | 0 | None |
| `events\germany_mengele.txt` | 0 | 0 | None |
| `events\japan_cbrn_campaign_raid_bridge.txt` | 0 | 0 | None |
| `events\japan_ishii.txt` | 0 | 0 | None |
| `events\soviet_gulag.txt` | 0 | 0 | None |
| `events\zombie_native_raid_bridge_events.txt` | 0 | 0 | None |
| `events\zombie_weaponized_special_projects.txt` | 0 | 0 | None |

## Changed-file and leaf ownership inventory

| Changed path | Scalar private leaves | Structured private leaves | Other C9 change |
| --- | ---: | ---: | --- |
| `common/ideas/048_old_great_bulgaria_ideas.txt` | 0 | 0 | Wartime condition and requirement key |
| `common/ideas/073_mongols_rise_ideas.txt` | 0 | 0 | Wartime condition and requirement key |
| `common/scripted_effects/002_zombie_outbreak_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/005_soviet_collapse_effects.txt` | 283 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_achievement_effects.txt` | 13 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_balkan_package_effects.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_bashkiria_mari_package_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_decision_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_don_package_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_effects.txt` | 12 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_evolution_effects.txt` | 13 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_force_effects.txt` | 12 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_form03_effects.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_form05_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_form48_effects.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_formable_registry_effects.txt` | 11 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_iberian_package_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_iw043_iw058_package_effects.txt` | 32 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_komi_package_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_kosovo_package_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_kuban_package_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_kurdistan_package_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_levant_arabia_package_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_milestone_effects.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_ready_formable_contracts_effects.txt` | 119 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_rhineland_bavaria_saar_package_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_siberian_package_effects.txt` | 9 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_tatarstan_package_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/006_independence_wave_western_package_effects.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_effects/009_white_peace_effects.txt` | 16 | 0 | Display-only leaf isolation |
| `common/scripted_effects/011_secret_alliance_effects.txt` | 84 | 0 | Maintained-protection phase/gate |
| `common/scripted_effects/012_africa_achievement_effects.txt` | 187 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_action_effects.txt` | 163 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_common_reserve_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_diaspora_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_effects.txt` | 12 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_elephant_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_evolution_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_focus_route_effects.txt` | 10 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_gods_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_gods_public_values_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_host_transfer_effects.txt` | 126 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_priority_member_character_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_priority_member_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_priority_member_force_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_proof_effects.txt` | 60 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_world_order_effects.txt` | 29 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_world_south_america_oceania_effects.txt` | 18 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_world_sponsorship_effects.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_effects/012_africa_world_union_war_effects.txt` | 43 | 0 | Display-only leaf isolation |
| `common/scripted_effects/013_natural_disasters_effects.txt` | 74 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_alien_infantry_api_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_achievement_effects.txt` | 11 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_aftermath_effects.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_containment_effects.txt` | 9 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt` | 34 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_effects.txt` | 144 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt` | 57 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt` | 19 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_host_reaction_effects.txt` | 10 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_project_effects.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt` | 53 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` | 16 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_raid_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_singularity_construction_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_brilliant_scientist_super_event_effects.txt` | 24 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_conventional_technology_api_effects.txt` | 17 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_dhrondan_contact_effects.txt` | 6 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_mengele_clone_production_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_mengele_native_prototype_effects.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_mengele_paleogenetics_deployment_effects.txt` | 6 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_mengele_paleogenetics_staff_effects.txt` | 19 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_mengele_project_stage_effects.txt` | 70 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_mengele_singularity_construction_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_mengele_singularity_terminal_effects.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_effects/016_portal_transit_batch_effects.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_effects/017_random_faction_effects.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_effects/018_resources_found_log_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/020_black_plague_rat_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/020_black_plague_response_effects.txt` | 9 | 0 | Display-only leaf isolation |
| `common/scripted_effects/021_random_civil_war_achievement_effects.txt` | 8 | 0 | Display-only leaf isolation |
| `common/scripted_effects/021_random_civil_war_active_evolution_effects.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_effects/021_random_civil_war_dynamic_front_candidate_effects.txt` | 15 | 0 | Display-only leaf isolation |
| `common/scripted_effects/021_random_civil_war_effects.txt` | 49 | 0 | Display-only leaf isolation |
| `common/scripted_effects/021_random_civil_war_event6_footprint_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/021_random_civil_war_evidence_effects.txt` | 14 | 0 | Display-only leaf isolation |
| `common/scripted_effects/021_random_civil_war_external_war_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/021_random_civil_war_front_ledger_effects.txt` | 20 | 0 | Display-only leaf isolation |
| `common/scripted_effects/021_random_civil_war_lifecycle_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | 196 | 0 | Display-only leaf isolation |
| `common/scripted_effects/023_sov_nuclear_bombs_achievement_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/023_sov_nuclear_bombs_closure_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt` | 40 | 0 | Display-only leaf isolation |
| `common/scripted_effects/023_sov_nuclear_bombs_reactor_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt` | 163 | 0 | Display-only leaf isolation |
| `common/scripted_effects/025_alien_technology_in_antarctica_holder_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/025_alien_technology_in_antarctica_lifecycle_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/025_alien_technology_in_antarctica_militarisation_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/025_alien_technology_in_antarctica_runtime_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/025_alien_technology_in_antarctica_signal_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/025_alien_technology_in_antarctica_wreck_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/026_black_friday_effects.txt` | 6 | 0 | Display-only leaf isolation |
| `common/scripted_effects/026_black_friday_native_sale_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/027_doctrine_research_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/029_riches_found_achievement_effects.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_effects/029_riches_found_aggregate_stage_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/029_riches_found_effects.txt` | 17 | 0 | Display-only leaf isolation |
| `common/scripted_effects/029_riches_found_late_outcome_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/029_riches_found_log_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/031_random_terror_achievement_effects.txt` | 81 | 0 | Display-only leaf isolation |
| `common/scripted_effects/031_random_terror_effects.txt` | 64 | 0 | Display-only leaf isolation |
| `common/scripted_effects/032_missiles_achievement_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/032_missiles_effects.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_effects/032_missiles_evolution_effects.txt` | 6 | 0 | Display-only leaf isolation |
| `common/scripted_effects/032_missiles_operations_effects.txt` | 16 | 0 | Display-only leaf isolation |
| `common/scripted_effects/032_missiles_payload_receipt_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/032_missiles_survey_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/033_acid_rain_achievement_effects.txt` | 20 | 0 | Display-only leaf isolation |
| `common/scripted_effects/033_acid_rain_aftermath_effects.txt` | 13 | 0 | Display-only leaf isolation |
| `common/scripted_effects/033_acid_rain_effects.txt` | 8 | 0 | Display-only leaf isolation |
| `common/scripted_effects/033_acid_rain_preparedness_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/035_great_depression_effects.txt` | 21 | 0 | Display-only leaf isolation |
| `common/scripted_effects/035_great_depression_external_adapters.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/036_cbrn_convention_effects.txt` | 35 | 0 | Display-only leaf isolation |
| `common/scripted_effects/037_mysterious_population_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/038_malta_crusaders_setup_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/039_murder_mystery_integration_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/042_equipment_from_heavens_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/biological_countermeasure_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/biological_lifecycle_effects.txt` | 44 | 0 | Display-only leaf isolation |
| `common/scripted_effects/biological_stockpile_safety_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/camp_administration_civil_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/camp_administration_country_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/camp_administration_effects.txt` | 16 | 0 | Display-only leaf isolation |
| `common/scripted_effects/camp_administration_integration_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/camp_administration_occupation_effects.txt` | 12 | 0 | Display-only leaf isolation |
| `common/scripted_effects/camp_administration_origin_effects.txt` | 22 | 0 | Display-only leaf isolation |
| `common/scripted_effects/camp_administration_ui_effects.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_effects/camp_repression_colonial_country_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/camp_repression_major_country_effects.txt` | 10 | 0 | Display-only leaf isolation |
| `common/scripted_effects/camp_repression_rework_effects.txt` | 18 | 0 | Display-only leaf isolation |
| `common/scripted_effects/cbrn_achievement_effects.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_effects/cbrn_biological_air_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/cbrn_protection_effects.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_effects/chaos_meter_effects.txt` | 21 | 0 | Display-only leaf isolation |
| `common/scripted_effects/chaos_unit_family_registry_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | 11 | 0 | Display-only leaf isolation |
| `common/scripted_effects/chaosx_event_cluster_effects.txt` | 11 | 0 | Display-only leaf isolation |
| `common/scripted_effects/chaosx_events_log_effects.txt` | 41 | 0 | Display-only leaf isolation |
| `common/scripted_effects/chaosx_logic_effects.txt` | 14 | 0 | Display-only leaf isolation |
| `common/scripted_effects/chaosx_settings_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/civilian_transfer_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/condemnation_sanctions_effects.txt` | 18 | 0 | Display-only leaf isolation |
| `common/scripted_effects/fallout_consolidated_effects.txt` | 38 | 0 | Display-only leaf isolation |
| `common/scripted_effects/famine_core_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/genocide_crisis_effects.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_effects/germany_mengele_effects.txt` | 15 | 0 | Display-only leaf isolation |
| `common/scripted_effects/humanitarian_runtime_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/migration_capacity_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/migration_cohort_history_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/migration_core_effects.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_effects/migration_persecution_effects.txt` | 12 | 0 | Display-only leaf isolation |
| `common/scripted_effects/zombie_special_project_effects.txt` | 71 | 2 | Display-only leaf isolation |
| `common/scripted_triggers/002_zombie_outbreak_triggers.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/003_holy_realm_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/005_006_liberations_collision_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/005_soviet_collapse_triggers.txt` | 246 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_balkan_package_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_bashkiria_mari_package_triggers.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_decision_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_first_footprint_package_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_force_package_mapping_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_iw043_iw058_package_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_kurdistan_package_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt` | 15 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt` | 22 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_package_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_ready_formable_contracts_triggers.txt` | 22 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_regional_framework_triggers.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_rhineland_bavaria_saar_package_triggers.txt` | 18 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_scotland_wales_package_triggers.txt` | 9 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_siberian_package_triggers.txt` | 10 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_tatarstan_package_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_triggers.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/006_independence_wave_western_package_triggers.txt` | 11 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/007_fury_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/008_tensions_rising_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/009_white_peace_triggers.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/011_secret_alliance_triggers.txt` | 21 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_achievement_triggers.txt` | 13 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_common_reserve_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_diaspora_triggers.txt` | 11 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_disease_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_evolution_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_focus_route_triggers.txt` | 8 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_gods_contract_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_gods_recovery_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_gods_strength_inputs_triggers.txt` | 6 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_host_transfer_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_priority_member_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_proof_triggers.txt` | 99 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_world_order_triggers.txt` | 18 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_world_sponsorship_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/012_africa_world_union_war_triggers.txt` | 19 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/013_natural_disasters_triggers.txt` | 16 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/014_cannibalism_triggers.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_alien_infantry_api_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_brilliant_scientist_country_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_brilliant_scientist_evolution_triggers.txt` | 13 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt` | 8 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt` | 70 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_brilliant_scientist_singularity_site_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_brilliant_scientist_super_event_triggers.txt` | 22 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_brilliant_scientist_triggers.txt` | 22 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_clone_maturation_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_dhrondan_contact_triggers.txt` | 8 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_mengele_clone_production_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_mengele_computation_incident_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_mengele_conventional_incident_triggers.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_mengele_paleogenetics_deployment_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_mengele_paleogenetics_staff_triggers.txt` | 17 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_mengele_project_stage_triggers.txt` | 12 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_mengele_singularity_incident_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_mengele_singularity_site_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_mengele_singularity_terminal_triggers.txt` | 15 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/016_portal_transit_batch_triggers.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/017_random_faction_triggers.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/018_resources_found_decision_triggers.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/018_resources_found_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/020_black_plague_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/021_random_civil_war_evidence_triggers.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/021_random_civil_war_external_war_triggers.txt` | 13 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/021_random_civil_war_lifecycle_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/021_random_civil_war_parent_triggers.txt` | 51 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/021_random_civil_war_triggers.txt` | 40 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/022_concentration_camps_triggers.txt` | 7 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/023_sov_nuclear_bombs_achievement_triggers.txt` | 34 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt` | 27 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/025_alien_technology_in_antarctica_triggers.txt` | 14 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/026_black_friday_triggers.txt` | 10 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/027_doctrine_research_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/029_riches_found_achievement_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/029_riches_found_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/031_random_terror_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/032_missiles_operations_triggers.txt` | 10 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/032_missiles_preparation_cost_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/032_missiles_survey_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/032_missiles_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/033_acid_rain_achievement_triggers.txt` | 25 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/033_acid_rain_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/034_industrial_boom_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt` | 5 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/035_great_depression_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/036_cbrn_convention_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/039_murder_mystery_integration_triggers.txt` | 2 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/040_lawrence_of_arabia_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/042_equipment_from_heavens_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/biological_lifecycle_triggers.txt` | 8 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/biological_stockpile_safety_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/camp_administration_origin_triggers.txt` | 14 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/camp_administration_triggers.txt` | 6 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/camp_administration_ui_triggers.txt` | 6 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/camp_repression_rework_triggers.txt` | 1 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/cbrn_doctrine_triggers.txt` | 4 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/chaosx_liberation_release_triggers.txt` | 3 | 0 | Display-only leaf isolation |
| `common/scripted_triggers/chaosx_settings_triggers.txt` | 0 | 1 | Display-only leaf isolation |
| `common/scripted_triggers/fallout_consolidated_triggers.txt` | 67 | 0 | Display-only leaf isolation |
| `docs/events/011_secret_alliance/overview.md` | 0 | 0 | Protection prerequisite |
| `events/002_zombie_outbreak.txt` | 5 | 0 | Display-only leaf isolation |
| `events/006_independence_wave.txt` | 1 | 0 | Display-only leaf isolation |
| `events/006_independence_wave_support_events.txt` | 19 | 0 | Display-only leaf isolation |
| `events/011_secret_alliance.txt` | 0 | 0 | Two paid-opening bookkeeping callers hidden |
| `events/012_africa_gods_of_africa.txt` | 6 | 0 | Display-only leaf isolation |
| `events/012_africa_world_package_union_war.txt` | 5 | 0 | Display-only leaf isolation |
| `events/016_brilliant_scientist_aftermath_events.txt` | 4 | 0 | Display-only leaf isolation |
| `events/016_dhrondan_country_events.txt` | 4 | 0 | Display-only leaf isolation |
| `events/023_soviet_nukes.txt` | 8 | 0 | Display-only leaf isolation |
| `events/025_alien_technology_in_antarctica.txt` | 3 | 0 | Display-only leaf isolation |
| `events/027_doctrine_research.txt` | 2 | 0 | Display-only leaf isolation |
| `events/029_riches_found.txt` | 1 | 0 | Display-only leaf isolation |
| `events/032_missile_crisis.txt` | 2 | 0 | Display-only leaf isolation |
| `events/039_murder_mystery.txt` | 2 | 0 | Display-only leaf isolation |
| `events/044_space_race.txt` | 2 | 0 | Display-only leaf isolation |
| `events/049_mass_panic.txt` | 2 | 0 | Display-only leaf isolation |
| `events/054_random_tech.txt` | 2 | 0 | Display-only leaf isolation |
| `events/089_tech_sharing_group.txt` | 7 | 0 | Display-only leaf isolation |
| `events/fallout_world_end_events.txt` | 41 | 0 | Display-only leaf isolation |
| `localisation/english/chaosx_chaos_meter_l_english.yml` | 0 | 0 | One appended public tier label |
| `localisation/english/chaosx_ideas_l_english.yml` | 0 | 0 | One appended requirement key |

## Follow-up cross-path idea grant review

Status: implemented source guards for confirmed cross-path regrants; this follow-up expands the earlier direct-event check across country history, scripted effects, focuses, decisions, events, and on_actions.

The static inventory found 1,759 granted idea ids and 210 ids referenced from more than one grant path; repeated references alone were not treated as defects because many are mutually exclusive country packages, distinct scopes, display-only tooltips, or intentional timed refreshes.

Same-country setup overlaps were confirmed for DTH (`death_country_without_breath`, `death_first_silence`), DHO (the five `cave_*` spirits), the RTA/RTX Event 20 carriers (`black_plague_rat_brood_instinct`, `black_plague_rat_king_dominion`, and `black_plague_rat_no_civilian_economy`), and the eight dormant Event 31 carriers (the three `random_terror_*` starting ideas). Each carrier's history already supplied the listed spirits before its first setup function ran.

The history sources reviewed for those setup pairs are `history/countries/DTH - Death.txt`, `history/countries/DHO - Oth-Kesh Host.txt`, `history/countries/RTA - Rat Nation.txt`, `history/countries/RTX - Rat King.txt`, `history/countries/JHX - Local Cell.txt`, `history/countries/JIX - Regional Insurgent.txt`, `history/countries/JKX - Transnational Network.txt`, `history/countries/JLX - Jihadist International.txt`, `history/countries/JMX - Final Command.txt`, `history/countries/JNX - Local Cell II.txt`, `history/countries/JOX - Regional Insurgent II.txt`, and `history/countries/JPX - Transnational Network II.txt`.

`common/scripted_effects/010_death_effects.txt`, `common/scripted_effects/018_resources_found_cave_effects.txt`, `common/scripted_effects/020_black_plague_rat_effects.txt`, `common/scripted_effects/020_black_plague_evolution_effects.txt`, `common/scripted_effects/031_random_terror_effects.txt`, `common/national_focus/020_black_plague_rat_focus_tree.txt`, and `common/national_focus/020_black_plague_rat_king_focus_tree.txt` now check each starting, focus, or terminal spirit before granting it. The Event 20 King Dominion terminal grant also checks for an existing spirit.

The three Event 20 focus rewards reviewed are `black_plague_rat_feral_quarantine`, `black_plague_rat_no_human_rations`, and `black_plague_rat_king_first_royal_decree`; their flags and variable gains remain intact when the starting idea is already present.

The bounded focus review found that `black_plague_rat_feral_quarantine` and `black_plague_rat_no_human_rations` are sibling focuses with the same prerequisite and no mutual exclusion, so both can be completed. The idea guards prevent regranting their shared spirits, but whether both focuses should remain available is an unresolved route-design question; no route lock was added within this duplicate-grant repair.

Targeted `hoi4.focus_inspect` completed for both Event 20 trees; the Rat Nation tree has no blocking diagnostics, and the Rat King tree has three existing `FOCUS_LAYOUT_LINEAR_DETOUR` warnings for `black_plague_rat_council_selective_harvest`, `black_plague_rat_crown_road_tithe`, and `black_plague_rat_hierophant_flea_liturgy`. No focus coordinates, prerequisites, or branch structure changed, so no render was requested for these reward-only edits.

Event 16's `.303` option in `events/016_brilliant_scientist_aftermath_events.txt` and the `brilliant_scientist_aftermath_exchange_countermeasures` decision in `common/decisions/016_brilliant_scientist_aftermath_decisions.txt` both grant `brilliant_scientist_aftermath_countermeasure_exchange`; both paths now check for the spirit, while their shared completion flag, stability, and treaty progress remain unchanged.

The Event 5 posture and Moscow reintegration paths grant `soviet_collapse_emergency_union_authority` and `soviet_collapse_new_union_negotiations` on more than one later route. The event, decision, and reintegration effect grants in `events/005_soviet_collapse.txt`, `common/decisions/005_soviet_collapse_decisions.txt`, and `common/scripted_effects/005_soviet_collapse_effects.txt` now add those ideas only when missing.

The Event 13 `.13` option and the capitulation fallback `genocide_try_trigger_tribunal_after_defeat` both grant `genocide_tribunal_preparation`; both paths now skip only the repeated grant, while the fallback's stability effect and delayed event remain unchanged.

The repeatable `genocide_enact_sanctions` decision re-enables after 60 days and retains its 60 political-power cost. Its helper now grants `genocide_international_sanctions` only when the target does not already have it; each eligible use still applies `genocide_sanctions_pressure` and raises `genocide_foreign_pressure`, and C6 human-transition cleanup can remove the idea so a later eligible use can grant it again.

The setup functions still add any missing spirit, while a complete history setup receives no second grant and a repeat after the setup flag is set does not enter its setup block. Reused Event 31 and Event 20 carriers can receive the same ideas again after their cleanup removes them, because the new guards test current idea presence rather than only the lifetime marker.

Representative overlapping-path checks retained existing protections: Event 1's immediate and state-control helper grants of `communism_spread_idea` are guarded, its option occurrence is tooltip-only, Event 18's `resources_found_threat_cooperation` grants are guarded, the Event 2 cure branches are mutually exclusive and tooltip-only, and Event 21 removes `event021_war_torn_administration` before its intentional timed refresh while its two permanent profile grants target the government and opposition countries separately.

No zombie stage tier transition was changed; the `zombies_idea_0` through `_3` evolution chain continues to use explicit `swap_ideas` transitions, and the separate timed cure refresh remains intact.

The source-derived repeated-call cases were checked for a complete history set, one missing idea, a subsequent repeated setup call, and a cleaned-and-reused carrier; complete sets add nothing, partial sets add only the missing idea, repeated setup adds nothing, and a cleaned carrier receives its removed starting set again. Event 2 zombie tier transitions still use their existing `swap_ideas` path, and the timed cure and recovery refreshes remain unchanged.

The 27 guarded grant sites cover these 19 idea identifiers: `death_country_without_breath`, `death_first_silence`, `cave_mineral_carapaces`, `cave_slow_blood`, `cave_resource_born_broods`, `cave_surface_starvation`, `cave_untranslatable_command`, `black_plague_rat_brood_instinct`, `black_plague_rat_no_civilian_economy`, `black_plague_rat_fractured_instinct`, `black_plague_rat_king_dominion`, `random_terror_improvised_command`, `random_terror_captured_economy`, `random_terror_contested_legitimacy`, `brilliant_scientist_aftermath_countermeasure_exchange`, `soviet_collapse_emergency_union_authority`, `soviet_collapse_new_union_negotiations`, `genocide_tribunal_preparation`, and `genocide_international_sanctions`.

No country tags, state ids, parties, focus ids, localization keys, formable ids, idea modifiers, or timed idea durations changed; three existing focus reward bodies gained idea-presence guards.

References used for this follow-up: installed `effects_documentation.md` `add_ideas` lines 1410-1418, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`; installed `triggers_documentation.md` `has_idea` lines 4034-4042, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`; offline `Effects - Hearts of Iron 4 Wiki.md` `add_ideas` line 1979, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`; `Idea modding - Hearts of Iron 4 Wiki.md` `Implementation` lines 102-129, revision `a6405eb98a02a9de4689b7c0ef80b5a887b6c6c747d3907f68c109ed3fd099ac`; `National focus modding - Hearts of Iron 4 Wiki.md` `Effects` lines 430-454, revision `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`; and vanilla `common/national_focus/austro_hungarian_releasable_shared.txt` lines 2156-2159, which guards a focus `add_ideas` reward with `has_idea`.

The source-oriented `hoi4.script_validate` calls for the Death and Oth-Kesh scripted-effect files timed out after 600 seconds, as did the targeted `reference_read` and vanilla `source_lookup` calls. The standalone installed documentation folder has no national-focus page, so the installed effect/trigger documentation, offline focus-modelling section, and local vanilla focus example supplied the applicable guidance. Direct source review and `.tmp/handoff3/ideas/verify_scenarios.py` provide the checks for this follow-up; no live-game behavior was observed.

The specific grant inventory and before-source snapshots are retained under `.tmp/handoff3/ideas/`.
