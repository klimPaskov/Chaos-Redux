# Event 027 AI domain probability comparison, 2026-10-04

Disposition: implemented (commit `317e43684`). The comparison covers the AI domain `random_list` in `doctrine_research_ai_choose_scored_domain` (`common/scripted_effects/027_doctrine_research_ai_effects.txt:72`) for scenarios DR-A01 to DR-A06. Validation limit: the score vectors are traced from source for the qualitative DR-A states; they are not native country readings.

## MCP route

- `hoi4.probability_inspect` with adapter `random_list` returned `INTERNAL_ERROR` for a `path` + `line` selector and again for the narrower `identifier` + `path` selector. No further inspect retries were made.
- `hoi4.probability_evaluate` with the same identifier selector returned `PROBABILITY_SURFACE_EMPTY`.
- `hoi4.probability_evaluate` with selector `{ path }` and the explicit candidate pool `...ai_effects.txt:72.entry.2` to `entry.6` (Army, Navy, Air, Special Forces, Chaos Warfare) completed. Workspace `mod_chaos_redux_ea3b2d67c2c0`, source hash `5adff3e5468e3d0bde0c09dd274709a5d4fa93c49c7ed5ee46ef4a2f85053159`.
- `hoi4.probability_compare` was not used: the `random_list` source is identical before and after, and the change lives in the score effect that feeds its five weight variables. The comparison is therefore the same scenario IDs evaluated with the before and after score vectors.

| Run | Analysis ID | Scenario hash | Source revision |
| --- | --- | --- | --- |
| Before | `probability-9200f46b562ac60b94d6a253` | `f2ddafc8fdcd9faf30c2338a8058892de08f03eb674acb59e29ef8d47af0fa37` | `314c15761cbbe92c5fb72930cf5c532d61f51c2c57d901fd105b3cf67ad90e18` |
| After | `probability-3122202ff88b30f677333c8d` | `cff47ac9df45ae16fbf6ff358983984b14c29648e29defe69314f7c533be9b8f` | `1cf114f2806bb6df751c464e0719b7f4cbef098b43107d59b26e83d861250f77` |

## Scenario states used for the trace

- DR-A01 land major: divisions with infantry and armour templates, 28 military factories and 7 dockyards, war with a land front, faction member, coastal states but an inland capital, a small fleet and some air wings, no Grand Doctrines, Special Forces valid without Special Forces templates.
- DR-A02 island naval power: Army Grand Doctrine active with incomplete tracks, Navy and Air empty, 20 dockyards and 9 military factories, convoy war without a land front, faction member, coastal capital, warships and air wings.
- DR-A03 air-centred continental power: Army active, Air empty, war with a land front, air wings, few dockyards, inland capital, small fleet.
- DR-A04 landlocked minor: no coast, fleet, or dockyards, small army, military factories but no air wings, at peace, no doctrines.
- DR-A05 near-landlocked country with a maritime plan: one coastal state, no fleet or dockyards yet, Army active, Navy empty, at peace.
- DR-A06 every ordinary domain complete.

## Results (conditional probability per domain)

| Scenario | Before: Army / Navy / Air / SF | After: Army / Navy / Air / SF | Expected ordering |
| --- | --- | --- | --- |
| DR-A01 | 29.0% / 25.8% / 25.8% / 19.4% | 42.0% / 24.0% / 28.0% / 6.0% | Army, Air, Navy |
| DR-A02 | 29.0% / 25.8% / 25.8% / 19.4% | 30.8% / 36.5% / 26.9% / 5.8% | Navy competes and normally leads |
| DR-A03 | 29.0% / 25.8% / 25.8% / 19.4% | 42.0% / 24.0% / 28.0% / 6.0% | Air in the top bounded pool |
| DR-A04 | 48.0% / 4.0% / 24.0% / 24.0% | 68.2% / 0% / 27.3% / 4.5% | Army clear lead, Navy invalid or near zero |
| DR-A05 | 38.9% / 16.7% / 22.2% / 22.2% | 53.6% / 14.3% / 21.4% / 10.7% | Navy above the landlocked score |
| DR-A06 | no candidate | no candidate | no candidate; the batch closes without compensation |

Score vectors (Army, Navy, Air, Special Forces): before A01 to A03 `18, 16, 16, 12`, A04 `12, 1, 6, 6`, A05 `14, 6, 8, 8`; after A01 and A03 `21, 12, 14, 3`, A02 `16, 19, 14, 3`, A04 `15, 0, 6, 1`, A05 `15, 4, 6, 3`. Chaos Warfare is invalid in all six states.

The analyzer flags Chaos Warfare as starved in every scenario (intended, no valid action) and Navy as starved in the after-state DR-A04 (intended, no naval capability). DR-A06 reports all eligible values zero, which matches the expected no-candidate closure.

## Remaining gap

DR-A03 still ranks Army first because air-heavy industry cannot be told apart from land industry by factory counts alone; Air holds second place. DR-A05 cannot see planned dockyards, so a fully landlocked country gains Navy weight only once it controls a coastal state. Both gaps are closed by decisions D17 (maritime plan for a landlocked country) and D18 (air-centred industry); see `probability_domain_round2_2026-10-05.md`.
