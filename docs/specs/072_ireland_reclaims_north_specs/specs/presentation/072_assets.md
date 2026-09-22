# Asset specification and production ownership

## Art direction

Build a coherent 1930s and 1940s HOI4 presentation with Irish civic, industrial, military, Gaelic, and maritime identities.
Use recognizably different visual motifs for constitutional settlement, culture, the imperial route, federal cooperation, Atlantic power, and the three military services.
Avoid making every icon a harp or every report a map on a desk.
The North's industrial and civilian life should be visible alongside the army and national symbols.

The structured asset inventory is in 072_asset_manifest.json.
It records proposed consumers and final-path intentions, not created assets.
Every row begins with production status planned.
Final sprite IDs and historical reference choices require a collision and source audit.
A group-level focus motif is a family brief.
Every final implemented focus still needs a distinct appropriate icon or a documented suitable reuse.
The 65 group briefs do not authorize reusing one icon for every node in a large group.

## Surface sizes and delivery

| Family | Native game target | Required treatment |
| --- | --- | --- |
| Report | 210 by 176 | Period photograph language, sepia or black and white, proper tilted-photo alpha treatment |
| News | 397 by 153 | Wide black-and-white period news composition |
| Super-event | 457 by 328 | Major milestone composition with a clear focal point and readable overlay area |
| Focus icon | 94 by 86 | HOI4 goal-icon composition, readable at native size |
| Idea icon | 64 by 64 | Independent small icon, not a reduced focus screenshot |
| Decision icon | 32 by 32 | Strong simple silhouette for the actual action |
| Achievement | 64 by 64 | Completed, grey locked, and not-eligible triplet using the approved immutable templates |
| Country portrait | 156 by 210 | Only if a real character gap requires it, source-verified historical or clearly original fictional |
| Advisor portrait | 65 by 67 | Only where a separately justified advisor consumer exists |
| Flag | 82 by 52, 41 by 26, 10 by 7 | Flat original design, final TGA files, inspect each size independently |
| Formable state piece | Generated from approved consumer projection | Exact registry geometry and static status variants, no generative redrawing |

The repository's asset skill and converter determine the final encoding and mip-level contract.
Record processed PNGs, runtime files, sprite registrations, alpha behavior, and decoded native-size previews.
A large attractive source image does not prove that its native-size game asset is usable.
Each asset must have an actual consumer or a clearly identified required future node.
Remove genuinely orphaned assets from the delivery manifest.

## Reports and news

The opening report shows a formed Irish force preparing to move toward the North, with equipment and people appropriate to the date.
The holder's report shows northern defensive urgency from the counterpart's view without assuming that the holder is British in every campaign.
The settlement report shows an achieved local settlement and returning civilian life.
The failure report must support either a stalled campaign or defeat without showing a fabricated destroyed capital.

Reunification news is the main early celebration image, with civic participation and visible political complexity.
Imperial proclamation combines the new state identity with its actual Irish-Scottish foundation.
Federal proclamation shows separate participating governments and their common charter without making them look like annexed provinces.
Atlantic recognition centers on shipping, naval air, ports, and maintained capability.
Do not place modern flags, contemporary military equipment, or unsupported historical personalities into these scenes.

## Flags and emblems

Reunited Ireland normally retains the valid Irish flag.
A distinct imperial flag is required for the Gaelic Empire, with a flat reference-constrained original design and usable ideology variants where necessary.
The federal bloc needs an original emblem reflecting several equal members.
It is not a replacement country flag for every member.
The Celtic league can use a simpler related emblem so league and federation remain distinguishable.
An Atlantic route emblem may be used for its focus and news identity without forcing a new country name or flag.

Use native transparent outputs where the surface requires alpha.
Flag design is strictly flat 2D, with no folds, lighting, poles, embroidered cloth, or perspective.
Historical symbols are researched and composed under the current flag workflow.
Do not claim a newly designed imperial symbol is an authentic historic flag.
Keep the Irish, Scottish, Welsh, and Breton identities distinct.

## Focus, idea, and decision families

U focuses use civic buildings, reconstruction, transport, law, and industrial motifs.
G focuses use education, print, cultural institutions, and modern military tradition.
E focuses use imperial administration, Irish Sea operations, Scottish institutions, and supported overseas commitments.
C focuses use visibly separate members, charters, joint workshops, and common defense.
T focuses use ports, merchants, access, shipping routes, and operational reach.
M, N, and A use the equipment and training roles described in their branches.

Idea icons separately identify Settlement and State, Defense Establishment, and External Commitments.
Their staged versions can change a meaningful detail while retaining the family's identity.
The decision icons depict the action, such as a treaty, repair program, training, logistics, or formation.
They cannot be illegible miniatures of a full news scene.
Achievement art is composed independently against its template, even when it shares a subject with a focus.

## Source and worker routing

The asset source researcher finds valid historical references and documents provenance, permissions, and date suitability.
Generated event art handles the original scene families.
The icon artist handles focus, idea, decision, emblem, and achievement work under their separate style requirements.
The portrait creator is used only if the character audit identifies a necessary gap.
The event UI worker owns only the 072-specific window work and its approved category linkage.
Shared settings and event-log integration remain parent-owned.

The normal infantry, artillery, motorized, marine, naval, and air families supply this campaign's units.
The asset manifest contains no requirement for a new custom 3D unit family.
Visual distinction can use verified existing insignia or cosmetic mechanisms without inventing missing model capabilities.
Historical photographs used as reference do not automatically carry permission for redistribution as finished art.
The final manifest must distinguish reference-only sources from redistributable assets.
