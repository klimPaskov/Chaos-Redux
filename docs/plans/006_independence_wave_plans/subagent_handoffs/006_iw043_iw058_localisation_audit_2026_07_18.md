# IW-043 / IW-058 localisation audit handoff

Date: 2026-07-18
Scope: Middle Volga / CHU (IW-043) and Assyria / ASY (IW-058) player-facing English localisation only.

## Documentation reconciliation note (2026-07-18)

This earlier localisation audit remains evidence for wording and key coverage.
Its fail-closed descriptions for FORM-12/13/18 capture the pre-promotion
state and are superseded by the exact CHU/ASY transaction attestation. Current
player-facing text should describe the paid 180-day consent congresses and
staged sovereignty-preserving integration; the final localisation audit is the
current key/encoding authority. Do not reopen the old missing-writer task.

## Changed files and keys

- `localisation/english/006_independence_wave_achievements_l_english.yml`
  - Removed implementation/package references from the Event 6 achievement eligibility and condition tooltips: `independence_wave_achievement_eligible_tooltip`, `independence_wave_achievement_one_state_to_statehood_tooltip`, `independence_wave_achievement_no_master_tooltip`, `independence_wave_achievement_found_league_tooltip`, `independence_wave_achievement_regional_formable_tooltip`, `independence_wave_achievement_small_to_major_tooltip`, `independence_wave_achievement_radical_bloc_tooltip`, and `independence_wave_achievement_every_flag_survival_tooltip`.
  - Reworded the CHU and ASY achievement descriptions/tooltips: `chaosx_006_volga_bulgaria_DESC`, `independence_wave_achievement_volga_bulgaria_tooltip`, `independence_wave_achievement_assyria_survives_tooltip`, and `independence_wave_achievement_host_remnant_tooltip`.
  - Hidden status for `chaosx_006_volga_bulgaria` and `chaosx_006_assyria_survives` was not changed.
- `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml`
  - Added fail-closed wording to `independence_wave_iw043_hold_form12_accession_congress_desc`, `independence_wave_iw043_hold_form13_compact_congress_desc`, and `independence_wave_iw058_hold_form18_federal_congress_desc`.
  - Added target-aware names and descriptions to `independence_wave_iw043_dispatch_volga_trade_delegation`, `independence_wave_iw043_dispatch_volga_trade_delegation_desc`, `independence_wave_iw058_open_diaspora_expert_mission`, `independence_wave_iw058_open_diaspora_expert_mission_desc`, `independence_wave_iw058_request_named_external_guarantee`, and `independence_wave_iw058_request_named_external_guarantee_desc` using the existing targeted-decision `FROM` scope.
  - Replaced implementation wording in `independence_wave_iw043_reopen_congress_clause_desc` with the actual single-use reconciliation result.
  - Existing custom cost, blocked-cost, and tooltip keys remain intact.
- `localisation/english/006_independence_wave_iw043_iw058_focus_l_english.yml`
  - Removed duplicate title/description definitions for `independence_wave_iw043_repair_cheboksary_workshops` and `independence_wave_iw058_fortify_mountain_river_corridor`; the decision localisation is now the single definition for those shared ids, while focus-specific `_tt` keys remain.
  - Repaired punctuation and player-facing wording in the Cheboksary, Bolgar memory, Muftiate, civilian-law, concordat, civic-assembly, and civilian-command focus tooltips/descriptions.

No advisor package, portrait, icon, sprite, dossier, or other asset localisation was added. The eight IW-043/IW-058 institutional character definitions were audited separately and all are male; this change does not alter character data.

## Audit results

### Missing keys

None found in the exact IW-043/IW-058 surfaces. A candidate-key scan over the scoped decisions, events, focuses, scripted localisation, scripted triggers/effects, and achievements resolved all actual localisation ids. The only non-resolving tokens were `Assyrian`/`Middle` text fragments and `Get...` scripted-localisation function names, not localisation keys.

### Duplicate keys

No duplicate keys remain inside the six scoped English files after the focus/decision shared-id cleanup. The removed duplicate pairs were `independence_wave_iw043_repair_cheboksary_workshops`/`_desc` and `independence_wave_iw058_fortify_mountain_river_corridor`/`_desc`. The engine now gets one title/description for each reused decision/focus id.

### Scripted localisation issues

No broken scripted-localisation reference was found. Event 5805 and Event 5807 already use their saved event-target scopes in dynamic text (`independence_wave_iw058_diaspora_partner` and `independence_wave_iw058_named_external_guarantee_target`). Category values already use dynamic variables for authority, rights, river control, cohesion, guarantees, corridor security, credibility, and church/secular balance.

### Dynamic text opportunities

- Fixed the highest-value opportunities on the three targeted decisions by naming `[FROM.GetNameDef]` in the title and description. This matches existing vanilla/Chaos Redux targeted-decision patterns and the `targets`/`FROM` source contract.
- The former-host transit decision stores `var:independence_wave_former_host` and still uses a generic "former host" title/description. A future UI pass could add `[?independence_wave_former_host.GetNameDef]` if the decision-card scope is confirmed safe in live UI; no risky change was made here.
- Event 5805/5807 dynamic target names are already correct and need no patch.

### Cross-surface mismatch notes

- Shared focus/decision ids are now intentionally defined only in decision localisation; the focus `_tt` keys remain focus-specific.
- FORM12, FORM13, and FORM18 remain fail-closed because the source gates require unattested adapter flags. Their descriptions now tell the player that the member roll is not complete and that the congress is closed; no route was unhidden or promoted.
- Gameplay follow-up: the success branches of `independence_wave_iw043_reopen_congress_clause` and `independence_wave_iw058_reopen_community_guarantee` appear not to call their matching `*_commit_paid_transaction` effects, even though resources are removed at start. This may leave each transaction-active receipt uncleared after a successful reconciliation. It is outside this localisation patch; the owning gameplay agent should verify both ledger cleanups before treating the new cost wording as final.
- The broader scenario localisation file still contains internal SCN-008/package terminology, but it is outside the exact IW-043/IW-058 localisation surface and was not rewritten in this bounded pass. Parent should decide separately whether that generic scenario UI is in scope.
- No wording was added for missing mechanics, and no route lore or character identity was invented.

### File encoding concerns

All six scoped English localisation files are UTF-8 with BOM after the edits. No non-BOM encoding change was introduced.

### Recommended follow-ups

1. Keep the three FORM12/13/18 adapter gates fail-closed until the owning gameplay pass provides a real attestation writer and member-roll provenance.
2. If the parent confirms that generic SCN-008 launch/summary screens are part of this feature surface, perform a separate scenario-localisation pass rather than mixing those keys into this handoff.
3. Optionally validate the former-host dynamic variable scope in a read-only decision UI render before changing `independence_wave_iw043_negotiate_former_host_transit` to show the host's current name.

## Validation performed

- Scanned the six scoped localisation files for duplicate ids, with `l_english` headers excluded.
- Verified UTF-8 BOM bytes on all six files.
- Scanned for player-facing em dashes, semicolon-heavy wording, internal package labels, and advisor/asset terms in the exact surface.
- Cross-checked direct decision/event/focus/achievement references against the English localisation corpus and inspected the target-decision `FROM` blocks in `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`.

Skipped: no game/UI render was run because the requested work is a text-only audit and the parent did not request an in-game render. No gameplay files, scripted localisation definitions, assets, or hidden achievement flags were changed.

Remaining uncertainty: the former-host decision's `[?independence_wave_former_host.GetNameDef]` card scope was not exercised in a live UI render. The generic scenario-file terminology and the gameplay-level formation provenance gap remain outside this localisation patch.
