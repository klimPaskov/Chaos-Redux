# Event 016 Country-Specific Institutional Settlement Tranche Addendum

## Status and recommendation

One bounded non-model content tranche is useful.

The current ten-tag country clause layer now continues through `.18`, but it changes presentation rather than player choice.
The smallest causal extension is a four-country pilot inside the existing institutional sequence `chaosx.nr16.5 -> chaosx.nr16.7 / chaosx.nr16.8`.
It adds no event ID, fire path, delay, evolution, cluster entry, decision, focus, GUI, country, scientist, project reward, or asset package.

This is not approval for separate country chains.
Full ladders for all ten named tags would repeat the existing institution reports and add bloat.
The six other named tags keep their current authored presentation and the same complete generic option pool.

## Prior addendum disposition

No earlier accepted Event 016 addendum remains unresolved.
The original improvement recommendations R1 through R7 are fully dispositioned in `016_source_of_truth_map.md`.
The host-context reaction tranche is implemented through `.7`, `.8`, and `.9` and its addendum is closed.
The implemented presentation handoff `subagent_handoffs/016_country_specific_context_flavor_2026-08-02.md` explicitly leaves causal country-specific choices queued.
This addendum therefore addresses a distinct implementation gap and does not layer a second plan over unresolved work.

## Design problem

Britain, the United States, the Soviet Union, and Japan already receive named country clauses in `.4` through `.18`, but the causal slice remains `.4` through `.9` and each country chooses from the same three assistant settlements in `.5`.
The current text recognizes different national institutions without letting those institutions shape a decision or the later facility and method-custody reactions.

The expansion should make one early national research settlement playable for each pilot country, then let that settlement bias rather than determine the first two Prototype governance reactions.
The player must remain free to reject national institutional momentum through the ordinary `.7` and `.8` options.

## Bounded route map

```text
Existing appointment and context event .4
  -> existing delayed assistant conflict .5
      -> existing generic assistant choices remain
      -> one conditional national settlement is available to ENG, USA, SOV, or JAP
          -> host-local settlement receipt and bounded Directorate vector
          -> existing impossible-lecture scheduler remains unchanged
  -> existing first-Prototype facility reaction .7
      -> settlement-specific description clause and AI preference only
  -> existing second-Prototype custody reaction .8
      -> settlement-specific description clause and AI preference only
```

There is no substitute incident when `.7` or `.8` does not qualify.
There is no new country event between these IDs.

## Event `.5` option contract

Add four conditional options to `chaosx.nr16.5`.
The existing `.5.a`, `.5.b`, and `.5.c` options remain available under their present triggers and keep their effects and AI weights.
Each national option must clear `brilliant_scientist_context_assistant_conflict_pending`, set `brilliant_scientist_assistant_conflict_resolved`, call its named settlement resolver, and call `brilliant_scientist_try_schedule_impossible_lecture` exactly once.

| Tag | Option localisation key | Availability | Working direction | Base resolver | Additional named deltas | Host receipt |
| --- | --- | --- | --- | --- | --- | --- |
| `ENG` | `chaosx.nr16.5.d_eng` | `tag = ENG` and public-science or distributed-research context | Charter a DSIR-style research-association compact that protects a professional school while accepting wider observation | `brilliant_scientist_context_recognize_assistant_school` | Exposure `+5`, Independent Capacity `+5` | `brilliant_scientist_country_settlement_british_research_associations` |
| `USA` | `chaosx.nr16.5.e_usa` | `tag = USA` and industrial-mobilization or distributed-research context | Build a federal university-industry contract network with faster delivery and explicit dependence and disclosure costs | `brilliant_scientist_context_mediate_assistant_conflict` | Dependence `+5`, Exposure `+5`, Project Capacity `+10` | `brilliant_scientist_country_settlement_american_federal_contracts` |
| `SOV` | `chaosx.nr16.5.f_sov` | `tag = SOV` and strategic-security or industrial-mobilization context | Put an Academy institute network under the state plan while preserving a limited independent technical cadre | `brilliant_scientist_context_bind_assistant_service` | Dependence `+5`, Project Capacity `+5`, Independent Capacity `+10`, Grievance `+5` | `brilliant_scientist_country_settlement_soviet_academy_plan` |
| `JAP` | `chaosx.nr16.5.g_jap` | `tag = JAP` and strategic-security or industrial-mobilization context | Convene a RIKEN-centered joint technical council whose coordination gains carry military and institutional rivalry costs | `brilliant_scientist_context_mediate_assistant_conflict` | Mandate `+5`, Dependence `+5`, Project Capacity `+5`, Grievance `+10` | `brilliant_scientist_country_settlement_japanese_riken_council` |

The resulting total vectors, including the called base resolver, are fixed as follows.

| Settlement | Mandate | Dependence | Exposure | Project Capacity | Independent Capacity | Grievance |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| British research associations | `+5` | `-10` | `+15` | `+5` | `+20` | `-15` |
| American federal contracts | `+10` | `+5` | `+10` | `+15` | `+5` | `-5` |
| Soviet Academy plan | `+5` | `+20` | `-5` | `+15` | `-5` | `+20` |
| Japanese RIKEN council | `+15` | `+5` | `+5` | `+10` | `+5` | `+5` |

These are deliberate tradeoffs rather than stronger replacements for the generic options.
Britain buys more independent replication with more exposure.
The United States buys delivery capacity with more exposure and dependence.
The Soviet Union preserves part of the technical cadre at the cost of higher dependence and grievance.
Japan buys coordination and capacity at the cost of dependence and service rivalry.

All numeric inputs must live in `common/script_constants/016_brilliant_scientist_country_settlement_constants.txt` under `brilliant_scientist_country_settlement_delta`.
The resolvers must use the existing bounded `brilliant_scientist_change_*` effects.
Do not write direct unclamped variable arithmetic.

## Persistent state and transfer contract

The four settlement flags are host-local institutional history.
They are mutually exclusive because `.5` resolves once.
They are not Kruger character flags and must not create, clone, rename, recruit, or re-scope Doctor Warren Kruger.

Do not add the four flags to `brilliant_scientist_transfer_to_target`, the ordinary context-copy block in `common/scripted_effects/016_brilliant_scientist_effects.txt`, or the KRG formation-copy block in `common/scripted_effects/016_brilliant_scientist_country_effects.txt`.
This is intentional behavior, not a substitute path.

- Transfer before `.5` lets the recipient's current tag determine which national option exists.
- Transfer after `.5` preserves the former host's local settlement receipt while the recipient receives only the already-supported generic assistant outcome and current Directorate state.
- Pending `.7` or `.8` ownership still moves under the implemented reaction contract, but the recipient does not inherit another country's institutional clause or AI momentum.
- Kruger State formation keeps the former host receipt with the former host and uses the existing rule that cancels unresolved `.7` and `.8` incidents.
- Terminal cleanup does not need to clear these inert historical receipts.

## Reactions in `.7` and `.8`

Do not add options or effects to `.7` or `.8`.
The country settlement changes their presentation and AI preference while leaving the player-facing three-way choice intact.

Append `[This.GetBrilliantScientistCountrySettlementFacilityClause]` to all five `.7` description keys and `[This.GetBrilliantScientistCountrySettlementCustodyClause]` to all four `.8` description keys.
Each selector reads the four host-local receipts and ends in an intentionally empty localisation key for countries without a national settlement.

Localisation direction only:

- British `.7`: research associations and grant-holding institutions demand access terms for the primary facility.
- British `.8`: the public research charter makes the second method's custody a dispute between the state and the funded association network.
- American `.7`: federal contractors, universities, and firms press for production, patent, and security terms at the primary facility.
- American `.8`: the second method exposes incompatible contract and patent claims without implying a free project reward.
- Soviet `.7`: the Academy institute and planning organs contest which chain commands the primary facility.
- Soviet `.8`: state ownership of the method does not settle whether technical custody rests with an institute or the executive reserve.
- Japanese `.7`: the RIKEN-centered laboratory structure meets army and navy procurement pressure at the primary facility.
- Japanese `.8`: the joint council's service rivalry returns when custody of a reproducible method must be assigned.

The descriptions must continue to name `[brilliant_scientist_primary_facility.GetName]` in `.7` and `[This.GetBrilliantScientistReactionCustodyProjectName]` in `.8`.
They must not portray real institutions as endorsing Kruger, human experimentation, or atrocities.

## AI contract

Add `brilliant_scientist_country_settlement_ai` to the new constants file with these exact values.

| Key | Value |
| --- | ---: |
| `option_base` | `10` |
| `option_preferred_factor` | `2.25` |
| `option_cautious_factor` | `0.50` |
| `reaction_preferred_factor` | `1.50` |
| `reaction_cautious_factor` | `0.70` |

The four national `.5` options use `option_base` and `option_preferred_factor` in their compatible context.
They may also use the existing mutually exclusive host-archetype factors.

- Britain adds `brilliant_scientist_host_flavor_ai.university` for a university host, then applies `option_cautious_factor` separately at war and at high Exposure.
- The United States adds `brilliant_scientist_host_flavor_ai.industrial` for an industrial host, then applies `option_cautious_factor` separately at high Dependence and high Exposure.
- The Soviet Union adds `brilliant_scientist_host_flavor_ai.militarized` for a militarized host, then applies `option_cautious_factor` separately at high Dependence and high Grievance.
- Japan adds the applicable industrial or militarized host-archetype factor, then applies `option_cautious_factor` separately at high Dependence and high Grievance.

Add only these downstream modifiers.

| Receipt | `.7` preference | `.7` caution | `.8` preference | `.8` caution |
| --- | --- | --- | --- | --- |
| British research associations | Civic compact `x1.50` | Restricted district `x0.70` | Public trust `x1.50` | Executive reserve `x0.70` |
| American federal contracts | Industrial charter `x1.50` | None | Patent pool `x1.50` | None |
| Soviet Academy plan | Restricted district `x1.50` | Civic compact `x0.70` | Executive reserve `x1.50` | Public trust `x0.70` |
| Japanese RIKEN council | Industrial charter `x1.50` | None | Executive reserve `x1.50` | None |

No factor is zero.
Existing high Exposure, high Grievance, high Dependence, war, and accident-pressure factors remain able to reverse the national preference.
Country identity must never force an AI outcome.

No MTTH or scheduling value changes.
The existing `.5`, `.7`, and `.8` delivery paths are sufficient, so the `hoi4-mtth` workflow is not needed for this tranche.

## Historical and regional basis

The internal research foundation is `docs/specs/016_brilliant_scientist_specs/research/016_historical_science_research.md`.
The design also uses these institutional sources.

- Britain: the [Science Museum Group DSIR history](https://collection.sciencemuseumgroup.org.uk/people/ap12254/department-of-scientific-and-industrial-research) records a department that supported universities, technical colleges, research associations, fellowships, and research contracts.
- Britain: the [UK National Archives Tube Alloys catalogue](https://discovery.nationalarchives.gov.uk/details/r/C1616) records cooperation among DSIR, the Ministry of Supply, ICI, universities, and international partners.
- United States: the [Library of Congress OSRD collection history](https://www.loc.gov/collections/office-of-scientific-research-and-development-reports/about-this-collection/) records the NDRC in 1940 and OSRD in 1941, including authority to contract for research and development.
- Soviet Union: the [Russian Academy of Sciences archive history](https://arran.ru/history) records the 1934 transfer of the Academy and many physical, technical, chemical, and biological institutions to Moscow to connect them more directly with government and industry.
- Japan: [RIKEN's institutional history](https://www.riken.jp/en/about/history/story/index.html) records its 1917 public-private foundation, the 1922 autonomous chief-scientist laboratory system, and a commercial network that grew through the 1930s.

Research limits are binding.

- The American option uses the generic term federal contract network before 1940.
  Do not name NDRC or OSRD in pre-1940 player-facing text.
- The Soviet Academy plan is a design compression of the Academy's administrative integration and institute network, not the name of one exact historical committee.
- The Japanese joint technical council is alternate-history institutional design inspired by RIKEN's autonomous laboratory and commercial structure.
  It is not a claim that RIKEN historically operated the proposed council.
- No real scientist becomes Kruger's assistant, supporter, victim, or rival.

## Localisation and asset contract

Implementation adds direction-complete English keys, not copied historical prose.

- Option keys: `chaosx.nr16.5.d_eng`, `chaosx.nr16.5.e_usa`, `chaosx.nr16.5.f_sov`, and `chaosx.nr16.5.g_jap`.
- Effect tooltips: `brilliant_scientist_country_settlement_british_tt`, `brilliant_scientist_country_settlement_american_tt`, `brilliant_scientist_country_settlement_soviet_tt`, and `brilliant_scientist_country_settlement_japanese_tt`.
- Scripted-localisation selectors: `GetBrilliantScientistCountrySettlementFacilityClause` and `GetBrilliantScientistCountrySettlementCustodyClause`.
- Eight receipt clauses and two intentionally empty keys are required, one facility and one custody clause per pilot settlement.

The tooltips must disclose all visible meter changes numerically and describe Independent Capacity and Grievance in player-facing institutional language.
They must not mention implementation history, hidden variable names, or balance adjustments.

The existing `GFX_report_event_016_brilliant_scientist_university_competition` for `.5` and `GFX_report_event_016_brilliant_scientist_directorate_dossier` for `.7` and `.8` are the intended final images.
This is deliberate reuse of the same institutional incidents.
No DDS, sprite registration, icon, flag, portrait, animation, audio, super-event, or 3D model is required.
No visual substitute or transform-only animation is proposed.

## Exact implementation surfaces

| File | Required identifiers and edits |
| --- | --- |
| `events/016_brilliant_scientist_context_events.txt` | Add the four conditional options to `chaosx.nr16.5` and preserve `.5.a` through `.5.c` |
| `events/016_brilliant_scientist_host_reaction_events.txt` | Add only the receipt-driven AI modifiers to `chaosx.nr16.7` and `.8` |
| `common/scripted_effects/016_brilliant_scientist_context_effects.txt` | Add four country-settlement resolvers that call the named base resolver and apply the exact additive vector |
| `common/script_constants/016_brilliant_scientist_country_settlement_constants.txt` | Add all delta and AI tuning values named in this plan |
| `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt` | Add the facility and custody receipt selectors with intentional empty branches |
| `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` | Add the four options, four tooltips, eight receipt clauses, and two empty keys, then append the selectors to `.7` and `.8` descriptions |
| `docs/events/016_brilliant_scientist/overview.md` | Record the four-country pilot and its non-expansion boundary |
| `docs/events/016_brilliant_scientist/systems/directorate.md` | Document option gates, vectors, receipts, transfer behavior, downstream AI, and asset reuse |

Do not edit the opening event, event registration arrays, evolution log, event log, project ledger, KRG character definition, country history, focus tree, decisions, scripted GUI, map data, or super-event files for this tranche.

After final localisation, compare Event 16's row in `docs/spreadsheets/chaos_redux_events_catalog.xlsx` with the implemented Event Details wording.
If the row does not enumerate the assistant conflict, record a no-change spreadsheet handoff.
If it does enumerate the conflict, update the workbook source and run `.tools/export_event_catalog_csv.py`.
Never edit the exported CSV files directly.

## Acceptance and balance scenarios

1. An `ENG` host in public-science or distributed-research context sees `chaosx.nr16.5.d_eng` alongside the valid generic options.
2. Selecting the British option applies the assistant-school base vector and exactly the additional Exposure and Independent Capacity deltas, sets only the British receipt, resolves `.5`, and schedules the impossible lecture at most once.
3. `USA`, `SOV`, and `JAP` each receive only their own national option under the exact compatible context gate, and each resolver produces the total vector in this plan.
4. An incompatible context hides the national option while leaving at least one generic `.5` option valid.
5. `GER`, `FRA`, `ITA`, `CHI`, `POL`, `CZE`, and every unnamed country retain the current complete generic `.5` choice set and country presentation clause.
6. `.7` still applies exactly one civic, restricted, or industrial result and `.8` still applies exactly one public-trust, executive-reserve, or patent-pool result.
7. National receipts change only the added description clause and the named AI factors in `.7` and `.8`.
8. Transfer before `.5` uses the recipient's tag.
   Transfer after `.5` does not copy the national receipt, does not replay `.5`, and does not attach the former host's institution to the recipient.
9. KRG formation and terminal cleanup preserve the existing pending-reaction and character-identity contracts without any new Kruger identity or reward.
10. All report pictures resolve to the currently registered `.5`, `.7`, and `.8` sprites, with no new texture or model reference.

The implementation balance pass must inspect the complete `.5`, `.7`, and `.8` option pools with `hoi4.probability_inspect` and `hoi4.probability_evaluate` under these named states.

| Scenario | Required ordering |
| --- | --- |
| Peaceful democratic British university host, public-science context, low Exposure | British research associations ranks first, generic assistant school remains nonzero and second-order competitive |
| British host at war with high Exposure | The British option falls below at least one compatible generic option |
| Peaceful democratic American industrial host, industrial-mobilization context, low Dependence and Exposure | Federal contracts ranks first, cabinet mediation and classified service remain nonzero |
| American host with high Dependence or high Exposure | Federal contracts loses first rank to a compatible generic option |
| Soviet militarized host, strategic-security context, low Dependence and Grievance | Academy plan ranks first but classified service remains competitive |
| Soviet host with high Dependence and high Grievance | Academy plan loses first rank |
| Japanese industrial or militarized host, industrial-mobilization context, low Dependence and Grievance | RIKEN council ranks first but cabinet mediation and classified service remain nonzero |
| Japanese host with high Dependence or high Grievance | RIKEN council loses first rank |

For `.7` and `.8`, confirm the direction in the downstream AI table and confirm that the existing high-pressure modifiers can reverse it.
Do not report normalized percentages unless the inspector proves the complete candidate pool and every scenario input.

## Tooling evidence and limitation

Direct source inspection establishes the existing `.5` option pool, `.7` and `.8` reaction choices, transfer copy behavior, scripted-localisation tag selector, and current assets.
A read-only Event Chain Viewer trace and options render for `chaosx.nr16.5` returned partial artifacts because the repository-wide graph exceeded the bounded inline view.
That partial result is not used as completion evidence and does not replace the source review.

The installed package has no separate Technology Tree Viewer.
This limitation does not affect the tranche because it adds no technology, doctrine, technology bonus, or unlock.
No focus, GUI, or map inspection was needed because those systems are outside the design.

## Promotion and closure recommendation

Keep this file in `docs/plans/016_brilliant_scientist_plans/` until the parent accepts or rejects the tranche.
If accepted, promote the contract into:

- `specs/016_brilliant_scientist_spec_part_1_core.md`
- `specs/016_brilliant_scientist_spec_part_2_host_directorate_and_decisions.md`
- `specs/016_brilliant_scientist_spec_part_4_evolutions_and_event_chain.md`
- `specs/016_brilliant_scientist_spec_part_7_world_reactions_and_ai.md`
- `matrices/016_event_chain_map.md`
- `matrices/016_ai_behavior_matrix.md`
- `acceptance/016_acceptance_criteria.md`
- `acceptance/016_balance_and_exploit_review.md`

After implementation and audit, update `handoffs/016_completion_status.md` and `016_core_runtime_handoff_map.md` with the exact disposition.
Do not run another improvement-loop pass for country-specific reactions while this addendum is unresolved.

Further per-tag event chains should stop here unless a later concrete country package supplies a distinct mechanic that cannot be expressed through the existing institutional sequence.
Germany, France, Italy, China, Poland, and Czechoslovakia do not need copied national options merely for symmetry.
Routine institutional choices do not justify a super-event, bespoke art family, new GUI surface, or model package.

## Parent handoff

- Design problem: the ten-tag layer is presentation-only, so national institutions do not yet alter a player choice or later reaction.
- Proposed expansion: four conditional settlement choices inside `.5`, followed by receipt-driven presentation and AI momentum in existing `.7` and `.8`.
- Research basis: British DSIR grant and research-association practice, American federal contracting through the later NDRC and OSRD model, Soviet Academy integration with central planning after the 1934 move, and RIKEN's autonomous laboratories and commercial network.
- Historical limits: American wartime office names are date-sensitive, the Soviet plan and Japanese joint council are design compressions, and no real scientist is attached to Kruger.
- Files written: this addendum only.
- Implementation surfaces: Event 016 context events, host-reaction events, context effects, one new constants file, host-flavor scripted localisation, Directorate localisation, Event 016 docs, and accepted spec and matrix promotion.
- Open questions: none required for implementation.
- Prior addendum unresolved: no.
- Plan disposition: remain in `docs/plans` until accepted, then promote the accepted contract into `docs/specs` before or with implementation.
