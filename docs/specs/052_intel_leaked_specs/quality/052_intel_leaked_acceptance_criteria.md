# Event 052 Implementation Acceptance Criteria

Event 52 should not be treated as complete until every applicable criterion below is supported by the final repository state and task-specific evidence.

## Identity and registration

- [ ] Event ID remains `52`.
- [ ] Namespace remains `chaosx.nr52`.
- [ ] Event type is Minor Repeatable.
- [ ] Event Chaos level is 1.
- [ ] Event 52 is a Low-severity member of Intelligence cluster 10.
- [ ] The event appears in event-name and debug-name selectors.
- [ ] Normal selection, manual normal firing, and force-trigger behavior use the correct entry path.
- [ ] The finished rework is added to the default-enabled allowlist only with complete integration.
- [ ] Event Details shows the correct premise, level, type, cluster, and evolution previews.
- [ ] Event Log actor mapping is correct for baseline and Total Compromise.

## Target selection

- [ ] Baseline initializes exactly one target.
- [ ] The source player route uses the current valid player-controlled country.
- [ ] The major route selects one valid major.
- [ ] Invalid route fallback uses the other route without creating two targets.
- [ ] Event 52 is unavailable when neither route has a valid target.
- [ ] Special Chaos actors and actual nonhumans are excluded from ordinary target treatment.
- [ ] A country with an active unresolved Event 52 target state cannot receive a second normal sequence.
- [ ] A country can be selected again in a later repeat firing.
- [ ] Target invalidation before and after opening fails closed and cleans partial state.

## Incident state

- [ ] Every firing creates a new sequence identity.
- [ ] Target, domains, Exposure, duration, exploiters, Reliance, risks, decisions, missions, deception, investigation, and cleanup are sequence-owned.
- [ ] Old incident state never leaks into a later firing.
- [ ] Real lasting consequences persist normally.
- [ ] Save and reload preserves one exact incident state without duplicate initialization.
- [ ] Ordinary sequences cannot overlap.
- [ ] Total Compromise owns several targets inside one sequence.

## Exposure

- [ ] Exposure is the only persistent public Event 52 custom value.
- [ ] Exposure uses a 0 to 100 range.
- [ ] Critical, Severe, Significant, Fading, and Neutralized stages match the specification.
- [ ] Initial values follow baseline, Deep Files, and severe Total Compromise ranges.
- [ ] Natural aging lowers Exposure.
- [ ] Relevant damage-control action lowers Exposure meaningfully.
- [ ] Action effects depend on active domains.
- [ ] Exposure cannot be reduced repeatedly by farming a completed one-shot action.
- [ ] The public tooltip explains meaning, current causes, next threshold, and available response.
- [ ] Hidden depth, confidence, risk, and Reliance values do not appear as extra public meters.

## Archive domains

- [ ] Baseline selects three to five domains with four as the normal center.
- [ ] Every baseline profile has at least one military or mobilization domain.
- [ ] Every baseline profile has at least one nonmilitary domain.
- [ ] Target capability gates remove unsupported domains or outcomes safely.
- [ ] Deep Files increases domain depth and sensitive-domain frequency.
- [ ] Severe Total Compromise supports seven to ten domains where valid.
- [ ] Research files do not grant free technology.
- [ ] Diplomatic files do not reveal hidden future routes.

## Broad foreign intelligence

- [ ] Every ordinary foreign government receives meaningful temporary intelligence against the target.
- [ ] Strength follows current Exposure.
- [ ] Active domains shape relevant intelligence.
- [ ] Applied intelligence is reversible and event-owned.
- [ ] No untracked permanent maximum intelligence remains.
- [ ] New recipients added by relationship changes receive only the current stage.
- [ ] Invalid recipients are removed safely.
- [ ] Exposure at zero leaves no Event 52 intelligence residue.

## Named exploiters

- [ ] Named exploiters are bounded by profile and sequence caps.
- [ ] Selection uses war, hostility, geography, claims, capability, agency strength, domains, and plans.
- [ ] A strategically relevant minor can outrank an irrelevant major.
- [ ] Friendly allies normally prefer warning, quarantine, or cooperation.
- [ ] Relationship changes update future behavior.
- [ ] Every exploitation family has capability and domain validity.
- [ ] Baseline incident produces a small number of meaningful concrete outcomes.
- [ ] Cooldowns prevent repeated report spam.
- [ ] One target does not consume the entire named-exploiter capacity in a multi-target sequence.

## Operatives and networks

- [ ] Agency-enabled path evaluates relevant operatives, networks, and operations through bounded checks.
- [ ] Base-game path remains complete.
- [ ] Risk uses Exposure, depth, target defenses, mission sensitivity, and foreign capability.
- [ ] Outcome ladder includes suspicion, network loss, delay, cancellation, burned cover, and rare capture.
- [ ] Capture requires several danger factors.
- [ ] Personnel at Risk failure produces one bounded severe result.
- [ ] A new severe roll requires a new proven tranche or other mapped cause.
- [ ] Recall and channel shutdown protect people through real operational sacrifice.

## Decision category

- [ ] The category uses an ordinary decision presentation with static category picture.
- [ ] The header shows Exposure, stage, domains, and one urgent status.
- [ ] Three to five primary actions appear in normal phases.
- [ ] Six is never exceeded.
- [ ] One to three active missions appear.
- [ ] Completed or irrelevant actions hide.
- [ ] Dynamic costs use correct texticons.
- [ ] No action exceeds four spendable cost types.
- [ ] Requirements are separate from costs.
- [ ] Long triggers use concise custom tooltips.
- [ ] AI has equivalent valid actions.
- [ ] The category never reads like a debug ledger.

## Required actions

- [ ] Replace Codes and Authentication Tables is domain-sensitive and causes temporary command friction.
- [ ] Recall Exposed Personnel identifies and sacrifices relevant access.
- [ ] Rewrite Compromised Plans uses the relevant military domain and experience.
- [ ] Shut Down Vulnerable Channels closes real networks, operations, or generic access.
- [ ] Rebuild Cover Identities restores protected capacity over time.
- [ ] Reconstitute Foreign Networks appears only when supported.
- [ ] Compartmentalize the Archive gives capped future resilience and a small current effect.
- [ ] Restore Trusted Liaison Channels requires a valid cooperative partner.
- [ ] Seed Contradictory Orders can succeed or strengthen foreign confidence on failure.
- [ ] Poison the Leak requires a valid high-Reliance recipient.
- [ ] Stage a False Deployment commits real forces or resources.
- [ ] Trace the Source returns one practical route class and never a final universal culprit.

## Missions

- [ ] Archive Freshness uses dynamic duration and closes residual exposure correctly.
- [ ] Personnel at Risk has success, partial sacrifice, and failure behavior.
- [ ] Emergency Replan names or highlights the relevant military objective.
- [ ] Deception Window tracks the selected false posture and relevant recipients.
- [ ] Mission cancellation cannot award success.
- [ ] Mission target invalidation has explicit cleanup.
- [ ] Save and reload cannot duplicate mission outcome.
- [ ] Timers fit the specified difficulty bands.

## Deception

- [ ] Recipient Reliance is stored per target-recipient pair.
- [ ] Poison the Leak affects only relevant reliant recipients.
- [ ] Land, naval, air, mobilization, diplomatic, industrial, and contact-chain profiles follow the specification.
- [ ] Strong deception needs coherent signals and real preparation.
- [ ] Success, partial success, and failure all exist.
- [ ] Outcomes trigger when a recipient acts in the matching domain.
- [ ] Full success creates a bounded operational mistake and a major credibility loss.
- [ ] Failure can raise Exposure, disrupt the target, or close the route.
- [ ] Blanket world penalties are absent.
- [ ] Feedback comes from observed behavior, allied reports, intercepts, or failed foreign operations.

## Investigation and variants

- [ ] Trace the Source supports all seven route classes.
- [ ] Route results improve one relevant recovery or future-resilience family.
- [ ] No route names a permanent culprit.
- [ ] Blank Archive changes recovery and uncertainty.
- [ ] Ally's Copy creates cooperative information.
- [ ] Enemy Curator creates one strong exploiter and a strong deception target.
- [ ] False Originals changes confidence and contradiction play.
- [ ] Mirror Leak reveals bounded exploiter information.
- [ ] Operational Diary creates high immediate risk and faster obsolescence after decisive change.
- [ ] Dead Drop Rain changes breadth, copy quality, and presentation.
- [ ] Variant combinations obey compatibility rules.

## Deep Files

- [ ] Eligibility begins at 400 Chaos.
- [ ] Activation is paced and not automatically instant.
- [ ] Evolution enable state is respected.
- [ ] One shared evolution log entry is recorded.
- [ ] Evolution activation gives zero Chaos.
- [ ] Pre-fire incidents start with the deep profile.
- [ ] Mid-incident second tranche uses delay, current Exposure, valid domain, and one-shot proof.
- [ ] Second tranche can add domains, Exposure, exploiters, and personnel risk once.
- [ ] Disabled evolution cannot set recorded flags or unlock deep content.

## Total Compromise

- [ ] Eligibility begins at 800 Chaos.
- [ ] Activation is paced and logged once.
- [ ] Evolution activation gives zero Chaos.
- [ ] Severe single, two-target, three-target, and four-target profiles exist.
- [ ] Pool-size fallback is resolved before target initialization.
- [ ] Every target is unique.
- [ ] Every target has separate state and cleanup.
- [ ] Human players manage only their own country state.
- [ ] Wartime mutual compromise works in both directions without one shared blanket modifier.
- [ ] Global processing and report caps prevent multi-target spam.
- [ ] Mid-incident escalation can add valid targets without resetting existing progress.

## Repeatability

- [ ] Current sequence closes fully before normal reselection.
- [ ] Shared Repeatable weight recovery and cap reduction remain authoritative.
- [ ] New sequence does not inherit temporary state.
- [ ] Same-country recurrence has safe flavour and capped lasting resilience.
- [ ] Achievement tracking distinguishes unique sequences.
- [ ] Cleanup cannot create another event-fire transaction.

## Cluster and connections

- [ ] Intelligence cluster row contains Event 039 and Event 052.
- [ ] Event 052 uses Low severity.
- [ ] Cluster transaction counts once for pacing.
- [ ] Event 52 member applies its own repeatable handling and history.
- [ ] Member skip reasons are recorded.
- [ ] Same-target Event 039 interaction uses public adapters and one bounded effect.
- [ ] Event 011 Evidence and Pact Readiness hooks are one-shot and use stable contracts.
- [ ] Event 008, 050, 094, and 097 interactions do not duplicate their core effects.
- [ ] Unavailable future events remain optional and nonblocking.

## Chaos

- [ ] Baseline manifestation applies once per sequence.
- [ ] Exceptional baseline extra point is rare and proved at opening.
- [ ] Severe personnel consequence applies once per target.
- [ ] Deep Files tranche applies once per sequence.
- [ ] Added-target Chaos counts actual new targets and respects cap.
- [ ] Severe single Total Compromise replaces ordinary manifestation value.
- [ ] Active neutralization reversal requires a Severe or Critical start and early zero.
- [ ] Passive expiry gives no reversal.
- [ ] Evolution activation gives zero.
- [ ] Generic war, tension, death, annexation, ideology, and buildup sources are not double counted.
- [ ] Chaos History uses Event 52-specific reasons.

## AI and probability

- [ ] All named probability scenarios are analyzed.
- [ ] Every weighted surface begins with `hoi4.probability_inspect`.
- [ ] Complete candidate pools are provided for normalized results.
- [ ] Exposure, agency strength, pool size, war danger, and Reliance sweeps are run where relevant.
- [ ] Baseline and final weights are compared with `hoi4.probability_compare`.
- [ ] Results distinguish exact, bounded, sampled, score-only, and unresolved evidence.
- [ ] Weak AI services prefer safe containment.
- [ ] Strong services use selective preservation and deception.
- [ ] Wartime AI prioritizes current military danger.
- [ ] Friendly AI avoids hostile exploitation without a relationship change.
- [ ] AI never loops on blocked or invalid actions.

## Presentation and localisation

- [ ] Final text follows the direction handoff and established Chaos Redux style.
- [ ] No working instruction or process note appears in player-facing text.
- [ ] Event, news, decision, mission, tooltip, achievement, Event Details, and workbook wording agree.
- [ ] Text avoids hidden mechanic spoilers.
- [ ] Exposure is explained clearly.
- [ ] Exploitation is shown through concrete foreign behavior.
- [ ] Deception success and failure are shown through observed consequences.
- [ ] Investigation preserves uncertainty.
- [ ] Multi-target reports identify scale without a popup flood.
- [ ] Integer values do not show unwanted decimal places.
- [ ] Localisation files use required encoding and key style.

## Assets

- [ ] Existing Event 52 DDS files receive exact LFS and container preflight.
- [ ] Existing report and news art is retained only if it passes visual review.
- [ ] Report and news images are distinct and period appropriate.
- [ ] Decision category icon and static picture exist and are wired.
- [ ] Every implemented action has its own decision icon.
- [ ] A status icon exists only when a real visible consumer uses it.
- [ ] Achievement icon triplets exist for all four achievements.
- [ ] Alpha-backed assets use real transparency and pass edge review.
- [ ] Final assets use correct runtime folders and stable sprite names.
- [ ] No runtime reference points into temporary `docs/assets/` evidence.
- [ ] Durable provenance and coverage facts are promoted before temporary workspace cleanup.

## Achievements

- [ ] Before the Ink Dries uses initial Exposure 90 or higher and blocks severe exploitation before threshold.
- [ ] A Better Falsehood counts three unique relevant hostile recipients.
- [ ] Everyone Knows Everything proves shared Total Compromise sequence, war enemy, early zero, and capital control.
- [ ] No Names Left Behind counts three unique personnel-risk incidents and equivalent DLC-safe proof.
- [ ] Force-trigger and debug disqualifiers work.
- [ ] Save and reload cannot duplicate progress.
- [ ] Names, descriptions, tracking, icons, docs, and tests are complete.

## Documentation and catalog

- [ ] Permanent Event 52 documentation explains the final system.
- [ ] Event 52 workbook row matches final in-game wording.
- [ ] Cluster 10 workbook row lists members 39 and 52.
- [ ] Mixed event-type representation follows workbook convention.
- [ ] Workbook is the only edited catalog source.
- [ ] CSV exports are regenerated with the official exporter.
- [ ] Event 52 implementation report lists changed files, systems, assets, audits, meaningful evidence, blockers, and simplifications.

## Final audit gate

- [ ] `hoi4.event_inspect`, render, and compare evidence covers the final event chain.
- [ ] Decision and mission audit is resolved.
- [ ] Probability audit and post-patch comparison are resolved.
- [ ] Localisation audit is resolved.
- [ ] Asset coverage and wiring review is resolved.
- [ ] Event completion audit is resolved.
- [ ] Improvement-loop addendum is implemented, folded into specs, queued with a reason, rejected with a reason, or closed through a closure handoff.
- [ ] Every unimplemented or simplified accepted requirement is reported clearly.
