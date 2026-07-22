# Event 006 IW-017 / IW-019 country-package audit

Date: 2026-07-22
Owner: country-package audit subagent
Scope: canonical IW-017 Corsica (`COR`) and IW-019 Sicily (`ASX`); static
country-package, map-binding, setup, force, politics, focus, decision, event,
AI, formable, localisation, and sourced-portrait checks. This handoff does not
admit a package, change runtime content attestation, edit the tag-audit tool or
reports, edit portrait sources/manifests/DDS files, or write map data.

## Canonical IDs and verdict

The task wording named “IW-016 COR” and “IW-017 ASX”. The accepted registry,
specification, and current runtime dispatch are authoritative instead:

| Accepted package | Tag | Identity | Anchor | Reservation |
|---|---|---|---:|---|
| IW-017 | `COR` | Corsica | state 1 | `RG-1` |
| IW-019 | `ASX` | Sicily | state 115 | `RG-115` |

IW-016 is Occitania (`OCC`), not Corsica. The correction is recorded here so a
future audit does not accidentally bind the wrong package.

Static package coverage is complete for both canonical packages after the
narrow history repair below. Both remain fail-closed: the compile-time Event
006 runtime-content attestation set is empty and the relevant admission/readiness
wrapper still resolves to `always = no`. This audit therefore makes no runtime
admission or campaign-completion claim.

## Changed gameplay file

`history/countries/ASX - Sicily.txt:17-21`

- Before: `recruit_character = ASX_salvatore_licata` referenced a character that
  is not defined anywhere in the active character package.
- After: `recruit_character = ASX_luigi_rizzo` matches the current sourced
  Sicilian straits-security commander and the exact roster trigger.

This restores the ASX history shell's five-character roster proof. The shell
still intentionally has no capital, state ownership, politics, focus tree, or
forces; the Event 006 setup transaction owns those runtime operations.

## Country-package coverage checklist

| Surface | IW-017 `COR` | IW-019 `ASX` | Result |
|---|---|---|---|
| Tag and identity | Vanilla `COR` remains guarded by `original_tag = COR`; package id is `constant:independence_wave_package_id.iw_017` | `common/country_tags/006_independence_wave_countries.txt:21` maps `ASX` to the Sicily shell; package id is `.iw_019` | PASS |
| State/capital binding | `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt:155-166` requires anchor/capital state 1, owned and controlled, with a living former host | Same file `:185-199` requires anchor/capital state 115, owned and controlled, with a living former host | PASS in source; no map write performed |
| Installed map facts | Vanilla state 1 (`history/states/1-France.txt`) is Corsica, owner `FRA`, core `COR`, VP 3838, naval base 3 | Vanilla state 115 (`history/states/115-Sicily.txt`) is Sicily, owner `ITA`, cores `ITA`/`TTS`, Palermo and multiple naval bases/air base | PASS |
| Host protection | Prepared triggers require the saved former host to exist, differ from `ROOT`, and retain its protected release state | Same protected-remnant proof | PASS in source |
| Baseline laws | Setup adds/ensures `civilian_economy`, `export_focus`, `volunteer_only` | History already adds these; setup reasserts them | PASS |
| Politics and parties | Setup starts democratic/elections allowed, 46/14/32/8 popularity; route party names are regional Corsican names | Setup starts democratic/elections allowed, 38/20/34/8 popularity; party names are Sicilian civic, labor, crown, security, and mandate names | PASS |
| Package value | `independence_wave_cor_maritime_access` starts 30 and stabilizes at 65 | `independence_wave_asx_port_authority` starts 22 and stabilizes at 70 | PASS |
| Starting ideas | `cor_exposed_island_supply` (or mature `cor_civic_coastal_compact`) and route swaps are exact-tag guarded | `asx_contested_port_authority` (or mature `asx_trinacrian_state_compact`) and route swaps are exact-tag guarded | PASS |
| Leaders/roster | Adolphe Landry civic congress; Jean Chiappe civilian/army security commander; portraitless advisors Paolo Pietri and Antone Rocchi | Luigi Sturzo provisional assembly; Pietro Lanza di Scalea crown council; Luigi Rizzo civilian/army straits commander; portraitless advisors Giuseppe Lo Giudice and Leone Messina | PASS; all active real leaders are male and sourced |
| Focus framework | Exact `independence_wave_focus_tree` full-framework assignment, five COR extension focuses, popular/radical routes explicitly excluded | Exact same tree, eight ASX extension focuses, constitutional/popular/traditional/emergency/patron routes enabled and radical explicitly excluded | PASS |
| Decisions/mission | COR category has eight projects plus founding mission, all package guarded and costed | ASX category has ten projects plus founding mission, all package guarded and costed | PASS |
| Incidents | Founding `chaosx.nr6.21`, route `chaosx.nr6.24`; scheduled only by exact COR setup | Founding `chaosx.nr6.23`, route `chaosx.nr6.26`, ambition `chaosx.nr6.27`; all exact ASX setup/choice guarded | PASS |
| AI | `common/ai_strategy/006_independence_wave_mediterranean.txt` uses `original_tag = COR`, exact package trigger, setup flag, survival/host-threat/route priorities | Same with `original_tag = ASX`, port/straits/dossier priorities | PASS; no world iteration |
| Host diplomacy | Negotiation, guarded-frontier, association, and reclamation routes are all registered; former-host settlement effects are bilateral and gated | Same; ASX has an explicit Italian property decision | PASS |
| FORM-05 and ambition | Mediterranean island league family, FORM-05 candidate/delegation flags, and ambition family are registered | Same, plus Two Sicilies dossier/republic choice and claims on 117/156 only after the dossier focus | PASS; shared FORM-05 remains separately fail-closed |
| Cleanup | Removes COR mission/decisions/ideas/flags, restores `generic_focus` only when the Event 006 tree is active, retires four COR characters | Removes ASX mission/decisions/ideas/flags, removes claims on 117/156, leaves history-owned dormant roster | PASS |

## Portrait and identity gate

The current sourced roster is wired to five large-only sprites:

| Character | GFX token | DDS |
|---|---|---|
| `COR_corsican_municipal_congress` / Adolphe Landry | `GFX_portrait_COR_independence_wave_adolphe_landry` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_adolphe_landry.dds` |
| `COR_jean_chiappe` / Jean Chiappe | `GFX_portrait_COR_independence_wave_jean_chiappe` | `gfx/leaders/006_independence_wave/portrait_COR_independence_wave_jean_chiappe.dds` |
| `ASX_sicilian_provisional_assembly` / Luigi Sturzo | `GFX_portrait_ASX_independence_wave_luigi_sturzo` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_sturzo.dds` |
| `ASX_sicilian_crown_council` / Pietro Lanza di Scalea | `GFX_portrait_ASX_independence_wave_pietro_lanza_di_scalea` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_pietro_lanza_di_scalea.dds` |
| `ASX_luigi_rizzo` / Luigi Rizzo | `GFX_portrait_ASX_independence_wave_luigi_rizzo` | `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_luigi_rizzo.dds` |

`interface/006_independence_wave_mediterranean_portraits.gfx` registers all
five tokens and each DDS path exists. There are no advisor, high-command,
officer-corps, dossier, commander-miniature, or `_small` consumers. Advisors
are intentionally portraitless under the current Event 006 asset boundary;
no advisor icons were created.

The installed vanilla Italy focus uses the literal string `Luigi Rizzo` only as
an `add_equipment_production` ship-line name at
`common/national_focus/italy.txt:7862,7938`. The installed vanilla build has no
`ITA_luigi_rizzo` character, leader portrait, or interface/GFX consumer. This is
not an active person/portrait ownership collision with the scoped
`ASX_luigi_rizzo` character. Source approval remains read-only and does not
re-admit ASX.

## Localisation and visible asset checks

- `localisation/english/006_independence_wave_mediterranean_l_english.yml`
  contains 310 unique keys. Character names/descriptions, party names, ideas,
  decision names/descriptions/tooltips, focus tooltips, event title/description/
  options, and package values referenced by the COR/ASX sources are covered.
- `localisation/english/006_independence_wave_countries_l_english.yml` contains
  the complete ASX name/adjective and ideology variants; COR uses vanilla
  country localisation plus the Event 006 party/route keys.
- All 60 focus/decision icon tokens referenced by the package sources resolve to
  defined sprites with existing textures. The event report picture also
  resolves to a defined sprite.

## Starting forces, technology, industry, and supply

`docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` binds:

- IW-017/COR to `coastal_maritime`, military tradition 53, navy inheritance,
  no air inheritance, and mountain/coastal infantry reinforcement paths.
- IW-019/ASX to `regular_defectors`, military tradition 65, navy and air
  inheritance, and coastal infantry/defector/port-defense paths.

The setup adapters load the exact mapping only after the command roster proof,
then call the shared generation-bound force transaction. That transaction
inherits former-host technology and research slots, creates the profile-specific
opening template/divisions, adds infantry/support/artillery/train/truck/convoy
stockpiles and fuel, and transfers only the approved navy/air fractions. The
prepared triggers require the exact package mapping, current generation, force
application flag, AI profile, lifecycle flag, and starting idea before setup can
publish completion.

## Validation evidence

Read-only checks run for this audit:

1. `python .tools/audit_event6_allocator.py` — passed (`149` publishers,
   `126` automatic/high-chaos selectable packages, `138` ranked selectable
   packages; Event 005 anchors precede Event 006 anchors in the joint order).
2. Decision source reference parser — 81 distinct player-facing keys, 0 missing
   English localisation keys.
3. Event source reference parser — 7 events, 42 distinct title/description/
   option/tooltip keys, 0 missing English localisation keys; report picture
   defined.
4. Focus/decision asset parser — 60 referenced GFX tokens, 0 missing sprite
   definitions or textures.
5. Character-reference parser — all active COR/ARX/ASX character references
   resolve to definitions; no active `COR_pasquale_venturi` or
   `ASX_salvatore_licata` references remain in gameplay/history/localisation/
   events/interface/GFX.
6. Installed-map inspection — state 1 and state 115 facts above match the
   installed vanilla state history. No `hoi4.map_rewrite` or other map write
   was used.

Live game loading, campaign execution, and runtime attestation were not run;
the parent task explicitly keeps runtime content attestation closed.

## Remaining risks, omissions, and blockers

- No runtime admission is granted. The compile-time content-attestation set is
  empty and the current readiness wrapper remains `always = no`.
- Older out-of-scope portrait inventories, source manifests, and earlier
  handoffs still contain archived `COR_pasquale_venturi`/
  `ASX_salvatore_licata` names and superseded role wording. Active gameplay is
  clean; those documentation/asset records were intentionally not edited in
  this country-package scope.
- The prompt's IW-016/IW-017 country numbering was corrected above to the
  accepted IW-017/IW-019 bindings.
- No fallback, generated portrait, invented leader, advisor icon, map edit, or
  broad identity/focus redesign was introduced. A fresh admission audit remains
  necessary after the parent enables runtime attestation.

## Files changed by this subagent

- `history/countries/ASX - Sicily.txt`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw017_iw019_country_package_audit_2026_07_22.md`

No other gameplay, localisation, asset, manifest, spreadsheet, tag-audit, or
consolidated-document files were changed for this audit.
