# Event 006 Pacific focus-icon ImageGen prompts

Production date: 2026-07-18
Source mode: built-in Codex ImageGen, one generation per icon
Reference inspected before generation: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/national_focus/contact_sheet.png`
Target: transparent HOI4 national-focus icon, processed to 94x86

All prompts shared this finish and constraint block:

> Use case: stylized-concept. Asset type: Hearts of Iron IV national focus icon, Event 006 Pacific focus family. Create one distinct bold centered emblem for the requested focus. Canonical HOI4 focus-icon finish, strong silhouette, painterly metal and enamel depth, muted steel blue, deep navy, aged gold, oxide red and sea-glass teal accents, high contrast and readable at 94x86. Transparent icon workflow: place the emblem on a perfectly flat solid #00ff00 chroma-key background for background removal, no shadows, gradients, reflections, texture, floor plane, text, invented flags, people, portraits, watermark, UI mockup, or border baked into the icon. Keep generous padding and crisp separated edges.

The following subject lines were appended individually; each generation was retained under `source_png/focuses/` with the exact stable stem.

| Stable source stem | Generation subject and identity constraints |
|---|---|
| `goal_independence_wave_hbx_screen_federal_arsenals_source.png` | Heavy screened arsenal gate with two stacked ammunition crates and a small California civic bear-seal medallion; no words. First HBX icon may use the restrained bear-seal motif. |
| `goal_independence_wave_hbx_reopen_coastal_supply_bureaus_source.png` | Coastal supply bureau ledger beside a small harbor pier, rolled manifests and stamped shipping forms tucked under a steel clipboard, tiny lighthouse-and-crate motif; avoid the screened arsenal gate and bear seal. |
| `goal_independence_wave_hbx_seat_sacramento_civic_convention_source.png` | Civic convention table beneath a simplified Sacramento civic dome, three empty leather chairs represented only as furniture silhouettes, brass gavel and bound charter at center; no people. |
| `goal_independence_wave_hbx_bind_ports_factories_and_guard_source.png` | Unified triad emblem: cargo ship bow, factory smokestack, and state-guard shield linked by a heavy steel chain, balanced radial composition; no flags or text. |
| `goal_independence_wave_hbx_settle_federal_asset_ledger_source.png` | Open federal asset ledger with two clasped brass seal medallions, balanced scales and a key crossing the pages, restrained California civic geometry only; no words. |
| `goal_independence_wave_hbx_charter_pacific_procurement_board_source.png` | Pacific procurement board as a brass contract clipboard behind a cargo crate, shipyard gantry hook, and small riveted harbor buoy, one unified industrial seal; no text. |
| `goal_independence_wave_hbx_convene_pacific_maritime_congress_source.png` | Three small ships on three radiating Pacific sea routes around a brass compass rose and maritime congress seal, clear three-route geometry; no text. |
| `goal_independence_wave_haw_reconcile_shipping_registers_source.png` | Civil shipping register and manifest bound with a brass clasp, harbor stamp, ink pen, and small cargo-ship silhouette, orderly administrative emblem; no words. Avoid invented or universal sacred symbols. |
| `goal_independence_wave_haw_organize_island_coastwatch_source.png` | Coastal watchtower with binoculars and harbor signal lantern, curved island shoreline line beneath, alert civilian watch emblem; no sacred symbols. |
| `goal_independence_wave_haw_seat_island_government_compact_source.png` | Representative island government compact: round council table from above with bound charter at center and four empty seats indicated by metal nameplates without words, island-coastline inlay; no people. |
| `goal_independence_wave_haw_bind_shipping_supply_and_coastwatch_source.png` | Inter-island network linking cargo ship, supply crate, coastwatch tower, and three small harbor lights with thick nautical lines, one coherent network seal; no flags. |
| `goal_independence_wave_haw_settle_base_and_property_accounts_source.png` | Civil base and property ledger crossed by old keys and a small surveyor compass, harbor warehouse silhouette behind, calm accounting emblem; no sacred or royal symbols. |
| `goal_independence_wave_haw_ratify_autonomous_pacific_mandate_source.png` | Rolled autonomy mandate scroll held by a bounded maritime shield and brass seal, ocean waves below, restrained civic authority; no invented Hawaiian emblem and no text. |
| `goal_independence_wave_haw_dispatch_pacific_delegation_source.png` | Diplomatic delegation ship approaching a harbor table with two sealed document folders and a compass, calm Pacific diplomacy emblem; no people, flags, or words. |

Negative constraints applied to every generation: no generated UI, text, watermark, portrait, people, flags-as-artworks, fake historical Hawaiian emblem, or universal sacred symbolism. The source contact sheet records the green chroma-key field before local alpha removal.
