# IW-093 Asante and IW-098 Sokoto packages

## What they are

The two West African signature packages of Event 006. Asante (`DOX`, anchor state 274 with Kumasi as capital, former host `ENG`) restores the confederacy under the Asantehene Prempeh II. Sokoto (`SOK`, anchor state 902, former host `ENG`) frees the Sultanate and its emirates. Both are admitted to automatic high-chaos waves, Join conversions and SCN-008 launches (agent decision D19, 2026-10-05).

## Setup and validation

- The executor releases the carrier, transfers the anchor and sets it as capital, then runs the package setup in the carrier's scope. Anchor, capital and former-host proofs compare with PREV, the released country, because ROOT is the launching country during the executor passes.
- Leadership: the neutrality government is formed first. DOX promotes Prempeh II. SOK promotes Sultan Hasan dan Mu'azu Ahmadu before 17 June 1938 and the vanilla Siddiq Abubakar III from that date.
- Rosters: Prempeh II, Kwame Frimpong and Kwaku Ntim (DOX) and Hasan dan Mu'azu, Muhammadu Dikko and Bello Rabah (SOK) are recruited in startup history and are never retired by cleanup, so a later release of the tag finds them again.
- Setup then writes the laws, politics, the four package values, the opening idea, the full Event 006 focus framework with the signature module, the formable family profile, the command-roster receipt and the mapped force (`river_jungle` p93 for DOX, `mounted_mobile` p98 for SOK).
- Final validation checks the same receipts, the anchor and host proofs and the date-appropriate leader.

## Sokoto succession

A Sokoto released before 17 June 1938 runs its own hidden check, `chaosx.nr006.9810`, every 14 days. From the cutover it fires `chaosx.nr006.9811` "A New Sultan in Sokoto" once: Hasan dan Mu'azu dies, Siddiq Abubakar III succeeds him and takes the government if Hasan led it, and the date receipts move to the post-cutover branch. The check stores a due date converted with `chaosx_convert_days_to_date_offset`, so a check left over from an earlier release does nothing. No world hook is used.

## Identity and assets

| Surface | Decision |
| --- | --- |
| Prempeh II portrait | The user-supplied HOI4-style final installed on 2026-08-21 from the archived source master, accepted as the final portrait |
| Hasan dan Mu'azu portrait | Source placeholder: an unchanged head-and-shoulders crop of the June 1934 London Zoological Gardens photograph, evidence under `docs/assets/portraits/006_independence_wave/round2_source_placeholders/`, pending a user-supplied styled final |
| Muhammadu Dikko portrait | The user-supplied HOI4-style final installed on 2026-08-21 |
| Frimpong, Ntim and Bello Rabah | Fictional officers of the new armies; their portraits depict no real person |
| DOX flags | The Asante yellow, black and green tricolour with the Golden Stool, shared with Event 012's DOX carrier (commit `da5fd37da`); every ideology and route uses the same flag, with medium and small variants |
| SOK flags | The vanilla Sokoto ideology flags of the vanilla carrier |

## Formables

FORM-24 (West African Federation, from DOX) and FORM-25 (Sahel Confederation, from SOK) stay closed. Setup registers each family profile for discovery, and the package readiness triggers (`can_prepare_independence_wave_form24_from_iw093`, `can_prepare_independence_wave_form25_from_iw098`) record progress, but neither family has a carrier tag, member roster, territory proof, consent rule or flag, and neither is in the shared commit allowlist.

## Foreign contacts

DOX registers FRA and USA, SOK registers FRA and SAU (`package_contacts.md`).

## AI

The package strategies `independence_wave_iw093_*` and `independence_wave_iw098_*` in `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` drive the route and host-crisis behaviour.

## Limitations

- The Hasan portrait is a source placeholder.
- FORM-24 and FORM-25 cannot be formed.
