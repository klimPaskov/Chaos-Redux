# Event 6 tag collision and reuse audit

Audit date: 2026-07-10

## Baselines

The audit compared the 206 candidate packages against:

- the public Hearts of Iron IV country tag index available on 2026-07-10
- the current Chaos Redux registry at repository commit `8044d232376fef3a1a3ca1ea3e0d487523924cc6`
- the Event 5 Soviet Collapse package and its custom tags

The public index is a discovery baseline, not the final engine authority. The implementation pass must still scan the installed game's `common/country_tags` files, all mod tag files, cosmetic tags, formable tags, and route tags.

## Outcome

- Packages reusing a registered tag: **78**
- Packages reserving a new Event 6 `X` tag: **128**
- Duplicate new Event 6 tags: **0**
- New Event 6 tags that do not end in `X`: **0**
- Collisions with the public baseline's known `X`-ending tags `LUX`, `MEX`, `SHX`, and `SAX`: **0**
- Collisions with current Chaos Redux custom tags: **0**

The binding result is in `research/006_package_research_resolution.csv` and the expanded candidate registry.

## Installed-registry reconciliation, 2026-07-14

The reserved and reused tags were scanned again against the installed game and current mod checkout:

- all **78** reused tags are registered.
- all **128** reserved new Event 6 tags remain unique and end in `X`.
- collisions between the 128 reserved tags and the installed or mod country-tag registries: **0**.
- collisions between the 128 reserved tags and current three-character cosmetic-tag keys: **0**.
- parsed installed and mod country-tag registry: **487** three-character tags.
- parsed current cosmetic-tag surface: **9** three-character keys.

This closes the implementation-time collision placeholder for the 2026-07-14 snapshot. It does not register the 128 tags and does not replace the package identity review required when content is assigned.

## Benin and Biafra separation

`BIA` remains assigned only to `IW-107`, the Biafran regional package. `IW-096`, the Edo Kingdom of Benin, uses the new Event 6 tag `DRX`. These are distinct identities and must not share one country tag. Their overlap is handled by `RG-NIGERIA-COARSE`, which permits only one automatic package from the coarse Nigeria state group unless the installed map provides distinct substates.

## Event 5 overlap

Registered tags in the former Soviet and imperial Russian regions may also appear through Event 5. Event 6 never reads Event 5 crisis membership from the tag alone. It sets Event 6 origin, package ID, wave ID, overlay, and route flags before content assignment. Event 5 does the equivalent with its own origin. A tag can therefore use different focus, decision, AI, league, and formable content depending on release origin.

Current Event 5 custom tags such as `OGB`, `IUL`, `MRC`, `FEV`, `SZA`, `UWD`, and the other Event 5 successors remain separate. Event 6 does not reuse those custom identities unless a future accepted package explicitly maps one and preserves origin separation.

## Future-change recheck

Repeat the repository-wide and installed-game collision scan if the installed build, country-tag registries, or cosmetic-tag registries change after 2026-07-14. If a reserved `X` tag becomes occupied, stop and reconcile the accepted package binding across every Event 6 matrix and asset filename before registration. Do not silently rename a tag in one implementation file.
