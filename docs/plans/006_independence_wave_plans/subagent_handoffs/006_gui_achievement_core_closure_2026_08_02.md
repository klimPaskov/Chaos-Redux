# Event 006 GUI and achievement core-surface closure audit

Date: 2026-08-02

Mode: source/static audit. No game launch, live GUI observation, save/load
test, package admission, asset promotion, or workbook status change was used.

## Result

The previously recorded Statehood Ledger and league-expulsion gaps are closed
at source level. The remaining boundary is focused presentation evidence that
can only be observed in the running game; live testing is outside the current
user-approved scope. This handoff supersedes the older audit wording that
called the expulsion disqualifier writerless.

## Statehood Ledger evidence

| Surface | Source evidence | Result |
|---|---|---|
| Category registration | `common/decisions/categories/006_independence_wave_categories.txt` exposes `independence_wave_status_scripted_gui` on the founding category | PASS |
| Window contract | `interface/006_independence_wave.gui` defines the 700x500 `independence_wave_status_window`, five value rows, host/patron/network/phase/mission panels, five tabs, refresh, and animation toggle | PASS |
| Visibility | `common/scripted_guis/006_independence_wave_scripted_gui.txt` requires `is_independence_wave_active_country = yes`; AI is disabled | PASS |
| Refresh | `independence_wave_status_refresh_click` calls `independence_wave_refresh_country_state`, which recomputes values, phase, and frame variables | PASS |
| Tab exclusivity | Each tab effect clears the other four tab flags; the government panel is the default when none is selected | PASS |
| Threshold frames | `independence_wave_refresh_status_frame_state` maps recognition bands, patron warning/severe instability, league phases, and formable discovery/integration/commitment to explicit frame enums | PASS |
| Animation fallback | Static state-strip sprites are visible when `independence_wave_status_gui_show_animation` is absent; authored frame-by-frame siblings are visible only when the flag is present | PASS |
| Cleanup | `independence_wave_reset_country_state` clears the tab and animation flags and the generation-local frame variables | PASS |
| Localisation | `localisation/english/006_independence_wave_gui_l_english.yml` covers title, values, host, patron, network, phase, mission, tabs, panels, and click tooltips | PASS |

No focus or GUI MCP artifact is claimed. The source contract is complete and
the remaining runtime presentation check is explicitly optional under the
current scope.

## Achievement matrix evidence

`docs/specs/006_independence_wave_specs/matrices/006_achievement_matrix.csv`
contains sixteen accepted IDs. `common/achievements/chaos_redux_achievements.txt`
defines all sixteen IDs, each with one exact `happened` trigger and the matrix's
visible/hidden disposition. The English achievement localisation contains the
matching names, descriptions, condition tooltips, and eligibility text.

The runtime icon audit remains 48 of 48 64x64 DDS files (complete, grey, and
not-eligible states for every ID). The proof chain remains bounded to origin,
host, league-member, patron, formable, and SCN-008 arrays; no whole-world
achievement scan is used.

The formerly open league-arbitration disqualifier now has a real writer:
`independence_wave_achievement_record_member_expulsion` sets
`independence_wave_achievement_member_expulsion_during_term` for the current
league leader, and `independence_wave_decision_resolve_charter_expulsion_vote`
calls it only after the charter vote revalidates the leader and target. The
same decision calls `independence_wave_expel_league_member`, applies concrete
cohesion/common-cause/patron/reserve/confidence costs, records the vote date,
and enters league crisis. A new leadership term clears the marker, so the
achievement can be earned in a later clean term.

The three factual ground writers remain `DM-60`'s recorded-ground path,
`DM-61` sponsored coup, and the rescue-abandonment/arbitration-refusal writers
in the existing decision surface. A stale member or lost leader cannot expel
anyone because both the decision and resolution effect recheck authority,
target validity, and active league phase.

## Remaining limitations

- No live GUI click/threshold/save-load observation is claimed, by user decision.
- Package admission, formable family readiness, 6001 rights/runtime, and asset
  provenance gates remain separate whole-event blockers.
- This audit does not promote IW-030, IW-043, IW-058, IW-093, or any other
  unadmitted package.

## Validation

- Matrix-to-definition count: 16/16.
- Matrix-to-final-trigger count: 16/16.
- Hidden disposition matches the four accepted hidden IDs.
- Icon triplets: 48/48 DDS files at 64x64.
- `independence_wave_achievement_member_expulsion_during_term` has a reset,
  active-term check, and a concrete expulsion writer.
- Statehood Ledger has one scripted GUI registration, five mutually exclusive
  tabs, four animated/static state-strip pairs, and a refresh path.

No gameplay fallback or shallow substitute was introduced.
