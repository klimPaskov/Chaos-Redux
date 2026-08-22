# Famine and Migration Report-Art Prompts

Source mode: generated with the official built-in ImageGen workflow. Generation fits because these are dynamic shared-system incidents rather than required depictions of a specific real photograph, real victim, or named real person.

All prompts requested a fictional 1936–1945 period documentary photograph, horizontal 3:2 composition, sober press-camera realism, period clothing, transport, architecture, and materials, no readable text, no logos, no flags, no UI, no watermark, no modern objects, no graphic injury or corpses, and no real-person likeness.

## `fm_report_generic_famine`

Prompt: “A fictional but historically grounded 1936–1945 documentary press photograph of a severe wartime food shortage in a rural European town: a long ration queue outside a weathered grain store with heavy wooden doors shut, empty sacks and a handcart in the foreground, a small relief team weighing grain and handing out plain parcels, worn brick and timber buildings behind them. Ordinary civilians and relief workers in period clothing, natural documentary distance, cold overcast daylight, quiet urgency and dignity, muted period tones suitable for later sepia processing, horizontal 3:2 composition with the queue and closed store as the anchor. No readable signs, logos, flags, newspaper layout, UI, watermark, modern objects, modern clothing, modern vehicles, graphic injury, corpses, starvation caricature, cinematic grading, fantasy, 3D render, malformed hands, distorted faces, duplicated people, contemporary plastic packaging, or real-person likeness.”

Seed: `7301`.

## `fm_report_island_blockade`

Prompt: “A fictional but historically grounded 1936–1945 documentary press photograph of an island famine under wartime blockade: a battered small harbor after shelling, idle cargo cranes and a damaged warehouse, a few moored freighters unable to sail, civilians waiting beside empty wooden carts while a port relief committee records sacks under a tarpaulin. Civilians and port workers in period clothing, clear maritime isolation and delayed relief, bleak coastal overcast, wind and salt haze, restrained patience, muted period tones suitable for later sepia processing, horizontal 3:2 composition with harbor damage and idle cranes behind waiting civilians and empty carts. No readable signs, logos, flags, newspaper layout, UI, watermark, modern objects, modern clothing, modern vehicles, modern shipping containers, graphic injury, corpses, starvation caricature, cinematic grading, fantasy, 3D render, malformed hands, distorted faces, duplicated people, contemporary plastic, or real-person likeness.”

Seed: `7302`.

## `fm_report_wartime_evacuation`

Prompt: “A fictional but historically grounded 1936–1945 documentary press photograph of an organized wartime civilian evacuation by rail: a steam railway platform under a simple iron canopy, an old passenger train with doors open, families carrying battered suitcases and bundled bedding, railway porters guiding orderly movement, a few children helped toward a carriage, no panic. Ordinary evacuees, porters, and a local reception worker in authentic period clothing, soft grey morning light, anxious but organized dignity, horizontal 3:2 composition with the train receding behind layered luggage and guided movement. No readable signs, logos, flags, newspaper layout, UI, watermark, modern objects, modern clothing, modern vehicles, modern barriers, graphic injury, corpses, cinematic grading, fantasy, 3D render, malformed hands, distorted faces, duplicated people, contemporary plastic suitcases, visible writing, or real-person likeness.”

Seed: `7303`.

## `fm_report_closed_border`

Prompt: “A fictional 1936–1945 documentary press photograph at a temporarily closed frontier crossing: an old rural road ends at a solid iron gate beside a modest timber checkpoint hut, several civilian travelers with suitcases and cloth bundles wait on the near side, two period uniformed sentries observe calmly, wooded hills and a distant railway lie beyond the gate. Waiting travelers, luggage, closed gate, and checkpoint clearly show interrupted movement, late autumn grey light, restrained uncertainty and administrative tension, horizontal 3:2 composition with the gate across the middle ground and travelers in the foreground. No readable signs, logos, flags, newspaper layout, UI, watermark, modern objects, modern clothing, modern vehicles, modern barriers, graphic injury, corpses, cinematic grading, fantasy, 3D render, malformed hands, distorted faces, duplicated people, contemporary plastic luggage, visible writing, or real-person likeness.”

Seed: `7304`.

Generation note: the first wording was rejected by the image safety filter; this neutral frontier-crossing wording generated the accepted result without changing the approved visual intent.

## `fm_report_relief_arrival`

Prompt: “A fictional but historically grounded 1936–1945 documentary press photograph of relief arriving after a food crisis: a damaged railway station or small harbor depot with a steam locomotive and relief wagons, workers unloading grain sacks and wooden crates, local volunteers organizing a calm distribution line, repaired masonry and temporary roof supports behind them. Food convoy unloading, practical local relief distribution, ordinary civilians and workers in period clothing, early morning light breaking through cloud, relief and exhaustion without triumphalism, muted period tones suitable for later sepia processing, horizontal 3:2 composition with unloading action foreground and train or depot background anchor. No readable signs, logos, flags, newspaper layout, UI, watermark, modern objects, modern clothing, modern vehicles, modern shipping containers, graphic injury, corpses, cinematic grading, fantasy, 3D render, malformed hands, distorted faces, duplicated people, contemporary plastic packaging, visible writing, or real-person likeness.”

Seed: `7305`.

## `fm_report_nuclear_evacuation`

Prompt: “A fictional 1940s press photograph of an organized civilian evacuation after a distant atomic blast: a far-off city skyline with one broad damaged district and a rising pale ash cloud, a road checkpoint in the foreground, evacuees moving in orderly groups with blankets and small cases, period medical staff in simple protective clothing guiding them toward buses and a railway siding. Organized survivor movement, medical assistance, ash-covered landscape, and distant destruction, sober alternate-history 1940s documentary photography, diffuse sun through ash haze, solemn urgency and practical care, horizontal 3:2 composition with the skyline secondary and evacuees and medical workers foregrounded. No readable signs, logos, flags, newspaper layout, UI, watermark, modern objects, modern hazmat suits, modern vehicles, graphic injury, corpses, burns, dismemberment, gore, mushroom-cloud spectacle, cinematic grading, fantasy, 3D render, malformed hands, distorted faces, duplicated people, contemporary plastic, visible writing, or real-person likeness.”

Seed: `7306`.

## `fm_report_return`

Prompt: “A fictional but historically grounded 1936–1945 documentary press photograph of voluntary civilian return and resettlement after a wartime food crisis: a steam train arrives at a damaged but repairing rural station, families step down with modest luggage and bundles, local workers repair a roof and clear bricks in the background, a small house and fields beyond begin to recover. Returning families, rail arrival, practical reconstruction, and a welcoming local worker, cool morning light with a little warmth on the horizon, cautious relief and reconstruction, muted period tones suitable for later sepia processing, horizontal 3:2 composition with family and train door foreground and repair work behind. No readable signs, logos, flags, newspaper layout, UI, watermark, modern objects, modern clothing, modern vehicles, graphic injury, corpses, cinematic grading, fantasy, 3D render, malformed hands, distorted faces, duplicated people, contemporary plastic luggage, visible writing, or real-person likeness.”

Seed: `7307`.

## Processing and conversion

Each source was retained unchanged at `1536x1024` RGB PNG. The repository report processor created a `210x176` RGBA report card with `192x153` card, `2`-pixel border, `3°` tilt, `4,5` shadow offset, `4.5` blur, `0.50` opacity, grain `7`, paper grain `2`, supersample `4`, edge soften `0.35`, and the seed above.

Each processed PNG was converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py --width 210 --height 176` to one-level uncompressed 32-bit BGRA DDS with no mipmaps.
