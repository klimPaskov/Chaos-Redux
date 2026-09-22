# Game validation matrix

## Status

Every test below is NOT RUN. These are execution instructions for a future implemented build. A planning-file check does not change their status. Record actual build commit, game version, DLC set, scenario setup, action, observed result, logs or capture evidence, and disposition for each executed test.

## Entry and grant tests

| Test | Setup and action | Expected result |
|---|---|---|
| T01 | Independent valid MON accepts baseline | One actor, one accounted army, dedicated tree and early campaign access |
| T02 | Human MON refuses | No army, no forced civil war, no hidden restoration |
| T03 | Subject MON accepts and overlord recognizes | Valid sovereignty transition without duplicate faction or army |
| T04 | Subject MON accepts and overlord refuses | Actual legal next step, no impossible foreign war shortcut |
| T05 | MON has reduced safe territory | Entitlement retained, deployment staged, no enemy-province spawn |
| T06 | MON has no valid reception territory | Entry waits or is ineligible with the correct existing engine behavior |
| T07 | Equivalent Mongol Empire already exists | Event unavailable, no second restoration |
| T08 | Repeat root or notification delivery | No duplicate grant or Chaos |
| T09 | Reload immediately before and after acceptance | Exactly one committed result |
| T10 | Inspect formed army and spare stockpile | Full formation costs separate from spare equipment |
| T11 | Lose a reception site while entitlement waits | No debit or spawn at the invalid site, entitlement remains |
| T12 | Destroy opening divisions then unlock next tier | Only cumulative tier difference is awarded |

## Military tests

| Test | Setup and action | Expected result |
|---|---|---|
| T13 | Inspect every normal recruitment and reward template | Cavalry line formations, valid support, no tank or infantry grant |
| T14 | Inspect bonuses on cavalry and unrelated armor | Intended category scope, no accidental strong armored army |
| T15 | Compare attack and static defense at all tiers | Offensive gain with persistent defensive weakness |
| T16 | Stack political, commander and late focus benefits | Three-spirit limit and reviewed combined modifier budget |
| T17 | Attack a defended urban position | Urban limitation remains visible and real |
| T18 | Attack fortified terrain | Fort limitation is not silently cancelled |
| T19 | Sever a critical supply link | Relevant benefits suspend and the army can be stopped |
| T20 | Test cold, desert, hills and true mountains | Supported actual effects, no nonexistent terrain key or universal immunity |
| T21 | Convert inherited noncavalry formations safely | No unit deletion in combat or duplicated equipment |
| T22 | Add foreign expeditionary forces | Ownership preserved and no false cavalry achievement proof |
| T23 | Trigger research loss or template lock | Respect current restrictions, no silent restoration of unrelated technology |
| T24 | Let an offensive stall, then consolidate | Momentum falls for actual stall and recovery uses actual resources |

## Focus and political tests

| Test | Setup and action | Expected result |
|---|---|---|
| T25 | Ordinary independent opening through two anchors | A valid expansion demand available within intended early pacing |
| T26 | Commit each political route separately | Clear exclusive settlement and distinct mechanics |
| T27 | Try to switch route and collect another opening reward | No duplicate political or military grants |
| T28 | Complete every capstone | Continuing meaningful regional or institutional play |
| T29 | Acquire an objective before its focus | Correct bypass without duplicate payoff |
| T30 | Target changes owner during preparation | Current owner preview and valid recheck |
| T31 | Lose a required corridor | Route pauses with a meaningful recovery path |
| T32 | Render full tree at normal scale | Readable branches, connectors, filters and inlay |
| T33 | Test long localisation and tooltips | No clipping or covered focus controls |
| T34 | Reach a vacancy with prepared succession | Real prepared options and preserved country continuity |
| T35 | Reach a vacancy with rival khan support | Visible bargaining and possible contest, no immediate arbitrary collapse |
| T36 | Resolve succession | Office updates, no opening army replay |

## Regional and country tests

| Test | Setup and action | Expected result |
|---|---|---|
| T37 | Complete each reviewed regional manifest | Puzzle, decision, AI and settlement agree |
| T38 | Hold territory militarily without ownership rights | No unauthorized permanent transfer |
| T39 | Create each of four khanate settlements | Valid capital, territory, economy, army, government and regional continuation |
| T40 | Existing matching tag is already alive | Reuse or negotiate correctly, no duplicate country |
| T41 | Human player controls regional target | Player receives real response and no silent tree overwrite |
| T42 | Soviet collapse or Independence Wave changed map | Current owners and institutions preserved |
| T43 | Persia restoration already exists | No duplicate Persia and no incompatible forced replacement |
| T44 | White Peace ends current campaign war | Revalidate objectives, no immediate forced replay |
| T45 | Direct rule changes into autonomy | Only lawful territory assigned, conquest reward remains spent |
| T46 | Repeatedly release and reconquer a region | No repeated recruits, stores, achievements or Chaos milestone |
| T47 | Northern limited campaign succeeds | Useful settlement without total annexation of opposing major |
| T48 | Attempt unreachable southern or western campaign | Correct block and explanation, no teleport or free naval route |

## Tribute, routes and capital tests

| Test | Setup and action | Expected result |
|---|---|---|
| T49 | Equipment tribute delivers normally | Donor debit equals receiver credit exactly once |
| T50 | Donor lacks promised stock | Feasible shortfall and arrears, no negative or invented stockpile |
| T51 | Recipient disappears before payment | No orphan payment or credit to an unrelated actor |
| T52 | Repeated payment callback or reload | No duplicate transfer |
| T53 | Review tribute during a war | Terms and feasible deferral reflect actual condition |
| T54 | Attack a compliant payer in breach of terms | Actual diplomatic and Authority consequences |
| T55 | Send manpower or a contingent | Verified donor cost and recipient gain, no double-counted force |
| T56 | Inspect resource agreement | Supported trade or relationship mechanism, no invented resource currency |
| T57 | Cut one continental route section | Dependent benefits stop, unrelated local benefits remain |
| T58 | Restore a genuine route | Correct connection and no farm through deliberate friendly break |
| T59 | Complete each Karakorum stage at limits | Valid facilities or stated already-satisfied result |
| T60 | Relocate capital to Karakorum | Actual validated site, correct state/province handling and government continuity |

## Evolution, collapse and Chaos tests

| Test | Setup and action | Expected result |
|---|---|---|
| T61 | Enter directly at each of four tiers | One correct cumulative grant and content set |
| T62 | Upgrade through all tiers after losses | Fixed occurrence scale and correct entitlement differences |
| T63 | Change Evolution settings and reload | Existing grants do not become claimable again |
| T64 | Cross a threshold without a concrete consequence | No direct Chaos from eligibility or unlock |
| T65 | Complete first gain, industry, khanate and region bands | Reviewed distinct event milestones and generic-source separation |
| T66 | One settlement qualifies for two overlapping bands | Coalescing rule prevents duplicate consequence charge |
| T67 | Complete universal proclamation | Required distinct regions and institutions, one presentation and Chaos result |
| T68 | Fail a small opening restoration | Ordinary defeat presentation, no false continental-collapse super-event |
| T69 | Fragment a substantial empire | Meaningful successors, correct obligations and no map reset |
| T70 | Center disappears while khanates survive | Center callbacks stop and successors continue |
| T71 | Stabilize a smaller empire or compact | No entry grant replay, durable recovery qualification |
| T72 | Contain the empire after a real campaign | Sustained containment source, not a second generic peace award |

## Interface, AI, assets and multiplayer tests

| Test | Setup and action | Expected result |
|---|---|---|
| T73 | Inspect every phase's action count | Normally three to five, never above six primary actions |
| T74 | Inspect active missions in every phase | No more than three, automatic objective completion |
| T75 | Affordability exactly equals cost | Visible, available, click, debit and AI agree |
| T76 | Target invalidates between click and commit | No cost consumed and clear feedback |
| T77 | Render all required GUI fixtures and supported scales | Native controls, readable text and no clipping |
| T78 | Run AI scenarios in the AI matrix | Legal targets, sensible ranking and measured probabilities where available |
| T79 | Run all final asset consumers | Correct images, flags, counters, portraits, model and audio |
| T80 | Inspect model export, animation, effects and sound | Proper scale, contact, firing, reimport and actual runtime states |
| T81 | Play each final super-event | Source-cleared text and audio, correct image and one-time trigger |
| T82 | Test every achievement positively and negatively | Exact intended condition, no force-test or one-day template-swap exploit |
| T83 | Two human players interact as center and target | Each controls its own response and payment is accounted once |
| T84 | Human overlord, center and khanate across succession | No involuntary hidden response, valid relationship transitions |
| T85 | Shared and independent event contexts | One physical restoration per committed occurrence, correct logs |
| T86 | Save/reload during transfer, succession and fragmentation | Stable records and no repeated grant, release or Chaos |
| T87 | Profile active and inactive event processing | Bounded active collections, no unnecessary global daily scan |
| T88 | Complete user review on final runtime hashes | Actual live-game acceptance recorded, not inferred from static checks |

## Evidence closure

A failure remains attached to its owning stage and requirement until repaired and retested. A role's confidence or a successful file parse cannot close a failed runtime case. Release requires the applicable matrix, independent reviews, and user acceptance, with any approved exceptions documented explicitly.
