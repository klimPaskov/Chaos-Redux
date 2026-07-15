# Static GUI Image Generation Prompts

Shared constraints for every prompt: fictional alternate-history HOI4 interface artwork; 1930s-1940s military materials; painterly documentary realism; explicit fictional gore; no readable text, numbers, letters, logos, watermark, modern object, recognizable named leader or face, real atrocity photograph, or copied living-cultural regalia. Compose important detail around the named text-safe regions and keep those regions dark, quiet, and legible.

## Window backgrounds

| Asset | Generated composition and text-safe direction |
| --- | --- |
| `early_category_background` | Blood-stained frontline command map under torn canvas, ruined ration ledger, cracked compass, mud, and a gore-smeared field dressing around the edges. Quiet zones: title x24-354 y14-46; meter/card column x20-298 y54-276; mission area x308-453 y216-258; buttons along y266-304. No cult leader or unique unifier symbol. |
| `network_window_background` | Wide evidence ledger in a damaged port command room: torn maps, telegraph scraps, rail and island photographs, prison evidence tags, dark blood-wet cords, and butchered military supply traces. Quiet zones: top x18-842 y12-124; thread canvas x18-842 y130-250; list panels x18-825 y264-512; selected card x243-617 y530-594. No face, personal mark, or proof of one leader. |
| `warlord_command_background` | Improvised bunker throne-command ledger made from scarred field steel, raw canvas, butchered ration crates, cracked officer fittings, blood, and bone-white scraps. Quiet zones: title x24-344 y14-46; meter/card column x20-298 y54-276; emblem/status column x306-448 y54-298; button y302-340. |
| `revealed_command_background` | Centralized black-red command chamber with torn 1940s military banners, blood-wet steel, stacked field orders, bone-white trim, and a distant massed-army suggestion. Quiet zones: title x24-434 y14-46; portrait x15-181 y49-269; metrics/cards x184-462 y58-304; terminal strip x16-454 y304-344; button y342-380. |
| `wendigo_command_background` | Frozen ruined command room with cracked black steel, ice-locked radio machinery, exposed fictional flesh caught in frost, frozen blood, and snow through shattered walls. Quiet zones: title x24-434 y14-46; portrait x15-181 y49-269; cards/meters x184-462 y58-280; anchor icon x310-374 y286-350; terminal strip x16-454 y320-360; button y362-400. No sacred motif or cultural regalia. |

## Meters, cards, and frames

| Asset | Purpose-built composition |
| --- | --- |
| `field_hunger_meter` | Empty dented mess tin, snapped spoon, dried blood and a gnawed ration edge at the far right; restrained khaki steel center for the value. |
| `command_integrity_meter` | Broken officer epaulette, snapped dispatch chain, torn orders, and bloodied whistle at the far right; field-grey center. |
| `cult_cohesion_meter` | Braided red field cord around identical damaged dog tags and ritual knife nicks, wholly invented and non-cultural; blackened center. |
| `primary_state_card` | Torn operational map corner, muddy pin, spent casing, bloodied field dressing and small recovered remains along the border; two-line safe center. |
| `network_country_card` | Dossier edge with blood thumbprint, torn diplomatic cable and cracked seal; flag-safe left edge and two-line text-safe center/right. |
| `network_state_card` | State evidence card with torn terrain map, hospital tag, rail spike and blood trail around the border; two-line safe center. |
| `network_target_frame` | Blood-wet forensic clamp frame and four dim selection lamps, open dark center for flag and target text. |
| `larder_meter` | Bolted ration crate plate, butcher hook, severed fictional material and wet inventory tally marks at far right; dark center. |
| `frenzy_meter` | Torn restraint straps, cracked teeth, fresh blood spray and bent bayonet guard at far right; dark red-black center. |
| `network_alignment_meter` | Converging courier wires, repeated torn dispatch corners and blood-stuck routing pins at far right; blackened center. |
| `controlled_state_card` | Occupation ledger plate with ruined village map, meat hook shadow, broken helmet and blood-soaked boundary strip; two-line safe center. |
| `global_larder_meter` | Heavy rail-inventory plate, stacked ration can, wet butcher cleaver and blood-dark chain at far right; black-red center. |
| `global_network_meter` | World-route command plate with converging cables, crushed radio valve and blood-marked map fragments at far right; dark center. |
| `warlord_loyalty_card` | Multiple distinct bloodied dog tags and knife hilts arranged around a black command ledger; two-line safe center. |
| `continental_target_card` | Torn continental operational map, convoy token, burning city edge and blood track around a two-line safe center. |
| `revealed_portrait_frame` | 166x220 blackened command steel frame with deep-red wet gore, scar-like cuts and bone-white non-symbolic trim; completely open 156x210 portrait aperture. |
| `transformed_portrait_frame` | 166x220 cracked black ice/steel frame with frozen blood and exposed fictional tissue, no antlers or cultural motifs; completely open 156x210 aperture. |
| `anchor_card` | Ice-cased 1940s field transmitter/rail relay, cracked bolts, frozen flesh and blood along the border; two-line safe center. |
| `countdown_frame` | Damaged field chronometer, frozen cable, cracked ice and dark blood at far right; clear value center. |
| `wendigo_unit_capacity` | Frozen ammunition links, torn black coat strip, claw-scarred steel and blood ice at far right; clear value center. |
| `winter_hunger_meter` | Ice-filled empty mess tin, frozen strip of fictional flesh and dark blood in snow at far right; clear value center. |

Each actual image-generation call expands the row into the shared structured prompt schema from the official `imagegen` skill and records the final prompt in the manifest.
