# Event 006 country-registry trigger merge

Date: 2026-08-26

Status: source-layout complete; executable behavior intentionally unchanged.

## Scope

The clean `common/scripted_triggers/006_independence_wave_country_registry_triggers.txt` registry is now folded into `common/scripted_triggers/006_independence_wave_package_triggers.txt` under the source marker `006_independence_wave_country_registry_triggers.txt`.

The moved section contains the exact Event 006 origin, Soviet-origin, Africa-origin, X-tag, registered-reuse, resolved-carrier, Africa-overlap, and Africa-carrier predicates. No file-scoped constants, namespace declarations, or callback keys were present in the removed file.

## Preservation evidence

The removed source contained 22 top-level scripted-trigger identifiers. The merged receiver contains all 22 moved identifiers, with no missing moved identifier and no duplicate top-level identifier across the receiver.

The moved identifier inventory hash is `fee2f3e43954f8bea3357dedfa44896b972a076fad827387e5da3da9c74ba867` before and after the merge.

The receiver plus the removed source measured 20,333 UTF-8 source bytes before the merge and 19,918 bytes after the merge in the working tree, saving 415 bytes after the redundant standalone banner was condensed.

## Documentation alignment

Current registry documentation now points to `common/scripted_triggers/006_independence_wave_package_triggers.txt`. Historical dated handoffs retain their original paths as provenance and are not rewritten.

## Validation boundary

The Event 006 allocator, country API, strict flag-family, FORM-16, GUI semantic, and SCN-008 static validators are run after this source-layout change. A bounded read-only Event MCP inspect/render pass is refreshed for `chaosx.nr6.1`.

The refresh returned `EVENT_INSPECTED_PARTIAL` and `EVENT_RENDERED_PARTIAL`, both with zero blocking diagnostics, at revision `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9`. The state render produced the source-linked manifest `event-state-744cd12bca3e-manifest.json`, JSON, SVG, PNG, and HTML artifacts. The MCP workspace-wide helper/lifecycle analysis remained deferred, so this is not a live parser or runtime claim.

This handoff does not claim live parser loading, save/load behavior, tooltip observation, or runtime callback execution. Package admission, allocation, origin separation, decisions, effects, AI, focus, localisation, assets, and the 32/29/40/161 boundary remain unchanged.
