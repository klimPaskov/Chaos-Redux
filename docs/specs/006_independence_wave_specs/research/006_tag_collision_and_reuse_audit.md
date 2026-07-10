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

## Benin and Biafra separation

`BIA` remains assigned only to `IW-107`, the Biafran regional package. `IW-096`, the Edo Kingdom of Benin, uses the new Event 6 tag `DRX`. These are distinct identities and must not share one country tag. Their overlap is handled by `RG-NIGERIA-COARSE`, which permits only one automatic package from the coarse Nigeria state group unless the installed map provides distinct substates.

## Event 5 overlap

Registered tags in the former Soviet and imperial Russian regions may also appear through Event 5. Event 6 never reads Event 5 crisis membership from the tag alone. It sets Event 6 origin, package ID, wave ID, overlay, and route flags before content assignment. Event 5 does the equivalent with its own origin. A tag can therefore use different focus, decision, AI, league, and formable content depending on release origin.

Current Event 5 custom tags such as `OGB`, `IUL`, `MRC`, `FEV`, `SZA`, `UWD`, and the other Event 5 successors remain separate. Event 6 does not reuse those custom identities unless a future accepted package explicitly maps one and preserves origin separation.

## Implementation recheck

Before creating any country file, the implementation agent must run a repository-wide and installed-game collision scan. If a reserved `X` tag has become occupied after this audit, assign another unused `??X` tag, update every Event 6 matrix and asset filename, and record the change. This is a version-binding check, not an unresolved research question.
