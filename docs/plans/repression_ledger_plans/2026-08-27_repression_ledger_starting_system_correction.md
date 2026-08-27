# Repression Ledger and 1936 Starting Systems Correction

## Overview

This correction replaces the compact category's separator-heavy status dump with country-specific prose and a natural status summary, completes the Ledger with a real Evidence & Reform tab, and establishes bounded 1936 camp and repression baselines for Germany, Japan, and the Soviet Union.

The starting systems use the existing registered-site and monthly Deaths contracts.

They do not create a new daily, weekly, or monthly world-country loop.

Later events and decisions retain ownership of additional camp construction, experiment programs, radicalization, contaminated methods, and major wartime escalation.

## Decision Category Presentation

The decision category remains a compact entry point to the full Ledger.

Its description is selected through explicit German, Japanese, Soviet, and neutral scripted-localisation branches, so country-specific prose cannot fall through into another country's interface.

The status summary uses sentences and line breaks rather than pipe characters, divider runs, fake columns, fake meters, or text pretending to be a button.

The category is visible when an eligible country has an operating network, inherited or dormant camp records, visible reform work, a managed network, an unlocked detention route, or a camp crisis.

`visible_when_empty = yes` keeps the category available when the operating system itself is the reason for visibility but no ordinary decision is currently listed.

## Functional Ledger Layout

The full Ledger has five real tabs with scripted visibility and click handling:

1. Overview presents reach, output, population loss, resistance, logistical burden, evidence, and reform pressure.
2. State Pools presents eligible territories, supports territory selection, and exposes valid activation orders.
3. Active Sites presents the operating-site registry, supports site selection, and exposes only valid site actions.
4. Country System presents country-specific institutions and orders through the existing shared action dispatcher.
5. Evidence & Reform presents discovery, foreign visibility, condemnation, tribunal exposure, attributed deaths, reform pressure, and closure status.

The Evidence & Reform tab is a real GUI panel with four data cards and dynamic evidence and reform seals.

It does not simulate a layout inside localisation.

## Germany at the 1936 Start

State `53`, the Dachau-area historical location, begins as an operating low-intensity detention site.

It is registered to Germany, contributes to the active network, appears in the Ledger, and receives the existing detention-site monthly population-loss profile.

The historical baseline marker exempts this inherited site from the political and evidence penalty used when the player deliberately opens a new core-territory site.

States `64` and `60`, the Sachsenhausen and Buchenwald historical locations, remain dormant records for later activation.

The German baseline sets only low opening racial-policy and archive-control pressure.

It does not create Auschwitz, an experiment site, a laboratory, a radicalized site, or a later wartime program.

## Japan at the 1936 Start

State `716`, the Manchurian forced-labor precedent, begins as an operating low-intensity detention site.

It is registered to Japan, contributes to the active network, appears in the Ledger, and receives the existing detention-site monthly population-loss profile.

State `611`, the North China forced-labor precedent, remains a dormant record for later activation.

The Japanese baseline sets only low Kwantung autonomy, Ishii influence, and occupation-record pressure.

It does not create the Pingfang experiment program, an outbreak route, or later wartime escalation.

## Soviet Union at the 1936 Start

States `644`, `874`, and `881`, representing the Kolyma, Magadan, and Karagandy historical records, begin as operating gulag sites.

Their quiet concentration-camp markers are converted to `gulag_labor_camp_network` buildings and registered to the Soviet Union.

The existing registered-state monthly processor applies the gulag population-loss profile and reports the resulting deaths through `chaos_meter_register_state_civilian_deaths_percent`.

State `881` also begins with the Soviet famine-pressure marker.

The country begins with moderate famine-aftermath pressure, forced-labor quota, grain-extraction burden, NKVD authority, republic fear, and old-movement grievance.

The existing famine refresh applies local manpower, production, resource, supply, and resistance pressure to eligible Soviet famine states and keeps future relief, concealment, quota, and crisis routes functional.

No separate opening death shock is applied because the registered monthly harm system owns recurring deaths from the start.

## Central Tuning

All opening values are stored in `camp_rework_1936_baseline` inside `common/script_constants/camp_repression_rework_constants.txt`.

The opening site selection remains explicit because the state identities are historical content, while the pressure and balance values remain centrally tunable.

The initialization is idempotent through `camp_rework_1936_baseline_initialized` and the existing state registration checks.

Migration temporarily permits an eligible historical perpetrator to retain responsibility for a registered site outside its current borders.

That exception exists only while `camp_rework_migration_in_progress` is set, so ordinary registration still rejects mismatched responsibility.

This preserves Japan's responsibility and the existing Japan-relative state-pool classification for state `716` while Manchukuo controls the territory.

## Decision Costs and Action Safety

Every spendable Ledger order uses at most four spendable resources, including political power.

Expansion and transfer orders use explicit icon-first cost text that matches their availability checks and deduction effects.

The restricted contaminated-site order selects and displays the exact chemical or biological payload and quantity that the action will consume.

Nerve-method mastery uses the same fixed-point quantities for availability, display, and consumption: `18.00` tabun, `15.75` sarin, or `12.60` soman cylinders for activation, with matching `2.70`, `2.25`, and `1.80` monthly quantities.

The Country System rebuilds its action slots in the same effect frame before checking payment, routes the selected action through the shared dispatcher, and records the cooldown only after that route runs.

The German war-construction order is unavailable in peace, leaving the 1936 German network at its intended low priority until wartime conditions and later escalation support further construction.

The Soviet famine-pressure mission represents a relief deadline: removing either famine pressure or grain-extraction pressure completes the mission before its timeout.

## GUI Assets and Wiring

No new visual asset was required.

The completed panel reuses the existing Ledger asset family registered in `interface/camp_repression_rework.gfx`:

- `GFX_repression_ledger_tab_discovery` reads `gfx/interface/camp_repression/GFX_repression_ledger_tab_discovery.dds`.
- `GFX_repression_ledger_card_bg` reads `gfx/interface/camp_repression/GFX_repression_ledger_card_bg.dds`.
- `GFX_repression_ledger_evidence_seal_static` reads `gfx/interface/camp_repression/GFX_repression_ledger_evidence_seal_static.dds`.
- `GFX_repression_ledger_reform_seal_static` reads `gfx/interface/camp_repression/GFX_repression_ledger_reform_seal_static.dds`.
- `GFX_repression_ledger_action_button` reads `gfx/interface/camp_repression/GFX_repression_ledger_action_button.dds`.
- `GFX_camp_restricted_payload_texticon` reuses `gfx/interface/decisions/decision_chaos_doom.dds` for the exact restricted-payload cost line.

The category continues to use the existing `GFX_decision_category_repression_ledger` sprite.

## HOI4 MCP Evidence

The post-change GUI inspection completed for `repression_ledger_category_window` and `repression_ledger_window` under named current-layout scenarios.

The final category inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f1afef8e42da556ecad6b031986f53f1fafa4de7e401df0034cea9c2586587f9/5378150cbce4191e690a1384f4b60a690ece89d60af19fe9252d0ba7d755c5cc/gui-inspect.92f2da424dc00017.json`.

The final category render artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/329de700000bcf60f3ae6a5c6944feb02199e57371a007e6a3fa302231160374/d8fc1bb8fd30d75db270da174c73bd6d478cad2a721127b4b0fa88607cb68752/repression_ledger_category_window-full.svg`.

The final post-change full Ledger render covered normal, hover, selected, empty-list, full-list, long-text, and missing-localisation states at `1920x1080`, `1600x900`, `1366x768`, and `1280x720`.

Its full-state artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b0179a2e4c0df19f733c338fc2bdf7d696c1236dd7cad8fa8ea08fc1d146f48b/c72eb7b994372a5107551192d7564eb62f4e40e25f416d989f4771eb7668c6bd/repression_ledger_window-full.svg`.

The latest successful post-cost Ledger inspection artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93389e8403c4d0d12cd6bf7298f99f31f6cc38b10274e3b4a14aae9f5ad06e96/dc01afdd231d38eb710ba49d40cdcec73a938ac5b2c858a2af35cda1950f40d3/gui-inspect.8d6b6d473e40a3ba.json`.

The matching compact post-cost render artifact for normal, long-text, and missing-localisation review at `1920x1080` is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/125c3b778d52bee555772509f03a11c3fe23da527cd883fde7a3ee338475afbc/c7836af7bf903630ec97f86c24ef403f9e7b48032ac6d416fb6f1ea0366d1726/repression_ledger_window-full.svg`.

The country-system tab label received a bounded two-line text box after the localisation audit isolated the old 90-pixel box as the remaining likely overflow source.

The GUI source graph also reports repository-wide symbol collisions and unresolved references from unrelated interfaces, so its global validation result is not treated as a clean ledger-specific pass.

A final inspection and compact render retry after the restricted-payload localisation additions each reached the MCP's 180-second repository-graph limit without producing a newer artifact; those additions did not alter the GUI layout source.

`hoi4.gui_rewrite` was attempted with a valid source package and then with narrow hash-guarded scalar patches.

The source call returned no applied change, one unsafe full-line patch was correctly rejected, and two valid scalar patch calls timed out after 180 seconds without changing the source.

The final GUI source edit therefore used the normal repository patch workflow after the mandatory inspect, render, and rewrite attempts, followed by fresh post-change inspection and rendering.

Narrow event inspection completed for `japan_ishii.1` and `germany_mengele.1` and preserved their existing later-escalation chains.

The equivalent `soviet_gulag.1` inspection and all three neighborhood renders timed out at the MCP's 180-second tool boundary while rebuilding the repository-wide 9,510-event graph; this is recorded as a tooling boundary rather than event-chain validation evidence.

The weighted audit inspected the major-country, generic, crisis, and colonial decision sources and compared identical named 1936 and United Kingdom/Raj scenarios.

The German construction route is hard-unavailable in peace and retains its existing wartime AI score, the United Kingdom/Raj expansion order retains its existing conditional AI weights after losing the command-power gate, and the restricted-site custom cost trigger does not change its `ai_will_do` block.

The principal compare artifacts are `probability-12e49ed5bbb7ad85220be135` for the major-country pool and `probability-5b77bfe4a4ec9879226f03cd` for the United Kingdom/Raj pool.

Both comparisons are score and reachability evidence rather than historical deltas because the MCP accepted current source paths but no immutable pre-change revision.

## Future Plans

Later German events may activate additional historical sites and create the Auschwitz and experiment-program routes at their appropriate stages.

Later Japanese events may activate the North China record and develop Pingfang, army review, retreat, outbreak, and tribunal routes.

Later Soviet events may expand the gulag network, intensify quotas or famine pressure, expose records, provide relief, or begin reform and dismantlement.

Any future category presentation should preserve the decisions-skill rule against separator bars, telemetry dumps, fake textual layouts, raw implementation state, and unsafe country-specific localisation fallbacks.

## Simplifications, Omissions, and Blockers

No gameplay or interface surface requested by this correction was omitted, and no fallback presentation was introduced.

The remaining evidence boundaries are the recorded MCP graph timeouts, repository-wide GUI diagnostics outside this window, and the absence of an immutable pre-change probability snapshot for direct before-and-after comparison.
