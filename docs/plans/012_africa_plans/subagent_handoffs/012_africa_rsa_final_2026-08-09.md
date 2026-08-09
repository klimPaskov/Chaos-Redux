# Event 012 RSA Allied-route final acceptance handoff

Date: 2026-08-09

Scope owner: `/root/event12_rsa_final`

## Acceptance result

The South Africa Allied-route entry now suppresses the generic first-contact popup when the dedicated RSA civil-war gate succeeds. The ordinary delayed first-contact path remains unchanged for every other initialized host and for RSA cases that fail the final Allied-route gate.

The optional Republican Nationalist side is implemented with the existing `ESX` (IW-123 Xhosa) carrier. `EQX` is never consumed. ESX is instantiated only when pre-war neutrality support reaches the documented high anti-war threshold (`constant:africa_rsa_pressure.high_anti_war = 60`) and a dynamic state scan finds a legal current SAF heartland. No new country tag, fallback state, fixed ESX anchor, or Event 006 package state is added.

## Changed files and identifiers

- `common/scripted_effects/012_africa_effects.txt`
  - Guards the delayed `chaosx.nr12.2` scheduling with `NOT = { africa_rsa_allied_branch_can_start = yes }`.
  - This file also contains concurrent Event 019 provider work from another owner; only the first-contact guard hunk belongs to this handoff.
- `common/script_constants/012_africa_rsa_constants.txt`
  - Adds the anti-war threshold, Republican/restored popularity values, Republican AI target and inverse cleanup value, and separate-settlement AI weight.
- `common/scripted_triggers/012_africa_rsa_triggers.txt`
  - Adds `africa_rsa_republican_breakaway_can_start` and `africa_rsa_republican_breakaway_is_active`.
- `common/scripted_effects/012_africa_rsa_effects.txt`
  - Snapshots one candidate state from current SAF-owned/controlled African SAF cores, excluding capital, naval-port states, ESX, and the reserved EQX anchor.
  - Adds `africa_rsa_initialize_republican_breakaway`, pairwise `africa_rsa_settle_republican_breakaway`, and `africa_rsa_republican_breakaway_cleanup`.
  - Removes the branch-only prepare-for-war and antagonize strategy entries before either principal settlement clears the coalition and Allied event targets.
  - Releases only the saved state to ESX, sets the branch cosmetic identity, creates one named male Xhosa king/paramount-chief leader (`King Mgolombane Sandile`), assigns independent AI hostility, and issues separate war declarations when legal.
  - Cleanup restores ESX to its normal Xhosa cosmetic/political identity, retires only the branch-created king/paramount-chief leader, and clears all branch targets/flags while retaining the legitimate ESX core.
- `common/on_actions/012_africa_rsa_on_actions.txt`
  - Cleans the branch when ESX capitulates without altering the principal civil-war settlement bridge.
- `events/012_africa_rsa.txt`
  - Calls the optional branch from the civil-war start effect.
  - Adds explicit separate-recognition options to coalition and loyalist settlement events, with principal settlement cleanup preserved.
  - Adds `chaosx.nr12.1210` branch notice.
- `common/countries/012_africa_cosmetic.txt`
  - Registers branch-only `AFRICA_RSA_REPUBLICAN_NATIONALIST` cosmetic identity.
- `localisation/english/012_africa_rsa_l_english.yml`
  - Adds branch country names, event text, options, and tooltips.

## Runtime behavior

1. `africa_rsa_snapshot_prewar_context` clears stale targets, records pre-war party support, and scans current SAF-owned/controlled African SAF-core states. The first qualifying state in deterministic engine order is saved as `africa_rsa_republican_state`; if none qualifies, the optional side fails closed.
2. `africa_rsa_start_allied_civil_war` runs the existing two-principal-side split, then calls `africa_rsa_initialize_republican_breakaway`.
3. The optional gate requires neutrality support `>= 60`, absent ESX, a saved state, no EQX core/owner overlap, and current ownership/control by one of the two principal RSA sides. The saved state is the only territory eligible for ESX.
4. ESX receives the saved state core, is released by the current state owner, is explicitly assigned state owner/controller and capital, and receives the direct branch cosmetic identity. It is not added to either faction and does not inherit a scripted intervention ledger entry.
5. ESX attempts independent `annex_everything` wars against the Continental Coalition and Allied Union Government only when `can_declare_war_on` permits them. War flags identify each relation independently; no automatic continental alliance is created.
6. Coalition victory offers the separate-recognition option alongside the normal Cape choices; the recognition option performs a closed-ports principal settlement and then a separate ESX white peace/truce. Loyalist victory offers a separate-truce option alongside suppression; that option performs loyalist suppression and then the ESX white peace/truce.
7. If the principal winner does not recognise ESX, the branch remains independent and can continue its own war. ESX capitulation invokes cleanup through `on_capitulation`.
8. Cleanup drops only the branch cosmetic, resets ESX to neutrality with the ordinary Xhosa name, retires the branch-created king/paramount-chief leader, clears branch flags/targets, and leaves the ESX core available as a normal Xhosa core.
9. Principal settlement cleanup subtracts the branch-only AI strategy entries while the two principal event targets still exist, preventing stale hostility after the RSA crisis closes.

## Map/state evidence

Mandatory `hoi4.map_inspect` was run for states `275, 541, 681, 719, 893, 894, 895`.

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f3b5bfab1abf8da3dbf9d65a5a3fb85a8806aa9a15205692f5af40242469afaf/ba2a4caf58cafe4d4a180cbb18bdd4c8a2e1723ca8eb374e12980fe447d52575/map-inspect.f8392b6591b771c7.json`
- State/region membership, province geometry, networks, adjacencies, supply, and rail checks passed for the inspected request.
- The installed map still reports unrelated global diagnostics for invalid building positions and floating-harbor locators in `mod:map/buildings.txt`; no RSA state rewrite was made.
- Vanilla state review confirms 275 Transvaal (capital), 681 Cape Town port, 719 Natal port, and non-port South African core candidates among 541/893/894/895. The candidate scan uses those map properties rather than hardcoding one of these IDs.
- Event 006 catalog/binding review confirms `EQX` is the reserved IW-121 Zulu/Natal carrier and `ESX` is IW-123 Xhosa with no current-map anchor. ESX is therefore used only as this documented branch-only carrier and receives no Event 006 baseline package territory.

## MCP event/focus/probability evidence

- `hoi4.event_inspect` focused lint after the leader, option-key, and AI-cleanup patches: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e34e7b0697ca0e9e65cc17607ece7c1ea757e1653830f88e65d9d6389fce9e9a/1f6eeadfc736431fbf114d6999f9c6075fa62fb046ad06fb9dc63cad34118479/event-lint-0da00e5a91a9.json`; focused source diagnostics reported `blockingDiagnostics: 0`. Workspace-wide helper projection was deferred by the MCP ceiling.
- `hoi4.event_render` post-change options view: artifact manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/39070b00d593c21f8dd16f52beeae12527d85bf980f70edcee7b4ce75d67971c/51cc2061a4bd8212268687a2579ce8041d1205f74a29fd1a51bb90e2b7fc3710/event-options-0da00e5a91a9-manifest.json`; focused render also reported no blocking diagnostics.
- `hoi4.probability_inspect` for `events/012_africa_rsa.txt` and adapter `event_option_ai_chance`: artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/879d461d7fc8726bbbbe1c435ab9ac088c6c75b7fee87229e95b4f2980bf26b7/631f59ca2b74f72a9d86807c271ac29489c8a79734175927f80cb66564eafa4e/probability-inspect-2aa132fa5c9e.json`. The source scan completed with no diagnostics; the adapter reports 16 discovered candidates and an incomplete normalisation pool, as expected for the bounded source scan.
- Baseline probability evaluation was run with scenario set `rsa-third-side`; MCP intentionally withheld normalised probabilities because the candidate pool is incomplete and marked ineligible options/inputs unresolved. The parent probability auditor should run the identical before/after comparison after staging this branch's AI weights.
- `hoi4.focus_inspect` for the preserved vanilla `south_african_focus` (`south_african_focus`) completed. The tree remains untouched; MCP reported existing vanilla icon-reference diagnostics unrelated to this event branch.
- No technology-tree edit is in scope. The installed package exposes no Technology Tree Viewer; that limitation remains unresolved as required by the repository contract.

## Documentation/assets

The Republican Nationalist branch uses the individually archived adult-male portrait `King Mgolombane Sandile` (`GFX_portrait_012_africa_rsa_mgolombane_sandile`) from `gfx/leaders/012_africa/rsa/portrait_012_africa_rsa_mgolombane_sandile.dds`. Source provenance is the Cape Colony Archives Depot image published as [Mgolombane Sandile - Xhosa Chief](https://commons.wikimedia.org/wiki/File:Mgolombane_Sandile_-_Xhosa_Chief.jpg), archived as `docs/assets/portraits/012_africa/source_master_rsa_mgolombane_sandile_archival.jpg` with the source crop and rights note beside it. The image is public-domain in the United States under the archival record, while Commons cautions that reuse terms can vary outside the United States.

This is an explicitly recorded alternate-history casting because no individually attributable archival portrait of the fictional `Archie Velile Sandile` was located. The branch identity, leader name, event text, sprite, and handoff therefore use the documented Xhosa king Mgolombane Sandile consistently; no generic vanilla portrait remains wired for RSA. The cosmetic tag is defined in `common/countries/012_africa_cosmetic.txt` and all player-facing keys are in the RSA localisation file.

## Remaining risks and review points

- The exact candidate state is map-derived and deterministic by engine state iteration order, not a fixed ID. This is deliberate; if no non-capital, non-port SAF core remains at snapshot time, the optional side does not spawn.
- `release = ESX` and the two independent war declarations remain engine-state dependent. The effect validates ESX existence and explicit ownership/control after release; diplomacy rules may still prevent one or both declarations, in which case ESX remains independent and its separate war flag is unset for that relation.
- If a player chooses the normal Cape option or normal loyalist suppression option instead of the explicit ESX settlement option, ESX remains a separate sovereign side until capitulation or a later external peace. This is intentional separate disposition, not automatic faction folding.
- The focused MCP event lint/render had no blocking diagnostics, but the full workspace reports unrelated existing diagnostics and deferred helper projections. No live Hearts of Iron IV session was launched.
- The parent should stage only the first-contact guard hunk from `common/scripted_effects/012_africa_effects.txt`; concurrent Event 019 provider additions in that file belong to their own owner.

## Future extension

The branch can later receive a bespoke ESX focus/decision package once Event 006 provides a legal current-map anchor. That work should preserve this fail-closed state contract and continue to avoid consuming EQX or inventing a fallback state.
