# Event 021 Maximum scenario preflight/commit repair

Status: implemented and queued for live testing; not a final acceptance certificate.

The owner repair is commit `5616c0fdc` (`Event 021: separate scenario preflight and commit pools`).

## Scope

The repair closes the distinction between the countries enumerated for a manual scenario and the countries whose immutable opening plans are actually safe to commit.

`event021_parent_scenario_opening_state_preflight_valid` now requires a viable capital for a same-tag topology, a viable non-capital anchor for an ordinary topology, or a complete dormant Event 006 package for the independence route. The absent-type branch keeps the scenario window discoverable before the player confirms a type.

`random_civil_war_trigger_manual_scenario` now records `global.random_civil_war_scenario_preflight_count`, builds `event021_parent_scenario_commit_targets` only from countries carrying `random_civil_war_scenario_plan_frozen`, retains failed rows in `event021_parent_scenario_unavailable_targets`, and records `global.random_civil_war_scenario_plan_eligible_count` plus `global.random_civil_war_scenario_preflight_skipped_count`.

The final requested count is the actual confirmation-time selected set, including the Maximum set and the bounded Low/Medium/High draw. `chaosx.nr21.15` is dispatched only from the frozen commit array, once per row, and the final skipped count remains requested minus committed. No route, package, anchor, or state is rerolled after preparation or ownership mutation.

## Validation evidence

The focused `hoi4.event_inspect` lint for `chaosx.nr21.1` was re-requested after the repair and returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and zero skipped sources. The service returned the cached revision `a8fde3e58546f004e81d855d73d29674ae3c5be8f894a1caf9586621929a6657`, graph hash `c83030c9d67b704f9c6437d31b7e4f5000463e6431ae40865f5b74e4cb15af21`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c997681a50d0bce34b26abe5dbdb93a06e7a94f7b7d562bd98520a33fe9148dc/7f4b00d90b44bb764d1fc432af2ea4ea60cfe9846414c18977af80e06656c586/event-lint-a8fde3e58546.json`.

The lint validation is partial because the large workspace defers helper and lifecycle projections; the receipt is structural evidence only and is not treated as a current full-source certificate.

The post-repair `hoi4_probability_inspect` request for `event021_parent_add_scenario_target_to_weighted_pool` with adapter `custom_weighted_pool` returned `PROBABILITY_SOURCE_DISCOVERED`, zero custom candidates, eight unrelated `random_list` examples, and `identifier_not_found`. Its current source revision was `f1c5a5762267a56e1463916c8fa79bf0bbf550e93eb2967affe9b1ce46daf844`, source hash `ad8a7b354b2de007480c42e18e97d9921f139ba2040212725b770bce546d564c`, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6e50a0c8bae8e19e5e66c218212517bd42679ec07dc367e432f28f9eddc963e1/afccda9641fb5180147c2db9d10452ddf58d96a60c3754c3bca04b3fdc98c9af/probability-inspect-ad8a7b354b2d.json`.

The direct adapter cannot expose Event 021's runtime country enumeration or the new two-array commit boundary, so this is a discovery receipt rather than a numeric Maximum distribution certificate. The mandatory independent before/after probability comparison and live scenario evidence remain open.

## Current source hashes

| Source | SHA-256 |
| --- | --- |
| `common/scripted_effects/021_random_civil_war_parent_effects.txt` | `DEE57540972EC329D61CB529476E40DB84EB9CA703136F92F36C9FB4A5C62E9A` |
| `common/scripted_triggers/021_random_civil_war_parent_triggers.txt` | `9AFBE2B87B4B16E60CA03F7FBBA44F3DBE968C8F994707FCBA716CE5A868E3F6` |
| `common/scripted_effects/021_random_civil_war_parent_effects.md` | `64553E88D7DC7F378431D6BC8382958EB43173CB34DC9BD555A72EDBF8AAF7FF` |
| `docs/events/021_random_civil_war/overview.md` | `0AC5141ECF523DF9A6F9D22C814D9ECC530FDCC12159D6BD560B05B26B611550` |
| `docs/events/021_random_civil_war/acceptance_evidence.md` | `B1C103087148575D6FF345A070BD08F668BBF7026CEA221C9C57ED0919996FDA` |

## Remaining gate

This repair does not claim that every frozen plan will commit in a live save. The user must exercise SCN-018 Maximum and the Low/Medium/High scenarios, record preflight/plan/commit/skipped counts, test actual nonhuman exclusion and one-state/all-island same-tag handling, and measure whether immediate setup stalls before any seven-day batching decision is made.
