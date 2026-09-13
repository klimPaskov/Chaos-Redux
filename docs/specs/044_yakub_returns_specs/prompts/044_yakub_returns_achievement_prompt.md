# Achievement implementation prompt for Event 044 Yakub Returns

Use `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, and the achievement rules in `AGENTS.md`.

Read spec part 5, spec part 6, the acceptance criteria, and the asset prompt. All titles below are working labels. Final player-facing titles and descriptions must follow the writing direction and must not expose hidden variables or implementation history.

Implement achievements in the single Chaos Redux achievement registry. Group Event 044 entries under one documented section. Use stable tracking flags and variables only where the final state cannot prove the full route. Do not make an achievement unlock from a debug launch, invalid tag switch, or scenario bypass unless the achievement explicitly allows manual scenarios.

Every achievement needs:

- final achievement ID
- localization
- exact eligibility
- route and starting-country proof
- unlock trigger
- disqualifiers
- hidden or visible state
- difficulty documentation
- tracking cleanup or persistence
- completed, grey, and not-eligible icon variants
- event documentation and catalog-facing achievement notes where used

## 1. No Martyrs

Working key:

`chaosx_044_no_martyrs`

Eligible start:

United States or the accepted American host in normal Event 44 play.

Unlock conditions:

- Event 44 baseline crisis has concluded.
- Yakub was never killed.
- No martyr crisis occurred.
- No Event 44 American civil war began.
- Yakubite Influence reached at least the Entrenched stage during the crisis.
- The final outcome reduced Influence below Entrenched through intelligence, material reform, legal process, public debate, monitored organization, or negotiated political work.
- General mass suppression was never used.

Disqualifiers:

- wrongful or failed raid marked as a martyr-producing action
- indiscriminate suppression route
- territorial breakaway
- civil war
- prohibited tag switching or debug proof under the achievement framework

Visibility:

Visible.

Difficulty:

High.

Tracking notes:

Track peak Influence, founder death, martyr incidents, civil war start, mass suppression, and accepted stabilizing action families. Do not rely only on the final Influence value.

Description direction:

Contain a powerful movement without killing its founder, creating a martyr, or fighting a civil war.

Icon direction:

Open case file, intact courthouse, and lowered microphone or torch.

## 2. The Peaceful Partition

Working key:

`chaosx_044_the_peaceful_partition`

Eligible starts:

United States and the formed American Event 44 state when the framework permits inherited event-country achievements.

Unlock conditions:

- A sovereign New Nation formed through the negotiated compact path.
- No civil war occurred between the signatories.
- A trade, transit, guarantee, or coexistence agreement remains active.
- Both states remain independent and viable for a meaningful stability period.
- The compact did not result from forced capitulation.
- The new state has a valid capital, supply access, and enough territory to function.

Disqualifiers:

- immediate treaty breach
- annexation or subject conversion during the stability period
- invalid one-state trap without supply
- scenario setup that begins after the compact unless scenarios are explicitly eligible

Visibility:

Visible.

Difficulty:

High.

Tracking notes:

Record compact formation path, signatories, war history, treaty continuity, independence, viability, and required elapsed time.

Description direction:

Create and preserve an independent New Nation through negotiation rather than civil war.

Icon direction:

Two hands over divided but connected industrial territory.

## 3. A Nation Before a State

Working key:

`chaosx_044_a_nation_before_a_state`

Eligible start:

United States movement host or formed American Event 44 state.

Unlock conditions:

- Every core parallel institution family reached the accepted established state before country formation.
- Yakubite Influence stayed below Secession Crisis until the institution network was complete.
- The movement later formed a sovereign or autonomous state through a valid path.

Core institutions:

- schools and political education
- food and relief
- businesses and finance
- courts and arbitration
- community defense
- press and communication
- political committees

Disqualifiers:

- state formation before all institution proofs
- Influence reaching Secession Crisis before completion
- scenario setup that pre-seeds completed institutions unless the scenario is explicitly eligible

Visibility:

Visible.

Difficulty:

Medium to high.

Tracking notes:

Use institution-family completion flags and a one-time proof that the full set was achieved before state creation. Do not require the player to keep seven public meters.

Description direction:

Build the movement's full institutional life before claiming statehood.

Icon direction:

School, food basket, printing press, courthouse, and shield as one compact symbol.

## 4. The Congress Holds

Working key:

`chaosx_044_the_congress_holds`

Eligible country:

Yakubite International anchor.

Unlock conditions:

- Form the Yakubite International.
- Include full or accepted member states from at least four approved world regions.
- Maintain International Cohesion in the high stage for the required period.
- No war occurs between members during that period.
- The International has rejected or defeated the Original Supremacy route.
- The bloc survives one major external war, sanctions crisis, or coordinated containment campaign.

Disqualifiers:

- member civil war or interstate war
- supremacist International form
- terminal scenario setup that grants all proof automatically
- Cohesion collapse below the accepted floor during the hold period

Visibility:

Visible.

Difficulty:

Very high.

Tracking notes:

Track distinct approved regions, membership state, Cohesion duration, member wars, International form, and external crisis survival.

Description direction:

Hold together a broad non-supremacist International through a major external crisis.

Icon direction:

Interlocking regional emblems around a central congress table.

## 5. Doctrine Without Dominion

Working key:

`chaosx_044_doctrine_without_dominion`

Eligible country:

A foreign Event 44 movement state or aligned state created through Evolution II.

Unlock conditions:

- Receive material, organizational, or diplomatic aid from a Yakubite state or International.
- Publicly reject the literal racial doctrine or Original Supremacy.
- Preserve local leadership and a local political identity.
- Win independence or establish a stable government.
- Remain an ally, associate, or treaty partner without becoming a subject of the American anchor or International headquarters.

Disqualifiers:

- subject status under the anchor
- local leadership replaced by imposed foreign leadership
- adoption of Original Supremacy
- independence granted automatically by a Maximum setup unless manual scenarios are eligible

Visibility:

Visible.

Difficulty:

High.

Tracking notes:

Record aid receipt, doctrinal rejection, local leadership continuity, independence or stability proof, and relationship status.

Description direction:

Use foreign support while keeping local doctrine, leadership, and sovereignty.

Icon direction:

Open book beside a broken chain and independent flag.

## 6. The Founder Is Gone

Working key:

`chaosx_044_the_founder_is_gone`

Eligible country:

Event 44 International or terminal anchor.

Unlock conditions:

- Yakub died or became permanently missing before terminal commitment.
- A valid non-Yakub succession completed.
- The International survived the succession.
- The successor activated The Yakubite World through normal readiness.

Disqualifiers:

- Yakub returns before commitment
- scenario creates a post-succession terminal actor without running a valid succession package
- International collapses and is rebuilt as an unrelated bloc

Visibility:

Visible or rare, according to the existing achievement presentation pattern.

Difficulty:

Very high.

Tracking notes:

Track founder state at commitment, succession outcome, International continuity, and terminal activation path.

Description direction:

Carry the International into its terminal campaign after its founder is dead or missing.

Icon direction:

Empty chair before a lit congress emblem.

## 7. The Inversion

Working key:

`chaosx_044_the_inversion`

Eligible country:

Original Supremacy route terminal anchor.

Unlock conditions:

- Adopt the Original Supremacy route.
- Form or seize control of a supremacist International.
- Activate The Yakubite World through the supremacist terminal variant.
- Retain enough members and military capacity to begin the terminal conflict.
- Survive the first major coalition-war phase or the accepted initial war duration.

Disqualifiers:

- route reform before terminal commitment
- immediate International collapse
- scenario-only setup unless the achievement explicitly accepts World Order scenarios

Visibility:

Visible or secret, based on existing Chaos Redux dark-route achievement practice.

Difficulty:

Extreme.

Description direction:

Frame the unlock as completion of an extremist authoritarian route. Do not write praise or treat racial domination as a moral victory.

Icon direction:

Severe inverted crown or hierarchy with cracked foundations.

## 8. Every Temple Empty

Working key:

`chaosx_044_every_temple_empty`

Eligible country:

An opponent of the Event 44 terminal order.

Unlock conditions:

- The Yakubite World activated.
- The player's coalition defeated the terminal actor or made the decisive accepted contribution.
- The International military command was dismantled.
- Terminal succession was resolved.
- No active supremacist terminal government remains.
- The defeat settlement completed.

Disqualifiers:

- a surviving supremacist terminal successor still controls the International
- terminal conflict ended through an unresolved script state
- the player joined the terminal order during the decisive campaign

Visibility:

Visible.

Difficulty:

Extreme.

Tracking notes:

Define decisive contribution through existing war participation or event-owned coalition proof. Do not unlock for a country that never participated. Track military-command dismantling, successor state, terminal-government registry, and settlement completion.

Description direction:

Defeat the terminal political order and dismantle its remaining supremacist command structure. Avoid language about eliminating civilians, Black politics, or Islam.

Icon direction:

Abandoned congress hall, broken banners, and daylight entering.

## Implementation and validation

Inspect existing Chaos Redux achievement definitions, localization, root registry patterns, icon filename requirements, and disqualifier behavior before editing.

Create an achievement coverage table with:

| Working label | Final ID | Eligibility | Tracking keys | Icon triplet | Status |
| --- | --- | --- | --- | --- | --- |

The asset worker must create separate completed source art for every achievement. Grey and not-eligible variants follow the exact existing workflow. No achievement icon may be a resized focus, idea, or decision icon.

Test each achievement against at least one positive and one negative scenario. For route-history achievements, test that final-state imitation without the required history does not unlock them.

Do not reduce difficult achievements to simple final flags. Do not mark the achievement set complete while icons, localization, tracking, disqualifiers, documentation, or scenario eligibility remain unresolved.
