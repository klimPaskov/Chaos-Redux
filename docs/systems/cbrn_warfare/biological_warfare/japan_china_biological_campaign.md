# Japan-China Biological Campaign Raids

## Acceptance and current source

The user's 2026-09-20 CBRN implementation request accepted exactly two shared raid categories and native delivery. `common/raids/japan_cbrn_campaign_raids.txt` defines Japan's historical China campaign inside the shared `biological_raids` category. The old Japan biological campaign decision category and its two exact-state decisions are retired. This current-source account awaits parent integration and live-game validation.

The six raid IDs follow `japan_china_biological_<anthrax|plague>_<normal|sale|evolution>_raid`. Each chooses an enemy-controlled Chinese state and a supply-node origin, requires an assigned division and army intelligence, and reserves exact agent bombs plus support equipment through native `essential_equipment`. Anthrax preparation takes 30 days and Plague preparation 45 days. The selected tier is fixed when the raid starts. Both human and AI actors use the same path, with outcome adapter `japan_bio_campaign_resolve_native_raid_outcome` in `common/scripted_effects/japan_biological_campaign_effects.txt`.

## Reservation and cost matrix

| Agent and tier | Exact bomb stock | Support equipment | Command Power |
| --- | ---: | ---: | ---: |
| Anthrax normal | 8 | 35 | 10 |
| Anthrax sale | 4 | 18 | 5 |
| Anthrax evolution | 2 | 9 | 3 |
| Plague normal | 10 | 45 | 14 |
| Plague sale | 5 | 23 | 7 |
| Plague evolution | 3 | 12 | 4 |

The matching bomb archetype is `anthrax_bomb_equipment` or `plague_bomb_equipment`. Native reservation is the sole material debit, and Command Power is the native allocation; the old Political Power cost and scripted refund path were removed under the parent-approved native-raid economy simplification. Sale and evolution variants remain within Biological Raids and do not add categories. A Black Friday sale can be chosen at preparation, but a transaction-specific achievement at reservation is not proven by the documented native lifecycle hooks; the one-day sale may expire before a multi-day outcome callback. The owner records this as an open achievement limitation, not a fabricated callback.

## Exact-state consequence and historical scope

The selected state is passed to `bio_lifecycle_route.japan_china_campaign` and the shared ordinary-pathogen lifecycle. The existing Pingfang, Ishii authority, occupation-linked China target, containment-route exclusions, and pathogen profile gates remain source requirements; the callback cannot substitute another target if the selected state is invalid. Anthrax represents a supply-network release and Plague a vector release. Incubation, detection, spread, treatment, evidence, attribution, deaths, Condemnation, and recovery belong to that shared lifecycle. The campaign does not convert weaponized zombies into ordinary pathogens. The callback brackets its seed with `bio_native_raid_dispatch_in_progress`; the lifecycle owner's Command Power recovery guard for that flag remains pending integration evidence.

The Japanese biological warfare program, Unit 731, plague-vector work, and releases in China are well attested. The 1940 Ningbo plague release is a documented Plague basis; the supply-network Anthrax route is a gameplay abstraction of a documented weapon capability, not a claim about one named historical operation. Background sources retained from the earlier decision design: [historical review](https://pmc.ncbi.nlm.nih.gov/articles/PMC1200679/), [American Experience Ishii biography](https://www.pbs.org/wgbh/americanexperience/features/weapon-biography-shiro-ishii/?flavour=full), and [NOVA history](https://www.pbs.org/wgbh/nova/bioterror/hist_nf.html).

## Source, presentation, and evidence limits

The active gameplay path is `common/raids/japan_cbrn_campaign_raids.txt`, `common/scripted_effects/japan_biological_campaign_effects.txt`, and the biological lifecycle effects and triggers. The former `japan_biological_campaign_category` and `japan_bio_campaign_contaminate_supply_network`/`japan_bio_campaign_disperse_plague_vectors` IDs and category art are historical. Biological raids reuse `GFX_raid_type_icon_anthrax_strike` and agent equipment icons; final native raid map presentation, localisation, and DDS consumers require parent and asset review.

The probability adapter reported no weighted raid surface and a cross-adapter comparison returned `PROBABILITY_SURFACE_EMPTY`; neither result proves AI target selection or outcome rates. Event 026 inspection was partial and its render timed out. Native reserved-equipment behavior on cancellation is not proved by installed documentation; this and the sale-achievement transaction remain open engine evidence gaps.

## Future depth

Add historically specific incident summaries only after exact target, native reservation, outcome, and shared lifecycle behavior have current source and live-game evidence.
