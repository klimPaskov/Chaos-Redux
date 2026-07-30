# Event 12 Event Log and detail localisation handoff (2026-07-30)

## Scope

This handoff covers the public Event 12 history title/detail surfaces, the
shared writer wrapper, and the logging-only world-order callsites now owned by
the Event 12 integration pass.

Baseline plus Evolutions I-III remain the only logged Event 12 evolution rows.
Evolution IV is not added to the evolution arrays; the World-order payloads in
this handoff are ordinary history rows for the post-unification phase.

The South Africa/RSA mappings in `012_africa_rsa_effects.txt` and the existing
RSA title/detail localisation are preserved without edits.

## Changed files

- `common/script_constants/012_africa_event_log_constants.txt` adds the stable
  payload ids in the `africa_event_log` group.
- `common/scripted_effects/chaosx_events_log_effects.txt` adds
  `africa_record_event_log_world_order_entry`, which supplies Event 12's id
  and fire-once type and accepts payload, actor, and secondary-actor inputs.
- `common/scripted_effects/chaosx_events_log_effects.md` documents the helper's
  inputs, side effects, and readiness boundary.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
  adds Event 12 title/detail branches for every new payload and the history
  actor-pair display helper.
- `localisation/english/012_africa_event_log_l_english.yml` adds 54 UTF-8 BOM
  title/detail keys (27 payloads, one title and one detail each).
- `localisation/english/chaosx_gui_l_english.yml` routes the History detail
  actor line through `GetEventsLogHistoryDetailsActorLine` and adds primary,
  secondary, paired, and unattributed actor wording.
- `common/scripted_effects/012_africa_world_order_effects.txt` wires Scramble,
  package-install, constituent-outcome, and terminal The World rows.
- `common/scripted_effects/012_africa_world_union_war_effects.txt` wires union,
  continental-war, postwar-settlement, successor, exile, and breakup rows.

## Payload and localisation coverage

| Payload group | Constants | Title/detail key prefix | Required actor order |
| --- | --- | --- | --- |
| Scramble recognition, conditional recognition, sanctions, ultimatum | `africa_event_log.scramble_*` | `africa.event_log.scramble.*` | foreign respondent, Event 12 host |
| Middle East, Europe, Asia, North America, South America, Oceania package installation | `africa_event_log.package_*` | `africa.event_log.package.*` | external package actor, Event 12 host |
| Constituent ratification, refusal, withdrawal | `africa_event_log.constituent_*` | `africa.event_log.constituent.*` | package actor, constituent |
| Successor, exile, breakup dispositions | `africa_event_log.package_successor/exile/breakup` | `africa.event_log.package.*` | predecessor/package actor, receiving actor or host when available |
| Two-continent union | `africa_event_log.two_continent_union` | `africa.event_log.union.two_continent.*` | union host, union partner |
| Continental war goals: restore sovereignty, break rival compact, compel settlement | `africa_event_log.continental_war_*` goal ids | `africa.event_log.war.*` | attacker, defender |
| Continental prewar settlement, postwar armistice, submission, constituent release | `africa_event_log.continental_war_*` settlement ids | `africa.event_log.war.*` | prewar defender/attacker; armistice attacker/defender; submission attacker/defender; release defender/attacker |
| The World resolution: unanimous union, last standing, continental campaign | `africa_event_log.the_world_*` | `africa.event_log.the_world.*` | Event 12 host, no secondary actor |

Every new payload has exactly two scripted-localisation branches: one title
branch in `GetEventsLogHistoryEventName` and one detail branch in
`GetEventsLogEventDetailDescription`. New detail strings use the open Event
Details actor arrays so public country names survive flag cleanup.

## Writer callsite integration (applied)

The world-order effects set the five temporary inputs documented by
`africa_record_event_log_world_order_entry` and invoke it only after the
outcome flag or terminal status is committed. The helper clears its own inputs
and refreshes open human Event Log views.

- `africa_scramble_choose_recognition`,
  `africa_scramble_choose_conditional_recognition`,
  `africa_scramble_choose_sanctions`, and
  `africa_scramble_choose_ultimatum` are foreign-participant scopes. Use the
  participant as primary actor and `event_target:africa_host` as secondary
  actor. These calls run after the corresponding response flag is set; the
  existing once-only guards and phase transitions are unchanged.
- `africa_world_install_current_package` is the package-actor scope. Before
  package flags are cleared, branch on `africa_world_continent_id` and use the
  six `package_*` payloads. The package actor is primary and
  `event_target:africa_host` is secondary. The row describes installation
  regardless of sponsored, independent, or rival status; the localisation says
  "administered by" rather than implying sponsorship.
- `africa_world_record_constituent_consent`,
  `africa_world_record_constituent_refusal`, and
  `africa_world_record_constituent_withdrawal` are constituent scopes. The
  saved package target is primary and `THIS` is secondary. Existing
  consent/refusal/withdrawal predicates and arithmetic are unchanged.
- `africa_world_union_war_commit_successor`,
  `africa_world_union_war_record_exile`, and
  `africa_world_union_war_record_breakup` are the defeated-package outcome
  wrappers. The predecessor/package actor is primary. The saved successor is
  secondary for continuation; exile records no secondary actor; breakup records
  the host only when its event target remains available. RSA exile rows are not
  duplicated.
- `africa_world_union_protocol_activate` is the canonical W4 two-continent
  union writer. The host is primary and the partner is secondary after the
  active and autonomous-partner flags are set. The older
  `africa_world_form_union_with_current_target` path remains unlogged to avoid a
  duplicate union row.
- The three `africa_world_continental_war_protocol_prepare_*` helpers retain
  their review-only role. The matching goal row is written by
  `africa_world_continental_war_protocol_start_war`, with attacker primary and
  defender secondary, after the actual wargoal is declared.
- `africa_world_continental_war_protocol_resolve_armistice`,
  `...accept_constitutional_settlement`,
  `...resolve_submission`, and
  `...release_constituents` write their matching settlement payload before
  `africa_world_continental_war_protocol_cleanup` clears the event targets.
  Prewar settlement uses defender/attacker; armistice and submission use
  attacker/defender; constituent release uses defender/attacker. Existing
  terminal-resolution arithmetic and cleanup are unchanged.
- `africa_form_terminal_world_identity` remains gated by
  `africa_the_world_super_event_package_ready`, which this pass does not set. It
  branches by the committed terminal method (unanimous union, last standing, or
  continental campaign), uses the Event 12 host as primary actor, and does not
  claim that a super-event or audio package exists in the detail text.

## Flag-to-payload guard map

Use the outcome flags below as the local once-only guard around each writer;
the payload branch itself remains the stable history discriminator.

- Scramble: `africa_scramble_recognised_africa`,
  `africa_scramble_conditional_recognition`,
  `africa_scramble_sanctions_active`, and
  `africa_scramble_ultimatum_issuer`.
- Package installation: `africa_world_package_installed` together with the
  route flag (`africa_world_middle_east_package`,
  `africa_world_europe_package`, `africa_world_asia_package`,
  `africa_world_north_america_package`, `africa_world_south_america_package`,
  or `africa_world_oceania_package`).
- Constituent outcomes: `africa_world_constituent_consent_recorded`,
  `africa_world_constituent_refusal_recorded`, and
  `africa_world_constituent_withdrawal_recorded`.
- Defeated-package outcomes: `africa_world_union_war_successor_committed`,
  `africa_world_package_exile_path_resolved`, and
  `africa_world_package_breakup_recorded`.
- Two-continent union: `africa_world_union_protocol_active` plus
  `africa_dynamic_two_continent_union_active`.
- Continental war: pair the goal payload with
  `africa_world_continental_war_protocol_prepared` or
  `africa_world_continental_war_protocol_active`; pair settlement payloads
  with `africa_world_continental_war_protocol_settled` and the specific
  settlement flag (`africa_world_war_settlement_sovereign_armistice`,
  `africa_world_war_settlement_confederal_submission`, or
  `africa_world_war_settlement_constituent_release`).
- The World: `africa_terminal_world_identity_formed` is the outcome flag. The
  writer must remain behind `africa_the_world_super_event_package_ready` and
  must not set that readiness flag.

## Existing RSA coverage preserved

The committed RSA helper continues to write payloads 12001, 12002, and
12004-12008 through `africa_rsa_record_event_log_history`. Its existing actor,
title, detail, and exile mappings were not changed by this handoff.

## Validation

- The new Event 12 localisation file and the modified GUI localisation are
  UTF-8 with BOM.
- Duplicate-key scan found no duplicates in either changed localisation file.
- All 54 new scripted-localisation references resolve to English localisation
  keys.
- The Event Log scripted-localisation file has no duplicate `defined_text`
  names, has balanced braces, and each of the 27 new payload ids appears in
  exactly one title branch and one detail branch.
- The two world-order effect files contain logging-only calls for every new
  payload family; no readiness, cost, AI, route, or terminal mechanic was
  changed by those callsites.

## Unresolved decisions

The canonical union writer is `africa_world_union_protocol_activate`, and the
canonical war-goal writer is `africa_world_continental_war_protocol_start_war`.
Package installation wording intentionally avoids assuming sponsorship because
the same callsite handles independent and rival routes. Breakup detail names
the host only when the secondary actor is available. No readiness flag, audio
fallback, super-event package, AI rule, cost, or route mechanic was changed.
