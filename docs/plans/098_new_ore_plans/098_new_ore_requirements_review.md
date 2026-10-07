# Event 098 New Ore requirements review

Historical initial research and proposals.
Final accepted design and dispositions are in [the source review](../../specs/098_new_ore_specs/098_new_ore_review_record.md) and [098_new_ore_final_completion_audit.md](098_new_ore_final_completion_audit.md).
This report's pending choices and workspace/source observations remain provenance for its original revision, not instructions to reopen settled design.

## Status and authority

This is a read-only requirements and connection review for the parent planning agent.
It is a proposed review checklist, not an accepted source specification or an implementation-completion audit.
The parent confirmed that the global source-reading gate passed in `source_gate/global_reading_ledger.json` before this work began.
No gameplay files were changed.
The user's current requirements control over blank or older catalog fields.
Where this document proposes a contract detail beyond the brief, it explicitly labels that detail as a proposal for parent acceptance.
No HOI4 MCP tool is exposed in the connected registry inspected by this reader.
No engine, probability, save/reload, or live-game result is claimed.

## Evidence index

| Reference | Supplied source or inspected repository source | Coverage and limit |
| --- | --- | --- |
| S1 | `source_gate/latest_archive/chaos_redux_events_catalog.csv`, Event IDs 028, 029, 086, 092 and 098 | Complete selected CSV records were parsed, including multiline fields. Physical source rows begin at lines 139, 140, 211, 217 and 223 respectively. |
| S2 | `source_gate/latest_archive/chaos_redux_clusters_catalog.csv`, Cluster 7 Positive Economy | Complete parsed record at line 8. |
| S3 | `source_gate/latest_archive/CHAOS_REDUX_MECHANICS.md` | Targeted reread of lines 115–151, 175–194, 423–499 and 560–576 for classification, tiers, evolutions, logs, clusters and scenarios. |
| S4 | `source_gate/latest_archive/chaosx_dynamic_effects.md` | Lines 421–462, including owner API index row `asteroid_mineral_control` at line 447 and owner/private API maintenance rules. |
| S5 | `source_gate/latest_archive/chaos-redux-events.md` | Targeted reread of spec fidelity, evolution implementation, MCP evidence, classification, log/cluster integration and final checklist. |
| S6 | `source_gate/latest_archive/chaos-redux-event-planning.md` | Targeted reread of input authority, achievements, active/pre-fire evolution paths, dynamic values/costs, AI, presentation hierarchy, asset coverage, effect strength, output contract and near-completion loop. |
| S7 | `source_gate/latest_archive/chaos-redux-improvement-loop.md` | Targeted reread of cadence and anti-bloat closure conditions. |
| S8 | `source_gate/latest_archive/chaos-redux-event-assets.md` | Fully read during the source gate as SRC-029. Canonical `gfx_references` path, consumer-specific family rules, nominal canvases, source/native review, independent family art, DDS and asset coverage contracts. |
| R1 | [events/098_new_ore.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/events/098_new_ore.txt) | Complete file read. Directory entry blob SHA `65cf46389e2f8db1cafc3336c3e9e0554ede7722`. |
| R2 | [common/ideas/098_new_ore_ideas.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/ideas/098_new_ore_ideas.txt) | Complete file read. Blob SHA `693c61742d6cd69fbdb2bc176a7f5a214300e3ef`. |
| R3 | [common/scripted_effects/028_asteroid_incoming_runtime_effects.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/scripted_effects/028_asteroid_incoming_runtime_effects.txt) | Only mineral-control/achievement context at lines 1712–1815 and capture tail at 1910–1933 was read in full. Blob SHA `803f4dabea34d2761be29dac21c371834af33c18`. Other runtime sections were not reviewed. |
| R4 | [common/ideas/028_asteroid_incoming_ideas.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/ideas/028_asteroid_incoming_ideas.txt) | Complete file read. Blob SHA `39909009ff5a481250a77ad8abf3a0376fe06f79`. |
| R5 | [events/086_world_claims.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/events/086_world_claims.txt) | Complete file read. Blob SHA `3756bb7b2f33a10c5f8afba2d567fb4e9345f68d`. |
| R6 | [events/092_greenland_sale.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/events/092_greenland_sale.txt) | Complete file read. Blob SHA `ff360c750670be9ca619228bbd220c2faf57aded`. |
| R7 | [common/dynamic_modifiers/098_new_ore_dynamic_modifiers.txt](https://github.com/klimPaskov/Chaos-Redux/blob/master/common/dynamic_modifiers/098_new_ore_dynamic_modifiers.txt) | Complete file read. Blob SHA `4ca12cfaecdd7028a5f03f5f9c9c2398e0cab496`. Current state marker names `GFX_idea_generic_exploit_mines`, without a canvas declaration. |

Repository files were retrieved from the current `master` paths on 2026-10-07.
Directory entries were used to record exact paths and blob identities.
The listing is inventory evidence, not full reading of other listed files.
The project supplied-source gate was already complete before targeted repository retrieval.

## Fixed requirements from the current user brief

| Requirement ID | Fixed requirement | What the assembled specification must preserve |
| --- | --- | --- |
| ORE-01 | Minor Fire-Once, Chaos level 1 | One normal initial discovery per campaign, registered as fire-once rather than a repeatable event. Later deposit creation belongs to the specified evolution. Preserve the existing entry identity `chaosx.nr98.1`. |
| ORE-02 | Positive Economy, High severity | Add Event 098 to Cluster 7 at High member severity and keep catalog/UI/runtime member attributes aligned. High is the cluster member attribute, not a replacement event type or a new minimum Chaos tier. |
| ORE-03 | One uniformly random valid state globally at initial discovery | Every state in the actual valid global pool has equal probability. Country population, country size, industry, geography and player status must not silently bias the roll. One valid chosen state produces one initial deposit. |
| ORE-04 | Current controller receives at least 50 percent actual armor benefit | The benefit must affect the intended real armor statistic and broad applicable existing and newly produced/deployed armored forces or equipment. Production, defense, speed or attack alone cannot satisfy this requirement. |
| ORE-05 | Deposit remains attached to its state and capture transfers the benefit immediately | Current control, rather than original discoverer or legal owner, determines the primary entitlement. Losing control removes the lost site's contribution and gaining control grants it without a later periodic wait. |
| ORE-06 | Selected countries may gain weaker foreign access | Trade, military, faction, political and payment terms must create concrete, weaker access with consent, validity, duration/termination and a meaningful transaction. Foreign access is not primary control. |
| ORE-07 | Ordinary diplomacy and warfare revolve around the deposit | Existing relations, trade/access agreements, faction incentives, claims, war goals, occupation and peace outcomes should carry the contest. The specification must honor the user's bounded ordinary-diplomacy scope. |
| ORE-08 | Deep Vein at 200 Chaos | Stronger original/controller benefit and stronger foreign-access potential, with clear active-event and opening-at-high-Chaos treatment. |
| ORE-09 | New Deposits at 400 Chaos | Dynamic creation in random valid states, with scalable quantity/cadence, unique state identity and an explicitly defined eligible pool. Do not collapse this to one fixed follow-up deposit. |
| ORE-10 | Ore Wars at 600 Chaos | Stronger demands and war incentives tied to actual relevant deposit controllers and targets. The resulting behavior must remain ordinary diplomacy/warfare. |
| ORE-11 | Super Alloy at 800 Chaos | Extreme, perceptible armor payoff with diminishing returns for multiple ore deposits. Diminishing returns must not reduce a sole controller below the required baseline armor floor. |
| ORE-12 | Connections with 029, 092, 086 and 028 | Each named connection requires a concrete condition and consequence. The Greenland connection is conditional on the actual marketed territory containing a deposit. The asteroid relationship must state an explicit separate/combined choice. |
| ORE-13 | Complete assets, achievements, AI and lifecycle | The pack must carry accepted requirements into asset rows, achievement tracking, actor/scenario AI, logs/details/catalog alignment, capture and agreement lifecycle, validation maps and implementation handoffs. |
| ORE-14 | No silent reduction | Technical limitations must be investigated, recorded and resolved explicitly. A narrower armored target, delayed transfer, arbitrary selection bias, weak cosmetic reward or missing connection cannot be presented as compliance. |

S1 currently lists 098 as Minor Fire-Once, Chaos level 1, To Be Reworked, with blank evolution and cluster fields.
Those blanks are older catalog state and do not cancel ORE-02 or ORE-08 through ORE-12.
S2 lists existing Positive Economy members 18, 29, 34, 55, 57 and 58, with their aligned severities.
Adding 098 requires aligned member ID, role/participation, minimum tier and High severity attributes without disturbing existing members.
The workbook is the only editable catalog authority and all three CSVs must be exported afterward, as required by S5.

## Review checklist for the assembled draft

### Discovery and physical deposit identity

- [ ] The global valid-state predicate is explicit and tested against the full installed map, including live controller existence and state validity.
- [ ] Selection is uniform over states, with a declared probability of `1 / N` for each of the N eligible states at the roll snapshot.
- [ ] Initial discovery produces exactly one site, even if the campaign is already above 400 Chaos.
- [ ] Pre-fire higher-tier treatment cannot silently replace the user's initial one-state roll with a multi-site opening.
- [ ] Empty pools fail cleanly with truthful N/A/details and no deposit, payment or fired reward falsely recorded.
- [ ] Every deposit has stable state identity, source/event identity and distinct provenance from a riches mine or asteroid crater.
- [ ] More deposits do not overwrite the original site's identity or disappear when its first discoverer dies.
- [ ] Broad valid-state coverage is preserved without an unapproved continental, major-country, industrial, player or owned-state restriction.

R1 uses `random_state` with only an existing-marker exclusion and grants the opening idea through `owner`.
That is evidence of current code structure, not proof of the required global pool or engine selection distribution.
The opening recipient must be corrected to the actual controller contract in the later implementation.

### Actual armor and broad coverage

- [ ] The draft states what actual armor means for each applicable engine consumer and how a paired ore-free comparison proves the baseline requirement.
- [ ] An applicability inventory covers all relevant vanilla and Chaos Redux armored families, including later unlocked or spawned content.
- [ ] Each included family is mapped through subunit, equipment type/archetype/category, consumer and real armor output, rather than assumed from a name containing armor.
- [ ] Existing fielded formations, equipment variants, stockpiles, production, deployment, reinforcement and newly created units receive the intended effect where their actual consumer supports it.
- [ ] Armor-zero infantry or unrelated statistics are not accidentally granted invented armor merely to make a universal modifier look comprehensive.
- [ ] Mixed templates and equipped/unequipped formations have declared measured outcomes, with the formation composition held constant during comparisons.
- [ ] The owner baseline floor, weaker foreign benefit, evolution gains and multi-deposit curve are consistent under other armor bonuses.
- [ ] A future custom armored family has a documented registration/applicability obligation and validation route.
- [ ] Native engine restrictions remain explicit until source and user runtime evidence settle them.

R2 currently has an `equipment_bonus` for the `armor` family with `armor_value = 1.00` and `instant = yes`, plus armored speed, defense and attack modifiers.
R4 instead uses `armor_factor` for the asteroid main and fragment mineral ideas.
Neither file proves broad existing/new coverage or native final-stat behavior by itself.
The differences require documentation, source and runtime reconciliation before choosing a delivery surface.

### Control transfer and ongoing validity

- [ ] Control change reconciles the old and new beneficiary in the same transaction or supported control-change hook, with no daily/monthly grace period.
- [ ] Owner/controller divergence, occupation, civil war, liberation, puppeting, annexation, release, peace return and selling territory all use actual post-change control.
- [ ] Each country's benefit is recomputed from its current unique deposit contributions, preserving other still-controlled deposits and legitimate foreign contracts.
- [ ] Repeated callbacks are idempotent and cannot duplicate reward, contract or achievement credit.
- [ ] Invalid/deleted countries do not retain effects, payers, targets, access rights or live UI rows.
- [ ] Save/reload restores the same state entitlements and contract outcomes.
- [ ] The current site's public marker and controller details remain intelligible after every transfer.
- [ ] Agreement reactions to capture are explicit, including termination, suspension or new-controller ratification and any refund basis.

R2 transfers through idea cancellation and `on_remove`, with an `every_country` scan for controllers.
The timing and scope of that mechanism are not proven to satisfy immediate transfer.
S5 and latest AGENTS.md prohibit introducing unapproved periodic whole-world hooks as a replacement.

### Foreign access and normal strategic play

- [ ] Beneficiary selection is explicit and bounded to useful real countries, with invalid targets removed.
- [ ] Trade, military, faction, political and payment routes have distinct reasons to choose them.
- [ ] The controller consciously grants access and receives an actual agreed return.
- [ ] Every foreign contribution is weaker than the corresponding primary entitlement at the same ore/evolution state.
- [ ] Costs use appropriate concrete commitments and dynamic country/state factors, rather than every action being a flat political-power purchase.
- [ ] A country cannot stack duplicated contracts, retain old terms after war/capture, or obtain its own primary benefit twice as importer and controller.
- [ ] Default, refusal, revocation, broken terms, faction exit, war and controller disappearance have explicit outcomes and readable requirements.
- [ ] Ore Wars targets and incentives change ordinary strategic priorities without awarding automatic control or starting unrelated wars.
- [ ] Peaceful access remains useful and monopoly/capture remain costly meaningful alternatives.
- [ ] Public information fits the one-to-four persistent-value budget and normal decisions/details/tooltips communicate control, armor and access.

### Evolutions, AI and presentation

- [ ] All four named evolution thresholds, gates, enable/disable controls, chance/pacing and consequence are specified.
- [ ] Active actors receive evolved behavior without refiring the fire-once discovery.
- [ ] High-Chaos first firing preserves the one initial site and explicitly schedules separate evolved incidents as appropriate.
- [ ] Evolution state/activation itself gives zero Chaos, and generic war/annexation/death sources are not double counted.
- [ ] New Deposits specifies exhaustion, invalid pool, duplicate state, cadence, growth and deposit-count behavior.
- [ ] Super Alloy has an explicit diminishing curve with sole-site floor, ordering rules and source-specific asteroid treatment.
- [ ] Controller, importer, faction partner, nearby rival, distant major and World Claims actor AI have distinct strategic conditions and invalid-route zeroing.
- [ ] Probability scenarios cover full pools, boundaries, dominance, starvation and pre/post comparison rather than decorative generic weights.
- [ ] Every report/news/idea/decision/category/achievement/state-marker asset has accepted source mode, consumer, reference family and handoff.
- [ ] Achievements reward sustained mastery, difficult recovery, unusual access/capture situations and evolved outcomes, with precise tracking and disqualifiers.
- [ ] The shared log, Event Details, name selectors, evolution previews, actor mapping, disabled controls, docs and authoritative catalog wording align.
- [ ] A proposed super-event has a clear milestone, source/quote/audio research and complete family handoff if the parent accepts that presentation.
- [ ] The mandatory near-completion improvement-loop pass resolves its addendum or records closure before completion.

## Source-grounded cross-event contracts

The user's request for each named connection is fixed.
The specific interaction details below are proposals for parent acceptance unless already supplied by the user.
An interaction must use current, verified owner APIs or a reviewed owner-side extension and must not silently modify another event's ledger.
This follows the owner/private API separation in S4.

### 029 Riches Found

S1 describes a state-attached mine with income/industrial value following current control, claims, transport/housing, revenue settlement, concessions, security and foreign-capture risk.
Its named evolutions are Institutional Corruption, Gold Disease and an underground force.

**Proposed entry condition:** the state has an actual active Event 029 mine and an actual Event 098 ore deposit, or a concrete ore-access negotiation is directed at that mine's current controller.
Simple global coexistence should not imply shared extraction from different states.

**Proposed consequence:** use the mine's real transport, housing, security or concession circumstances to change an ore extraction/access negotiation or a joint investment outcome.
Preserve separate sources of mine revenue, ore armor entitlement and foreign contract rights.
The ore event does not automatically grant 029's initial political windfall, replay its repeatable discovery, or inherit Gold Disease/underground consequences solely because both minerals exist.
If the parent accepts a real shared-site incident, its condition, agency and outcome should be authored explicitly and call the 029 owner through a verified interface.

**Lifecycle acceptance:** capture reconciles both state-attached benefits once with their owners, and a terminated ore contract cannot erase mine concessions or vice versa.
Different-state and same-state cases must produce intentionally different results.

### 092 Greenland Sale

S1 says countries compete to buy Greenland.
R6 contains Danish offer and buyer-facing events, but the inspected event file alone does not prove exact current sale-settlement, state-transfer or bid-price mechanics.

**Fixed entry condition:** the exact territory currently offered for sale includes a live ore deposit.
An ore site somewhere else, a Greenland story mention, an unrelated concession or a sale offered but withdrawn is not a completed transfer.

**Proposed consequence:** identify the included ore sites in the offer and modify the real valuation, bid incentive or access terms through the sale owner's verified transaction.
Keep the ordinary auction/sale event as the sale owner.
If an accepted sale actually transfers control of a deposit state, the primary ore benefit transfers through the normal control lifecycle.
If it transfers only ownership while controller remains unchanged, the ore beneficiary does not change merely because a deed changed hands.

**Lifecycle acceptance:** refusal, sale cancellation, competing bids, invalid seller/buyer and a deposit outside the marketed state set produce no ore transfer.
Existing foreign access follows the explicitly accepted contract ratification/termination rule.

### 086 World Claims

S1 permits Germany or the Soviet Union to proclaim a claim to the world.
R5 currently chooses Germany and its accepted option adds claims to every state.
That source/catalog difference must remain explicit until the parent verifies the intended current claimant behavior.

**Proposed entry condition:** an actually participating World Claims actor has a relevant claim and strategic interest in a live ore state controlled by another country.
The claimant is taken from the event's actual runtime outcome, not invented from the catalog's alternative actor description.

**Proposed consequence:** the valuable ore state sharpens an existing claimant's target priorities, access demand, ultimatum or war-goal incentive through normal diplomacy.
Claims remain claims.
They do not grant legal ownership, current control, primary armor or an importer contract.
Ore Wars can strengthen the incentive while preserving war legality, target validity, faction/subject relations and refusal paths.

**Lifecycle acceptance:** an inactive/dead claimant, withdrawn claim, allied/subject conflict or a state already controlled by the claimant cannot produce a stale demand or duplicate entitlement.
Capture supplies control-based benefit whether or not the conqueror had a claim.

### 028 Asteroid Incoming

S1 says Extraordinary Minerals at 800 Chaos requires Global Fragmentation and grants transferable land-division armor of plus 100 percent from the main crater and plus 20 percent per fragment site.
S4 indexes a newer current-controller mineral API with unique processed fragment counts, uncapped armor, caller scopes, normal outputs and annex/release cleanup.

The exact indexed documentation path `common/scripted_effects/028_asteroid_incoming_mineral_effects.md` was reported 404 by the parent.
This reader's exact `.txt` fetch also returned 404, code search returned no results, and a successful current `common/scripted_effects` directory inventory had no matching mineral API `.md` or `.txt` file.
R3 has older embedded refresh logic with six explicit fragment idea slots and every-country removal before reapplication.
R4 has separate main/fragment armor-factor ideas.
This is a material supplied-source/current-repository discrepancy.
It does not establish that the indexed uncapped owner API is usable from the fetched revision.

**Fixed design decision:** explicitly choose how ore and asteroid mineral contributions relate.
The pack must not leave separate versus combined behavior to incidental native stacking.

| Choice | Proposed contract | Required proof |
| --- | --- | --- |
| Separate ledgers, explicit coexistence | Each event keeps its own physical-site ledger, controller entitlement, foreign-access rules and diminishing-return rules. State coexistence does not create a bonus merger. The pack still specifies the exact final-stat composition of both accepted sources. | Paired ore-only, main-crater-only, fragment-only, both-same-state and both-different-state results. Event 028's specified main/fragment gains remain intact. |
| Deliberate combined alloy route | A defined, visible alloy choice or bounded production agreement requires real access to both mineral sources and explicitly changes the ore contribution or combines source outputs. Preserve source IDs, site provenance and the independent Event 028 contract. | A complete recipe/eligibility/consent/cost/termination design and explicit before/after source contribution matrix. Capture or access loss removes the correct component without deleting the other event's benefit. |

The table offers two design alternatives and does not select one for the user.
The parent must record the accepted choice and its exact armor-composition rule.
A combined final display can still preserve separate owner ledgers, but such aggregation is a proposal pending owner API and engine verification.
Ore's multi-deposit diminishing returns must not silently cap Event 028's separate per-fragment entitlement described in S1/S4.
Unique-state/source accounting is mandatory for a shared site to avoid counting one crater or ore state twice through aliases or repeated callbacks.

## Important semantic risks and resolution evidence

| Risk | Why it can invalidate the requested design | Review resolution |
| --- | --- | --- |
| Global uniformity confused with a country-first draw | Equal country probabilities followed by equal country-local state probabilities would bias states by country size. Native `random_state` behavior has not been verified by this reader. | Define the global eligible pool, inspect the actual selector and use a complete candidate distribution. No probability claim from an incomplete country/state pool. |
| Legal owner mistaken for controller | R1's opening grant uses `owner`, which can differ from controller during occupation. | Paired occupation and owner/controller-divergence cases must grant only the actual controller's primary entitlement. |
| Displayed plus 50 percent mistaken for actual relative improvement | A modifier label, base-stat additive increase, equipment bonus and final formation armor can differ. Other bonuses and composition can change the paired result. | Define the reference statistic and compare the same formation/equipment with all non-ore conditions held constant. If the user means final-value uplift, an additive factor alone must not be assumed sufficient. |
| One equipment family mistaken for all armored content | R2's `armor` equipment family is not evidence that every armored car, mechanized, special armored or future custom family is covered. | Inspect exact installed/mod family mappings and measure named representative existing/new consumers. Carry unresolved families as blockers. |
| Rewriting only future equipment | The user includes existing forces, so a new production model or tech unlock alone can miss fielded formations and old stock. | Separate existing-fielded, stockpile, variant, newly produced/deployed and reinforcement scenarios with actual stat evidence. |
| Transfer through delayed idea cancellation | R2 provides no evidence of same-transaction removal/grant or exhaustive release/annex behavior. | Read supported control callbacks and verify before/after states for old and new countries, including repeated callbacks and save/reload. |
| Multiple sites overwritten or counted twice | A single global `ore_state` container or repeated idea identities can lose contribution provenance. | Maintain a unique live-state/source inventory and test capture of one site while retaining another. |
| Foreign access surviving invalid terms | Capture, faction exit, war, payment default or donor disappearance can leave a free armor effect. | Explicit per-contract validation, settlement/termination and current-controller consent with zero duplicate sources. |
| Super Alloy curve weakening the mandatory floor | A global cap or averaging curve can lower a sole controller below the baseline or penalize capture. | State the floor and each marginal contribution, and compare one/two/many sites before and after transfers. |
| Asteroid policy changed by accidental shared cap | Ore diminishing returns could weaken the separate main/fragment contract. | Explicit source-aware composition and independent Event 028 acceptance. Resolve current API mismatch first. |
| Threshold activation mistaken for evolution consequence | Logging at 200/400/600/800 can omit playable changes or refire discovery. | Define active-event and pre-fire entry, MTTH/timing, disabled evolution paths and zero activation Chaos. |
| Greenland flavor mistaken for territory marketing | Global event coexistence can create bid or armor effects when the actual ore state is not offered. | Compare exact marketed-state identity to current ore site inventory and the completed transfer result. |
| Claim mistaken for entitlement | A global claim could grant armor without access, possession or consent. | Keep political claims separate from current control and valid weaker agreements. |
| Catalog completion mistaken for implemented completion | 098 currently has blank evolutions and no cluster row, while planning creates complete intent. | Catalog status remains honest until gameplay, assets, docs and meaningful validation meet the repository completion contract. |

## Named acceptance scenarios for the later audit

| Scenario | Minimum observed or documented expectation |
| --- | --- |
| Uniform pool with unequal country sizes | Every valid state has the same initial selection share regardless of country state count. |
| Occupied discovery | The owner and controller differ. Only controller gets the primary ore entitlement. |
| Existing and newly deployed armor | Matching representative existing/new formations or equipment show the agreed actual armor uplift. |
| Broad applicable-family matrix | Vanilla and custom armored families include tanks and their relevant roles, armored cars/mechanized or special families where their actual armor consumer applies, and future-family registration. Any domain ambiguity is resolved explicitly. |
| Immediate capture A to B | A loses the site's contribution and B gains it in the accepted control-change transaction. Other sources remain unchanged. |
| Two-site controller loses one | Its diminishing-return total is recomputed, rather than losing all ore or retaining both contributions. |
| Release, annexation and civil-war controller | Entitlement follows current live controller and no dead-country residue remains. |
| Trade/military/faction/political/payment access | Distinct accepted obligations produce weaker access, and violation/termination behaves as specified. |
| Capture with foreign contract | The imported right follows the accepted ratification/termination rule, without silent retention or duplicated payment. |
| 200/400/600/800 entry and disabled tracks | Each named evolution has real behavior, truthful logging, an active-event path and safe disabled-state handling. |
| New Deposits exhausted pool | No duplicate sites, invalid targets or endless attempts. Quantity and cadence remain dynamic when valid states remain. |
| 029 same state versus different states | Only the explicit shared-site/access condition triggers the accepted concrete connection. |
| 092 offered state includes/excludes ore | Price/access connection occurs only for included ore territory, and control transfer occurs only on a completed real transaction. |
| 086 claimant/controller distinction | Claims change strategic priorities but grant no primary armor. Capture and lawful weaker access remain separate. |
| 028 alone, 098 alone and both | Exact chosen armor composition and each owner's source contribution are visible and preserve accepted contracts. |
| AI import versus attack, nearby versus distant | Named scenarios show intended preference ordering, valid targets, no starvation of peaceful access and deliberate 600-Chaos aggression. |
| Achievement abuse attempts | Trading a state back and forth, repeating callbacks, self-contracting, puppet shortcuts and duplicated sources do not farm milestones. |
| Save/reload | Site identity, actual controllers, source contributions, terms, evolution history and achievements survive without recomputing false ownership. |

These are future task-specific checks, not checks already passed.
The coding parent must use event inspect/render/compare and probability inspection/evaluation/sweeps/compare through the relevant project audit roles when those routes are available.
Unavailable routes must remain explicit in the final evidence and cannot be replaced with an engine-validation claim from source review.

## Asset reference evidence and production gates

The parent's current presentation direction is native ordinary decisions, one eligible static category picture, direct/controller and foreign-access idea icons, a state-deposit icon, report/news art and achievement icons.
This direction remains within S6/S8's ordinary-category hierarchy when the category contains concise text, an ordinary decision list and at most basic formatted values.
The picture eligibility gate must be reconsidered if the accepted category later gains custom controls, meters, rich panels or other animations.
The family list describes relevant requested presentation and does not authorize other asset families.

S8 explicitly makes `.agents/skills/chaos-redux-event-assets/assets/gfx_references/` the canonical reference root.
Any residual `vanilla_reference` terminology in older project material requires path reconciliation rather than an automatic legacy substitution.
The exact following GitHub contents paths were attempted on 2026-10-07 and all returned 404 from the fetched current repository:

- `.agents/skills/chaos-redux-event-assets/assets/gfx_references/README.md`
- `.agents/skills/chaos-redux-event-assets/assets/gfx_references/CATALOG.md`
- `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/ideas`
- `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/decisions`
- `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/decision_categories/pictures`
- `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/state_modifiers`
- `.agents/skills/chaos-redux-event-assets/assets/gfx_references/icons/achievements/template/overlay.png`

These responses mean the requested reference evidence could not be inspected through these repository paths.
They do not prove that the user's installed local reference shelf is missing.
No reference image, contact sheet, template pixels or native consumer texture was visually reviewed by this reader.

| Asset surface | Source-supported planning canvas | Exact future evidence required before final production |
| --- | --- | --- |
| Controller/direct and foreign-access idea icons | Nominal 64x64 idea family from S8. Distinct original sources for the two meanings. | `gfx_references/icons/ideas/contact_sheet.png`, cataloged owning sprite/consumer and exact current idea `.gfx`/DDS. Any visual-components layer must have a permitted catalog role. |
| Ordinary action icons | Nominal 32x32 ordinary decision family from S8. | `gfx_references/icons/decisions/contact_sheet.png` and exact owning decision sprite/native consumer. Category icons are a separate family. |
| Eligible static category picture | S8 identifies 114x101 as this reference family's native example canvas. It explicitly says the actual consumer decides the final target. | `gfx_references/icons/decision_categories/pictures/contact_sheet.png`, CATALOG row and the exact category picture sprite plus native category `.gui` consumer, crop/alpha behavior and any scale/frame settings. Do not present 114x101 as already verified for the proposed runtime category. |
| State-deposit marker | Consumer-specific and unresolved. No universal 64x64 state-modifier size is justified. | `gfx_references/icons/state_modifiers/contact_sheet.png`, exact active marker definition and owning sprite/texture/GUI consumer, DDS native dimensions, visible bounds, alpha and frame/state semantics. R7 supplies current marker identity but not dimensions or verified final appearance. |
| Report picture | Nominal final 210x176 with local tilted documentary-card treatment from S8. | `gfx_references/event_art/report/contact_sheet.png`, actual event sprite path, source/processed art, consumer framing, processor and final DDS/native review. |
| News picture | Nominal final 397x153 black and white from S8. | `gfx_references/event_art/news/contact_sheet.png`, actual news sprite/consumer, source-mode/era proof and final DDS/native review. |
| Achievement triplets | Exact 64x64 supplied-template workflow in S8. | `gfx_references/icons/achievements/contact_sheet.png` plus untouched `template/achievement_template.png`, `achievement_template_grey.png`, `overlay.png`, verified source integrity, aligned original color/grey/not-eligible layers and final strict DDS pixel-equality proof. |

R7 currently reuses an idea sprite identity for the state marker.
That reuse is evidence of the current lookup token, not approval to resize a new controller idea into the requested state-deposit family or to assume its display dimensions.
S8 requires separate family-specific briefs, original source art, actual consumer references and asset rows.

Before production, the asset handoff must read the local canonical README/CATALOG, inspect each matching contact sheet and exact individual reference, then follow the owning definition to the native DDS and GUI consumer.
Record source path, owning token, native width/height, noOfFrames/frame order, alpha/background treatment, visible painted bounds and consumer display scale.
If any required reference or consumer cannot be inspected, keep its target dimension provisional and mark that row `blocked` or `needs_user_review` for production.
An inaccessible reference does not authorize a guessed canvas, renamed old art, primitive substitute or undocumented alternate reference library.

## Handoff disposition

All ORE fixed requirements are supplied user design.
The connection details, paired-stat comparison definition and specific contract reactions are review proposals until the parent records acceptance.
Native selector behavior, exact armor delivery and future-family reach, immediate callbacks, completed sale mechanics, current World Claims actor scope and the indexed asteroid API remain implementation questions requiring the stated evidence.
The parent should map each checklist row to the assembled draft, resolve the asteroid separate/combined choice and technical gaps, and then send the complete pack for the actual read-only completion audit.
