# Event 006 FORM-05 decision body crosswalk (2026-09-20)

## Disposition

`IMPLEMENTED SOURCE AUDIT / NO SOURCE-SAFE PATCH`.

This parent-owned crosswalk closes the current source-level body audit for the FORM-05 Mediterranean Island League decision file. It does not promote the FORM-05 package, open FORM-07, or replace native decision-row, typed probability, live execution, or save/load evidence.

## Scope and references

The audited gameplay file is `common/decisions/006_independence_wave_form05_decisions.txt`.

The paired player-facing file is `localisation/english/006_independence_wave_form05_l_english.yml`.

The FORM-07 Iberian Federation is not a decision body in this file or in `common/decisions/006_independence_wave_formable_decisions.txt`; its current surface is a readiness-controlled formable trigger/effect registry and remains separately fail-closed under its accepted package, identity, member, flag, territory, integration, and probability gates.

## Body results

The file contains 16 entries: two automatic deadline missions and fourteen paid charter, membership, and integration actions.

The two deadline missions are `independence_wave_form05_charter_deadline` and `independence_wave_form05_complete_first_maritime_board`. Each has a player-facing name and description, an icon, an intentionally inactive `activation` and `available` gate, a timeout effect, a cancellation trigger, and `fire_only_once = no`. Their absence of a spendable cost and ordinary completion effect is intentional because they are timer consequences activated by the existing scripted lifecycle.

The eleven paid actions are `independence_wave_form05_petition_maritime_congress`, `independence_wave_form05_accept_charter_invitation`, `independence_wave_form05_withhold_charter_invitation`, `independence_wave_form05_chart_convoy_guarantees`, `independence_wave_form05_ratify_common_defense_protocol`, `independence_wave_form05_conclude_customs_convention`, `independence_wave_form05_settle_congress_seat`, `independence_wave_form05_proclaim_island_league`, `independence_wave_form05_reopen_maritime_congress`, `independence_wave_form05_establish_common_shipping_board`, `independence_wave_form05_link_coastal_warning_stations`, `independence_wave_form05_open_customs_clearinghouse`, `independence_wave_form05_ratify_first_maritime_board`, and `independence_wave_form05_reconvene_first_maritime_board`.

Every paid action has `name`, `desc`, `icon`, a visibility gate, an availability gate, a matching `custom_cost_trigger`, a `custom_cost_text`, a completion payment or action effect, a remove effect, a cancellation trigger, and an `ai_will_do` block.

The ordinary paid actions use the existing four-group resource palette and the shared payment helpers. The localized cost rows are icon-first and each paid cost has a matching `_tooltip` alias and `_blocked` red variant.

The two actions with explicit cancellation effects are the charter opening and charter reopening, each using the existing reservation-cancellation helper; the remaining paid actions intentionally close without a refund when their cancellation trigger becomes false. No missing refund or cleanup defect was proven by this source audit.

## Localisation crosswalk

A read-only key scan resolved all 16 entry names and descriptions, all explicit custom effect tooltips, and all 14 paid cost families with zero missing keys.

The localization file contains 152 unique keys, has the required UTF-8 BOM, and contains no duplicate key in the audited surface.

The source-to-localization audit therefore found no safe gameplay, lifecycle, cost, AI, or player-facing wording patch.

## Validation boundary

This audit is source evidence only. The installed HOI4 MCP does not provide native decision-row rendering for this body, the current typed probability fixtures cannot bind all campaign inputs, and no live execution or save/load evidence is claimed.

The current Event 006 authority remains `HOLD / PARTIAL` with central admission at 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows.

No gameplay, localisation, asset, GUI, spreadsheet, registry, or package-admission file was changed by this audit.
