# Event 012 provenance and vanilla council recruitment fix

Date: 2026-07-24

Owner: `/root/africa_tag_provenance_character_fix`

## Scope

This handoff covers the narrow Event 012 country-audit fixes for active Event 006 provenance and institutional-council ownership.

No country-tag, country-history, map, territory, core, subject, faction, cosmetic-tag, portrait, icon, localisation, workbook, or asset file was changed.

## Files changed

- `common/scripted_triggers/012_africa_priority_member_triggers.txt`
- `common/scripted_effects/012_africa_priority_member_effects.txt`
- `common/scripted_effects/012_africa_priority_member_character_effects.txt`
- `events/012_africa_priority_member_events.txt`
- `docs/plans/012_africa_plans/012_africa_independence_wave_tag_loading_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_priority_member_provenance_recruitment_fix_2026_07_24.md`

## Helper and call-site map

| Identifier | Scope | Inputs | Outputs and side effects | Call sites |
|---|---|---|---|---|
| `africa_priority_member_has_active_event6_shell_receipt` | Country | Current country | Requires `is_independence_wave_registry_event6_origin = yes` and rejects the ended-origin receipt, which validates the live Event 006 origin flag and liberation-origin value | Seven niche origin triggers and seven niche origin-recording limits |
| `africa_priority_member_is_vanilla_council_carrier` | Country | Current Event 012 package ID | Identifies the nine vanilla package identities that use event-owned council recruitment | Queue helper and hidden recruitment event trigger |
| `africa_priority_member_queue_vanilla_council_recruitment` | Country | Active package ID and completion flag state | Fires `africa_priority_member.1240` only for a vanilla carrier without the completion receipt | `africa_priority_member_register_requested_package` after `africa_priority_member_package_active` is set |
| `africa_priority_member.1240` | Country event | Active Event 012 package, vanilla-carrier package ID, no completion receipt | Idempotently recruits exactly one matching vanilla council, then sets `africa_priority_member_vanilla_council_recruitment_complete` | Fired synchronously by the queue helper |

The seven niche council characters remain owned by their existing Event 006 country-history shell files. The character scripted-effect file no longer contains any `recruit_character` call.

## Provenance behavior

`DOX`, `DSX`, `DUX`, `DYX`, `DZX`, `EMX`, and `EQX` now require the shared live Event 006 receipt before their package-origin predicates can pass.

The same gate flows through `africa_priority_member_has_supported_carrier_identity`, so the promotion survey cannot expose a dormant shell as a roster target.

The same gate also flows through `africa_priority_member_has_valid_origin` and therefore blocks package registration when a shell is only a bare registered original tag.

The nine accepted vanilla carriers remain explicitly eligible from their normal live identities through their existing exact-tag predicates and nonmatching-vanilla carrier roster. Their paths retain the Soviet-origin exclusion.

## Recruitment behavior

After package registration sets `africa_priority_member_package_active`, the queue effect fires hidden event `africa_priority_member.1240` for `SOK`, `MLI`, `COG`, `UGA`, `TIG`, `HAR`, `SUD`, `ZIM`, or `MAD` package identities.

The event's per-character `has_character` guards prevent duplicate recruitment, and the package-level completion flag prevents repeated queueing after the first successful handoff.

The event does not install a leader role or alter politics. Existing ratification helpers continue to perform those effects, so ratification behavior is unchanged.

## Acceptance scenarios

1. A game-start dormant shell cannot pass `africa_priority_member_promotion_survey_is_available` or `africa_priority_member_can_register_package` from original-tag membership alone.
2. An Event 006-created active shell can survey and register on the same original tag after the normal Action 102 and host gates pass.
3. `DYX`, `DZX`, and `EMX` remain dormant and non-actionable while Event 006 has no legitimate creation path for them.
4. Soviet-collapse provenance fails every supported-carrier origin path and the final package-registration gate.
5. Each accepted vanilla carrier can register from its normal live identity and receives exactly one matching institutional council through `africa_priority_member.1240`.
6. Replaying the queue or package-registration recovery does not duplicate a council or change ratification outcomes.
7. No Event 012 effect adds a state, core, owner, controller, subject, faction, or cosmetic tag.

## Validation

Repository source checks confirmed that the seven niche origin predicates and origin-recording limits reference the shared active Event 006 helper, while the nine vanilla origin paths remain ungated by Event 006 provenance and keep their Soviet exclusions.

Repository source checks confirmed that `recruit_character` is absent from both Event 012 scripted-effect files and appears only in the hidden Event 012 event plus the seven existing country-history shell files.

Repository source checks confirmed that `africa_priority_member.1240` has one definition, one queue call, nine package branches, nine matching character IDs, and one completion flag.

The offline Paradox wiki core pages and Character modding page were consulted, together with vanilla `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, and the vanilla hidden synchronous event precedent in `events/006_independence_wave.txt`.

## Remaining risks

The three shell tags remain intentionally unreachable until an Event 006 allocator path is designed outside this task. This is a documented dormant-state outcome, not a fallback.

Live in-game acceptance still needs the parent to exercise one active shell, one dormant shell, one vanilla carrier, and one Soviet-origin exclusion path after the full Event 006 and Action 102 chains are available.
