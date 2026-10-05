# Event 009: White Peace

This overview records current source behavior, accepted design boundaries, and validation limits. The source design is in [the Event 009 specification](../../specs/009_white_peace_specs/specs/009_white_peace_spec.md), and the implementation scenarios are tracked in [the validation matrix](../../plans/009_white_peace_plans/009_white_peace_validation_matrix.md).

## Runtime Flow

1. `chaosx.nr9.1` enters through repeatable Event 9 or the Peace cluster. The dispatcher recalculates the current war pressure and eligible pair pool before selecting a branch. A valid Settings precheck carries its prepared branch and country targets into `.1`; the entry rebuilds context only if that data is incomplete.
2. Event 009 can select only an isolated one-on-one war. Each selected country must have the other country as its only active enemy, hold its own capital, and pass the country and pair safety triggers. Protected, special, nonhuman, civil-war, subject, faction, recently settled, and near-capitulation actors remain excluded.
3. Multi and broad branches select additional separate eligible wars. A country already settled during the chain is blocked by recent-country memory, and the branch stops when no new safe pair remains or its existing cap is reached.
4. `chaosx.nr9.1` applies every successful `white_peace` effect before opening a report or news event. The result options are acknowledgements and cannot re-read or change the selected outcome.
5. After the effect, the event records successful settlement counts, applies a capped Chaos reduction, updates the event-log evolution when its setting and tier permit it, and routes one aggregate result variant. Every human-controlled participant in the settled wars receives that result once. If all participants are AI, one global news event is sent to observers.
6. A forced invalid root entry stores its skip reason on the initiating country and can show `chaosx.nr9.6`, which confirms that no peace was imposed. The Settings precheck calls `white_peace_report_failed_manual_request` for its saved human requester, so the blocked request receives the same reason report without event dispatch or repeatable-history accounting.

## Evolution and Settings

The base one-on-one minor settlement remains available even when every evolution is disabled.

Each existing war-pressure threshold is an additional qualification for its evolution stage. Stage I multi-settlement behavior requires its matching `is_current_evolution_enabled` check, Stage II major settlements require the Stage II check, and Stage III broad settlements require the Stage III check. The helper sets Event 9's evolution event ID, type, stage, and tier in caller-local temporary variables before checking the setting. Disabled branches receive zero selection weight. Old global stage-unlock flags cannot bypass a current disabled-stage or tier check.

Stage I can settle two separate minor wars, or three when the existing high-pressure candidate threshold is met. Stage II adds a rare branch for an isolated war involving at least one major country. Stage III adds a broader branch that can settle up to five separate isolated minor wars. A multi-country war is excluded at every stage because the target model cannot prove that other participants would be safe.

The Event Settings check is a gameplay gate, not only a log visibility switch. Event log entries still record only when the matching evolution is enabled and its tier has been reached.

## Dynamic Weight

The tuning table is in `common/script_constants/009_white_peace_constants.txt`. The environment cap begins at `125`, rises with active-war, safe-minor-pair, minor-only-war, and clutter pressure, and never exceeds `1500`. The repeatable event recovery ratio and the current enabled stage multiplier reduce the live cap used by the picker.

`calculate_white_peace_dynamic_cap` keeps the recovered repeatable value intact and clips only the live chance. `score_white_peace_pair` favors minor, independent, non-faction actors and prolonged wars. Weighted pair selection happens after the safety vetoes. Probability sweeps and the required before/after comparison timed out through the installed MCP route, so the numeric behavior remains uncertified.

`global.white_peace_active_war_count` is a pressure proxy over ordinary unprotected wars, while `global.white_peace_safe_minor_pair_count` and `global.white_peace_major_candidate_count` count eligible pair candidates. The pressure proxy can still include wars that fail a candidate gate, so its contribution to the chance is a remaining balance question rather than proof that each counted war can be settled.

## Effects, Memory, and Achievements

The settlement returns the selected countries to their prewar borders without an indemnity, adds the existing status-quo opinion modifier on both sides, and marks recent settlement memory. During settlement, Event 009 suppresses the ordinary per-country peace Chaos adjustment and then applies its capped branch-level reduction.

`recent_white_peace_country` lasts 181 days so that another settlement cannot re-arm a No Winner watch at the same time as its day-180 check. Exact pair memory lasts 360 days, major-country memory lasts 540 days, and broad-branch memory lasts 720 days.

The No Winner check is scheduled on the saved primary country and carries the exact partner as `white_peace_no_winner_partner`. Both countries must still exist, remain independent, and remain uncapitulated when the 180-day check runs. Event-owned callbacks in `common/on_actions/009_white_peace_on_actions.txt` permanently clear the watch after capitulation, annexation, or a subject-status transition, so later restoration cannot regain eligibility.

The five achievements are tracked only from Event 009 settlement logic or its delayed survival check:

- `009_white_peace_status_quo_ante`: a player minor is part of an isolated prolonged minor war settlement and remains independent and outside factions.
- `009_white_peace_no_winner`: both countries complete the continuous 180-day survival watch.
- `009_white_peace_chain_of_tables`: six separate minor wars settle before any major-country settlement occurs.
- `009_white_peace_silence_of_giants`: a player major is included in a prolonged isolated major-country settlement.
- `009_white_peace_the_circular`: one broad settlement ends at least three separate isolated minor wars.

## Event Log and Integration

Event 9 remains registered as a repeatable event and as a Peace cluster member with cluster ID `4`. `prepare_white_peace_runtime_context` saves the first selected primary as `event_cluster_actor` and separate report targets. After a multi-war chain, it restores the initial pair scopes so the shared event-history actor continues to point to the original primary.

The entry is wired in `events/009_white_peace.txt`. Candidate and outcome logic lives in `common/scripted_effects/009_white_peace_effects.txt`, `common/scripted_triggers/009_white_peace_triggers.txt`, and `common/script_constants/009_white_peace_constants.txt`. The [effect call contract](../../../common/scripted_effects/009_white_peace_effects.md) records temporary output ownership and persistent inputs/outputs. The forced invalid reason selector is in `common/scripted_localisation/009_white_peace_scripted_localisation.txt`.

The Settings-owned precheck in `common/scripted_effects/chaosx_settings_effects.txt` stops an invalid manual selection before it reaches `chaosx.nr9.1`, then calls `white_peace_report_failed_manual_request`. That helper snapshots the skip reason onto the original human requester, sets the existing one-report receipt, and opens `.6` without marking the repeatable event as dispatched.

For successful chains, the entry clears `white_peace_human_report_pending` across countries and clears `white_peace_current_invocation_has_human` at the start. Each applied pair marks both human-controlled endpoints and sets the invocation flag. After settlement, one bounded country loop sends the same aggregate result to each marked human, then clears the pending flags and invocation flag. An all-AI chain instead sends one global news event.

The current shared event-details, evolution, availability, and achievement wording reflects the accepted in-game mechanics. The [decision log](../../plans/009_white_peace_plans/agent_decisions_2026-10-05.md) records accepted design changes and their basis. The [catalog pending note](../../plans/009_white_peace_plans/catalog_changes_pending.md) records workbook fields that remain queued.

## Visual Assets

The report popup uses `GFX_report_event_009_white_peace` from `gfx/event_pictures/009_white_peace/report_event_009_white_peace.dds`, registered in `interface/009_white_peace_event_images.gfx`. It decodes at `210x176` and the native-size preview has no clear visual defect. Its original source, prompt, and durable provenance manifest are absent from the current package, so source provenance remains unresolved.

The all-AI observer news uses `GFX_news_event_009_white_peace` from `gfx/event_pictures/009_white_peace/news_event_009_white_peace.dds`, registered in the same `.gfx` file. Its opaque monochrome preview is `397x153`, and the decoded DDS matches its processed PNG pixel-for-pixel. Prompt, source candidate, processing notes, manifest, and round-trip evidence are under `docs/assets/009_white_peace/`.

The five achievement icons each use completed, grey, and not-eligible textures. Their runtime paths are `gfx/achievements/009_white_peace_<achievement>{,_grey,_not_eligible}.dds`, registered in `interface/chaosx_achievements.gfx`. All fifteen textures decode at `64x64` and the visual states are distinct at native size. Their current source art and prompt provenance are absent from the event package.

The exact accepted asset rows, runtime registrations, consumers, and provenance gaps are listed in the [asset coverage crosswalk](../../plans/009_white_peace_plans/009_asset_coverage_crosswalk.md).

No dedicated scripted GUI, character portrait, country package, flag, super-event, or animation is required by the accepted Event 009 design.

## Evidence and Remaining Limits

The report-color audit returned zero color-bearing Event 009 report keys. The two installed references consulted directly for the native settlement are `documentation/effects_documentation.md:8588-8602` and the offline wiki row `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:1507`. Those sections establish the country/target syntax, but they do not explain the wider war side effects, which is why the accepted candidate rule stays limited to isolated one-on-one wars.

The offline on-action table documents `on_capitulation`, `on_annex`, `on_puppet`, `on_release_as_free`, and `on_release_as_puppet` at `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md:254-263`, and subject transitions at lines `434-436`. Installed vanilla source uses the same ROOT/FROM scopes in `common/on_actions/00_on_actions.txt:931-950` and `common/on_actions/12_wuw_on_actions.txt:3055-3108`. The installed `_documentation.md` lists the corresponding callback names at lines `30-61`.

The connected event inspection and reachability-render routes timed out, and the final probability inspection and comparison also timed out without artifacts or a numeric delta. The supplied `evt009_sheet.jpg` shows unrelated USA/Japan popups and Rhineland/Aussa news, with no White Peace popup or observer-news example. No Hearts of Iron IV session was launched for this audit.

## Future Suggestions

If a later design needs settlement inside a multi-country war, first add a reliable war-participant registry that can identify every actor affected by `white_peace`, prove each participant safe, and carry survival and achievement tracking for the whole affected group.

If the repeatable weight model is retuned, first restore the probability-inspection and same-scenario comparison routes and review how ineligible ordinary wars contribute to the pressure proxy.
