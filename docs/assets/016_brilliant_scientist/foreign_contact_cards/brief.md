# Event 016 Foreign-Contact Card Brief

The `.100–.181` foreign-contact chain needs its own report-card language. It must not reuse the appointment image. Five dedicated states cover invitations, protection offers, recruitment, theft, sabotage, defection, extraction, and assassination without revealing the acting country through a hard-coded flag.

All source scenes are fictional, generated with the built-in image generator, and then processed through the repository report-event pipeline to 210 x 176 sepia cards with transparent clipped corners.

| State | Runtime sprite handoff | Intended event uses | Scene contract |
| --- | --- | --- | --- |
| neutral | `GFX_report_event_016_brilliant_scientist_foreign_contact_neutral` | first invitation or cautious diplomatic approach | anonymous attaché presents a sealed scientific invitation across a neutral desk |
| offer | `GFX_report_event_016_brilliant_scientist_foreign_contact_offer` | protection and recruitment offers | open research contract, passport, protected transport papers, guarded but non-coercive meeting |
| threat | `GFX_report_event_016_brilliant_scientist_foreign_contact_threat` | coercion, blackmail, threatened assassination | torn correspondence, shadowed operative, Kruger under surveillance; no explicit injury |
| operation | `GFX_report_event_016_brilliant_scientist_foreign_contact_operation` | theft, sabotage, extraction attempt | night laboratory breach with evidence case and damaged apparatus; readable covert action |
| resolved | `GFX_report_event_016_brilliant_scientist_foreign_contact_resolved` | defection, successful/failed extraction, assassination aftermath or final diplomatic resolution | abandoned meeting table, recovered dossier, closed transport case, guards securing the scene; no gore |

The parent agent owns the final event-to-state mapping and `.gfx` registration. The delivery handoff will list recommended mappings for every event namespace range and exact DDS paths.
