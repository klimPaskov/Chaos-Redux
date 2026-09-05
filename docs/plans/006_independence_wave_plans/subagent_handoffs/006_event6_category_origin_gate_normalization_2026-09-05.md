# Event 006 category origin-gate normalization — 2026-09-05

Status: implemented; source-only visibility hardening.

The remaining Event 006 package and shared decision-category selectors in `common/decisions/categories/006_independence_wave_categories.txt` now use `is_independence_wave_event6_local_content_active` consistently. This covers the Altai, Buryatia, network, league, evolution-incident, Far Eastern, IW-043, IW-058, IW-093, IW-098, Khakassia, Komi, Kurdistan, Mari, Micronesia, Fiji, NAV, GLC, Sakha, Udmurt, and IW-095 category blocks that still used the legacy `is_independence_wave_active_country` spelling.

The replacement is behavior-preserving for an actual Event 006 country: `is_independence_wave_event6_local_content_active` requires `exists = yes` and then calls the same `is_independence_wave_active_country` predicate. It makes the player-facing origin contract explicit at every category registration and keeps Event 021 adapter receipts from being treated as a published Event 006 surface. No category ID, icon, picture, decision, cost, mission, package gate, or pre-event receipt was added or removed.

Focused source checks after the normalization report no remaining `is_independence_wave_active_country` selector in the consolidated Event 006 category file. The allocator, strict flag, country API, FORM-16, SCN-008, and Event 006 GUI semantic audits remain green. This source pass does not claim live UI visibility, save/load behavior, or engine completion.
