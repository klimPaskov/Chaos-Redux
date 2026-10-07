# Event 098 New Ore: Improvement-loop closure

Review date: 7 October 2026. Reviewer: `chaosx_improvement_loop_planner`. Scope: the assembled source-spec planning package, before gameplay implementation.

## Closure decision

**Close the planning expansion loop.** Event 098 is now deep, connected, replayable, and sufficiently bounded to stop adding design scope. No expansion addendum is required. No unresolved core design choice was found in the final reviewed revision.

The smallest necessary planning corrections have been integrated by the parent and checked in the current source parts and handoffs. Remaining questions concern native feasibility, exact implementation, production, or evidence. They are recorded as proof gates and do not justify another round of speculative mechanics.

This is a design closure. It does not certify native armor behavior, control callbacks, equipment transfers, war-goal cleanup, AI execution, final art or audio, save compatibility, or implemented gameplay. The implementation-stage improvement-loop pass remains mandatory when the built event reaches near completion.

## Complete review coverage

The reviewer completely read all nine numbered source parts, both architecture and requirements review plans, and every currently assembled specialist, coding, goal, research, map, and package-use document. Final changed parts 3, 5, 8, and 9 and the changed coding and decisions prompts were completely reread after the peaceful-transfer correction. The final source-reading ledger was read as metadata in four contiguous ranges covering characters `[0, 69085)`.

The table records the reviewed current source-package revision. Counts are Unicode characters, including newlines. They identify the reviewed artifacts and are not substitutes for the complete reads.

| File in `docs/specs/098_new_ore_specs/` | Reviewed characters | Coverage |
| --- | ---: | --- |
| `098_new_ore_spec_part_1_core.md` | 13,254 | Complete |
| `098_new_ore_spec_part_2_evolutions.md` | 13,294 | Complete |
| `098_new_ore_spec_part_3_foreign_access.md` | 22,001 | Complete |
| `098_new_ore_spec_part_4_ore_wars_and_ai.md` | 15,774 | Complete |
| `098_new_ore_spec_part_5_connections_and_chaos.md` | 16,367 | Complete |
| `098_new_ore_spec_part_6_presentation_and_assets.md` | 17,292 | Complete |
| `098_new_ore_spec_part_7_achievements.md` | 15,236 | Complete |
| `098_new_ore_spec_part_8_campaign_lifecycle.md` | 14,790 | Complete |
| `098_new_ore_spec_part_9_balance_and_acceptance.md` | 23,686 | Complete |
| `098_new_ore_asset_prompt.md` | 9,155 | Complete |
| `098_new_ore_achievement_prompt.md` | 17,338 | Complete |
| `098_new_ore_decision_mission_prompt.md` | 10,646 | Complete |
| `098_new_ore_super_event_prompt.md` | 5,980 | Complete |
| `098_new_ore_coding_prompt.md` | 14,677 | Complete |
| `098_new_ore_goal_prompt.md` | 3,979 | Complete, below the 4,000-character ceiling |
| `098_new_ore_implementation_map.md` | 22,349 | Complete |
| `098_new_ore_research_notes.md` | 14,562 | Complete |
| `098_new_ore_readme.md` | 5,198 | Complete |
| `098_new_ore_source_reading_ledger.json` | 69,085 | Complete metadata review |

Additional complete review inputs in `docs/plans/098_new_ore_plans/` are `098_new_ore_architecture_review.md`, 29,561 characters in the revision read, and `098_new_ore_requirements_review.md`, 37,535 characters in the revision read. These plan counts identify the reviewed revisions rather than later live files. The architecture report subsequently received a source-trace correction that avoids implying a proven state-local scope bug.

The supplied-source gate had already passed before this design review. The reviewer personally fully read canonical contents SRC-001, SRC-007, SRC-013, SRC-030, SRC-032, and SRC-034, along with the current role definition, source protocol, and AGENTS prerequisites. SRC-030 was also fully reread by the parent and is credited to that parent read in the global ledger. Five other assigned contents are credited to this reviewer. The collective gate covers 88 distinct contents and 131 physical text instances. The parent verified identical copies by complete byte equality. This reviewer does not claim to have personally displayed every physical duplicate or every source assigned to another reader.

Earlier truncated attempts in this review were recovered through complete bounded reads. No required range in the reviewed final input set remains unaccessed. The eventual parent review record and package manifest are generated from final reports, so they were not prerequisites for issuing this closure.

## Why the event is ready to stop expanding

### The physical rule already produces a campaign

The opening state is selected uniformly from the complete valid world pool. That single draw changes which country can bargain, which frontier becomes worth defending, which army gains an advantage, and which rivals have a reason to act. The source remains physically attached to its state. Current control, rather than title or faction membership, decides direct access. That makes conquest, occupation, liberation, and peace settlement strategically consequential without adding another simulated commodity economy.

The armor promise is substantive and preserves the user's premise. The baseline is at least a 50% effective increase for all applicable existing and new positive-armor consumers. It is measured against the otherwise identical consumer with other bonuses unchanged. Deep Vein, foreign access, and the extreme Super-Alloy have equally explicit effective targets. Source loss and recipient equipment ownership have defined consequences. A parser-valid raw coefficient cannot substitute for the required result.

These rules provide several viable positions. A fortunate minor can reserve the material, buy protection through access, obtain real equipment, or develop its forces through ordinary systems. A major can exploit direct armor while protecting an exposed dependency. A customer can purchase a weaker advantage or maintain one backup. A denied rival can improve its offer, pursue another supplier, use normal piercing and operations, or attempt to seize the actual place. An occupation can immediately invert the strategic balance.

### The four evolutions change distinct decisions

Deep Vein changes material grade and diplomatic capacity. New Deposits changes geography, supplier competition, resilience, and concentration. Ore Wars changes access pressure and the value of credible military preparation. Super-Alloy changes the military stakes and adds deliberately diminishing value to extra controlled sources.

The tracks are independent at 200, 400, 600, and 800 Chaos. Disabled predecessors do not prevent a later enabled track. High-Chaos first firing still starts with exactly one baseline deposit. Highest manifested grade prevents out-of-order activation from downgrading the alloy. Persistent progress and pause/resume rules prevent capture or save reload from becoming a timer-reset strategy. These are enough mutation paths for this premise.

The scarcity rule and global linear cadence preserve a scarce territorial prize over a long campaign. Random later discoveries can weaken a monopoly, create a rival supplier, rescue a customer from dependence, or reinforce one empire by chance. Uniform selection permits those outcomes without forcing a scripted continental spread or a named enemy.

### Agreements create choices without becoming a separate diplomacy game

Commercial, security, and faction allocation have different purposes and meaningful commitments. The supplier keeps its superior direct tier. The customer receives one weaker tier. Export places, the six-customer limit, the two-source recipient limit, and one counteroffer keep the interaction bounded.

The detailed paid-term rules are justified by concrete risks. Exact stock payments, inclusive affordability, failed-activation rollback, protected supplier-caused qualification loss, one future renewal period, unused-payment buyback, and consensual reassignment make a bargain understandable and prevent equipment creation or arbitrary loss of purchased days. These are states of the same finite agreement, rather than extra resource meters or management games.

The peaceful-transfer correction also has a narrow purpose. An event-controlled voluntary sale settles unused actual payments before transfer. An already-effective external non-hostile transfer still changes the controller immediately and ends the source contract. Its unpaid delivery failure produces a bounded 720-day supplier-wide block on new AI prepaid commercial/security periods. Real hostile capture and imposed wartime peace retain their disclosed risks. No new public reputation meter is needed.

### Ordinary diplomacy and warfare remain meaningful

Ore interest and military feasibility are separate. A source can be extremely desirable while unreachable or protected by an overwhelming coalition. Demands require a qualifying failed prior negotiation, payable terms, and credible pressure. Uncompleted acceptance does not become a manufactured refusal. Preparation uses normal political restrictions, never declares war automatically, and requires exact cleanup of owned goals.

The optional source-defense objective requires a real threat, a meaningful supplied force, continuous control, and elapsed time. It can succeed, fail, or close neutrally. The deposit remains valuable without taking that objective. This gives players a concrete defensive commitment without forcing an unrelated mission ladder.

The 15 named AI situations and 50 acceptance cases provide sufficient implementation targets for these choices. Adding another generic AI score or another incident lottery would not strengthen the campaign identity.

### Connections and achievements reward existing play

The four requested connections have genuine conditional facts and separate ownership. Riches Found requires actual same-state coexistence. Greenland Sale requires an actual ore-bearing marketed lot and uses its real price and transfer owner. World Claims changes interest and eligible cost without granting possession. Asteroid minerals remain distinct and must preserve the ore's effective multiplier against the separate asteroid result.

The eight achievements test prolonged monopoly, wartime recovery, independent supply, a competitive territorial purchase, two-material control, breaking an enemy monopoly, geographically dispersed Super-Alloy, and an honored security settlement. Their force thresholds, dates, exact actors, interruptions, and disqualifiers resist obvious shortcut play. They do not require additional mechanics merely to create achievement variety.

Presentation is also bounded. One ordinary category exposes two aggregate values and uses native state context plus concrete records. The one Super-Alloy reveal is tied to a direct controller actually receiving at least +200% with applicable armor in service or stock. It shares its concrete Chaos receipt. The asset and research handoffs cover that presentation without inventing final localisation or pretending that missing native references were inspected.

## Final corrections and disposition

| Concrete issue reviewed | Current disposition |
| --- | --- |
| Deep Vein resolving after Super-Alloy could imply a downgrade or false grade-increase reward | Highest-grade precedence is explicit in part 2 and coding. Deep still raises export capacity, with no downgrade, repricing, or false +3 receipt |
| Additional-deposit interval could be interpreted as linear or compounded | Part 2 gives the exact linear formula and bounds. Part 9 excludes accidental reuse of first-discovery modifiers |
| Operational Super-Alloy milestone could ambiguously count a foreign-only user | Parts 5 and 6 and the super/coding handoffs require a direct +200% or stronger controller with applicable armor |
| A future paid renewal could lose protection or discard existing paid days | Parts 3 and 8 and the decisions/coding handoffs preserve the original expiry, one future period, actual separate payments, and protected current/future terms |
| Price capacity could be reduced by temporarily changing production queues | Part 9 and implementation handoffs use controlled military factories plus dockyards, independent of assignments |
| Navy XP eligibility lacked a minimum useful naval path | Part 3 explicitly permits a deployed positive-armor ship or a verified positive-armor production/refit project. The five-ship threshold scales effort rather than gating the path |
| Controller-free sources could suspend and later revive stale paid access | Parts 1 and 8 and coding preserve the geological identity but terminate its source agreements |
| Friendly source cycling could collect repeated prepayments without delivering the remaining term | Parts 3, 5, 8, A26 and coding/decision handoffs now require voluntary settlement or the bounded absolute AI prepaid-period block |
| Implementation maps lacked several required execution fields | The revised map provides phase, inputs, allowed outputs, forbidden overlaps, dependencies, parent review, MCP baselines, blockers, and follow-up owners under Source Protocol sections 12 and 13 |
| Goal command exceeded the hard character ceiling | Final complete prompt is 3,979 characters |

Every issue above has been resolved in the reviewed planning revision. No additional design correction is required by this pass.

The final documentary precision update aligns the demand description with the qualifying failed-negotiation gate and labels plan character counts as the revisions actually read. These are source-trace corrections only and do not reopen design expansion or certify a native scope bug.

## Anti-bloat boundaries to preserve

Do not reopen the design merely to add an extraction meter, refinery progression, ore stockpile, separate trade currency, worldwide mineral auction, cartel minigame, mandatory production chain, hybrid asteroid material, or additional player reputation meter. None is needed to explain the present territory and access decisions.

The event empowers dynamically selected countries through one material entitlement. It does not create or transform national political identities. Dedicated country packages, focus trees, formables, leaders, new unit families, or an elaborate custom window are therefore unnecessary for this accepted scope. Broad existing equipment coverage remains a requirement and should be solved directly through supported armor delivery.

Keep the four independent evolutions, three agreement families, two aggregate public values, one meaningful defense objective, one global Super-Alloy reveal, and eight difficult achievements. Contextual actions can vary by situation while respecting the three-to-five primary action target and six-action readability budget. All valid sources remain reachable.

Scarcity, export selection, territorial vulnerability, normal military counterplay, and diminishing additional deposits are the balancing tools. Tuning must not quietly lower the baseline guarantee, restrict it to future tanks, introduce source bombing decay below the floor, or cap the independent Asteroid contribution.

Reopen planning only for a concrete contradiction or a supported implementation result that exposes an actual design gap. A new idea's thematic plausibility alone is insufficient. Any proposed change must identify the missing player decision or failed accepted outcome it repairs and show that an existing action or rule cannot already handle it.

## Proof gates remain open for implementation

The following are future implementation requirements, already assigned in the map. They were not performed by this review.

| Gate | Required evidence before the affected implementation claim can close |
| --- | --- |
| G01, effective armor | Complete positive-armor consumer inventory, supported modifier semantics and paired actual stats, including intrinsic custom contributions, naval armor, old/new stock, imports, commanding/owning scopes, other modifiers, and separate 028 composition |
| G02, immediate control | Supported control and transformation callbacks, idempotent reconciliation, and proof that loss/grant occurs before the next applicable combat evaluation |
| G03, payments | Exact equipment tokens and stock transfer, helper documentation/code discrepancy resolved, below/equal/above affordability, rounding/discount agreement, actual debit/credit and bounded receipt refunds |
| G04, diplomacy and AI | Native legal preparation, precise event-owned goal cleanup, meaningful state-target consumers, real mission timer behavior, all named AI comparisons, and peaceful-transfer provenance/reliability behavior |
| G05, Asteroid owner API | Owner-side resolution of the missing newer indexed mineral API without silently adopting the legacy fixed-fragment limit |
| G06, Greenland Sale | Actual lot, comparative value provider in native sale units, competing bids, paid settlement, unused-term settlement where required, and real control transfer |
| G07, references and assets | Installed canonical shelf and exact native consumers inspected, missing category/state sizes resolved, complete original source and converted assets, manifest, sprites, required states, and native review |
| G08, Super-Alloy text/audio | Verified exact wording and attribution, separate composition and recording rights, distinct real recording, unique framework slot, image getter, settings-aware playback, and full native presentation |
| G09, saved campaigns | Actual save and native evidence for migration, controller changes, all meaningful pending states, receipts, toggle combinations, retained timing progress, and achievement continuity |

Unavailable native documentation or tools must remain an explicit block on the affected claim. Structural MCP or parser output does not prove behavior it does not observe. The handoffs correctly continue independent authorized work while preserving the accepted guarantee.

## Parent closure handoff

Record this review as **planning depth and anti-bloat closure, no expansion addendum**. Promote the accepted dispositions into the final parent review record and include the required research, maps, prompts, reading ledger, and manifest in the final planning package. Use the single `098_new_ore_specs/` archive root and keep temporary continuation prompts out of the delivered source pack.

`098_new_ore_coding_prompt.md` is the consolidated implementation entrypoint. The complete goal command is within its ceiling. The README supplies installation and reading order. Additional alternate master-prompt files would duplicate the present handoff and are unnecessary.

The parent should finish the package's ordinary file and archive checks, preserve the catalog's To Be Reworked status, and deliver the source design with its honest implementation limits. No further gameplay expansion is recommended before implementation. This closes the planning pass only.
