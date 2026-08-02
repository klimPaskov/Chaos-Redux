# Event 016 aftermath family report-art wiring handoff

Date: 2026-08-02

## Scope

This bounded non-model tranche adds reviewed project-family aftermath report cards and routes the existing qualifying-defeat hearings through them. It also reprocessed the six previously routed report scenes through the repository report-card processor so the affected DDS files use the required sepia treatment, transparent card edges, and deterministic grain. No project cost, decision, receipt, country, evolution, super-event, or 3D entity was added.

## Runtime assets

| Runtime DDS | Sprite | Family selector branch |
| --- | --- | --- |
| `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_aftermath_clone_machine.dds` | `GFX_report_event_016_brilliant_scientist_aftermath_clone_machine` | Clone or Machine |
| `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_aftermath_biological_reserve.dds` | `GFX_report_event_016_brilliant_scientist_aftermath_biological_reserve` | Biomedical, Biological Weapons, Paleogenetics, or Xenobiological Synthesis |
| `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_aftermath_portal_temporal.dds` | `GFX_report_event_016_brilliant_scientist_aftermath_portal_temporal` | Teleportation or Temporal |
| `gfx/event_pictures/016_brilliant_scientist/report_event_016_brilliant_scientist_aftermath_alien_singularity.dds` | `GFX_report_event_016_brilliant_scientist_aftermath_alien_singularity` | Alien Arms or Strategic Singularity |

Each runtime file is `210x176`, one-level uncompressed 32-bit BGRA DDS, exact size `147968` bytes. Source masters, processed PNGs, evidence DDS files, and prompts remain in the ignored `docs/assets/016_brilliant_scientist/report_news_expansion/` workspace.

## Gameplay wiring

- `interface/016_brilliant_scientist.gfx` registers the four sprites.
- `common/scripted_localisation/016_brilliant_scientist_aftermath_scripted_localisation.txt` defines `GetBrilliantScientistAftermathRemnantPicture`. It reads the persistent custodian remnant flags and returns one of the four family cards, then returns the shared remnant card for a prototype-only or unresolved record.
- `events/016_brilliant_scientist_aftermath_events.txt` uses the selector for `.301` and `.310` through `.318`; `.303` remains on the shared card because the regional settlement has no single project owner.
- `common/scripted_localisation/016_brilliant_scientist_directorate_scripted_localisation.txt` defines `GetBrilliantScientistIncidentPicture`. `chaosx.nr16.13` now uses the same reviewed family cards for incident groups while keeping the Directorate dossier as its unresolved-family default.

The selectors are presentation-only. They do not set or clear remnant flags, alter project stage, modify costs, change AI weights, create receipts, or dispatch another event.

## Processing correction

The two breakthrough cards and the shared remnant card from earlier presentation tranches were reprocessed from their retained source masters with `.agents/skills/chaos-redux-event-assets/tools/process_report_event_image.py` using a `192x153` card, 2-pixel border, 3-degree tilt, soft shadow, sepia tone, deterministic grain, and a transparent `210x176` canvas. The first-laboratory, university-competition, and security-expansion cards received the same correction. All six now match the accepted alpha and sepia contract.

## Validation

- Four new source scenes were visually reviewed at native processed size. They show clone or machine custody, biological quarantine, portal or temporal apparatus inspection, and alien or singularity custody without readable text or logos.
- All seventeen Event 016 report DDS files now decode as `210x176` legacy BGRA cards. The six corrected scenes and four new family scenes have alpha range `0..255`, transparent corners, and non-grayscale sepia channels.
- The offline Event Inspector was run for the aftermath event file and the incident event. Dynamic picture syntax follows the existing Event 016 breakthrough selector and the vanilla `picture = "[ScriptedLocalisation]"` precedent.
- No Hearts of Iron IV session was launched; live presentation and terminal acceptance remain user-owned.

## Remaining boundary

Broader country-specific flavour, quantitative balance evidence, live consumer validation, and all seven reusable Event 016 3D entity packages remain deferred. Further incident art could still be added later, but the current family-group routing removes the single-dossier presentation for every mapped incident family without introducing a new fire path.
