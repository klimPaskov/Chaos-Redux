# Condemnation and Sanctions

## Purpose

Condemnation is the shared consequence layer for publicly known unconventional warfare and exposed atrocity systems. It records why a country is condemned, converts the public total into seven tiers, scores potential sanction participants, creates native embargo relations where the engine supports them, applies scalable economic and diplomatic restrictions, and gives targets and participants concrete response choices.

This document describes the implemented system. The accepted design source remains `docs/specs/condemnation_system_specs/specs/condemnation_impact_system_spec.md`. When the design spec and implementation differ, this document names the implemented behavior and records the difference under limitations or validation risks.

## Source-of-truth map

| Surface | Source of truth |
| --- | --- |
| Accepted design | `docs/specs/condemnation_system_specs/specs/condemnation_impact_system_spec.md` |
| Shared tuning | `common/script_constants/condemnation_sanctions_constants.txt` |
| Country state, source gains, tiers, pair scoring, native embargo ownership, decay, cleanup, and scalable penalties | `common/scripted_effects/condemnation_sanctions_effects.txt` |
| Compliance, defiance, and evasion effects | `common/scripted_effects/condemnation_response_effects.txt` |
| Tier, cost, pair-validity, and relation-rule triggers | `common/scripted_triggers/condemnation_sanctions_triggers.txt` |
| New lend-lease diplomacy gates during arms sanctions | `common/scripted_triggers/zz_condemnation_diplomacy_overrides.txt` (late-load override of the vanilla trigger names) |
| Target and participant decisions | `common/decisions/condemnation_sanctions_decisions.txt` |
| Decision category visibility | `common/decisions/categories/condemnation_sanctions_categories.txt` |
| Scalable target and participant penalties | `common/dynamic_modifiers/condemnation_sanctions_dynamic_modifiers.txt` |
| Timed response ideas | `common/ideas/condemnation_sanctions_ideas.txt` |
| Supporting diplomatic memory | `common/opinion_modifiers/condemnation_sanctions_opinion_modifiers.txt` |
| Targeted diplomatic lifecycle hooks | `common/on_actions/condemnation_sanctions_on_actions.txt` |
| Self-scheduling monthly pulse and native embargo release dispatchers | `events/condemnation_sanctions_events.txt` |
| Condemnation list and selected-country UI snapshot | `common/scripted_effects/chaos_meter_effects.txt` |
| Condemnation UI interaction | `common/scripted_guis/chaosx_scripted_gui_chaos_meter.txt` |
| Condemnation UI layout | `interface/chaosx_chaos_meter_popup.gui` |
| Dynamic UI text selection | `common/scripted_localisation/chaosx_scripted_localisation_chaos_meter.txt` |
| Player-facing UI and decision wording | `localisation/english/condemnation_sanctions_l_english.yml` and `localisation/english/chaosx_chaos_meter_l_english.yml` |
| Chemical source adapters | `common/scripted_effects/chemical_warfare_effects.txt`, `common/scripted_effects/chemical_ability_effects.txt`, `common/scripted_effects/chemical_air_bomb_effects.txt`, `common/scripted_effects/chemical_infantry_effects.txt`, `common/scripted_effects/chemical_tank_shell_effects.txt`, `common/scripted_effects/chemical_livens_support_effects.txt`, and `common/scripted_effects/JAP_chemical_campaign_effects.txt` |
| Biological and weaponized-zombie source adapters | `common/scripted_effects/biowarfare_effects.txt` and `common/scripted_effects/zombie_special_project_effects.txt` |
| Nuclear and thermonuclear source adapter | `common/scripted_effects/chaos_meter_effects.txt` |
| Camp, experiment-site, restricted-site, and destroyed-record discovery adapters | `common/scripted_effects/genocide_crisis_effects.txt` |
| Mengele-linked atrocity and coverup adapters | `common/scripted_effects/germany_mengele_effects.txt` |
| Final Silence nuclear source adapter | `common/scripted_effects/003_holy_realm_effects.txt` |
| Air Cleanliness Treaty embargo owner | `common/scripted_effects/chaos_meter_effects.txt` |
| Great Embargo event owner | `events/050_the_great_embargo.txt` |

## Data model

### Public country record

The public total is recalculated from six visible components:

```text
condemnation_total = condemnation_chemical
                    + condemnation_biological
                    + condemnation_nuclear
                    + condemnation_atrocity
                    + condemnation_coverup
                    + condemnation_repeat_use
```

The total is clamped from `0` to `1000`. Each source bucket is clamped from `0` to `1000`. `condemnation_repeat_use` is capped at `200`, and `condemnation_recent_gain` is capped at `300`.

The country record also stores:

- `condemnation_tier` and `condemnation_next_threshold`
- `condemnation_peak_tier`
- `condemnation_recent_gain`
- `condemnation_decay_credit`
- `condemnation_sanction_pressure`
- `condemnation_evasion_pressure`
- `condemnation_black_market_exposure`
- `condemnation_compliance_state`
- `condemnation_recent_civilian_deaths`
- `condemnation_contamination_pressure`
- last-source type, context, gain, victim, and date
- participant counts, weighted shares, practical-penalty values, and average fatigue

`condemnation_peak_tier` is persistent tier memory. It adds `4` participant-score points per historical tier and is also exposed in the detail UI.

### Hidden evidence

Hidden evidence is stored outside the public total:

- `condemnation_hidden_chemical`
- `condemnation_hidden_biological`
- `condemnation_hidden_nuclear`
- `condemnation_hidden_atrocity`
- `condemnation_hidden_coverup`
- `condemnation_hidden_total`

Before visibility and severity, optional civilian-death and contamination inputs scale the source:

```text
scaled base = base
            + min(civilian deaths / 10000, 100)
            + min(contamination pressure x 0.50, 50)
```

Visibility then controls the public and hidden split:

| Visibility | Public share | Hidden share |
| --- | ---: | ---: |
| Hidden | `0%` | `100%` |
| Suspected | `35%` | `65%` |
| Discovered | `75%` | `25%` |
| Public | `100%` | `0%` |

Severity then multiplies the source value:

| Severity | Multiplier |
| --- | ---: |
| Minor | `0.75` |
| Combat | `1.00` |
| Major | `1.35` |
| Mass death | `1.75` |
| Doomsday | `2.50` |

Active inspections disclose `10%` of each remaining hidden bucket on each targeted monthly pulse. Active observers disclose `5%` of each remaining hidden bucket. Chemical disclosure applies that fraction independently to the offender's append-only exact action rows and transfers only the amount reconciled to those rows; unmatched aggregate Chemical liability remains hidden rather than being assigned to an inferred action. The exposed amount becomes public, updates recent gain, records a public source entry, recalculates the tier, and can refresh participants.

Camp operation, restricted-site operation, and concealment effects accumulate canonical hidden atrocity or cover-up evidence before discovery. A camp or restricted-site discovery exposes `100%` of the stored hidden atrocity and cover-up buckets, then adds the public discovery source calculated for that state.

### Recent source log

Each country keeps four aligned arrays with the eight most recent public source changes:

- `condemnation_source_log_types`
- `condemnation_source_log_contexts`
- `condemnation_source_log_gains`
- `condemnation_source_log_dates`

New entries are inserted at index `0`. Hidden evidence enters this log only when some of it becomes public. The selected-country UI snapshot exposes the three newest source types, gains, and dates, with the latest entry's context and severity in the tooltip. The eight-entry arrays remain the authoritative recent-source history.

### Pair record

The condemned target owns participant arrays. The sanctioning participant owns a dynamic record keyed by the target country id:

- tier
- score
- trade dependency estimate
- strategic-resource dependency estimate
- moral pressure
- enforcement cost
- start date
- review expiry date
- carve-out, quiet-breach, tight-enforcement, abstention, and shield expiry dates

The target arrays separate all active sanctioners from arms, strategic, total, and pariah participants. Separate arrays track likely participants, abstainers, shields, humanitarian carve-outs, quiet breaches, and tightened enforcement.

## Source contexts and source integrations

The shared helper is `condemnation_add_source`. Callers provide source type, base gain, visibility, severity, optional deaths, optional contamination, optional victim country, and a context id. A verified no-release attempt may additionally supply temporary `condemnation_source_is_no_release_attempt` proof; the helper then records evidence-backed Condemnation without writing repeat-use, pledge-breach, stockpile-restriction-breach, recent-use, or `used_unconventional_weapon` history, and clears that one-shot proof before returning.

| Context | Implemented source |
| --- | --- |
| `chemical_combat` | General abilities, Livens support, and chemical tank support after real combat use |
| `chemical_air_strike` | Sarin and soman raids, plus enabled chemical air-bomb runtime |
| `chemical_doomsday` | Full chemical stockpile release, scaled from acute stockpile points |
| `biological_strike` | Tactical biological strikes |
| `biological_outbreak` | Strategic outbreak operations and spreading biological attacks |
| `biological_doomsday` | Full biological stockpile release |
| `weaponized_zombies` | Hostile weaponized-zombie deployment |
| `nuclear_strike` | Normal nuclear strike |
| `thermonuclear_strike` | Thermonuclear strike |
| `final_silence` | Final Silence terminal nuclear release |
| `camp_discovery` | Discovered concentration camp, extermination camp, or gulag evidence |
| `experiment_site` | Exposed experiment or Mengele-linked site |
| `restricted_chemical_site` | Discovered restricted chemical site |
| `inspection_disclosure` | Hidden evidence made public through inspections |
| `observer_report` | Hidden evidence made public through foreign observers or an observer-linked source |
| `camp_operation` | Hidden atrocity evidence accumulated by camp or gulag operation |
| `restricted_site_operation` | Hidden atrocity evidence accumulated by an active restricted chemical site |
| `destroyed_records` | Exposed evidence destruction or other public coverup record |
| `blocked_inspection` | Refusal of inspections |
| `black_market_exposure` | Exposed evasion or participant breach |
| `pledge_breach` | A public source that also breaks a non-use pledge or source-specific stockpile restriction |
| `concealment_operation` | Hidden cover-up evidence accumulated by internal concealment actions |
| `unspecified` | Default when a caller does not set a context |

Pledge-breaking logic adds fixed coverup and repeat-use values inside the original source call and labels that triggering source-log entry `pledge_breach`. It does not write an additional pledge-breach row for the fixed values.

Important source behavior:

- A repeated public use within the `180` day recent-use window adds `25%` of the new public gain to `condemnation_repeat_use`.
- Breaking a non-use pledge or a source-specific stockpile restriction adds `35` coverup and `25` repeat-use pressure, then creates `365` days of pledge-break memory.
- Repeat-use, pledge-breaking, unconventional-use memory, and source-specific stockpile-restriction breaches are gated by explicit chemical, biological, nuclear, thermonuclear, or Final Silence use contexts. Camp evidence, experiment-site evidence, restricted-site discovery, inspection disclosure, coverups, and evasion exposure can block decay as recent public conduct but cannot masquerade as weapon use.
- Chemical combat gain remains source-specific and is reduced by Integrated Chemical Operations multipliers. State-based ability, tank, infantry, Japan-campaign, and air-raid paths capture the affected controller as the victim when that scope exists; chemical raids use their explicit `victim_country` scope. These adapters also pass measured civilian deaths and contamination where available, so the shared casualty and contamination terms can increase the gain. Combat-result on-actions that expose only the acting unit owner cannot identify an opposing country unless their state scan supplies one. Use only against zombie-held fronts is exempt.
- Japan's state-targeted China campaign decision consumes cylinders, contaminates the target, and calls the shared chemical-use helper. It uses its own reduced base and per-cylinder values, supplies the target owner and contamination measurement, and invokes the Air Cleanliness Treaty use hook. Japan's general-led cylinder use against Chinese targets remains a separate reduced-condemnation path.
- Chemical doomsday release uses a base of `40`, adds acute stockpile points divided by `1000`, caps that scaling addition at `80`, then applies the `2.50` doomsday multiplier.
- Tactical biological use starts from `18`, strategic outbreak use from `35`, and biological doomsday release from `90` before severity and doctrine multipliers.
- Nuclear gain starts from `55`, adds `0.55` per million people, and uses the shared state-density multiplier. States above `5`, `10`, or `20` million people add a further `1.15`, `1.35`, or `1.65` population-band multiplier. A capital adds `35`, and a state with more than `8` industrial complexes adds `20`. Non-belligerent and ally or subject targets each apply a `1.50` multiplier. Thermonuclear use multiplies that calculated base by `2.25`. The strike then passes its measured civilian deaths and fallout intensity through the shared casualty and contamination terms. Major severity applies to a normal strike, while doomsday severity applies to the thermonuclear result.
- Every nuclear and thermonuclear strike reaches the shared source helper. There is no country-pair exemption.
- Camp, restricted-site, and concealment operations accumulate hidden atrocity or cover-up evidence before discovery. They do not add passive public condemnation merely for existing. Enemy occupation or liberation exposes the responsible country's stored hidden atrocity and cover-up buckets, then adds the state-specific public discovery gain.
- First discovery values are `8` for a concentration camp, `30` for an extermination camp, and `12` for a gulag before severity. Repeat discoveries use lower values divided by the number of already discovered sites plus one. Experiment and restricted-site bonuses are added before the shared severity multiplier.
- Destroyed or failed coverup evidence adds a distinct coverup source in addition to the atrocity discovery.

## Tier thresholds

Threshold comparisons are inclusive.

| Tier id | Tier | Public total | Next threshold | Mechanical gate |
| ---: | --- | ---: | ---: | --- |
| `0` | Normal standing | `0` to `24.999` | `25` | No sanction tier |
| `1` | International concern | `25` to `49.999` | `50` | Monitoring and early compliance visibility |
| `2` | Formal censure | `50` to `99.999` | `100` | Broader target responses and participant abstention or shielding |
| `3` | Arms embargo | `100` to `174.999` | `175` | Native embargo claim, volunteer restriction, military-support AI restrictions, and arms bottleneck |
| `4` | Strategic embargo | `175` to `299.999` | `300` | Equipment-market relation restriction and import-sensitive shortage |
| `5` | Total embargo | `300` to `499.999` | `500` | Isolation economy and stronger diplomatic AI hostility |
| `6` | Pariah state | `500` to `1000` | `1000` | Pariah pressure and contain or antagonize AI strategy |

Tier alone does not create a sanction pair. A potential participant must pass pair validity and scoring, or a player must take the matching targeted decision.

At Tier 1, countries in the watch band receive a `-15` monitoring opinion and light AI pressure of `-60` lend-lease desire, `-50` volunteer desire, and `-40` military-access acceptance. Tier 2 and higher use the stronger censure values of `-200`, `-175`, and `-150`. Per-target watch records guarantee that the exact values are restored when a target changes tier, disappears, or leaves the watch band.

## Participant score

### Positive pressure

| Factor | Score change |
| --- | ---: |
| Target tier | `tier x 18` |
| Highest historical tier | `peak tier x 4` |
| Recent gain | `recent gain x 0.20` |
| Nuclear bucket | `nuclear x 0.08` |
| Biological bucket | `biological x 0.07` |
| Atrocity bucket | `atrocity x 0.08` |
| Coverup bucket | `coverup x 0.06` |
| Repeat-use bucket | `repeat use x 0.10` |
| Contamination pressure | `contamination x 0.20` |
| Recent civilian deaths | `(deaths / 1000) x 0.10` |
| Democratic participant | `+28` |
| Fascist or communist participant against another ideology | `+18` |
| Non-aligned participant | `+6` |
| Last recorded victim | `+45` |
| At war with target | `+24` |
| Neighbor | `+10` |
| Capital distance below `1200` | `+10` |
| World tension above `40%` | `+12` |
| World tension above `75%` | `+18` instead of `+12` |
| Faction leader | `+12` |
| Major participant | `+12` |
| Participant has more factories than target | `+8` |
| Target evasion pressure | `evasion x 0.45` |

### Negative pressure

| Factor | Score change |
| --- | ---: |
| Same faction | `-70` |
| Overlord or subject relation | `-65` |
| Same ideology | `-12` |
| Fighting the same war | `-18` |
| Participant has fewer than `12` factories | `-12` |
| Target is a major | `-10` |
| Target has more factories than participant | `-15` |
| Capital distance at least `5000` | `-12` |
| Participant's own condemnation | `own total x -0.12` |
| Aggregate trade dependency estimate | `dependency x -0.75` |
| Strategic-resource dependency estimate | `dependency x -0.50` |
| Participant fatigue | `fatigue x -0.60` |
| Target compliance credit | `credit x -0.40` |

The trade and strategic-resource dependency inputs are estimates. They combine the participant's aggregate imports and consumption with the target's aggregate export capacity. HOI4 does not expose an exact scripted bilateral trade volume for this calculation. The UI therefore labels the aggregate complementarity value as an estimate.

### Result bands and actual AI use

| Score or condition | Implemented result |
| --- | --- |
| Below `15` | No likely-participant entry |
| `15+` | Watch status and likely-participant eligibility |
| Below `30`, or aggregate trade dependency at least `40` | AI can record abstention when no sanction applies |
| `55+` and Tier 3+ | AI can apply an arms sanction |
| `85+` and Tier 4+ | AI can escalate to strategic sanction |
| `120+` and Tier 5+ | AI can escalate to total sanction |
| `155+` and Tier 6 | AI can apply pariah enforcement and tighten after evasion |
| Fatigue `75+` and score below `155` | AI withdraws from the active pair |
| Pair is invalid because of faction, subject, or war relation, and score is `-45` or lower | AI can shield the target |
| Active pair, aggregate trade dependency at least `40` after dependency relief, and score below `105` | AI can quietly breach its own sanction |

Players use targeted participant decisions, while AI countries can act through the same decisions and through the periodic score-driven recalculation. Availability triggers prevent duplicate pair creation and require the corresponding tier and concrete enforcement resources.

## Native embargo ownership

### Engine behavior

Native embargoes use `send_embargo`, `break_embargo`, and `is_embargoing`. The native relation is broad trade denial. It is not a resource-specific oil, rubber, chromium, tungsten, or equipment embargo.

Native embargo actions require By Blood Alone support. Without By Blood Alone, the sanctions system still records scripted pairs, AI restrictions, response choices, dynamic penalties, and opinion memory, but it cannot create the native embargo relation.

### Source ownership

Three Chaos Redux systems share native embargo ownership:

1. Condemnation sanctions
2. Air Cleanliness Treaty
3. Event 50, The Great Embargo

Each sanctioning country keeps separate arrays for condemnation, Air Treaty, Event 50, pre-existing external embargoes, and native embargoes created by the shared helper. A source release removes only that source's claim. The helper calls `break_embargo` only when all of these are true:

- the relation was created by the shared system
- no condemnation claim remains
- no Air Treaty claim remains
- no Event 50 claim remains
- the embargo was not recorded as pre-existing external state

The Air Treaty refresh registers treaty-member embargoes against non-members and unregisters the treaty claim when the relation no longer qualifies. A treaty violation also registers the Air Treaty claim immediately from eligible foreign countries.

Event 50 registers the Great Embargo claim for every other country against the selected target. Event 50 has no expiry or release action, so its ownership claim remains until another implementation explicitly releases it or the target is removed.

## Relation rules and practical restrictions

### Pair restrictions

The first active pair on a participant installs relation-rule overrides. The last cleared pair removes them.

- The sanctioning participant cannot send volunteers to an arms-tier target through `can_send_volunteers = no`.
- The sanctioning participant cannot access an arms-tier target's equipment market through `can_access_market = no`.
- The vanilla outgoing and incoming lend-lease enable triggers are preserved and extended so a sanctioning participant cannot begin a new lend-lease agreement with its arms-tier target.

Applying a pair also recalls the participant's existing volunteers and attaché from the target. New volunteer and attaché actions are detected through on-actions, registered as observed breaches, and recalled. The lend-lease on-action remains a breach guard for agreements or deliveries that reach the runtime despite the diplomacy gate.

AI strategies apply the following pair pressure:

| Tier | Strategy change |
| --- | --- |
| Arms | Lend-lease desire `-1000`, volunteer desire `-1000`, equipment-market desire `-1000`, military-access acceptance `-750` |
| Strategic | Additional equipment-market desire `-1500` |
| Total | Befriend `-250`, protect `-400` |
| Pariah | Antagonize `+150`, contain `+150` |

Equal and opposite strategy values are added when the pair clears.

### Engine limits

The installed engine exposes direct recall effects for volunteers and attachés. It does not expose a safe generic effect that cancels every already active lend-lease, revokes every production licence, or removes a country from every active research-sharing group. The implementation therefore behaves as follows:

- volunteers and attachés are recalled
- new volunteer and attaché violations are detected
- new lend-lease agreements from a participant to its arms-tier target are blocked in both diplomacy directions
- lend-lease willingness is also suppressed through AI strategy, while an already active lend-lease is not generically cancelled
- licence access is made costly through dynamic modifiers and equipment-market access is restricted at arms tier, but existing production licences are not generically revoked
- total embargo applies a research-speed penalty and diplomatic isolation, but existing research-sharing membership is not generically cancelled

## Practical target penalties

### Severity model

Each active participant contributes an industry weight:

```text
1 + clamp(total factories / 20, 0, 5) + 3 if the participant is a major
```

That weight is multiplied by the participant pair tier:

- arms `x1`
- strategic `x2`
- total `x3`
- pariah `x4`

Relief comes from the humanitarian-carve-out share times `0.25`, faction-shield share times `0.35`, evasion pressure divided by `100` and times `0.20`, and active defiance programs. The tightened-enforcement share times `0.20` is subtracted from relief. Total relief is clamped from zero to `75%`. The adjusted raw severity is divided by `35` and capped at `1` to produce the practical-penalty factor.

### Maximum dynamic penalties

Actual values scale linearly from zero to these maxima.

| Sanction layer | Maximum practical penalty |
| --- | --- |
| Concern and censure pressure | Trade opinion `-15%`, licence purchase cost `+20%`, research speed `-3%`. Tier 1 applies half and Tier 2+ applies the maximum |
| Arms import bottleneck | Production efficiency gain `-18%`, licence purchase cost `+60%` |
| Strategic shortage | Factory output `-20%`, dockyard output `-15%`, fuel gain `-40%`, consumer goods `+12%`, synthetic-refinery and fuel-silo construction `-20%` |
| Isolation economy | Factory output `-18%`, research speed `-16%`, consumer goods `+16%`, trade opinion `-60%` |
| Pariah pressure | Enemy operative detection chance `-30%`, resistance target in occupied states `+15%`, stability `-10%` |

Strategic factory, dockyard, consumer-goods, and resource-project penalties also multiply by target import vulnerability. Strategic fuel pressure multiplies by target oil-import vulnerability.

The defiance relief values are:

- autarky `20%`
- forced extraction `15%`
- substitute materials `18%`
- military rationing `12%`
- subject pressure `18%`
- controlled shipping `15%`

## Participant burden and fatigue

A new participant pair pays `6` convoys and `3%` of current fuel capacity. Its enforcement cost begins as:

```text
(1 + aggregate trade dependency estimate x 0.10) x tier factor
```

Tier factors are `1.00` for arms, `1.50` for strategic, `2.25` for total, and `3.00` for pariah enforcement. Escalating an existing pair costs `2` convoys and `1%` of current fuel capacity, then replaces the old continuing burden with the tier-scaled burden. Tight enforcement adds a separately recorded burden that is removed on expiry, withdrawal, annexation, or pair cleanup.

Total enforcement burden divided by `20`, capped at `1`, scales these maximum penalties on the participant:

- consumer goods `+8%`
- factory output `-8%`
- fuel gain `-10%`

AI participants with active pairs gain fatigue equal to `1 + 25%` of the pair's previous enforcement cost during participant recalculation, capped at `100`. Fatigue divided by `100` scales up to `-6%` stability. Fatigue also reduces future participant score by `0.60` per point. At `75` fatigue, an AI participant whose score is below the `155` lead-enforcement band withdraws. Clearing a pair reduces fatigue by `15`, then refreshes the participant burden. Clearing the final pair resets fatigue to zero.

## Target choices

### Compliance

| Decision | Concrete cost and duration | Result |
| --- | --- | --- |
| Accept inspections | `180` days of `+5%` consumer goods and `-15%` encryption | `+12` decay credit and `10%` hidden-evidence disclosure per targeted pulse |
| Destroy chemical stockpiles | Removes `75%` of every strategic chemical-agent lot, filled-shell lot, prepared air-payload lot, and each of the seven legacy cylinder stocks, then creates a `365` day chemical-use restriction | `+20` decay credit and stockpile-destruction state |
| Destroy biological stockpiles | Removes `75%` of anthrax, plague, tularemia, smallpox, and weaponized-zombie bomb stocks and creates a `365` day biological-use restriction | `+25` decay credit and source-specific stockpile-destruction state |
| Dismantle restricted sites | Clears controlled restricted chemical, Auschwitz or SS experiment, and Japanese biowarfare-atrocity site flags and marks the sites destroyed | `+22` decay credit and site-dismantlement state |
| Pay compensation | `12 + 4 x current tier` convoys, `500` infantry equipment, `12%` fuel, then `180` days of `+7%` consumer goods and `-4%` factory output | Transfers convoy and equipment compensation to the last victim when valid and adds `+18` decay credit |
| Issue non-use pledge | `365` days of `-3%` war support | `+10` decay credit. Clean completion grants `180` days of verified non-use and `+25` more credit |
| Allow observers | `4` convoys and `180` days of `+3%` consumer goods and `-20%` enemy-operative detection | `+14` decay credit and `5%` hidden-evidence disclosure per targeted pulse |
| Reform unconventional command | `30` army XP, `20` air XP, `20` navy XP, then `270` days of `-6%` army organization and `+15%` training time | `+30` decay credit and persistent command-reform memory |

### Defiance

All timed defiance programs last `180` days.

| Decision | Concrete cost or burden | Sanction relief or effect |
| --- | --- | --- |
| Refuse inspections | Adds public coverup condemnation from base `18` at major severity and blocks decay for `180` days | No economic relief |
| Domestic propaganda campaign | Immediate `-2%` stability, then `180` days of `+8%` war support, `-3%` stability, and `+4%` consumer goods | Adds participant moral pressure and marks an openly defiant line |
| Emergency autarky | Pays `8%` fuel, then gives `+25%` local resources, `+8%` consumer goods, and `-5%` factory output | `20%` relief |
| Forced extraction | Immediate `-4%` stability, then `+35%` local resources and `-10%` production-efficiency gain | `15%` relief |
| Substitute materials | `+15%` local resources and `-8%` production-efficiency gain | `18%` relief |
| Military rationing | Military fuel consumption `-18%` and factory output `-4%` | `12%` relief |
| Pressure subject supply | Requires a subject, applies immediate `-3%` stability, then `+20%` local resources and `-3%` stability factor | `18%` relief |
| Controlled shipping | `10` convoys and `5%` fuel, then `+12%` convoy escort efficiency and `-3%` factory output | `15%` relief |
| Hardline mobilization | `+5%` war support and `-5%` stability | No direct severity relief |

### Evasion

Every evasion route lasts `120` days, adds `10` exposure, and increases evasion pressure. Exposure is multiplied by `0.75` each monthly pulse. The monthly detection roll is current exposure plus `5`, capped at `100`.

| Decision | Concrete cost or gain | Evasion pressure and timed effect |
| --- | --- | --- |
| Black market arms | `12` convoys and `8%` fuel, then gains `500` infantry equipment and `100` support equipment | `+12` pressure and `-3%` factory output |
| False manifests | `8` convoys | `+10` pressure and `+10%` convoy escort efficiency |
| Neutral intermediaries | `6` convoys, then gains `250` infantry equipment | `+8` pressure and `-15%` licence purchase cost |
| Subject front | Requires a subject and applies `-3%` stability | `+10` pressure and `+12%` local resources |
| Covert fuel route | `10` convoys, then gains `12%` fuel | `+10` pressure and military fuel consumption `-8%` |
| Reflag shipping | `6` convoys | `+8` pressure and `+18%` convoy escort efficiency |
| Stolen licence | `8` convoys | `+8` pressure and `+5%` production-efficiency gain |
| Smuggled laboratory | `6` convoys and `5` support equipment | `+8` pressure and `+4%` research speed |

An exposed target evasion route adds coverup condemnation from base `16` at major severity. An exposed participant quiet breach adds coverup condemnation to the target and the participant, removes the quiet-breach relief, and applies diplomatic damage.

## Participant choices

| Decision | Cost and duration | Result |
| --- | --- | --- |
| Join arms embargo | New pair pays `6` convoys and `3%` fuel | Creates arms pair and native embargo claim where supported |
| Escalate strategic, total, or pariah embargo | Requires an existing pair, sufficient target tier, `2` convoys, and `1%` fuel | Raises pair tier and continuing enforcement burden without charging the initial-pair cost again |
| Abstain | No direct stockpile cost, review lasts `180` days | Records abstention; the last victim and active sanction participants gain negative opinion of the abstainer |
| Humanitarian carve-out | `5` convoys for `180` days | Reduces effective target pressure through carve-out relief |
| Quiet breach | `8` convoys, `4%` fuel, and `300` infantry equipment for `120` days | Adds target evasion pressure and exposure while risking discovery. AI use requires estimated dependency of at least `40` after dependency relief and a pair score below `105` |
| Tighten enforcement | `6` convoys for `180` days | Removes quiet-breach status, raises enforcement burden, and reduces target relief |
| Shield ally | `8` convoys for `180` days | Adds shield relief, supporting opinion, and `1` fatigue |
| Withdraw sanctions | No direct cost | Clears the condemnation pair and releases only the condemnation native-embargo claim |

## AI roles

Participant AI is automatic and score-driven:

- democracies receive strong moral pressure
- fascist and communist countries receive extra pressure against ideological rivals
- neutral traders are strongly restrained by dependency and can abstain or breach an active sanction
- faction leaders receive added sanction pressure but same-faction and subject relations normally invalidate enforcement and can produce shielding
- participants with high condemnation suffer a hypocrisy penalty
- fatigue and target compliance lower enforcement willingness
- evasion and direct victim status raise enforcement willingness
- international concern creates light monitoring pressure before embargo eligibility; formal censure strengthens the lend-lease, volunteer, and military-access reductions while retaining the monitoring opinion record
- democratic or highly trade-dependent AI participants can add a paid humanitarian carve-out to an active pair

Condemned-target decision AI uses the visible decision conditions:

- a non-major with fewer than `12` factories is explicitly classified as weak, while a major or a country with at least `50` factories is explicitly classified as strong
- democratic, import-dependent countries under formal censure favor inspections, stockpile destruction, compensation, pledges, observers, and command reform
- non-democratic industrial majors without an unrestricted route favor denial, partial compliance, and autarky
- radical high-chaos countries require an explicit unrestricted route before they favor refusal, propaganda, hardline mobilization, black-market procurement, and a more willing allied shield
- an unrestricted country near victory gains an additional defiance preference only when at least one actual enemy has reached the centralized native surrender-progress threshold
- a country near capitulation destroys chemical and biological stockpiles when it lacks the explicit doomsday route or extreme-use policy; the separate doomsday decision remains responsible when that authorization exists
- a severe visible recent source increases both compliance and selected defiance weights, while Tier 5 or Tier 6 adds further compliance pressure
- high import vulnerability favors autarky and substitute materials
- high fuel vulnerability favors covert fuel routes
- high black-market exposure sharply reduces further black-market use

The explicit classifiers add `+35` compliance and `-20` defiance weight for weak targets, with the signs reversed for strong targets.

Human players see three zero-cost view selectors for compliance, defiance, and evasion. The selectors only curate the visible decision list; AI countries continue to evaluate all eligible target-response actions. Participant decisions remain player controls with zero AI weight because `condemnation_recalculate_participants` already owns AI sanction, abstention, carve-out, breach, enforcement, shielding, escalation, and withdrawal behavior. Enabling both surfaces would duplicate the same pair action.

## Decay and memory

Base public-bucket decay per targeted monthly pulse is:

| Tier | Base monthly decay |
| --- | ---: |
| Normal | `0.50` |
| Concern | `0.75` |
| Formal censure | `0.60` |
| Arms embargo | `0.45` |
| Strategic embargo | `0.30` |
| Total embargo | `0.20` |
| Pariah | `0.10` |

Decay bonuses are:

- inspections `+0.75`
- observers `+0.50`
- verified non-use `+1.00`
- compensation `+0.75`
- stockpile destruction `+1.25`
- site dismantlement `+1.00`
- command reform `+0.75`

Refused inspections subtract `1.00` and any active evasion route subtracts `0.50`. Decay credit converts at `0.10` decay per credit, capped at `2` extra decay in one pulse. Total monthly public-bucket decay is capped at `7`.

Decay is set to zero while the target has recent use, refused inspections, a broken pledge, or exposed evasion. When decay is allowed, the five public source buckets decay proportionally to their share of the public total. Hidden evidence does not naturally decay.

Independent memory fades continue each pulse:

- repeat use `-0.20`
- recent gain `-0.35`
- recent civilian deaths `x0.85`
- contamination pressure `x0.90`
- black-market exposure `x0.75`

The highest tier reached remains in `condemnation_peak_tier`, contributes long-memory participant pressure, and is shown in the UI. No current helper clears it.

## Targeted runtime and lifecycle cleanup

The condemnation system does not add a broad daily, weekly, or monthly all-country on-action pass.

`condemnation_start_targeted_pulse` schedules hidden event `condemnation_sanctions.1` for the affected country after `30` days. The event runs `condemnation_monthly_pulse` and schedules itself again only while the country still has a public record, active sanctions, unresolved compliance, defiance, or evasion, or residual evasion pressure or exposure. A hidden-only evidence record remains in the targeted registry without running a pulse until a public source or disclosure path activates maintenance.

Participant recalculation also runs after relevant source gains and tier changes, and from targeted relation hooks for war, puppeting, and faction joins.

Cleanup covers:

- invalid pairs caused by war, faction, subject, or overlord relations
- target tier falling below the active pair tier
- player withdrawal or AI score change
- expired carve-outs, breaches, tight enforcement, abstentions, and shields
- dead participant scopes in target arrays
- annexed target pair variables across countries
- participant relation-rule removal after the last pair
- source-owned native embargo release
- stale selected-country UI state after a target loses its public record
- removal of a country from `global.condemnation_targets` when no visible or hidden state remains

## UI read model

The Condemnation tab keeps its existing tab layout. Country rows are clickable and open a selected-country detail overlay.

The sorted row arrays contain:

- country scope
- public total
- current tier
- recent gain
- largest public source bucket
- active sanction count
- highest active sanction tier
- compliance state

The detail snapshot copies these categories into viewer-scoped UI variables:

- public total, tier, peak tier, and next threshold
- chemical, biological, nuclear, atrocity, coverup, and repeat-use buckets
- the three newest public source types, gains, and dates, plus the latest context and severity
- total active sanctions and arms, strategic, total, and pariah participant counts
- native embargo count
- earliest active bilateral sanction-review expiry, with the nominal tier bands retained in its tooltip
- carve-out, quiet-breach, shield, tightened-enforcement, and likely-participant counts
- up to three likely participant country scopes
- candidate and active industry or trade estimates
- average participant fatigue
- compliance and decay state
- evasion and exposure state when the viewer is allowed to know it
- import and fuel vulnerability
- isolation severity
- current practical penalty values

The list is built from `global.condemnation_targets`, not a world-country scan. Only the public total is shown, so hidden evidence cannot leak through the tab. Background country pulses mark the list dirty; only player tab and sort interactions rebuild the shared row arrays, preventing AI-country scopes from overwriting the player's sort order.

## Reused final icons

The sanctions system adds no new or placeholder visual asset. It uses final vanilla or existing Chaos Redux sprites.

### Chaos Redux sprites

| Sprite id | Texture path | GFX file |
| --- | --- | --- |
| `GFX_decision_deploy_field_hospitals` | `gfx/interface/decisions/decision_deploy_field_hospitals.dds` | `interface/chaosx_decisions.gfx` |
| `GFX_decision_emergency_mobilization` | `gfx/interface/decisions/005_soviet_collapse/decision_emergency_mobilization.dds` | `interface/005_soviet_collapse.gfx` |
| `GFX_decision_seize_depots` | `gfx/interface/decisions/005_soviet_collapse/decision_seize_depots.dds` | `interface/005_soviet_collapse.gfx` |
| `GFX_decision_soviet_collapse_foreign_trade` | `gfx/interface/decisions/005_soviet_collapse/decision_soviet_collapse_foreign_trade.dds` | `interface/005_soviet_collapse.gfx` |

### Condemnation UI sprites

| Sprite id | Texture path | GFX file |
| --- | --- | --- |
| `GFX_chaosx_chaos_meter_entry` | `gfx/interface/chaosx_world_tension_entry.dds` | `interface/chaosx.gfx` |
| `GFX_tiled_plain_bg` | `gfx/interface/tiles/tiled_plain_bg.dds` | `interface/countrytechtreeview.gfx` |
| `GFX_closebutton_small` | `gfx/interface/closebutton_small.tga` | Vanilla `interface/general_stuff.gfx` |
| `GFX_mini_tooltip` | `gfx/interface/tiles/tiled_mini_dialog.dds` | Vanilla `interface/core.gfx` |
| `GFX_flag_small2` | `gfx/interface/flag_overlay_small.dds` with `gfx/interface/shield_small_mask.tga` | Vanilla `interface/general_stuff.gfx` |
| `GFX_diplo_countrylist_flag_frame` | `gfx/interface/diplo_countrylist_flag_frame.dds` | Vanilla `interface/countrydiplomacyview.gfx` |

### Vanilla decision sprites

All entries below are defined in vanilla `interface/decisions.gfx`.

| Sprite id | Texture path |
| --- | --- |
| `GFX_decision_category_generic_crisis` | `gfx/interface/decisions/decision_category_generic_crisis.dds` |
| `GFX_decision_category_generic_economy` | `gfx/interface/decisions/decision_category_generic_economy.dds` |
| `GFX_decision_generic_intelligence_operation` | `gfx/interface/decisions/decision_generic_intelligence_operation.dds` |
| `GFX_decision_generic_scorched_earth` | `gfx/interface/decisions/decision_generic_scorched_earth.dds` |
| `GFX_decision_generic_construction` | `gfx/interface/decisions/decision_generic_construction.dds` |
| `GFX_decision_generic_political_address` | `gfx/interface/decisions/decision_generic_political_address.dds` |
| `GFX_decision_generic_military` | `gfx/interface/decisions/decision_generic_military.dds` |
| `GFX_decision_generic_political_rally` | `gfx/interface/decisions/decision_generic_political_rally.dds` |
| `GFX_decision_generic_industry` | `gfx/interface/decisions/decision_generic_industry.dds` |
| `GFX_decision_generic_research` | `gfx/interface/decisions/decision_generic_research.dds` |
| `GFX_decision_generic_political_discourse` | `gfx/interface/decisions/decision_generic_political_discourse.dds` |
| `GFX_decision_generic_protection` | `gfx/interface/decisions/decision_generic_protection.dds` |
| `GFX_decision_SWI_support_humanitarian_efforts` | `gfx/interface/decisions/decision_SWI_support_humanitarian_efforts.dds` |

### Vanilla idea sprites

All entries below are defined in vanilla `interface/ideas.gfx`.

| Sprite id | Texture path |
| --- | --- |
| `GFX_idea_isolation` | `gfx/interface/ideas/idea_isolation.dds` |
| `GFX_idea_free_trade` | `gfx/interface/ideas/idea_generic_free_trade.dds` |
| `GFX_idea_undisturbed_isolation` | `gfx/interface/ideas/idea_undisturbed_isolation.dds` |
| `GFX_idea_can_wartime_prices_and_trade_board` | `gfx/interface/ideas/idea_can_wartime_prices_and_trade_board.dds` |
| `GFX_idea_generic_intel_bonus` | `gfx/interface/ideas/generic_intel_bonus.dds` |
| `GFX_idea_generic_spy_intel` | `gfx/interface/ideas/generic_spy_intel.dds` |
| `GFX_idea_generic_foreign_capital` | `gfx/interface/ideas/idea_generic_foreign_capital.dds` |
| `GFX_idea_generic_constitutional_guarantees` | `gfx/interface/ideas/idea_generic_constitutional_guarantee.dds` |
| `GFX_idea_generic_army_war_college` | `gfx/interface/ideas/idea_generic_army_war_college.dds` |
| `GFX_idea_generic_exploit_mines` | `gfx/interface/ideas/idea_generic_exploit_mines.dds` |
| `GFX_idea_generic_research_bonus` | `gfx/interface/ideas/generic_research_bonus.dds` |
| `GFX_idea_generic_production_bonus` | `gfx/interface/ideas/generic_production_bonus.dds` |
| `GFX_idea_generic_oppression` | `gfx/interface/ideas/idea_generic_oppression.dds` |
| `GFX_idea_generic_war_preparation` | `gfx/interface/ideas/idea_generic_war_preparation.dds` |
| `GFX_idea_generic_deal_with_the_devil` | `gfx/interface/ideas/idea_generic_deal_with_the_devil.dds` |
| `GFX_idea_generic_deal_with_the_devil2` | `gfx/interface/ideas/idea_generic_deal_with_the_devil2.dds` |
| `GFX_idea_generic_license_production` | `gfx/interface/ideas/idea_generic_license_production.dds` |

## Validation scenarios and expected outcomes

These are expected results from the current implementation. They are not a claim that every scenario has been executed in a live game session.

| # | Scenario | Expected outcome |
| ---: | --- | --- |
| 1 | Chemical support is used in several combats, then stops | Each verified human-target combat adds to the chemical bucket. When a chemical adapter supplies measured civilian deaths or contamination, the shared capped terms increase that source. Uses inside `180` days also add `25%` repeat pressure. Public decay remains blocked until recent use expires, then chemical pressure decays proportionally. |
| 2 | One nuclear strike hits a low-population military target | The nuclear adapter adds its tuned base plus population and density scaling, with no capital bonus and no major-industry bonus unless the factory threshold is exceeded. Measured civilian deaths and fallout intensity add the shared casualty and contamination terms. The nuclear context is recorded for every attacker-target pairing. |
| 3 | A thermonuclear strike hits a populous capital | Population, density, capital, possible industry, diplomatic relation, thermonuclear, and doomsday factors combine into a much larger nuclear gain. Fallout intensity contributes to participant pressure. |
| 4 | A biological strike creates a spreading outbreak | Strategic biological gain enters the biological bucket with outbreak context, doctrine reduction where unlocked, repeat-use pressure when applicable, and Air Treaty use response. |
| 5 | A restricted chemical site is discovered after occupation | Operation has already accumulated hidden atrocity evidence, including deaths. Discovery exposes the responsible country's hidden atrocity and cover-up buckets, then adds the restricted-site public atrocity gain. Destroyed or failed cover-up evidence adds a separate public cover-up source. No public chemical-use gain is created merely by operating the hidden site. |
| 6 | A camp system is exposed through discovery or liberation | Camp operation has already accumulated hidden atrocity evidence. Discovery exposes the responsible country's hidden atrocity and cover-up buckets, then adds site-type and repeat-scaled public atrocity gain. First discoveries can fire discovery events and threshold reactions. Hidden operation before discovery does not add passive public condemnation. |
| 7 | A country reaches Tier 3 | Eligible AI participants scoring at least `55`, or players taking the targeted action, create arms pairs. With By Blood Alone active, the helper also creates native embargo relations. Without it, the scripted pair, relation restrictions, AI pressure, and practical sanctions still apply. Volunteers and attachés are recalled, new lend-lease is blocked in both diplomacy directions, equipment-market access is blocked, and the arms bottleneck begins to scale. |
| 8 | A country reaches Tier 4 | Eligible participants scoring at least `85` can pay the escalation cost and raise the pair to strategic enforcement. Strategic shortage scales from participant industry weight, pair tier, import vulnerability, fuel vulnerability, and relief. |
| 9 | A country reaches Tier 5 with strong faction shielding | Same-faction or subject relations invalidate ordinary enforcement. Very low scores can create shield records. Shield share reduces target severity while the shielding country pays convoys and fatigue. |
| 10 | A country reaches Tier 5 with no shielding and high trade dependency | Eligible participants scoring at least `120` can apply total sanctions. The target's import vulnerability magnifies strategic penalties, and isolation-economy penalties scale with weighted severity. |
| 11 | A neutral trader has high dependency | Dependency strongly reduces participant score. At `40` or more estimated dependency, the AI can record abstention when no sanction applies. |
| 12 | A neutral trader quietly breaches sanctions and is exposed | An active AI pair can create a `120` day quiet breach when estimated dependency is at least `40` after dependency relief and score is below `105`. Exposure removes the breach, adds coverup condemnation to target and participant, and applies breach opinion damage. |
| 13 | A condemned country accepts inspections and destroys stockpiles | Inspections add burden and decay credit while exposing `10%` of hidden evidence per pulse. Chemical exposure is reconciled row by row against exact recorded actions and never allocated to a guessed record. Stockpile decisions remove `75%` of the matching stock and add source-specific restriction and further credit. |
| 14 | A condemned country breaks a non-use pledge | The pledge clears. The country gains `365` days of broken-pledge memory, `35` coverup, `25` repeat pressure, and zero public decay while the memory flag remains. |
| 15 | A condemned country repeatedly uses black-market procurement | Each route increases evasion pressure and exposure. Exposure decays by `25%` per pulse, but the monthly discovery chance is exposure plus `5`. Discovery adds public coverup pressure. |
| 16 | A participant stops sanctions after tier decay or fatigue | AI recalculation clears a pair when the target no longer supports the pair tier, the score no longer supports enforcement, or fatigue reaches `75` while score is below `155`. Pair variables, AI strategies, relation rules, modifiers, opinion support, and the condemnation native-embargo claim are cleaned. Other native owners remain intact. Clearing a pair reduces participant fatigue by `15`, and clearing the final pair resets it to zero. |
| 17 | A target is annexed or dies | The target is removed from the global registry. Pair variables and native-ownership arrays are cleared across countries, burden is reduced, and relation overrides are removed when no pairs remain. |
| 18 | AI targets choose compliance when weak and defiance when strong | Non-majors below `12` factories are explicitly weak and receive `+35` compliance and `-20` defiance weight. Majors or countries with at least `50` factories are explicitly strong and receive `-20` compliance and `+35` defiance weight. Ideology, war, recent-source severity, critical tier, import vulnerability, fuel vulnerability, and exposure provide further route weighting. |
| 19 | The UI opens a condemned-country entry | The taller row shows public total, tier, recent gain, main source, active sanctions, highest sanction tier, and compliance state without clipping long country names. Clicking opens the detail snapshot with source breakdown, the three newest public source entries, full dated source history in the tooltip, threshold or Pariah cap, participant counts, earliest active review expiry, all practical penalties, decay, and allowed evasion data. |
| 20 | Decision requirements and costs are inspected | Eligible targeted rows remain visible when resources are missing. Concrete stockpile, convoy, fuel, equipment, XP, subject, and state requirements use custom localisation, and multi-resource blocked costs color only the missing components. Raw trigger blocks remain hidden. |

## Supported behavior, limitations, and remaining risks

- Native embargo is supported through the engine's broad diplomatic embargo and requires By Blood Alone.
- Native embargo is not a resource-specific sanction and cannot represent an exact oil-only or arms-only trade denial.
- Exact bilateral trade volume is unavailable to script. Participant trade dependency and the UI trade value are aggregate complementarity estimates.
- Active volunteers and attachés can be recalled. New volunteer and attaché violations are detected.
- New lend-lease is blocked, but already active lend-lease, production licences, and research-sharing membership cannot be generically cancelled or revoked with the available effects. The system uses diplomacy gates, relation rules, AI strategies, licence-cost pressure, research penalties, and breach detection around those engine limits.
- Chemical combat-result callbacks that expose no opponent or affected-state scope cannot name a victim. State-based chemical use and raids do record the affected controller, enabling victim scoring and compensation.
- The recent-source arrays keep eight entries, while the compact detail panel presents the newest three.
- The detail view shows up to three likely participants in the gameplay array's current order. Inactive candidate scores are not persisted, so the UI does not claim that these names are score-ranked.
- Event 50 has no native-embargo release action and therefore retains its ownership claim.

## Future extensions

- Add a scrollable archive for all eight recent source-log entries if the compact details overlay is expanded.
- Add source-specific scripted restrictions only where the engine can present them honestly without mislabeling a broad native embargo.
