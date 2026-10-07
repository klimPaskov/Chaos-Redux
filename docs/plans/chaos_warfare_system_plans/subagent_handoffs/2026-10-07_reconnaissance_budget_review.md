# CBRN reconnaissance budget review

Disposition: accepted and implemented by the parent after this read-only review, with native reconnaissance semantics unresolved.
The source table and pre-change discussion below retain the captured review baseline; the selected allocation is implemented in the [accepted correction](../../../specs/chaos_warfare_system_specs/corrections/2026-10-07_reconnaissance_combined_budget.md) and verified by the [221-check source audit](2026-10-07_reconnaissance_budget_source_checks.md).
This read-only follow-up addresses an omitted reconnaissance combination after the doctrine reward and mastery revisions in commits `7b27f8e8` and `56429bca0`.
Only this handoff was written.
No gameplay, shared documentation, index, icon, AI, or runtime source was changed.

## Finding and acceptance basis

The present reconnaissance stack exceeds 35% under every reviewed straightforward source model, although exact native accumulation has not been established.
Weather technology alone is not the complete budget.
The 137-check combat audit covers soft attack, hard attack, breakthrough, defense, and organization, and does not prove a reconnaissance ceiling.

The user-approved `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md:5,55` establishes the general combined dedicated-CBRN static ceiling of 35%.
Its wording does not specifically name reconnaissance, prescribe a reconnaissance formula, or separately resolve utility versus combat stats.
`docs/systems/cbrn_warfare/chaos_warfare_doctrine.md:203` records that an earlier parent resolved that general ceiling to include reconnaissance utility.
The same interpretation is present in the system document at commit `7b27f8e8`, where its table compares the three weather grants alone with the 35% ceiling.
That is documented parent interpretation within the overhaul, rather than a separately located explicit user reconnaissance decision.
The bounded source search found no accepted-spec correction explicitly spelling out a total reconnaissance ceiling including doctrine and HQ modifiers.
For this discovered combination, the parent explicitly accepted the earlier conservative 35% total-reconnaissance interpretation on 2026-10-07 and accepted the allocation below within the original combined-budget scope.
The parent acceptance preserves the committed 25% adoption reward and identifies the secondary numerical reductions as a budget correction, not a new HQ capability or policy.
This is the current acceptance basis recorded in this handoff, rather than an assertion that the earlier accepted spec separately named reconnaissance.

The newer accepted correction, `docs/specs/chaos_warfare_system_specs/corrections/2026-10-07_doctrine_reward_mastery.md:3-5,16-17`, expressly preserves the existing 25% Operations adoption allowance and all other authored stats and milestone effects.
It does not explicitly rescind or redefine the earlier reconnaissance interpretation.
The parent's follow-up acceptance resolves the current source-budget interpretation and allocation while leaving native field semantics open.
Documentation cleanup alone must not promote a weather-only calculation into combined proof or silently exclude HQ reconnaissance from a combined ceiling.

## Exact contributing source and legal composition

| Source | Exact field and value | Scope and recipient |
| --- | --- | --- |
| `common/doctrines/subdoctrines/land/chaos_warfare_operations_subdoctrines.txt:18,77` | `@CBRN_INTEGRATED_COMMAND_ACTIVATION_RECON = 0.25`, used as `recon_factor` | Country adoption modifier, not a company-category reward |
| `common/script_constants/cbrn_doctrine_constants.txt:233` | `operations_adoption_recon = 0.25` | Shared mirror of that existing allowance |
| `common/technologies/chaosx_technologies.txt:57-59,1051-1073` | `recon = 0.20`, `0.40`, `0.60` | `category_cbrn_reconnaissance` grants from `portable_anemometer`, `meteorological_stations`, `upper_air_soundings` |
| `common/units/cbrn_regimental_support.txt:52,243,257` | Base `recon = 4.00` | Chemical Reconnaissance Detachment is the sole retained member of that CBRN category |
| `common/units/cbrn_regimental_support.txt:115,603-607,621` | Base `recon = 2.00` | Field Medical Support. It is not in `category_cbrn_reconnaissance` or `category_recon` |
| `common/units/cbrn_hq_support.txt:33,75-77` | Operations HQ `recon_factor = 0.15` | `deployed_leader_modifiers`, alongside planning speed 0.05 |
| `common/units/cbrn_hq_support.txt:49,197-200` | Medical HQ `recon_factor = 0.10` | `deployed_leader_modifiers`, alongside wound and sickness reduction of 0.30 each |

All three weather grants are reachable through the visible instrument research chain.
Chemical Detection Paper grants `portable_anemometer` at `chaosx_technologies.txt:1197`, Mobile Sampling Laboratories grants `meteorological_stations` at line 1238, and Theater CBRN Command Set grants `upper_air_soundings` at line 1279.
They are not mutually exclusive alternatives.
Their hidden research flags and date labels do not impose a lifetime exclusion between their stat grants.

Operations and Medical HQ sections have different unit IDs, are HQ-only, and have no authored mutual exclusion or shared `same_support_type` lock in `cbrn_hq_support.txt:52-243`.
`common/scripted_triggers/cbrn_hq_triggers.txt:89-93` explicitly checks all three sections on the current leader.
`common/scripted_effects/cbrn_achievement_effects.txt:207-213` calls that check inside one `any_army_leader` scope, establishing that the package expects the Operations, Protection, and Medical sections to coexist in one command.
The vanilla `common/units/hq_support.txt:112-146` likewise supplies an HQ-only `hq_recon` company with `deployed_leader_modifiers.recon_factor = 0.10`.
These sources support the legal same-command combination of one Operations and one Medical section.
They do not establish native fill scaling, duplicate-company behavior, deployed-commander modifier accumulation, or field-marshal propagation.
The calculations below use one equipped instance of each relevant section and do not fabricate extra HQ copies.

A broad unfiltered scan of `common/**/*.txt` for `recon_factor` and `recon_factor_while_entrenched` found no additional CBRN-authored factor in a differently named leader or idea file.
The remaining mod matches belong to Events 012, 014, 018, and 087.
Examples are `cannibalism_commander_suspicious_tyrant` in `common/unit_leader/014_cannibalism_traits.txt:93-99` and the Event 018 cave senses ideas.
They are separate event effects, not missing CBRN advisor grants, and are not edited or assumed to vanish.
Ordinary vanilla reconnaissance research, vanilla HQ Recon, generic leaders, and other event modifiers must be retained equally in both sides of a comparison of the CBRN-authored benefit.
The reviewed CBRN historical/high-command traits, officer-corps spirits, HQ status traits, and CBRN MIO files add no further `recon_factor` grant.

## Flat points, percentage factors, and evidence limits

The offline wiki `Modifiers:973` explicitly calls `recon_factor` percentual.
The installed modifier documentation at lines 4537-4541 confirms its recognized name and army/defensive categories, but gives no accumulation formula.
The deployed HQ fields and country doctrine use this factor, rather than a flat company `recon` field.

The existing owner interpretation and source comment treat the three weather technology values as flat reconnaissance points.
Vanilla `common/technologies/support.txt:536-543` uses `category_recon = { recon = 2 }` and a separate helicopter grant of `recon = 1`.
Vanilla `common/technologies/infantry.txt:2789-2792` supplies a further `category_recon = { recon = 1 }` precedent.
The offline `Unit modding` snapshot at lines 308-317 lists `recon = 1` as a unit reconnaissance stat.
These sources support the current flat-point reading and allow fractional numeric point increments.
They do not explicitly document every field-specific technology exception or prove the resulting native value.

There is a reference limitation to retain: the offline `Technology modding` snapshot at line 105 generically calls sub-unit modifiers multiplicative and does not enumerate the reconnaissance exception.
That generic sentence must not be cited as proof that all `recon` fields are flat.
The flat-point allocation below is a source-model proposal grounded in the vanilla precedents and prior owner interpretation.
It is not engine verification.
If native technology `recon` proves fractional instead, its budget must be recomputed rather than presenting the flat-point result as a pass.

Chemical Reconnaissance also carries `category_recon`, so ordinary vanilla reconnaissance technology can add to its equal-baseline stat.
Field Medical carries neither reconnaissance category and receives no weather or ordinary category-recon grant from that membership.
Country and deployed-leader factors can still affect the field medical reconnaissance contribution.
No reviewed source proves how several companies' reconnaissance becomes the final division statistic or battle advantage.
The following arithmetic therefore describes per-company inputs, rather than claiming a summed division reconnaissance or tactic-selection probability.

## Current combined arithmetic

Take a legal comparison with Chemical Reconnaissance base 4, all three weather grants, Operations adoption, and one each of Operations and Medical HQ in the same command.
Treat unrelated research, leaders, and other events as the same baseline on both sides.

| Combination | Explicit model | Authored benefit |
| --- | --- | --- |
| Weather only | `(4 + 0.20 + 0.40 + 0.60) / 4` | +30% |
| Weather and adoption, no HQ | `1.30 * 1.25` | +62.5% |
| Adoption and Operations HQ, no weather | `1.25 * 1.15` | +43.75% |
| Adoption and Medical HQ, no weather | `1.25 * 1.10` | +37.5% |
| Adoption and both HQ factors pooled together, no weather | `1.25 * (1 + 0.15 + 0.10)` | +56.25% |
| Weather, adoption, and HQ factors pooled together | `1.30 * 1.25 * 1.25` | +103.125%, producing an input of 8.125 from base 4 |
| Weather, adoption, and each HQ factor reserved independently | `1.30 * 1.25 * 1.15 * 1.10` | +105.5625%, producing an input of 8.2225 from base 4 |
| Field Medical, adoption, and pooled HQ factors | `2 * 1.25 * 1.25` | Input 3.125, or +56.25% on its unchanged base 2 |
| Field Medical, adoption, and independent HQ factors | `2 * 1.25 * 1.15 * 1.10` | Input 3.1625, or +58.125% |

Even a hypothetical single pool for all percentage factors would give adoption plus HQs +50% before weather technology.
The 35% issue therefore does not depend on deciding whether country and leader percentage factors form one pool or separate layers.
The final engine result remains unverified, but there is no supported source calculation that lets both existing HQ factors coexist with the full 25% adoption reward under a total 35% utility allowance.

If the equal-baseline reconnaissance stat were 10 after ordinary vanilla research, the weather, adoption, and pooled-HQ comparison would be `11.2 / 10 * 1.25 * 1.25 = 1.75`, still +75%.
This is an illustrative baseline, not a claimed exact vanilla technology maximum.
Additional equal-baseline research cannot make adoption plus the two CBRN HQ factors alone fit 35%.

## Accepted bounded allocation under the 35% source interpretation

Preserve the full 25% adoption reward and retain the real roles of both HQ sections.
The parent's candidate is feasible under the existing flat-point reading and the conservative independent-layer source model.
It requires five existing numeric changes and no new script, modifier, helper, or administration system.

| Existing constant | Current | Proposed | Explicit reduction |
| --- | ---: | ---: | --- |
| `@CBRN_HQ_OPERATIONS_RECON` | 0.15 | 0.04 | 15% to 4%, down 11 percentage points |
| `@CBRN_HQ_MEDICAL_RECON` | 0.10 | 0.02 | 10% to 2%, down 8 percentage points |
| `@CBRN_WEATHER_RECON_BASIC` | 0.20 | 0.01 | Down 0.19 flat points |
| `@CBRN_WEATHER_RECON_IMPROVED` | 0.40 | 0.02 | Down 0.38 flat points |
| `@CBRN_WEATHER_RECON_ADVANCED` | 0.60 | 0.03 | Down 0.57 flat points |

Weather's total reconnaissance increment falls from 1.20 to 0.06 points, a 95% reduction of that secondary grant.
This is a substantial explicit reallocation to preserve the immediate 25% doctrine payoff, not a numerically unchanged consolidation.
The combined country and independent HQ factors become `1.25 * 1.04 * 1.02 = 1.326`.
Weather's flat-point factor becomes `4.06 / 4 = 1.015`.
The complete point-model bound is `1.015 * 1.25 * 1.04 * 1.02 = 1.34589`, or +34.589%.
Even normalizing each weather point grant independently gives `1.0025 * 1.005 * 1.0075 * 1.25 * 1.04 * 1.02 = 1.3459812868125`, or +34.59813%.
Field Medical's corresponding input becomes `2 * 1.326 = 2.652`, or +32.6% over base 2.
Both reviewed flat-point source bounds fit the interpreted 35% total reconnaissance allowance.

This recommendation reduces secondary numerical reconnaissance only.
It preserves Operations HQ planning speed 5%, all HQ ability IDs and unlock chronology, and Medical HQ wound/sickness reductions of 30% each.
The sections retain their exact manpower, equipment, training, transport and supply bills, including the Operations and Medical roles' original costs.
The three instrument technologies retain their names, grant path, date gates, visible equipment research, and equipment unlocks.
All mastery contributors, AI coefficients, doctrine costs, policy authorization, main icon, and committed assault/projector changes remain intact.
There is no change to Field Medical's base 2 or Chemical Reconnaissance's base 4.
Native database values stay in their existing file-local constants because arbitrary shared constant tokens are not established for these unit and technology fields.

If technology `recon` were interpreted as fractional rather than flat, the same `.01/.02/.03` candidate would instead reserve `1.06 * 1.25 * 1.04 * 1.02 = 1.40556`, exceeding 35%.
That is why this candidate must carry its field-semantic limitation and cannot be called native cap proof.
A semantics-agnostic extra-conservative variant could use technology increments `.0025/.005/.0075`, totaling .015, while retaining HQ 4% and 2%.
It fits the above conservative bound even when those increments are treated as percentage fractions, but it nearly removes the weather stat reward under the existing flat-point reading.
That variant is a weaker explicit alternative and is not recommended without a parent decision to reserve both interpretations.
No such fallback was implemented.

The parent has accepted this total reconnaissance interpretation and the preferred allocation, including the explicit secondary reductions above.
Preserving the current 25% adoption plus existing HQ 15% and 10% is incompatible with a strict total 35% allowance in the reviewed source models, even if all weather bonuses are removed.
No source-only workaround should promise those same three numbers and a 35% combined result.

## Validation, MCP reference evidence, and handoff limits

The actual source definitions, consumers, category memberships, hidden grants, same-command expectations, and vanilla precedents above were read directly.
Arithmetic was evaluated from those existing values without creating a script, helper, test, or report generator.
The broad factor scan included non-CBRN filenames to avoid omitting a package trait solely by naming.
The final exact-token pass confirmed that the five proposed constants feed only their existing native technology stat or deployed-HQ factor fields.
No trigger, ability gate, readiness calculation, policy check, or scripted-effect call site consumes those numeric constants.
The HQ role predicates use exact section counts, and doctrine recorders unlock the same section IDs.
Thus changing these five numbers preserves the reviewed role hooks without renaming a capability or substituting an implementation.
No omitted CBRN reconnaissance grant was found in the reviewed mod source.
No generic test count is used as reconnaissance evidence.

Live `hoi4.reference_search(query=deployed_leader_modifiers)` returned no installed/offline section match.
Native HQ accumulation therefore remains an exact documentation coverage gap, with the installed vanilla HQ source supplying precedent rather than an engine-rule substitute.
Live `hoi4.reference_read` read installed `documentation/modifiers_documentation.md:4537-4541`, revision `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e`.
It also read offline `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md:971-974`, revision `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f`.
The relevant Unit and Technology modding snapshot sections were read locally for the stat name and generic technology-rule limitation.
No online Paradox wiki was accessed.

The parent's saved native inspection artifact is `docs/testing/2026-10-07_reconnaissance_budget_review/portable_anemometer_explain.json`, revision `dd8c2c6b9ac09d6e927fe3328c8c7c0f1ef33a3c2e0f784ccfe4a1d31ee30314`.
It returned `TECH_INSPECTED_PARTIAL`, resolves the hidden source, grant consumers and icon, but contains `matchingBonuses = []` and deferred helper projections.
The artifact was read and does not establish a numeric grant or accumulation proof.
No duplicate technology inspection or probability call was launched for this follow-up.

Source SHA-256 snapshots:

| File | Revision |
| --- | --- |
| `common/units/cbrn_hq_support.txt` | `0ed4ceab08bf248369d3abb3c3a8b153b3529fa0156faaa465ff0e3501b627ff` |
| `common/units/cbrn_regimental_support.txt` | `45e062f4b4878ba481dd8ebfbbbf039f3d576de37853e3bf331d91668eedb8e8` |
| `common/technologies/chaosx_technologies.txt` | `7cd703a7ef6639189115ff21b805ab025fa4c27cfa65fba6a73ec371ece5b9f7` |
| `common/doctrines/subdoctrines/land/chaos_warfare_operations_subdoctrines.txt` | `68bc949e8bb77591c6c9248036a17bc098c220fbd89183c0badd8781879ecd95` |

Skills applied: `chaos-redux-events` for preserving real capability and reporting weakening, and `chaos-redux-subagents` for read-only ownership, acceptance provenance, and parent review.
No helper, constant, call site, cleanup hook, or source patch was implemented.
The proposal identifies the necessary field allocation without adding an event target, variable lifecycle, recurring hook, or central wrapper.
The report is complete as a bounded source and contract review.
Native accumulation and exact company/division reconnaissance output remain unresolved.
No gameplay completion, fallback implementation, game launch, or commit is claimed.
