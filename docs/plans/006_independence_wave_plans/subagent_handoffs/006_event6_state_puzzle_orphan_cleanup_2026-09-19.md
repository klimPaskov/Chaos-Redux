# Event 006 state-puzzle orphan cleanup

Date: 2026-09-19.

Disposition: implemented bounded runtime cleanup; no gameplay, consumer, identity, or package-admission changes.

The FORM-12 and FORM-13 state-puzzle consumers were rebound from the superseded state 256 to the installed-map state 833. The current manifests, GFX registry, grouped GUI, scripted GUI, scripted localisation, and localisation contain no state-256 consumer. A focused repository search confirmed that no current runtime surface names either `independence_wave_form12_state_256` or `independence_wave_form13_state_256`.

The following four tracked runtime DDS files were stale generated artifacts and were removed:

- `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_256_unresolved.dds`
- `gfx/interface/formables/state_puzzles/006_form12_state_puzzle/states/independence_wave_form12_state_256_qualifying.dds`
- `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_256_unresolved.dds`
- `gfx/interface/formables/state_puzzles/006_form13_state_puzzle/states/independence_wave_form13_state_256_qualifying.dds`

No current source or processed PNG package for those state-256 files remains under `docs/formables/state_puzzles/`, and no accepted manifest row names them. The accepted state-puzzle runtime set is therefore the 100 manifest-attested unresolved/qualifying pieces across the 14 active Event 006 formable families. The repaired state-puzzle source PNGs remain explicitly runtime-recovered evidence rather than original authored masters.

The cleanup does not promote any formable identity, widen the accepted state set, add a fallback, or alter the fail-closed FORM-12/FORM-13 admission rules. It only removes files that had no live consumer and could be mistaken for active runtime art.

## Validation

The focused consumer search found zero remaining state-256 references in `interface/`, `common/scripted_guis/`, `common/scripted_localisation/`, `localisation/`, or Event 006 formable consumers. The active FORM-12 and FORM-13 manifests continue to cover five states each (`249`, `397`, `399`, `651`, and `833`) with unresolved and qualifying variants. The four deleted files were previously reviewed in the state-puzzle asset audit and had valid 21x22 DDS geometry, but were not part of any accepted consumer.

No live Hearts of Iron IV launch, save/load proof, or dynamic GUI claim is made. ASSET-039 and ASSET-046 remain open for dynamic Statehood Ledger behavior, formable identity, and reachability gates.
