# Necessary Ground case-card manifest

## Runtime contract

- Native size: `300x96`.
- Format: legacy DDS, one level, uncompressed BGRA8, fully opaque.
- Runtime folder: `gfx/interface/015_utopia_manifesto/ledger/`.
- GUI position: `x = 8`, `y = 4` in `utopia_ledger_ground_panel`.
- Composition: calm dark field across the left and centre; authored state
  pictogram and border treatment on the right.
- Text policy: source and runtime artwork contain no readable text, letters,
  numerals, labels, signatures, or pseudo-writing. Live localisation remains
  separate GUI text.

## Accepted states

| State | Visual read | Stable runtime stem | Runtime SHA-256 |
|---|---|---|---|
| No target selected | Vacant shield docket and inactive brass register | `utopia_ledger_case_no_target` | `b1dfd0c309df27d83eb7eedd4e3fbab3552b78107ee281ffcd22f24befe32eda` |
| Target eligible | Pristine candidate dossier, open clasp, compass and laurel | `utopia_ledger_case_target_eligible` | `2f3f083810f03d9a53991b5e571fae3b37f6e119158f3ea5ee9c9c6e69ae5415` |
| Target selected | Single bright selected dossier, intact amber seal and compass | `utopia_ledger_case_target_selected` | `34aad86e1f758bc0423bd0e659eccf04acf54f6c624b153f85b10ff8cfc7c371` |
| Offer pending | Blank charter packet, dispatch tube and running sandglass | `utopia_ledger_case_offer_pending` | `40d09c6648efac69d58d1569ee71082a40ee9b491267df712c49467a096f6075` |
| Counteroffer | Two opposed dockets joined by exchange ribbons and balance hinge | `utopia_ledger_case_counteroffer` | `115fc808d5f6c092403d3472a9a6162df8d29db0a12be5a74a3622c725b16302` |
| Refusal | Cross-latched dossier and cracked oxblood seal | `utopia_ledger_case_refusal` | `aecfac192ff87f526feed207cabee3119877b3572333bfda862691f268c5919b` |
| Ultimatum available | Sealed demand, nearly spent sandglass, civic gavel and red-gold frame | `utopia_ledger_case_ultimatum_available` | `18e376f0ed725ef951cde4057e01c9562b81979cf2eb4705662c4c5eac75d214` |
| Case expired | Brittle curled file, stopped sandglass and cold slate seal | `utopia_ledger_case_expired` | `049af0a95c6229672ee0949c26ac29bfdfd535861c1e8a5971dbbd4f7c2d31a5` |
| Stewardship active | Open ledger, civic keys, dividers and teal stewardship seal | `utopia_ledger_case_stewardship_active` | `d896d25fb308c6982802dba8806223f14eed2873f03c7b9add63bad36d3ac61e` |
| Associate established | Linked civic seals, joined institutions and completed teal ribbon | `utopia_ledger_case_associate_established` | `fb5f116af9e9050303f9bf6f514be44d39d00e6acc26dc6ddc50c5e90217fffc` |

Each stem maps one-to-one across:

- `sources/<stem>_source.png`
- `processed_png/<stem>.png`
- `decoded_png/<stem>.png`
- `gfx/interface/015_utopia_manifesto/ledger/<stem>.dds`
- `GFX_<stem>`

The full binary inventory is frozen in
`metadata/binary_checksums.sha256`. No placeholder, borrowed icon, reused
state master, or external stock asset is present in the accepted set.

