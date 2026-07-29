# Event 015 League integrity, consent, and war-callback correction

Date: `2026-07-17`  
Worker: `league_integrity_fix`  
Mode: bounded gameplay, localisation, mapping, and documentation patch; no commit created

## Outcome

The confirmed League relationship defects are corrected in the live Event 015 source.

- Every guarantee created by the League records the exact founder and the exact guarantee direction on the partner scope. Cleanup revokes only a live guarantee carrying that exact Event 15 attribution.
- Formal defense uses a unique faction template. Partner membership records its exact founder only after the country actually joins that template, and teardown proves the current faction's template identity before leaving or dismantling it.
- Compatible partner roles may layer for one founder, but exact active and pending arrays prevent a second Event 15 founder from owning the same League package.
- Full-invitation and reserve-compact answers resolve only while the exact request and founder League remain live. Delayed responses after collapse or terminal teardown clear stale state without calling a role recorder.
- League sponsorship is a targeted, time-bounded request. The selected major chooses technical sponsorship, sponsorship backed by its own guarantee, or refusal. The founder cannot install a sponsor or guarantee before that answer.
- League-member attacks and founder attacks are handled by the existing one-shot war-relation callback. A member attacking its exact founder records an obligation breach; a founder attacking its exact member opens a paired leave-or-remain response.
- Every recognition-bearing League role records a deduplicated package source even when another system already made the partner visible. That marker survives layered-role removal and is consumed after the final exact League role; a live compact or association can then preserve visible recognition.
- Exit, expulsion, collapse, runtime teardown, annexation, timeout, cancellation, and response resolution clean their exact pair state without recurring country scans.
- League sponsorship and betrayal AI now reads legitimacy, autonomy, Need, reserves, world threat, ideology, opinion, coercion, stale-claim conduct, and sponsor-defense pressure where relevant.

No simplification, fallback, placeholder, recurring scan, or omitted requested branch was used.

## Files changed

### Gameplay

- `common/factions/templates/015_utopia_manifesto.txt`
- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
- `events/015_utopia_manifesto.txt`

### Localisation, mapping, and documentation

- `localisation/english/015_utopia_manifesto_decision_completion_l_english.yml`
- `localisation/english/015_utopia_manifesto_events_l_english.yml`
- `docs/assets/015_utopia_manifesto/decision_icon_mapping.csv`
- `docs/events/015_utopia_manifesto/overview.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_4_decisions_and_missions.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_6_evolutions_events_and_reactions.md`
- `docs/specs/015_utopia_manifesto_specs/specs/015_utopia_manifesto_spec_part_8_assets_localisation_and_acceptance.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/asset_manifest_plan.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/completion_coverage_matrix.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/decision_mission_matrix.md`

These are shared Event 15 files and were under concurrent modification. The identifiers below define this worker's exact ownership surface.

## Guarantee provenance contract

All three provenance arrays live on the partner country and may contain more than one Event 15 founder.

| Partner-side array | Created relation | Precheck before creation | Postcheck before attribution | Exact revocation |
| --- | --- | --- | --- | --- |
| `utopia_manifesto_league_founder_guarantee_founders` | founder guarantees member | member is not already guaranteed by founder | member is guaranteed by founder | founder disables its guarantee toward that partner |
| `utopia_manifesto_league_member_guarantee_founders` | member guarantees founder | member has not already guaranteed founder | member has guaranteed founder | partner disables its guarantee toward that founder |
| `utopia_manifesto_league_sponsor_guarantee_founders` | sponsor guarantees founder | sponsor has not already guaranteed founder | sponsor has guaranteed founder | partner disables its guarantee toward that founder |

`utopia_manifesto_remove_root_league_created_guarantees` is partner-scoped with the exact founder as `ROOT`. It checks each attribution independently, revokes only that direction when still live, and always removes only that founder from the matching array. Pre-existing guarantees and guarantees created by another system or another Event 15 founder survive.

The two-way member-defense attribution is created by `utopia_manifesto_record_from_league_defense_consultation`. Sponsor attribution is created only by `utopia_manifesto_apply_from_league_sponsor_guarantee_package`; technical sponsorship calls no guarantee effect.

## Faction provenance and role ownership

Formal defense is created from `faction_template_utopia_manifesto_commonwealth_league`, replacing the deprecated raw `create_faction` call. The unique template preserves the existing Commonwealth League name, uses the existing vanilla `GFX_faction_logo_generic_democratic`, and gives cleanup an engine-visible identity through `has_faction_template`.

Partner-side `utopia_manifesto_league_faction_founders` records the exact creator. `utopia_manifesto_join_root_league_faction_if_unaligned` requires the partner to be factionless and the founder to lead the unique League template, calls `add_to_faction`, then attributes the founder only after both the live faction relation and template postcheck pass. `utopia_manifesto_remove_root_league_created_faction_membership` requires that exact founder attribution and the live League template before `leave_faction`; it cannot remove a partner from an unrelated faction.

Collapse and terminal runtime teardown require all three founder checks before `dismantle_faction`:

- `utopia_manifesto_league_formal_defense`;
- `is_faction_leader = yes`;
- `has_faction_template = faction_template_utopia_manifesto_commonwealth_league`.

If external script replaces the founder's original faction, the template check fails and the unrelated faction survives even if the Event 15 summary flag is stale.

Compatible flags form one founder-owned package: member plus defense, sponsor plus observer, and member plus aid or reserve are valid. `utopia_manifesto_has_conflicting_league_partner_relationship_for_root` filters the partner's generic reverse-founder array through every linked founder's exact active and pending arrays. It therefore rejects a different founder's package without treating candidate-only or unrelated external-network links as owners. Candidate and sponsor eligibility require an unowned active package; paid aid, technical, reserve, reconstruction, and defense actions recheck exact ownership in both target and availability gates before payment; all six role recorders repeat the guard before changing arrays, flags, guarantees, or cohesion. The current founder may layer compatible duties, but another founder cannot spend resources and then hit a global-flag no-op.

When `utopia_manifesto_post_founder_defense_league_survives` records a successful successor transfer, `utopia_manifesto_remove_root_league_created_faction_membership` removes the former founder from the partner attribution array but skips `leave_faction`. Generic runtime teardown can clear Event 15 flags and diplomacy without emptying or dissolving the preserved template faction.

## Consentful targeted sponsorship

The existing decision ID remains stable:

- `decision_utopia_accept_league_sponsorship` is player-facing as **Request League Sponsorship**;
- it selects one valid major, records both sides of the exact request, prepares `utopia_manifesto_league_days`, activates `mission_utopia_league_sponsorship_answer`, and fires event `.215` for that target;
- it does not record a sponsor and does not create a guarantee.

The pair contract is:

| Founder state | Target state |
| --- | --- |
| `utopia_manifesto_league_sponsorship_pending_targets` contains target | `utopia_manifesto_league_sponsorship_pending_founders` contains founder |
| `utopia_manifesto_league_sponsorship_pending` | `utopia_manifesto_league_sponsorship_request_pending` |

The response flow is:

1. `.215` is target-rooted and validates both sides of the pair.
2. The target chooses technical help, a sponsor-to-founder guarantee, or refusal.
3. Hidden founder bridge `.216` validates the exact pair through `utopia_manifesto_from_is_exact_pending_league_sponsorship_response`.
4. `utopia_manifesto_resolve_from_league_sponsorship_response` records a sponsor only for the two accepted packages and calls the guarantee helper only for the defensive package.
5. `.72` is an acknowledgment of already accepted terms. Its trigger requires the accepted package and the exact sponsor relationship; it has no sponsor-installation effect.
6. Timeout is an exact refusal. Cancellation and all teardown paths close the exact targeted mission with `remove_targeted_decision`, clear both sides of the pair, and leave no sponsorship or guarantee behind.

The mission reuses the existing League aid-corridor icon. Its dedicated mapping row is registered, so no new art asset or sprite definition was required.

## Fail-closed invitation responses

Hidden founder bridge `.212` resolves both full invitations from `.210` and reserve compacts from `.211`. `utopia_manifesto_from_is_exact_pending_league_invitation_response` requires:

- an initialized founder League that is neither collapsed nor cleaning up;
- the exact founder target array and matching target-side request flag for the full invitation or reserve compact;
- no package owned by another Event 15 founder;
- exactly one response allowed by that request type.

`utopia_manifesto_resolve_from_league_invitation_response` closes the exact targeted mission, founder array entry, target request flag, and all target response flags before calling a role recorder. If any contract check fails, it calls only the close helper. A human response event left open across collapse, annex cleanup, or terminal runtime teardown therefore cannot recreate member, observer, reserve, defense, or refusal state on a disabled founder.

## One-shot war behavior

`on_war_relation_added` already supplies attacker `ROOT` and defender `FROM`. The correction adds two bounded exact-pair branches and no periodic maintenance hook.

### Member attacks founder

The branch requires both directions of the durable League relationship:

- attacker is a League member and records the defender in `utopia_manifesto_league_founders`;
- defender is an active Event 15 League founder and records the attacker in `utopia_manifesto_league_members`.

The attacker receives `utopia_manifesto_league_obligation_breached`; the exact founder records League failure. No founder-wide breach flag is used.

### Founder attacks member

The branch records an exact pair in:

- founder `utopia_manifesto_league_betrayal_pending_targets`;
- member `utopia_manifesto_league_betrayal_pending_founders`.

Event `.217` lets the attacked member leave or remain. Hidden event `.218` returns the exact response to the founder. `utopia_manifesto_from_is_exact_pending_league_betrayal_response` requires both pair arrays and exactly one response flag. The founder records betrayal, coercion disqualification, and League failure; a leaving member uses the ordinary exact League-exit cleanup, while a remaining member records that it survived the breach.

## Recognition cleanup contract

`utopia_manifesto_league_created_recognized_partners` is the stable legacy identifier for a package-wide League recognition source marker. `utopia_manifesto_add_from_as_league_recognized_partner` adds it, deduplicated, whenever a recognition-bearing League role is recorded, even if a compact or association had already placed the partner in `utopia_manifesto_recognized_external_partners`.

`utopia_manifesto_remove_root_league_created_recognition_if_unbased` is partner-scoped. It removes that marker only after `utopia_manifesto_has_live_league_recognition_role_for_root` proves that none of the founder's exact member, observer, sponsor, aid, reserve, or defense roles remains. It then preserves visible recognition only when an independent exact pair remains in:

- `utopia_manifesto_recognized_compacts`;
- `utopia_manifesto_recognized_associates`.

Member-plus-aid, member-plus-reserve, sponsor-plus-observer, and similar packages therefore retain their marker when one role ends. Collapse and terminal cleanup clear the exact League role arrays first, then consume the marker snapshot and remove visible recognition only when no compact or association survives. This covers both ordering directions: a League role added over pre-existing visible recognition still records its source, and the final League role cannot leave recognition immortal after an earlier layered-role exit.

Collapse first removes League-only bases, snapshots the created-recognition attribution array, and then applies this helper. Compact- or association-supported recognition therefore survives collapse. Terminal runtime cleanup applies the same attribution-aware pass before clearing all terminal Event 15 network state.

## Cleanup coverage

| Lifecycle path | Pair request state | Guarantee attribution | Recognition attribution | League flags and arrays |
| --- | --- | --- | --- | --- |
| sponsorship answer | exact pair closed | package-dependent | sponsor basis retained only on acceptance | response flags cleared |
| sponsorship timeout/cancel | exact pair closed | none created | none created | pending/objective state released |
| member exit/expulsion | betrayal pair cleared | exact founder directions revoked | removed only when unbased | only attributed League-template faction membership removed; member/defense state removed |
| League collapse | all targeted missions and pending pairs closed | member, defense, sponsor, and reverse-link partners checked | League bases cleared, then attribution-aware snapshot cleanup | faction dismantled only with exact template identity; active League state cleared |
| terminal runtime teardown | all pending state closed | all recorded exact partners checked | attribution-aware cleanup before terminal network teardown | faction dismantled only with exact template identity; all League runtime state cleared |
| partner annexation | exact targeted sponsorship mission removed before pair deletion | exact founder directions revoked through the founder callback | annexed partner removed from founder network arrays | exact faction attribution, partner flags, and reverse-founder arrays cleared after callbacks |

`utopia_manifesto_has_recorded_league_relation_for_root` includes the sponsorship and betrayal pair arrays plus all three guarantee-attribution arrays. Reverse-link reconciliation can therefore retain a partner long enough for exact annexation and teardown cleanup without scanning all countries.

## AI behavior

The request decision and sponsorship-response options account for:

- founder League legitimacy and retained partner autonomy;
- high Need and insecure reserves;
- world-threat and current-war pressure;
- shared ideology and bilateral positive opinion;
- founder coercive conduct and stale-claim disqualification;
- whether a defensive sponsorship package would answer immediate security pressure.

The founder-betrayal response similarly weighs live war, opinion, ideology, legitimacy, autonomy, world threat, coercion, stale claims, and an existing sponsor defense package. The logic uses existing Event 15 tuning constants; no new magic-number AI table was introduced.

## Localisation and canonical inventories

- The sponsorship decision, mission, requirements, timeout, event `.72`, target response `.215`, and betrayal response `.217` have aligned English localisation.
- The unique faction template uses the localised `utopia_manifesto_commonwealth_league` name and an existing vanilla faction icon; no new asset or `.gfx` registration was required.
- Hidden bridges `.216` and `.218` require no player-facing localisation.
- Frozen League-tranche inventory before the later association-review relay: **105 unique event definitions**, including **11 hidden events**. The integrated package subsequently added visible `.221` and made `.207` a hidden reservation bridge, producing 106 definitions and 12 hidden events in the canonical documentation.
- Current main decision inventory: **105 decisions** and **40 missions**.
- Current decision-icon mapping inventory: **174 rows**: 9 categories, 121 decision rows, and 44 mission rows.
- Both edited English localisation files retain UTF-8 BOM encoding.

## Validation evidence

- The six gameplay sources, including the faction template, have balanced block depth after the concurrent Event 15 integration work.
- All 105 Event 15 IDs in this frozen League-tranche snapshot were unique; the later integrated inventory is covered by the final whole-package audit.
- New sponsorship and betrayal localisation keys are each defined once.
- Invitation and reserve responses require a live exact pair and one request-valid response; the resolver closes pair and response state before any recorder and fails closed after teardown.
- Guarantee creation has a matching precheck, live-relation postcheck, partner-side attribution producer, and exact-direction cleanup consumer.
- Faction creation has a unique template; partner joins have a factionless precheck, live-template postcheck, exact-founder attribution, and exact-template removal consumer.
- Both faction dismantle sites require the exact Event 15 template, so external faction replacement cannot redirect teardown.
- Exact active/pending founder-array conflict checks cover candidate/sponsor selection, all five paid target actions, and all six role recorders while preserving same-founder layered packages.
- The post-founder survival flag is checked inside faction-membership cleanup, so successor transfer survives generic runtime teardown while obsolete founder attribution is still removed.
- Sponsorship's technical branch contains no guarantee effect; refusal and timeout contain no sponsor-registration effect.
- The only new war handling is inside `on_war_relation_added`; no daily, weekly, monthly, or whole-world maintenance action was added.
- `git diff --check` found no patch whitespace error in the touched surface; repository line-ending warnings remain informational.

The HOI4 MCP lint/render path was attempted twice, but artifact retention failed with `ARTIFACT_STORAGE_LIMIT`. The optional stored MCP artifact is therefore unavailable. Direct source inspection, inventory checks, and independent package audits remain the completion evidence.

## Audit status and remaining risks

Independent country-package and diplomacy-link re-audits both returned **PASS** on the frozen League surface, with no remaining League P1 or P2 finding. Their final traces covered exact guarantee direction, cross-founder package exclusion, same-founder layered roles, unique faction-template teardown, post-founder faction preservation, full-invitation and reserve-compact fail-closed responses, recognition added over a pre-existing compact or association, member-plus-aid marker retention, final-role marker consumption, collapse, and terminal cleanup.

The shared Event 15 effects and documentation files also contain association and colony-provenance regions owned by the parent integration task. Findings in those non-League regions were routed to the parent and are not part of this League completion claim. Final counts above were taken from the live integrated files, not from an isolated snapshot.

## Skills and references used

- `chaos-redux-events`
- `hoi4-decisions-missions`
- `chaos-redux-subagents`
- required offline Paradox wiki core pages, including data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, and AI modding
- offline `Faction modding` wiki snapshot and vanilla `common/factions/_documentation.md`
- vanilla decision, trigger, effect, event, scope, and on-action documentation and exact targeted-decision removal precedents

## Simplifications, omissions, and blockers

- Gameplay simplifications: none.
- Fallbacks: none.
- Placeholder content: none.
- Missing localisation or icon mapping: none.
- Missing requested AI branch: none.
- Recurring scan substitute: none.
- Validation tooling blocker: the optional HOI4 MCP artifact could not be retained because the shared artifact store was full.
