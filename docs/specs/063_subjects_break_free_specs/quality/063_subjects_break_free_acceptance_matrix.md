# Event 063 acceptance matrix

## Use

This matrix defines the minimum implementation and playtest evidence needed before Event 063 can move from `To Be Reworked` to `Needs Testing`, then to a later completed status under the repository workflow.

Each row needs a verdict and evidence path. A passing count alone is insufficient when a critical row fails.

## A. Candidate pool and transaction

| ID | Test | Setup | Expected result |
| --- | --- | --- | --- |
| A01 | No candidates | No valid subject country exists | Event list shows `N/A`. Manual normal fire fails closed. No history row is written. |
| A02 | One candidate | One valid subject exists | Exactly one country is released. |
| A03 | Small pool | Four valid subjects exist | Two countries are released under ordinary baseline tuning. |
| A04 | Large pool | At least thirty valid subjects exist | Baseline release count remains within five to six. |
| A05 | Evolution I cap | Large pool and Evolution I active | Completed batch never exceeds eight. |
| A06 | Frozen pool | First selected release changes overlord strength and faction state | Remaining picks still follow the frozen snapshot. |
| A07 | Selection without replacement | Candidate pool contains several subjects | No country is selected twice. |
| A08 | Baseline diversity | Several overlords have valid subjects | Picks spread across overlords where practical. |
| A09 | Cohort selection | Evolution I and one overlord has several valid subjects | One same-overlord cohort of two to five is selected. |
| A10 | Reservation conflict | One candidate is reserved by Event 006 or Event 005 | Candidate is excluded or replaced before release. |
| A11 | Late invalidation | Candidate disappears after earlier releases complete | Earlier releases remain. Candidate is skipped. No pool rebuild occurs. |
| A12 | Cleanup | Any successful or failed firing | All temporary arrays, transaction flags, and reservations are cleared. |
| A13 | Repeat cooldown | A freed country is resubjugated quickly | Event 063 cannot immediately release it again. |
| A14 | Overlord cooldown | One overlord loses a batch | Short-term weight shifts toward other valid overlords unless severe pressure overrides it. |
| A15 | Force mode with no target | Force trigger enabled and no candidates | Runtime still fails safely without fabricated target. |

## B. Existing-country preservation

| ID | Test | Setup | Expected result |
| --- | --- | --- | --- |
| B01 | Territory | Release an ordinary subject | Owned and controlled states remain with the same tag. |
| B02 | Army | Subject has deployed units and templates | Units and templates remain. No replacement army is spawned. |
| B03 | Navy and air | Subject has fleets and wings | Fleets, wings, and equipment remain. |
| B04 | Stockpile and production | Subject has active lines and stored equipment | Lines and stockpiles remain. |
| B05 | Politics | Subject has custom leader, ideology, laws, and advisors | Political state remains intact. |
| B06 | Research | Subject has active research and completed technologies | Research state remains intact. |
| B07 | Focus tree | Subject has completed and active focuses | Focus state remains intact. |
| B08 | Country-specific mechanic | Subject has a balance of power or dynamic modifier | Owner system remains functional after release. |
| B09 | Cosmetic identity | Subject uses a cosmetic tag or route flag | Existing visible identity remains unless another owner system changes it. |
| B10 | Shared provenance | Event 006 country becomes subject, then Event 063 frees it | Event 006 first origin remains and Event 063 becomes latest origin. |

## C. Settlement and diplomacy

| ID | Test | Setup | Expected result |
| --- | --- | --- | --- |
| C01 | Independence cannot be vetoed | Human subject or overlord chooses the harshest option | Country remains independent until a valid war or later ordinary action changes it. |
| C02 | Negotiated separation | Friendly high-autonomy pair | Ordinary agreements can be retained or converted. No restoration goal appears. |
| C03 | Unilateral recognition | Negotiation fails over terms but overlord accepts independence | Subject remains independent and recognized. Dependent arrangements are reviewed. |
| C04 | Contested separation | Overlord refuses recognition without safe war | Contested condition, narrow pressure tools, and recognition mission appear. |
| C05 | Armed refusal | Safe strong former overlord chooses restoration | Independence war begins with restore-subject objective. |
| C06 | Common external war | Subject and overlord are co-belligerents on an unsafe shared side | Immediate direct war is blocked. Contested wartime separation appears. |
| C07 | Real-border incident | Contested pair shares a land border and is not mutually at war | Border-incident bridge can appear. |
| C08 | No-border dispute | Contested pair has no land border | Border incident does not appear. Diplomatic, naval, or ultimatum pressure is used instead. |
| C09 | Existing unrelated wars | Either side fights another country | Event does not treat unrelated war as a direct pair war. |
| C10 | Expeditionary control | Former overlord controls subject units | Units are returned or foreign control is cleared before hostility. |
| C11 | Faction retention | Peaceful separation inside a compatible faction | Released country can remain when the faction relationship remains valid. |
| C12 | Former-overlord faction war | Armed refusal inside former-overlord faction | Released state leaves or is expelled before war. |
| C13 | Third-party faction | Released state belongs to an unrelated faction | Event does not remove it solely to simplify settlement. |
| C14 | Narrow claims | Former overlord contests separation | New temporary claims or goals apply only to relevant former-subject territory. |
| C15 | Claim cleanup | Recognition or peace occurs | Event-created temporary claims and restoration goals are removed. |
| C16 | Overlord disappears | Former overlord ceases to exist during dispute | Recognition resolves and ownerless restoration pressure is removed. |
| C17 | Human timeout | One human side does not answer | Pragmatic default resolves after the deadline. No automatic restoration war is chosen for a silent human. |
| C18 | Save and reload | Save during pending human settlement | Choices and deadline persist. Release does not repeat. |

## D. Independence wars

| ID | Test | Setup | Expected result |
| --- | --- | --- | --- |
| D01 | Baseline single-war cap | Evolution II inactive and several selected pairs qualify for armed refusal | At most one new independence-war theater opens. Other hostile pairs remain contested. |
| D02 | Compound war | Evolution II active and cohort is refused | Cohort enters one coherent war under one breakaway leader. |
| D03 | Evolution II theater cap | One coordinated cohort and at least two individual armed refusals against other overlords qualify in one firing | No more than two new Event 063 theaters open across compound and individual wars. |
| D04 | Unsafe cohort member | One cohort member cannot safely join | That member remains contested outside the war. |
| D05 | Restoration objective | Former-overlord side wins | Subject relation is restored. Annexation does not occur by default. |
| D06 | Breakaway victory | Breakaway side wins | Independence is recognized and temporary restoration pressure is removed. |
| D07 | Preserving white peace | War ends without restoration | Breakaway remains independent and is treated as recognized. |
| D08 | Long stalemate | War remains static and costly | Mediation becomes available. |
| D09 | External support cap | Three liberated states have directly intervened | Further Event 063 direct-entry actions are unavailable. |
| D10 | Material support after cap | Direct-entry cap reached | Aid, recognition, volunteers under ordinary rules, and mediation can still occur. |
| D11 | No access | Potential supporter cannot reach theater | Direct entry receives zero practical weight. |
| D12 | War topology cleanup | Peace ends | War missions, mobilization condition, promises, and theater reservations clean up. |

## E. Shared liberation network

| ID | Test | Setup | Expected result |
| --- | --- | --- | --- |
| E01 | Event 063 registration | Ordinary successful release | First or latest origin record is written once. |
| E02 | Event 006 first origin | Event 006 country later freed by Event 063 | First origin remains Event 006. |
| E03 | Soviet successor origin | Soviet successor later freed by Event 063 | Soviet first origin remains. |
| E04 | Subject suspension | Active network state becomes a subject | Active status and Pact membership suspend. History remains. |
| E05 | Reactivation | Suspended state becomes validly independent | Network status revalidates without duplicate first origin. |
| E06 | Annexation | Active state ceases to exist | Active network state clears. Historical origin remains available for restoration checks. |
| E07 | Severe conflict | Two liberated states have a major core conflict | Cooperation and invitation are blocked or heavily reduced. |
| E08 | Recognition target cap | Many new liberated states exist | Country sees only a bounded relevant recognition set. |
| E09 | Real aid | Donor sends equipment | Equipment leaves donor and reaches recipient through a valid route. |
| E10 | Aid cooldown | Recipient requests repeated packages | Duplicate package is blocked or sharply reduced. |
| E11 | Support remaining subject | Network decision targets a valid subject | Candidate pressure or recognition readiness rises. Subject is not directly released. |
| E12 | Owner boundary | Event 063 acts on Event 006 country | Event 006 private ledger and package data are not overwritten. |

## F. Liberation Pact

| ID | Test | Setup | Expected result |
| --- | --- | --- | --- |
| F01 | Congress unavailable | Evolution III inactive | Founding congress does not appear. |
| F02 | Too few members | Evolution III active with insufficient network | Network remains informal. |
| F03 | Cross-origin threshold | Four compatible states from at least two origins | Congress can become available. |
| F04 | Same-origin threshold | Five compatible states from one origin | Congress can become available. |
| F05 | Failed congress | Too few full-member acceptances | Pact does not form. Network remains and founder receives cooldown. |
| F06 | Successful congress | Minimum full membership accepts | Pact, founder, roster, charter, and initial cohesion are created. Cohesion begins from 35 to 65 and never begins in the Fractured or United band. |
| F07 | Factioned candidate | Compatible liberated state is already in another faction | Partner or observer status is offered. No forced exit. |
| F08 | Cohesion display | Pact exists | Numeric Liberation Cohesion and correct band are visible. |
| F09 | Cohesion icon family | Cohesion crosses each band | Charter spirit changes to the matching state. |
| F10 | Fulfilled commitment | Member completes relevant aid or defense promise | Cohesion rises once. |
| F11 | Abandoned commitment | Reachable member refuses a valid obligation | Cohesion falls once. |
| F12 | Duplicate cohesion hook | One aid package triggers several event paths | Only one cohesion reward occurs. |
| F13 | Leader loss | Founder becomes subject or ceases to exist | Valid leadership transfer occurs. |
| F14 | Voluntary exit | Member exits outside a defensive obligation | Member leaves and cohesion changes. Provenance remains. |
| F15 | Aggressor member | Member attacks or subjects another liberated state | Censure or expulsion becomes available. |
| F16 | Dissolution | Fewer than two members remain through grace period | Formal Pact dissolves. Informal network remains. |
| F17 | Existing Event 006 institution | Event 006 congress faction exists | Event 063 does not merge, rename, or steal it. |
| F18 | Free Republics' League | Event 005 League exists | Compatible states can partner without replacing the League. |

## G. Decisions, missions, and AI

| ID | Test | Setup | Expected result |
| --- | --- | --- | --- |
| G01 | Decision cap | Country has many possible targets | No more than six decisions appear. |
| G02 | Normal visibility | Ordinary phase | Three to five relevant decisions normally appear. |
| G03 | Mission cap | Country qualifies for several mission families | No more than three missions are active. |
| G04 | Obsolete cleanup | Dispute resolves | Settlement actions and missions disappear. |
| G05 | Cost relevance | Use aid, access, command, and mediation decisions | Costs match the action and do not rely only on political power. |
| G06 | Donor shortage | AI donor lacks equipment | Material-aid weight drops or decision is unavailable. |
| G07 | Candidate ordering | Run CS-01 through CS-07 | Results match the expected rankings and limits. |
| G08 | Settlement ordering | Run ST-01 through ST-07 | Results match the expected rankings and topology gates. |
| G09 | Intervention ordering | Run IV-01 through IV-05 | Material support exceeds direct entry across ordinary supporters. |
| G10 | Pact invitation ordering | Run PI-01 through PI-05 | Full membership, partner, observer, and rejection outcomes follow validity. |
| G11 | Evolution timing | Run ET-01 through ET-07 | Timing falls inside intended bands and responds to pressure. |
| G12 | AI impossible route | Missing target, faction, border, access, or war path | Invalid action receives zero practical weight. |

## H. Chaos, clusters, and logs

| ID | Test | Setup | Expected result |
| --- | --- | --- | --- |
| H01 | Liberation Chaos | One subject actually becomes independent | Shared liberation source fires once. |
| H02 | No duplicate batch Chaos | Several subjects released | No separate Event 063 batch grant duplicates the country releases. |
| H03 | Evolution Chaos | Evolution activates without consequence | Direct Chaos change is zero. |
| H04 | War Chaos | Independence war begins | Shared war source handles the war. |
| H05 | Peace Chaos | War ends | Shared peace source handles the outcome. |
| H06 | Faction Chaos | Pact forms or member joins | Shared faction sources handle actual changes. |
| H07 | Re-subjugation Chaos | Former overlord restores subject status | Shared puppeting source handles the transition. |
| H08 | Liberations cluster | Cluster 2 fires with valid Event 063 member | Event 063 participates under shared reservations and keeps its own history. |
| H09 | Cluster skip | Cluster 2 fires with no valid subjects | Event 063 records an ineligible reason and does not show an empty report. |
| H10 | Domestic Unrest ID | Current registry lacks a stable ID | Implementation does not guess one. Secondary integration remains pending or is added only after proper registration. |
| H11 | Event history | Ordinary firing completes | One Event 063 row records actor, count, former-overlord count, outcome, and evolution context. |
| H12 | Cluster history | Cluster firing includes Event 063 | Cluster and event rows remain distinct and aligned. |
| H13 | Reload history | Reload after firing | History and origin records do not duplicate. |

## I. Presentation, assets, and achievements

| ID | Test | Setup | Expected result |
| --- | --- | --- | --- |
| I01 | Global report | Several AI countries are released | One global report appears. |
| I02 | Human subject notice | Human subject is released | One direct settlement event appears. |
| I03 | Human overlord batch | Human overlord loses several subjects | One batch event appears, not one popup per subject. |
| I04 | First cohort news | First Evolution I cohort occurs | One news event appears and never repeats for ordinary later cohorts. |
| I05 | First war news | First compound independence war occurs | One news event appears and never repeats for ordinary later wars. |
| I06 | First Pact news | Pact forms | One news event appears. |
| I07 | Report image | Main report appears | Correct 210x176 processed card asset is used. |
| I08 | News images | Threshold news appears | Correct 397x153 black-and-white asset is used. |
| I09 | Category picture | Decision category opens | Correct consumer-sized static picture appears without fake controls. |
| I10 | Asset coverage | Review accepted asset matrix | Every row has source, final path, registration, consumer, and current audit evidence. |
| I11 | Achievement 1 | Meet survival, recognition, and support conditions | Independence Secured unlocks once. |
| I12 | Achievement 2 | Meet Pact membership, origin, cohesion, and time conditions | Pact Founder unlocks once. |
| I13 | Achievement 3 | Win valid disadvantaged compound war with external support | Independence War Victory unlocks once. |
| I14 | Achievement 4 | Recognize four releases and preserve relations for two years | Peaceful Release unlocks once. |
| I15 | Achievement disqualifiers | Force-run or invalid path | Achievement does not unlock. |

## Critical failures

Any of these blocks completion:

- country recreation or loss of preserved state
- double release or owner-transaction collision
- player ability to cancel the independence premise
- unsafe direct war across protected common-war topology
- broad free claims or default annexation objective
- Event 063 writing Event 006 or Event 005 private ownership data
- forced removal from unrelated factions for Pact membership
- more than one public persistent Event 063 value
- duplicate Chaos for a shared source
- unbounded equipment or cohesion farming
- missing AI probability audit
- missing asset requirement row
- missing workbook and CSV alignment
- completion claim with unresolved critical rows
