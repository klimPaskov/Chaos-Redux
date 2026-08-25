# Event 006 compact decision-registry merge

Date: 2026-08-25.

Owner: `/root`.

Status: source-layout cleanup complete; no gameplay design change.

## Scope

The regional trigger/effect registries already combined the Rhineland/Bavaria/Saar and Bashkiria/Mari package blocks, but the matching decision categories remained in four parser files. This tranche combines only those same-ownership decision files.

## Receivers

- `common/decisions/006_independence_wave_rhineland_bavaria_saar_decisions.txt`
- `common/decisions/006_independence_wave_bashkiria_mari_decisions.txt`

## Removed parser files

- `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt`
- `common/decisions/006_independence_wave_saar_decisions.txt`
- `common/decisions/006_independence_wave_bashkiria_decisions.txt`
- `common/decisions/006_independence_wave_mari_decisions.txt`

## Preservation evidence

The Rhineland/Bavaria/Saar receiver contains three category identifiers and 42 unique one-tab decision identifiers. The Bashkiria/Mari receiver contains two category identifiers and 22 unique one-tab decision identifiers. No decision identifier collides within either receiver, and both files have balanced braces at 772/772 and 495/495 respectively.

After removing comments, blank lines, and file-local constant declarations for comparison, each receiver's executable sequence is identical to the concatenation of its two former source files. Constants were collected once at the receiver header; all package-local category keys, costs, timers, triggers, effects, cancellation, cleanup, and AI blocks remain unchanged.

The four former files total 122,668 bytes and the two compact receivers total 122,138 bytes, saving 530 source bytes while removing two parser files from the load surface.

## Validation

Read-only source checks confirmed category and decision uniqueness, balanced braces, and normalized executable equivalence. The maintained Event 006 allocator, country API, scenario-matrix, strict flag, formable, and GUI-matrix audits remain the relevant static follow-up checks; this source-layout merge does not widen package admission or claim live gameplay validation.

## Remaining risks

The whole Event 006 completion boundary remains **HOLD / PARTIAL**. Runtime decision/mission inspection, typed probability evidence, package admission, GUI evidence, asset rights, and live scenario receipts remain separate concerns.
