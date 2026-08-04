# Fallout manual province sweep proof

Date: 2026-08-04

Status: active installed-map sweep with static engine-surface proof. Live HOI4 observation is outside the approved goal.

## Outcome

The manual Fallout scenario issues one native thermonuclear strike against every valid installed land province. The pinned target set contains 10,154 unique province ids across 1,081 states. It does not substitute one strike per state, a province modifier, or a variable-only consequence.

The sweep completes all 41 batches, verifies issued calls and observed callbacks, reconciles population and Deaths, waits exactly seven days, then submits the standard Fallout request coordinator. The scenario uses the same blackout and rewrite path as terminal and 100 percent Air Contamination requests.

## Engine-native launch route

Official `effects_documentation.md` defines `launch_nuke` in country scope with `province`, `use_nuke`, and `nuke_type`. Vanilla `common/raids/nuclear_raids.txt` passes a variable province target and uses `thermonuclear_bomb` on its thermonuclear paths.

Every range loop stores its current province id in the temporary variable `fallout_manual_target_province` and calls one meta helper:

```txt
fallout_manual_launch_current_target_province = {
	meta_effect = {
		text = {
			launch_nuke = {
				province = [FALLOUT_MANUAL_TARGET_PROVINCE]
				use_nuke = no
				nuke_type = thermonuclear_bomb
			}
		}
		FALLOUT_MANUAL_TARGET_PROVINCE = "[?fallout_manual_target_province|.0]"
	}
}
```

This produces an engine-native `launch_nuke` block with a concrete province token. No `province = var:fallout_manual_target_province` call remains, and no temporary variable is incorrectly scoped through ROOT or PREV.

## Installed map identity

- Installed Hearts of Iron IV build inspected: 1.19.2.0
- Installed `map/definition.csv` SHA-256: `86846BE71198D6772C651638AA22E3656133198DE9B7C49C6234ED48CF33D87B`
- State-source manifest SHA-256: `9C2B20312B4D774999C55958094C0E8302BDE089BC178999BA7B56FF978C8A8F`
- All assigned state membership SHA-256: `290C400BED83A545556E418D7EF676831625F968D1C97877A6366D30290B39ED`
- Valid land membership SHA-256: `4546CC398C5D4756DF8D8DF097A77E48509CD53D417663A14ECED1EF3899E763`
- Sorted valid province id SHA-256: `A0F5504AEA22EC76D8C687228C9A4BF485B255C2F8CA9E7DB8A62CFB8D259949`
- Chaos Redux map or state overrides found: none

## Target derivation

A target id must be greater than zero, classified as land by `definition.csv`, and assigned by exactly one installed state province block. Static derivation found 10,272 assigned province ids, excluded 118 non-land ids and province zero, and retained 10,154 valid land ids. The set includes 126 land provinces in impassable states because no official rule says `launch_nuke` rejects them.

The canonical proof artifacts are `FALLOUT_MANUAL_VALID_PROVINCE_IDS.txt`, `FALLOUT_MANUAL_PROVINCE_LEDGER.csv`, `FALLOUT_MANUAL_PROVINCE_RANGES.csv`, and `FALLOUT_MANUAL_STATE_SOURCE_MANIFEST.csv`.

## Batch proof

`common/scripted_effects/fallout_consolidated_effects.txt` defines batches 0 through 40. Batches 0 through 39 contain 250 targets and batch 40 contains 154. Their 533 inclusive range loops expand to 10,154 unique ids in canonical order.

The static re-expansion found zero duplicates, missing ids, extra ids, order mismatches, batch-index mismatches, and declared-size mismatches. There is exactly one native `launch_nuke` definition, owned by the meta helper called from every range loop.

## Completion barrier

Events `chaosx.fallout.910` through `.950` map one-to-one to the 41 batch indices. Events `.960` through `.966` are bounded verifier attempts. Every callback stores and revalidates the current manual transaction generation.

The countdown cannot begin until the ledger proves all of the following:

- next batch equals 41
- issued launch calls equal 10,154
- observed `on_nuke_drop` callbacks equal 10,154
- unique struck-state count equals 1,081
- state strike-count sum equals 10,154
- struck-state array size equals 1,081
- no manual sweep error owns the transaction

A failed or partially observed batch is never replayed because some native calls may already have executed. The transaction fails closed instead of duplicating strikes.

## Population and Deaths reconciliation

Each state stores its prestrike population baseline. Native callback effects and the exact Fallout reconciliation are measured together. The reconciliation removes only the remaining amount needed to reach the deterministic 90 through 95 percent loss band, protects a one-person floor, and records the complete observed loss once through Fallout Deaths reason 19 without applying population twice.

## Exact seven-day handoff

The verified barrier stores a start day and an end day equal to the start plus seven. Event `chaosx.fallout.903` is scheduled once with `days = 7`. Its trigger requires `global.num_days` to equal the stored end day, the same host coordinator, transaction generation, and countdown receipt. No daily fallback submits or reschedules the request.

## Scenario identity and consequence boundary

The manual scenario owns raw id 14, one greater than the previous live maximum 13. Existing scenario ids are unchanged. The retired Final Silence row redirects to Fallout compatibility handling and has no independent world-end implementation.

The manual row is a scenario launcher, not an ordinary Event Log entry, evolution, Event Details card, or ordinary super-event. After the seven-day barrier it enters `fallout_request_aftermath`, the same idempotent consequence coordinator used by terminal sources and 100 percent Air Contamination.

## Validation boundary

The user explicitly excluded live HOI4 testing from this goal. Static proof covers the installed-map target set, native effect construction, batch and callback identities, exact completion barrier, population reconciliation, and seven-day request handoff. Runtime performance and presentation remain user-owned campaign validation and do not disable the source path.
