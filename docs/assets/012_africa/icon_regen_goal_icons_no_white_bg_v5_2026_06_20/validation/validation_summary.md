# Event 012 Africa Goal Icon v5 Validation

- Target size verified: `94x86` for every processed PNG and live DDS.
- Alpha verified: every processed PNG and live DDS contains transparency.
- Corner check: all four corners are fully transparent for every asset.
- Border check: no non-transparent outer-border pixels detected after the final margin pass.
- Matte check: no near-white low-alpha border/background pixels detected by the validation script.
- Chroma-key check: no magenta-key outer background remains in processed PNGs or live DDS files.
- Hidden-RGB check: no non-zero RGB values remain under fully transparent pixels.
- Bright subject-edge highlights are tracked in `validation_metrics.json`; these are parchment/map/artwork highlights, not a background matte, and are not treated as failures when the outer border and low-alpha background checks pass.

## Assets
- `goal_africa_archive_old_seats`: processed PNG and live DDS passed scripted checks.
- `goal_africa_authority_atlas`: processed PNG and live DDS passed scripted checks.
- `goal_africa_charter_league_diplomacy`: processed PNG and live DDS passed scripted checks.
- `goal_africa_charter_league_emblem`: processed PNG and live DDS passed scripted checks.
- `goal_africa_high_chaos_bestiary`: processed PNG and live DDS passed scripted checks.
- `goal_africa_industry_logistics`: processed PNG and live DDS passed scripted checks.
- `goal_africa_liberation_war_office`: processed PNG and live DDS passed scripted checks.
- `goal_africa_military_forces`: processed PNG and live DDS passed scripted checks.
- `goal_africa_political_congress`: processed PNG and live DDS passed scripted checks.
- `goal_africa_regional_integration`: processed PNG and live DDS passed scripted checks.
- `goal_africa_scramble_for_africa`: processed PNG and live DDS passed scripted checks.
- `goal_africa_sponsor_paths`: processed PNG and live DDS passed scripted checks.
- `goal_africa_world_order_route`: processed PNG and live DDS passed scripted checks.
