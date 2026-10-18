# Event 107 Lootboxes and Event 108 Wrestling probability review

Audit date: 2026-10-10

Disposition: Read-only design-math review complete. The imported packages are planning specifications, not implemented gameplay sources. The calculations below establish what the authored formulas imply; they do not establish native game behavior or campaign balance. One numeric boundary defect is identified in Event 108, and one engine-randomness requirement is missing from the Event 107 implementation handoff.

## Scope and source identity

The immutable inputs were read from .tmp\import107_108_112_20261010\original\107_lootboxes_specs\ and .tmp\import107_108_112_20261010\original\108_wrestling_tournament_specs\. The current docs\specs copies of Event 107 Parts 02, 03, and 05 and Event 108 Parts 03 and 06 had byte-identical SHA-256 values to their original package copies at audit time.

| Surface | Exact source file | SHA-256 |
| --- | --- | --- |
| Event 107 invariant | .tmp\import107_108_112_20261010\original\107_lootboxes_specs\01 - Event Identity and Core Loop.md | 6C7C0BF4655CD7CEE096629BD175AD1A07A209385B48601B9F74D7011E32989A |
| Event 107 rarity formulas | .tmp\import107_108_112_20261010\original\107_lootboxes_specs\02 - Rewards, Probabilities and Evolutions.md | F59DA829AF3A50C1D83F28A5B772DBEE67E70751D8CE67A223E76FFDDAB60AC7 |
| Event 107 burden and recovery | .tmp\import107_108_112_20261010\original\107_lootboxes_specs\03 - Hidden Influence and Peace Recovery.md | 1148270427F051BEF05BCA8E74B2FDF0AA32152FBF41E90D0CE8B8FF3AA6D9AD |
| Event 107 AI and integration | .tmp\import107_108_112_20261010\original\107_lootboxes_specs\05 - Decisions, AI and Integration.md | FEEE4D9DCC6DA4BFBF1B9D0B1C15703FAE6C37F2AE909EA45895499FE3670BBD |
| Event 107 acceptance invariants | .tmp\import107_108_112_20261010\original\107_lootboxes_specs\06 - Achievements and Validation.md | F33FBD5D487E884801DF2FEC674A8E38108B44159B835EC259E93B67CF9C1C4F |
| Event 108 entrant and calendar boundaries | .tmp\import107_108_112_20261010\original\108_wrestling_tournament_specs\01 - Tournament, Countries and Careers.md | 87B8C6136016906954F1A9EFD639502A948D4FCAD83F32603CE6E83209EE6FEB |
| Event 108 action and pool boundaries | .tmp\import107_108_112_20261010\original\108_wrestling_tournament_specs\02 - Preparation, Decisions and Scandals.md | AFF4E7B5A860CB8CEC4AEE88D26BD682B8184CD7D6A86B86F733A1A63CA29BE1 |
| Event 108 match, draw, and award formulas | .tmp\import107_108_112_20261010\original\108_wrestling_tournament_specs\03 - Seeding, Matches and Championships.md | 11267C306953A742CB8406053E949D0428F5BBDC875483D0BED581D3BE5F66D7 |
| Event 108 corruption bounds | .tmp\import107_108_112_20261010\original\108_wrestling_tournament_specs\04 - Evolutions and Cross-event Connections.md | F953028F8F1946804D4B7B7ACC906F3D5B77AECBF2D47441312892F86C8BF15B |
| Event 108 AI and probability handoff | .tmp\import107_108_112_20261010\original\108_wrestling_tournament_specs\06 - AI and Probability Handoff.md | B69E3F69BD6B10532F34E690FFE70A993D1019EF4FD07DB244CE137EF75E045A |
| Pure design calculator | .tmp\import107_108_112_20261010\original\108_wrestling_tournament_specs\Design Math Check.py | 630AB4D044053F84E638745BA4284B3EF133818316372E9802B736CFC932AC59 |

## MCP and reference evidence

The initial read-only MCP call was hoi4.probability_inspect with adapter custom_weighted_pool and source docs/specs/107_lootboxes_specs/02 - Rewards, Probabilities and Evolutions.md. It returned status error, code PROBABILITY_SOURCE_NOT_FOUND, workspaceId mod_chaos_redux_ea3b2d67c2c0, filesScanned empty, and no artifacts. The path exists locally as Markdown, but it is not a probability source recognized by the adapter. No retry was made because the package has no Clausewitz probability source to select instead. No probability evaluation, sweep, comparison, simulation, sequence, or render was produced, and there is no analysis ID, scenario hash, comparison ID, artifact URI, or rendered evidence path.

The local reference workflow succeeded for the rules used in this audit:

| Local reference | Path and lines | Revision | Rule used |
| --- | --- | --- | --- |
| Offline wiki, AI modding | paradox_wiki\AI modding - Hearts of Iron 4 Wiki.md, lines 26-37 | 917cd261f7da51fe4d8687c5d7663e768a09c5c101ac130ce646bc64637aa818 | Most ai_will_do values are sampled as scores; event-option ai_chance is a separate proportional pool with a 1-percent effective resolution. |
| Offline wiki, event options | paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md, lines 151-179 | 96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d | Event options have their own complete ai_chance pool; the resulting shares are quantized to whole percentages. |
| Offline wiki, decision AI | paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md, lines 357-374 | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 | ai_will_do is required for AI consideration of a decision; it is not a normalized click chance. |
| Offline wiki, repeated-decision seed | paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md, lines 383-386 | 7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162 | A repeated decision uses a fixed random seed by default; fixed_random_seed = no permits a different random result. |
| Offline wiki, random effects | paradox_wiki\Effects - Hearts of Iron 4 Wiki.md, lines 4504-4571 | 997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c | random_list weights normalize by their sum; repeatable decisions can replay the same result unless their seed is made dynamic. |
| Installed game documentation, random_list | Hearts of Iron IV\documentation\effects_documentation.md, lines 5413-5432 | 2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af | random_list selects a random effect using its associated weight; current-scope variables can be weights. |
| Vanilla decision source lookup and direct read | game:common/decisions/FRA.txt, line 56; owner FRA_communist_civil_war_decision, lines 3-66 | MCP source revision d832ed8249f25306b27b6957c92a61532a9e42212711984db8365f4b2c4e3588; direct-file SHA-256 19422E278C26A662E4DBD2996D60E77AC04BF03AF8D19DB4B7D2B6B445A7376C | A vanilla repeatable decision contains fixed_random_seed = no in the decision body. This confirms the syntax and placement; the offline wiki above supplies the repeated-random-list behavior. |

The design calculator was opened and inspected before execution. It contains only bounded arithmetic, assertions, and prints; it performs no file reads or writes and invokes no game runtime. Running it returned PASS for seed permutation, half and quarter placement, high-seed byes, no empty-versus-empty first pairing, N-1 intact-field bouts, N-32 qualifiers, 32 unique main entrants, probability symmetry and monotonicity on Delta -200 through 200, double-absence handling, 130,816 registration-to-lock field pairs, 2,807 official-bias threshold contexts, and selected all-upset identity propagation. It printed 50/50 at Delta 0, 71.2574/28.7426 at 12, 85.0333/14.9667 at 24, 92.8310/7.1690 at 40, and 95.3843/4.6157 at 60.

## Event 107: Lootboxes

### Rarity pool normalization and suppression

Let poor-result pressure p range from 0 to 1, and let the fixed conditional split among non-Common tiers be Rare 65%, Epic 25%, Mythic 8%, and Legendary 2%. The authored anchors imply Common = 70% - 15p for ordinary boxes and Common = 60% - 15p for Premium boxes. Each remaining probability is (1 - Common) times its fixed conditional split.

| Shell | Pressure p | Common | Rare | Epic | Mythic | Legendary | Sum |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Ordinary | 0 | 70.00% | 19.50% | 7.50% | 2.40% | 0.60% | 100% |
| Ordinary | 0.5 | 62.50% | 24.375% | 9.375% | 3.00% | 0.75% | 100% |
| Ordinary | 1 | 55.00% | 29.25% | 11.25% | 3.60% | 0.90% | 100% |
| Premium | 0 | 60.00% | 26.00% | 10.00% | 3.20% | 0.80% | 100% |
| Premium | 0.5 | 52.50% | 30.875% | 11.875% | 3.80% | 0.95% | 100% |
| Premium | 1 | 45.00% | 35.75% | 13.75% | 4.40% | 1.10% | 100% |

For an ordinary-to-Premium shell mixture with Premium incidence s, the unconditional pool is the convex combination (1-s) ordinary plus s Premium at the same pressure. At the authored 20%-35% Premium incidence bounds, fresh-history mixtures are [68, 20.8, 8, 2.56, 0.64]% at s = 20%, and [66.5, 21.775, 8.375, 2.68, 0.67]% at s = 35%. Maximum-pressure mixtures are [53, 30.55, 11.75, 3.76, 0.94]% and [51.5, 31.525, 12.125, 3.88, 0.97]% respectively. Each sums exactly to 100%.

The five rarity tiers form a complete declared top-level pool. All are strictly positive and strictly ordered in every ordinary, Premium, and mixed state. The narrowest adjacent margin is Mythic over Legendary at fresh ordinary pressure, 1.8 percentage points. The narrowest Common-over-Rare margin in a single shell is 9.25 points for maximum-pressure Premium. In the 20%-35% shell mixture, the narrowest Common-over-Rare margin is 19.975 points at maximum pressure and 35% Premium incidence. Raising pressure from zero to one moves 15 points from Common into the other tiers while preserving their 65:25:8:2 split, so all four non-Common probabilities rise. Premium at a matched pressure moves 10 points from Common into the same split, raising every non-Common tier. No rank reversal or top-level rarity starvation occurs in the declared decimal model.

The precision condition remains untested: Part 02 requires each tier to stay positive after conversion to the engine's supported weight precision, and no actual Clausewitz source or active pool exists. The 0.60% ordinary-fresh Legendary entry is mathematically positive, but its native representation has not been established. These percentages must be implemented through a proportional random pool or another verified sampler, not event-option ai_chance, whose documented d100 resolution cannot preserve arbitrary sub-1% shares.

Within-tier recipe pools are not complete. The reward-family matrix is a planning map, not a list of certified recipe identifiers and actual country eligibility. The design correctly requires all tiers to retain eligible useful recipes and says an empty tier must not shift probability to Common, but exact recipe probabilities, country-specific starvation, and reward dominance cannot be calculated until those pools and providers exist.

### History, burden, and recovery

The illustrative pressure transition is +2 after each completed Common result, -3 after any completed non-Common result, clamped to [0,100]. The next reward samples the already earned pressure; the current opening updates it only after completion. In named history scenario LB-HIST-C-C-N-C, pressure progresses 2, 4, 1, 3 and burden progresses 5, 10, 15, 20. The next ordinary rarity pool is 69.55% Common, 19.7925% Rare, 7.6125% Epic, 2.436% Mythic, and 0.609% Legendary.

In LB-HIST-25-COMMON, 25 completed Common boxes produce pressure 50 and burden 125 with no recovery. The next ordinary pool is the p=0.5 row above, while the country is already in the Deep burden band. Fifty consecutive Common results reach pressure 100 and burden 250; future Common remains 55% ordinary or 45% conditional Premium. The history saturates, does not approach a pity guarantee, and does not use lifetime count alone. At every finite pressure value the Common probability remains positive.

With 5 burden per completed opening and no recovery, the fifth completed opening moves burden from 20 to 25 and enters Established; the twelfth moves 55 to 60 and enters Heavy; the twenty-fourth moves 115 to 120 and enters Deep. These are exact consequences of the illustrative burden charge and the authored band boundaries. The opening-level omen chance after evolution is only bounded by the spec's broad bands: low single digits for Light, 5%-15% Established, 15%-30% Heavy, and 30%-45% Deep. Current Chaos and recent cadence affect those values, but no exact function or complete quiet/immediate/delayed/combined weight pool is authored. The actual episode probability, outcome mix, delay branch share, and cumulative 90-120 day sequence therefore remain unresolved. The one-episode gate and terminal delayed check prevent multiplying an immediate risk by a separate later withdrawal roll.

Peace recovery is bounded by actual attributable negative Chaos, conversion of 5-15 burden per allocated point, and current burden. At the first baseline conversion of 10, an actual one-point contribution can remove at most 10 existing burden, or two ordinary box charges; the zero-burden state cannot bank future credit. A request for -3 when global Chaos is 1 provides only one actual point, hence at most 10 existing burden at the baseline. These are exact design calculations; the source-contributor inputs and owner callbacks remain unimplemented.

### Payment, pending commitment, and AI policy

The fixed 50 PP price, one unresolved paid box, sealed contents, five accepted human activations, and no paid reroll make the result non-rerollable by closing, saving, or reopening. The UI uses no campaign day between accepted activations. However, burden and the hidden episode commit on the fifth accepted activation, and the episode uses completion-time evolution, Chaos, post-opening burden, and cadence. A human can pay, retain one sealed box, and defer both its reward and its risk until a chosen completion time; the spec expressly permits recovery before completion to lower existing burden. This creates a timing option, not a reroll. AI purchases auto-resolve through the common path, so parity of rules at matched completion state is specified, while parity of player-selected completion timing is not. This is a deliberate unresolved balance/information boundary that should receive a named immediate-versus-delayed completion scenario.

A more important engine integration risk is not specified in the package. Event 107 uses a repeatable purchase decision as its recurring action. The offline Decision modding section says decisions use a fixed random seed by default, so a random_list run inside the same repeated purchase decision can return the same result every time. If the rarity or recipe sampler executes in that decision's effect, the accepted design needs fixed_random_seed = no or another verified unique per-purchase seed. The one-time seal must still occur at payment and be retained before the GUI opens. This is conditional on the chosen implementation route; no current script exists to prove the defect has occurred.

The syntax is corroborated by installed vanilla source: game:common/decisions/FRA.txt has fixed_random_seed = no at line 56 inside FRA_communist_civil_war_decision. MCP source_lookup returned complete location coverage at revision d832ed8249f25306b27b6957c92a61532a9e42212711984db8365f4b2c4e3588, and the direct installed-file read matched SHA-256 19422E278C26A662E4DBD2996D60E77AC04BF03AF8D19DB4B7D2B6B445A7376C. This is a syntax/placement precedent, not proof that vanilla's decision implements Lootboxes behavior.

The human purchase threshold is exactly 50 PP. The AI reserve rule is score policy, not selection probability: PP must be at least 50 plus the greater of the reserve floor and urgent obligations plus a 25 PP buffer. With no larger obligation, the 100 PP ordinary floor implies a 150 PP threshold; a 200 PP crisis floor implies 250 PP. If an urgent commitment costs C PP and controls the reserve, the threshold is C + 75 PP. The planned 30-day ordinary opportunity interval and approximately 60-day severe-crisis deferral are cadence anchors, not a measured purchase frequency. Native decision willingness is a score/priority until its full candidate set and engine choice route are inspected. It must not read hidden burden or omen chance.

## Event 108: Wrestling tournament

### Draw totals and calendar

For a locked field N, P is the next power of two at least N. The intact single-elimination tree has P-N first-round byes and N-1 contested bouts. Above 32 entrants, N-32 of those bouts are qualifiers and 31 occur in the 32-place main draw. The supplied recurrence preserves seed identities and leaves the top seeds with the needed byes.

| Locked entrants N | Leaves P | Byes | Qualifier rounds | Qualifier bouts | Main bouts | Total contested bouts |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 2 | 0 | 0 | 0 | 1 | 1 |
| 3 | 4 | 1 | 0 | 0 | 2 | 2 |
| 12 | 16 | 4 | 0 | 0 | 11 | 11 |
| 17 | 32 | 15 | 0 | 0 | 16 | 16 |
| 32 | 32 | 0 | 0 | 0 | 31 | 31 |
| 33 | 64 | 31 | 1 | 1 | 31 | 32 |
| 47 | 64 | 17 | 1 | 15 | 31 | 46 |
| 64 | 64 | 0 | 1 | 32 | 31 | 63 |
| 65 | 128 | 63 | 2 | 33 | 31 | 64 |
| 128 | 128 | 0 | 2 | 96 | 31 | 127 |
| 257 | 512 | 255 | 4 | 225 | 31 | 256 |

For the default 90-day preparation, registration closes day 20, roster lock is day 110, the first reserved competition slot is day 120, and later round slots are five days apart. With R countries accepted at close, the reserved round count is ceil(log2 R); with N locked entrants, the actual tree uses its matching number of trailing reserved slots. WT-CAL-R65-L32 therefore schedules days 130, 135, 140, 145, and 150, retaining the published final on day 150. WT-CAL-R65-L2 uses only the trailing day 150 final. WT-CAL-R47-L32 uses days 125 through 145. The calculator exhaustively checked every registered R from 2 through 512 and every locked N from 2 through R, totaling 130,816 pairs. This is exact calendar arithmetic under the authored formulas, not a maximum population guarantee; the spec explicitly says 512 is test coverage, not the eligible-country cap. No actual roster count or engine storage limit was inspected.

### Conditional match probability and ordering

For two fit eligible wrestlers with a frozen input snapshot, the planning equation is p(A) = 0.04 + 0.92 / (1 + exp(-Delta/12)), where Delta = S_A - S_B + C and C is the bounded antisymmetric approach adjustment. With all outside inputs included in Delta, this is an exact conditional design probability:

| Delta | A win | B win | Interpretation |
| ---: | ---: | ---: | --- |
| -60 | 4.6157% | 95.3843% | A is the underdog; its upset chance remains above the 4% asymptote. |
| -40 | 7.1690% | 92.8310% | A can still upset. |
| -24 | 14.9667% | 85.0333% | A remains a credible but clear underdog. |
| -12 | 28.7426% | 71.2574% | A remains the upset path, including the authored <=30% upset-report condition. |
| 0 | 50.0000% | 50.0000% | Equal fit entrants remain exactly even. |
| 12 | 71.2574% | 28.7426% | A is favored but B still has the authored upset-report chance. |
| 24 | 85.0333% | 14.9667% | A is favored; B retains a material upset chance. |
| 40 | 92.8310% | 7.1690% | A strongly favored, not guaranteed. |
| 60 | 95.3843% | 4.6157% | Near the cap while preserving an ordinary underdog path. |

The function is strictly increasing with Delta and satisfies p(-Delta) = 1 - p(Delta). At equal base scores, C=+4 yields A 57.5965%; C=-4 yields 42.4035%. In WT-APPROACH-REVERSAL, a base A-minus-B score of -2 plus the maximum +4 approach adjustment gives Delta +2 and 53.8245% for A, compared with 46.1755% at Delta -2. The bounded approach cycle can reverse close comparisons whose raw difference is less than four points; it cannot dominate a large score gap. This is exact conditional formula math. The seed score uses five public normalized criteria, while the match score uses six physical attributes, condition, injury, study, unfamiliarity, and approach. Seed rank alone does not establish match probability, and no complete entrant profiles exist for a field-level champion ranking.

The pure checker tests probability symmetry, monotonicity, and bounds over Delta -200 through 200, wider than the approximately -160 to +160 range derived from the declared score bounds and C. The effective maximum/minimum cap is approached rather than attained at finite Delta. Full tournament champion probabilities remain unresolved: opponent profiles, actual draw, changing fatigue and injury, recovery, public information, AI choices, and all later pairings affect the field-level result. Part 06 correctly forbids multiplying a single-bout chance five times as if those factors stayed fixed.

### Complete authored random pools and AI scores

These are exact normalized design pools only when all listed candidates are eligible and their weights are implemented through a proportional random-list mechanism. Modifiers and excluded branches change the denominator.

| Scenario | Declared complete baseline pool | Normalized result |
| --- | --- | --- |
| WT-CAMP-BASELINE, healthy camp with every branch eligible | no incident 800; favorable report 70; strain/injury 30; allegation 20; tonic 20; experimental offer 10; sponsor pressure 30; eligibility friction 10; travel trouble 10 | 80%, 7%, 3%, 2%, 2%, 1%, 3%, 1%, 1% |
| WT-INJURY-BASELINE, healthy ordinary bout | no new injury 940; manageable injury 50; serious injury 10 | 94%, 5%, 1% |
| WT-INV-TRUE-STRONG | substantiated 800; cleared 20; inconclusive 180 | 80%, 2%, 18% |
| WT-INV-TRUE-WEAK | substantiated 250; cleared 100; inconclusive 650 | 25%, 10%, 65% |
| WT-INV-INNOCENT-STRONG | substantiated 0; cleared 850; inconclusive 150 | 0%, 85%, 15% |
| WT-INV-INNOCENT-WEAK | substantiated 0; cleared 450; inconclusive 550 | 0%, 45%, 55% |

Each of the four winner-dependent result-method rows sums to 100: at least 24 advantage uses 55/30/10/5; 12 up to 24 uses 40/30/20/10; 0 up to 12 uses 15/35/35/15; underdog winner uses 10/45/30/15. The official-dependent branch is a separate complete two-method pool, narrow decision 60 and long decision 40, with pins and submissions excluded. The normal pin-versus-submission subpool does not have a separate declared split, so method-family probabilities are exact conditional weights but the internal submethod distribution is incomplete.

AI inputs are scores, not click chances. The peaceful invitation fixture lists Enter 65 and Decline 35. The healthy training fixture lists seven legal camp scores 15/20/20/10/10/5/20; the strained fixture lists 5/10/10/5/10/50/10 only when those options remain legal. Their sums of 100 do not establish normalized probabilities for native decision AI, a GUI selector, or independently visible actions. Nomination, funding, approach, corruption, and other family weights do not have complete numeric pools. No frequency, dominance, or total AI tournament entry probability can be claimed.

The camp incident pool is complete only in its named healthy fixture. When a scientific offer or another branch is unavailable, the spec says to remove that candidate and recompute the active denominator. High Strain, injury, risky training, travel, and treatment factors are not numerically specified, so those states are bounded or unresolved rather than exact. The same holds for injury modifiers outside the healthy reference case.

### Official-bias information and pool

The correct declared method uses one three-branch pool from p_clean and p_biased. If the scheme favors A, the weights are p_clean for an unaffected A win, p_biased minus p_clean for an official-dependent A win, and 1 minus p_biased for an unaffected B win. Reverse the threshold ownership when the scheme favors B. Rounding both threshold values to the same integer denominator preserves nonnegative weights and the intended winner totals. The supplied calculator checks this partition across 2,807 contexts and keeps the dependent method to narrow/long referee decision only.

The accepted spec does not give the official-bias magnitude. The calculator tests offsets of -6, -4, -1, 0, +1, +4, and +6, but these are test inputs, not accepted cap values. WT-OFFICIAL-BIAS-4 is therefore an explicitly hypothetical illustration: if +4 score points are added to Delta=0, p_clean=50%, p_biased=57.5965%; at an illustrative 10,000 integer scale the branches are 5,000 unaffected A, 760 official-dependent A, and 4,240 unaffected B. The dependent branch then splits 60/40 between narrow and long referee decisions. This is not a selected balance target or native result. Exact scheme probability, positive/negative rank changes, and AI choices remain unresolved until the source contract declares a supported adjustment and complete eligibility inputs. The information boundary is clear in design: an AI may know its own authorized wrongdoing, but not an opponent's undiscovered tactic or a future roll.

## Findings and recommended corrections

1. Event 107 rarity normalization, Common suppression, and Premium mixture pass the declared design-math checks. Preserve the five-tier pool and test the 0.60% Legendary ordinary-fresh weight against actual engine precision. Do not move these shares into event-option ai_chance.

2. Event 107 needs an implementation requirement for decision randomness. If the repeated purchase decision runs the rarity or recipe random_list, set fixed_random_seed = no or use a verified unique per-purchase seed. Preserve the sealed result at payment so the GUI cannot draw again. The relevant omission is in docs\specs\107_lootboxes_specs\05 - Decisions, AI and Integration.md, AI purchase policy and fixed-price integration; no gameplay patch was applied.

3. Before claiming an exact Event 107 curse probability or recipient reward distribution, declare the complete episode outcome pool, current-Chaos and cadence function, Premium incidence function, recipe identifiers, country eligibility, and provider failure gates. Parts 02 and 03 give bounded anchors but do not define those full pools. A named immediate-versus-delayed opening scenario should make the player timing option and AI completion parity explicit.

4. Event 108 bracket and date arithmetic pass the calculator's declared 2..512 range. Before implementation acceptance, measure the actual eligible roster and capacity; 512 is not an accepted cap. Repeatable Event 108 arrival cadence is not calculated because the shared event weight, cap reduction, and external recurrence state are outside this design-only probability pass.

5. Fix the overlapping winner-method boundaries in docs\specs\108_wrestling_tournament_specs\03 - Seeding, Matches and Championships.md, lines 224-226. Make the bins explicitly disjoint, for example advantage >=24, 12<=advantage<24, 0<=advantage<12, and advantage<0, with the winner's signed advantage defined consistently for A and B. This changes no win-probability target; it removes ambiguity at exactly 12 and 24.

6. Before modeling official fixing, define the accepted maximum signed official adjustment in docs\specs\108_wrestling_tournament_specs\04 - Evolutions and Cross-event Connections.md and align Part 03, Part 06, and the calculator. Do not promote the calculator's +/-6 test range into design without an explicit decision.

7. Keep native decision AI weights separate from normalized random pools. The Event 108 65/35 and training scores are score-only until a concrete native decision or event-option route and all competing candidates are identified. Retain the four complete investigation pools and the healthy camp/injury fixtures as conditional reference cases, not as implementation evidence.

## Classification, limits, and handoff

| Claim | Classification | Candidate-pool and external-factor status |
| --- | --- | --- |
| Event 107 top-level rarity anchors and normalized rows | Exact design math | Five rarity candidates complete; shell and pressure explicitly fixed per scenario. Recipe eligibility and engine precision are not complete. |
| Event 107 Premium shell mixture | Bounded/exact at declared s endpoints | Five rarity candidates complete; s is only bounded at 20%-35%; no Chaos-to-s formula exists. |
| Event 107 Common history and burden thresholds | Exact design arithmetic | Transition and opening charge fixed to illustrative anchors; no recovery in named examples. |
| Event 107 omen rate and outcome split | Bounded/unresolved | Only broad burden bands are provided; full pool, current Chaos, cadence, and scheduled episode transitions are incomplete. |
| Event 107 AI purchase frequency | Score-only/unresolved | Reserve thresholds calculable; native candidate set, competing decisions, exact obligations, and cadence execution are incomplete. |
| Event 108 draw counts and calendar | Exact design arithmetic | N, registration R, preparation, and intact-field assumptions declared; actual campaign roster and capacity unknown. |
| Event 108 individual fit-bout probability | Exact conditional formula | Two fit wrestlers and frozen Delta declared; no claim about complete tournament title share. |
| Event 108 camp, healthy-injury, and investigation pools | Exact conditional design ratios | Complete listed candidates in named baseline scenarios; state modifiers and native sampling unverified. |
| Event 108 AI policy weights | Score-only | The design itself disclaims native normalized-choice semantics; competing actions and runtime route are not defined. |
| Event 108 official-bias change | Bounded formula; actual magnitude unresolved | Three branches complete given p_clean and p_biased; the accepted adjustment magnitude and scheme eligibility are missing. |
| Event 108 champion ranking and title probabilities | Unresolved | Full entrant profiles, changed-state transitions, and all later candidate pools are absent. |

No gameplay, AI, event, focus, decision, mission, technology, doctrine, scripted-effect, trigger, GUI, localisation, country, history, asset, audio, spreadsheet, or runtime file was edited. No scenario simplification or balance target was chosen, and no commit was created. The only created file is this authorized handoff.

Skills read and applied: chaos-redux-subagents, chaos-redux-events, chaos-redux-event-planning, hoi4-ai-strategies, and chaos-redux-mtth. No MTTH entry or MTTH-backed weight was present in the formulas reviewed.
