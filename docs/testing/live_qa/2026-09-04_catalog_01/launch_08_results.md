# Launch 08 startup verification

The game passed the former native crash point and remained responsive through later script and flag loading.
Startup acceptance remains incomplete because fresh mod errors are still present; no visual main-menu or campaign-map pass is claimed.

Launch used the unchanged approved desktop shortcut on 2026-09-05 at 10:30:13 Europe/Kiev, recorded PID 31608.
The parent stopped only that verified HOI4 process after the fresh error gate failed and archived the current logs under `logs/launch_08/logs/`.
The newest crash directory remained `hoi4_20260905_095120`; no new crash directory appeared during this attempt.
No campaign or save was entered, and no desktop control or media capture was performed.

## Targeted error comparison

These are occurrences of the listed diagnostic patterns, not unique defects or a complete count of all startup issues.

| Diagnostic family | Launch 07 | Launch 08 |
| --- | ---: | ---: |
| Containment unsupported arguments | 56 | 0 |
| Unsupported country flag clearing | 888 | 0 |
| Idea modifier malformed constant values | 13 | 0 |
| Event 024 digit-leading traits | 6 | 0 |
| Doctrine mastery amount constant | 214 | 0 |
| Doctrine index effect | 214 | 214 |
| Unsupported timed-country-flag effect | 28 | 5 |

The archived launch 08 error log contains 4,598 lines and 765,041 bytes.
SHA-256: `bf366cb28a644961fa7aa433fa04946e3b42746142e71715036cd34e19a5f967`.
The archived launch 07 error log contains 7,559 lines.

The containment parameter repair, supported effect-name corrections, Event 024 wrappers/traits, and idea numeric aliases cleared their targeted diagnostics.
The mastery amount repair cleared its malformed constant tokens, while all 214 index diagnostics persisted.
This disproves the earlier interpretation that the index diagnostics were merely amount-token cascades; exact mastery targeting remains under investigation without removing its selector.

## Remaining work

Fresh errors include unsupported temporary cleanup, missing helper references, malformed static constants, invalid triggers, doctrine index fields, missing country histories and flags, and repression helper parameter cascades.
Read the current repair ledger and bounded handoffs for source changes applied after this launch; those changes are not validated by this earlier log.
The Event 021 MTTH correction requires native parser confirmation; probability comparison was attempted but the installed adapter returned `PROBABILITY_SURFACE_EMPTY` for reusable MTTH entries.

Catalog/system live testing, save/reload tests, feature-only teaser screenshots, recordings of all custom 3D units, and mechanics-guide media remain pending clean startup.
The full user goal remains active and incomplete.
No feature was substituted or redesigned in this verification attempt.
