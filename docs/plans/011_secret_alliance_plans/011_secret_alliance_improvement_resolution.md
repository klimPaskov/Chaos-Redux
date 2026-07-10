# Event 011 improvement-loop resolution

Date: 2026-07-10

## Status and boundary

The accepted mandatory addendum `011_secret_alliance_implementation_improvement_addendum.md` is fully disposed. Every accepted requirement in tranches A-G, every mandatory architecture carryover, and every acceptance scenario has an implementation or promotion record below. No accepted item remains queued or unresolved.

The implementation chronology is `abc70f55` for the causal gameplay tranche, `6a33976e` for the first reveal wording freeze, `3a48a344` for valid-human recruitment capacity, `690dae0e` for reveal-time casualty baselines, `a1f47c0c` for the main lifecycle and presentation closure, `7563648f` for counted delayed-callback isolation, `97a2da80` for wording and catalog mirrors, and `1c87d923` for the final high-impact balance freeze. DM-15 through DM-20 and CA-01 through CA-13 are resolved. This resolution closes the accepted improvement plan. The holistic verdict is owned by `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`; this plan-closure record does not replace it.

## Plan disposition

| Plan or requirement set | Disposition | Reason |
| --- | --- | --- |
| `011_secret_alliance_improvement_addendum.md` | Folded into the accepted five-part specification, then superseded as an implementation checklist | Its hidden-coalition design, roles, operations, counterplay, reveal, assets, and cleanup became source design. Its no-manual-scenario direction was rejected by the later accepted SCN-009 specification. The file remains historical design chronology. |
| `011_secret_alliance_implementation_improvement_addendum.md` tranches A-G | Implemented and resolved | The bounded causal-depth requirements are mapped below to current helpers, events, AI, UI, and documentation. |
| Mandatory architecture carryover in the implementation addendum | Implemented and resolved | Candidate safety, arrays, costs, faction transaction guards, dynamic naming, lifecycle hooks, and history separation are active. |
| Optional future ideas | Retained as optional future work | Country-specific incidents, later cross-event hooks, and a deeper postwar bloc were never part of the accepted completion boundary. |
| Anti-bloat boundary | Preserved | No new tag, focus tree, formable, world-end branch, achievement family, broad GUI, or second super-event was added. |

## Accepted tranche resolution

### Tranche A: standing conference, roles, and commitments

| Accepted item | Disposition | Current evidence |
| --- | --- | --- |
| Durable motive, commitment band, operational role, support capability, and private bargain for every member | Implemented | `secret_alliance_assign_current_member_profile`, `secret_alliance_assign_current_member_motive`, `secret_alliance_refresh_current_member_commitment`, member variables, and member arrays in `common/scripted_effects/011_secret_alliance_effects.txt` |
| Geography-appropriate border, logistics, intelligence, political, liaison, maritime, and distant-support work | Implemented | Role and support assignment helpers, sponsor theater profiles, operation-family weights, scenario identity, and revealed AI routing |
| Motive and commitment affect operations, defection, delayed calls, and reveal conversion | Implemented | Commitment tickets, defection selection, delayed-call pools, operation actor selection, and `secret_alliance_convert_hidden_values_to_war_state` |
| Disputes preserve incompatible promises and affect later behavior | Implemented | Dispute participants, promise-conflict state, agenda delay, commitment changes, reveal fracture reserve, and public conflicting-war-aim facts |

### Tranche B: operation dossiers and adaptive pacing

| Accepted item | Disposition | Current evidence |
| --- | --- | --- |
| Six accepted operation families replace scene labels as the mechanical families | Implemented | Diplomatic isolation, intelligence penetration, industrial and transport sabotage, political and social pressure, military preparation, and recruitment in `secret_alliance_launch_weighted_operation` |
| Baseline, Evolution I, and Evolution II capability gates | Implemented | Baseline keeps diplomatic, intelligence, sabotage, and recruitment. Evolution I opens political and military work. Evolution II adds the rare political-violence event `chaosx.nr11.21`. |
| One stored dossier with actor, family, surface, readiness layer, evidence class, risk, and recovery state | Implemented | Global operation targets and variables prepared by `secret_alliance_launch_weighted_operation` and consumed by the resolution helpers |
| Doctrine, role, motive, target state, prior result, recency, Alertness, and Preparedness shape selection | Implemented | Family ticket adjustments, actor tickets, surface availability gates, prior-result weights, and MTTH factors |
| Outcome uses the stored dossier instead of rerolling identity | Implemented | `secret_alliance_prepare_operation_risk_resolution`, `secret_alliance_prepare_operation_disruption_risk_resolution`, `secret_alliance_change_named_operation_readiness`, and `secret_alliance_register_operation_clue` |
| Physical surface effects and protections are causal | Implemented | Exact industrial-state infrastructure damage, mapped military surface, exposed surface, and `secret_alliance_check_current_operation_surface_protection` |
| Dynamic cadence and recovery replace one fixed pulse | Implemented | `common/mtth/011_secret_alliance_mtth.txt`, recent-family pressure, severe recovery, dispute delay, Evidence responses, and target-state factors |

### Tranche C: evidence, corroboration, and suspect curation

| Accepted item | Disposition | Current evidence |
| --- | --- | --- |
| Six source-aware evidence classes | Implemented | Method, communications, financial, diplomatic, military, and human classes in constants and clue helpers |
| Same source and class pair cannot farm Evidence | Implemented | Per-source class flags, independent-class counters, and `secret_alliance_apply_new_clue` |
| Global case strength and country confidence remain separate | Implemented | Global Evidence, per-suspect confidence, and per-suspect corroboration thresholds |
| Public actions require case strength and independent corroboration | Implemented | Public-case triggers and decision availability in Event 011 triggers and decisions |
| False leads can be disproved and weak planted leads can be archived | Implemented | False-traffic source memory, suspect clearing, `secret_alliance_close_disproved_lead`, and credibility recovery |
| Repeated unsupported accusations have durable consequences | Implemented | Innocent-accusation flags, capped cohesion and alertness reactions, diplomatic damage, and achievement disqualifiers |
| Human panel is capped at three while AI reads the full array | Implemented | `global.secret_alliance_visible_suspects`, `secret_alliance_rebuild_visible_suspects`, compact scripted GUI, and full-array AI selection |
| Complete-network and founder achievements remain protected | Implemented | Reveal-state records, independent-class requirements, true-founder proof, and innocent-targeting disqualifiers |

### Tranche D: maintained Preparedness and real objectives

| Accepted item | Disposition | Current evidence |
| --- | --- | --- |
| Seven Preparedness components are recalculated from live sources | Implemented | Staff, industrial, transport, border, continuity, allied, and known-plans contributions in `secret_alliance_recalculate_preparedness` |
| Projects have costs, burdens, durations, and idempotent expiry | Implemented | Protection effects, timed flags and events, source-specific expiry helpers, ideas, and slot release logic |
| Five map-facing protections store the selected state | Implemented | Protected industrial, stockpile, border, port or airfield, and continuity event targets |
| State protection affects only a matching operation surface | Implemented | `secret_alliance_check_current_operation_surface_protection` compares the recorded operation state with the protected state before denial |
| Family caps govern live actions and missions | Implemented | Two investigations, one protection, one diplomacy, one offensive, one border, and one emergency slot with acquire and release helpers |
| Named missions verify real delayed objectives | Implemented | Seven missions, prepared state and suspect targets, delayed verification, repeat verification, and full, partial, failure, cancellation, and expiry resolution |
| Hardened Networks is not permanent click accumulation | Implemented | Maintained staged use plus the separate Preparedness-scaled hidden-collapse aftermath idea |

### Tranche E: interruptible evolutions

| Accepted item | Disposition | Current evidence |
| --- | --- | --- |
| Evolution I opens recruitment without manufacturing a fourth member | Implemented | Scheduled invitations and the dynamic member-cap helper |
| Recruitment outcomes include accepted, conditional, refused, and leaked states | Implemented | AI response weights, human event `chaosx.nr11.20`, conditional commitment, leak pause, and outcome histories |
| Recruitment cap reacts to target strength, target tension, and actual candidate capacity | Implemented | `secret_alliance_maybe_recruit_member`, weak-target and peaceful-target penalties, dynamic floor, and a candidate ceiling that counts valid AI and human recruits |
| Evolution II courts one strategically valid sponsor | Implemented | Operational reach, capacity, opposition reason, theater profile, weighted response, and minor-led continuation |
| Evolution II opens serious incidents without filling six members | Implemented | Serious incident delay, response category, six-family operation state, and rare `chaosx.nr11.21` branch |
| Evolution III gates a second sponsor behind the first sponsor and operation time | Implemented | `secret_alliance_maybe_schedule_second_sponsor` and pulse-based minimum and retry constants |
| Evolution III can be delayed, controlled, forced, weakened, or fractured by current state | Implemented | `secret_alliance_resolve_coalition_countdown`, `secret_alliance_public_conference_reveal`, controlled flag, public-dossier route, weakened route, and fractured route |
| Pre-fire Evolution III passes through Evolution II and preserves a response interval | Implemented | Pre-fire pending state and shared evolution opening helpers |
| Disabled evolutions do not consume gated progression | Implemented | Evolution enable checks remain in the shared evolution logging and application path |

### Tranche F: public faction, roles, and Resolve

| Accepted item | Disposition | Current evidence |
| --- | --- | --- |
| Real Event 011 faction, goals, rules, and manifest | Implemented | Event-owned faction template, doctrine goals, rule group, rules, dynamic anti-target name, and postwar manifest |
| Reveal transaction is rollback-safe | Implemented | Leader precedence, previous-faction snapshots, temporary creation authority, complete hostile-war call verification, rollback, and idempotent cleanup |
| Preparedness delays eligible calls except on hostile-war reveal | Implemented | `secret_alliance_assign_preparedness_delayed_calls` and hostile-war delay clearing |
| Role-aware public AI includes real target-front allocation | Implemented | Positive target-specific `front_unit_request` plus conquest and concentration for front-capable members, negative target-front request for distant support, and sponsor protection |
| Resolve reads factual war state rather than a farmable timer | Implemented | Target objective progress, failed offensive, post-reveal member casualties, surrender burden, sponsor aid and distraction, route survival, concessions, capital loss, promises, rivalry, separate terms, and fractures |
| Pre-event casualties cannot trigger Event 011 war burden | Implemented | Reveal-time `secret_alliance_reveal_casualties_snapshot` and post-reveal casualty subtraction in `secret_alliance_update_named_war_objectives` |
| Two-major leadership crisis has factual gates and does not force immediate collapse | Implemented | Saved sponsor theaters and doctrine pressure, failed objective or distraction gates, coordination loss, and public conflicting-war-aim state |
| Postwar continuation needs Resolve, members, leadership, and doctrine support | Implemented | Doctrine-specific settlement helpers, minimum Resolve and membership gates, sponsor and dispute checks, and conversion to Coalition Security Council |

### Tranche G: AI, scenario identity, and achievements

| Accepted item | Disposition | Current evidence |
| --- | --- | --- |
| Founder and recruit AI use motive, target behavior, capacity, wars, stability, access, and sponsor support | Implemented | Weighted candidate helpers and response-weight preparation |
| Operation AI reacts to role, target vulnerability, Evidence, and Preparedness | Implemented | Operation family and actor tickets plus route cleanup, false traffic, member cover, and accelerated reveal responses |
| Target AI uses full suspect state and shared costs and effects | Implemented | `secret_alliance_ai_select_action_target` and `secret_alliance_run_target_ai_response` |
| Wartime AI separates front-capable and distant support roles | Implemented | Dynamic revealed AI, `front_unit_request`, force concentration, sponsor protection, and cleanup mirrors |
| All five scenario types have distinct composition and behavior | Implemented | Regional Ring reach, Ideological Front opposition, Great-Power Sponsor reach, Unlikely Coalition mixed motives and promises, and Random Coalition weighted derivation |
| Type and intensity gates block impossible compositions without substitution | Implemented | Scenario viability triggers, requested and achieved snapshots, and abort path |
| Scenario members are AI-only and normal human recruits require explicit consent | Implemented | Scenario candidate gates and the five-option normal human invitation including conditional acceptance |
| Six achievements retain causal proof and anti-farming state | Implemented | Independent Evidence coverage, preserved turned channel, Event 011 fracture exits, immutable scenario snapshots, major snapshots, capital snapshot, and forced-origin disqualifiers |

## Mandatory architecture carryover

| Accepted correction | Disposition and evidence |
| --- | --- |
| Civil-war and unsafe faction-state exclusions | Implemented in founder, recruit, and sponsor validity triggers. |
| Maintained arrays and counts instead of repeated broad decision scans | Implemented through member, founder, sponsor, suspect, confirmed, turned, public, and archive registries. |
| Stored dynamic costs shared by display, availability, and payment | Implemented through `secret_alliance_refresh_dynamic_costs`, cost triggers, and payment helpers. |
| Survivor rebuild instead of clearing flags inside live arrays | Implemented by validity refresh and survivor arrays. |
| Separate founder, visible-suspect, confirmed-member, and turned-member registries | Implemented and used by UI, AI, reveal, achievements, and cleanup. |
| Narrow lifecycle hooks | Implemented in the Event 011 on-action file for war, capitulation, government, annexation, faction, subject, civil-war, peace, and postwar-bloc changes. |
| Reveal recursion guard and complete anchor-war validation | Implemented across reveal, faction creation, war calls, retries, rollback, and outcome reentrancy. |
| Dynamic faction-name grammar fallback | Implemented through `secret_alliance_initialize_faction_name_grammar` and `secret_alliance_faction_name_country_exception`. |
| History and achievement facts separated from runtime cleanup | Implemented through target-owned run records, reveal-state records, outcome facts, and explicit preservation rules. |

## Acceptance scenario closure

| # | Accepted scenario | Disposition |
| --- | --- | --- |
| 1 | Different motives and geography produce different roles and operation weights | Implemented through profile and ticket helpers. |
| 2 | Same source and clue class cannot be farmed | Implemented through source-class memory. |
| 3 | False leads can be cleared and unsupported accusations carry consequences | Implemented through false-traffic memory, Close Disproved Lead, and durable accusation effects. |
| 4 | Human panel shows three suspects while AI uses the full set | Implemented through separate arrays. |
| 5 | Expiring protection removes only its own Preparedness | Implemented through source-specific contribution and expiry helpers. |
| 6 | Industrial, courier, and border operations attack relevant protection layers | Implemented through family, readiness-layer, and state-surface dossiers. |
| 7 | One substantial operation runs at a time with recency and recovery | Implemented through the active flag, one dossier, prior-result weights, and recovery flags. |
| 8 | Evolution I does not guarantee a fourth member | Implemented through scheduled invitations and dynamic capacity. |
| 9 | Evolution II sponsor acceptance, refusal, and leak have distinct continuations | Implemented through weighted sponsor response branches. |
| 10 | Evolution III has a value-driven response window | Implemented through one defense delay and controlled, forced, weakened, and fractured resolution. |
| 11 | The four doctrines use different goals and fracture conditions | Implemented in faction goals, war facts, and doctrine settlement logic. |
| 12 | Maritime and distant members avoid generic land-front posture | Implemented through role assignment and opposing `front_unit_request` values. |
| 13 | Two-major leadership disputes do not automatically collapse the faction | Implemented through a staged coordination and Resolve penalty. |
| 14 | Resolve reacts to objective, loss, access, sponsor, promise, and withdrawal facts | Implemented with guarded named facts and reveal-time casualty baselines. |
| 15 | Every scenario type has distinct composition and behavior checks | Implemented through type-aware gates and identity effects at all four intensities. |
| 16 | Human membership and war entry require consent | Implemented for normal invitations. Scenario coalitions use AI members only. |
| 17 | All six achievement positive paths remain possible | Implemented in the achievement registry and snapshot helpers. Final audit remains responsible for the whole-event verdict. |

## Audit-remediation disposition

| Audit range | Disposition at final freeze `1c87d923` | Evidence boundary |
| --- | --- | --- |
| DM-15 through DM-20 | Resolved; independent decision specialist returned CLEAN | Public-war-start gating, mission-aware phase cleanup, current suspect-bound border pairs, valid envoy objective state, revealed cost refresh, and exact AI protection-state selection |
| CA-01 through CA-13 | Resolved on completion-audit rescan | Route-aware leader and exit state, exact border transaction, repeat-turn guard, preemption route handling, fractured text, lifecycle-safe notifications, delayed-event guards, origin-safe history and achievements, durable presentation snapshots, per-run Sponsor Accountability, and counted callback draining including `.50` through `.53` |
| Holistic completion verdict | External authority | Owned by `docs/plans/011_secret_alliance_plans/subagent_handoffs/completion_audit.md`; this scoped improvement resolution does not replace it |

The direct AI controller is the unique owner of eight protection routes, Turn Member, and three wartime actions. Engine weights for those actions are blocked, and target-owned cooldowns are 120, 180, and 120 days respectively. Scripted-GUI suspect selection and clearing refresh the stored border pair and are unavailable during an unresolved border conflict. The reveal presentation holds route, target, leader, member count, and faction-name grammar snapshots for the 14-day display slot, then `.202` removes the context on day 15.

## Promotion result and current blockers

The accepted addendum did not expand the five-part source specification's completion boundary. It supplied causal implementation detail already required by that design. The completed behavior is promoted into `docs/events/011_secret_alliance.md`, while this resolution remains the itemized audit trail.

No accepted improvement-loop item remains unresolved. No DM-15 through DM-20 or CA-01 through CA-13 blocker remains open at the final freeze. This resolution remains a plan-closure record, while the holistic verdict is maintained in the final completion-audit handoff.
