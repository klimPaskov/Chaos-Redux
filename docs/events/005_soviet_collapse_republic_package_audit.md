# Event 005 Soviet Collapse Republic Package Audit

Audit date: 2026-05-21

## Scope

This audit covers the ordinary and vanilla-supported internal republic tags required by the final clean merged Event 005 package. It verifies the country-package surface for each tag that can be created or freed by Soviet Collapse release logic:

- ordinary republics: `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`
- internal republics: `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, `TAN`

The tags are vanilla country tags. Event 005 does not redefine their base country files; it uses vanilla tag registration, vanilla history, vanilla country localisation, and vanilla flag assets, then adds the crisis package at runtime.

## Shared Runtime Package

Every event-created republic in this audit receives the shared breakaway country setup through `soviet_collapse_setup_breakaway_country` and `soviet_collapse_apply_breakaway_setup_package`.

The shared package:

- sets `soviet_collapse_breakaway`
- adds the country to `global.soviet_collapse_breakaway_countries`
- increments global and Soviet breakaway counters
- applies dynamic manpower and equipment packages from `constant:soviet_collapse_breakaway_support.*`
- applies major, regional, chaos-tier, Soviet-war, weak-center, depot-pressure, foreign-access, preempted-declaration, emboldened-declaration, and terminal modifiers where relevant
- clamps starting field units
- adds `soviet_collapse_republican_startup_disorder`
- initializes recovery, institution, league-support, and local-authority variables
- creates the locked `Emergency Republican Guard` and `Emergency Republican Field Brigade` templates
- creates dynamic starting units at the capital through `meta_effect`
- fires the first dynamic-unit explanation report once per campaign
- fires the internal-republic sovereignty news event once for internal republic tags

Terminal release logic covers both unreleased tags and existing Soviet republican subjects:

- unreleased tags are released by `SOV = { release = PREV }`, marked `soviet_collapse_event_created_republic`, given the setup package, and routed through focus-tree loading
- existing Soviet subjects are freed with `set_autonomy = { target = PREV autonomy_state = autonomy_free }`, marked as event-created republics for Event 005 crisis integration, given the setup package, and routed through focus-tree loading

## Per-Tag Checklist

| Tag | Package type | Vanilla country surface | Event 005 release and setup | Focus-tree package | League/news integration | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `UKR` | ordinary major republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package with major breakaway bonuses. | `soviet_collapse_ukraine_focus_tree` with 81 focuses. | Free Republics' League and foreign-recognition paths; ordinary release reporting uses normal events/news. | complete |
| `BLR` | ordinary regional republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package with regional breakaway bonuses. | `soviet_collapse_belarus_focus_tree` with 53 focuses. | Free Republics' League and foreign-recognition paths; ordinary release reporting uses normal events/news. | complete |
| `KAZ` | ordinary major republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package with major breakaway bonuses; also has the Kazakhstan-after-Central-Asian-cascade release path. | `soviet_collapse_kazakhstan_focus_tree` with 92 focuses. | Central Asian League, Free Republics' League, and foreign-recognition paths; ordinary release reporting uses normal events/news. | complete |
| `MOL` | ordinary regional republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package. | `soviet_collapse_moldova_focus_tree` with 48 focuses. | Eastern Buffer/Free Republics' League style integration and foreign-recognition paths; ordinary release reporting uses normal events/news. | complete |
| `LIT` | Baltic ordinary republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package with regional breakaway bonuses. | `soviet_collapse_baltic_focus_tree` with 42 focuses and Lithuania-gated content. | Baltic League, Free Republics' League, and foreign-recognition paths; ordinary league presentation uses news/report events. | complete |
| `LAT` | Baltic ordinary republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package with regional breakaway bonuses. | `soviet_collapse_baltic_focus_tree` with 42 focuses and Latvia-gated content. | Baltic League, Free Republics' League, and foreign-recognition paths; ordinary league presentation uses news/report events. | complete |
| `EST` | Baltic ordinary republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package with regional breakaway bonuses. | `soviet_collapse_baltic_focus_tree` with 42 focuses and Estonia-gated content. | Baltic League, Free Republics' League, and foreign-recognition paths; ordinary league presentation uses news/report events. | complete |
| `GEO` | Caucasus ordinary republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package with regional breakaway bonuses. | `soviet_collapse_caucasus_focus_tree` with 40 focuses and Georgia-gated content. | Caucasus League, Free Republics' League, and foreign-recognition paths; ordinary league presentation uses news/report events. | complete |
| `ARM` | Caucasus ordinary republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package. | `soviet_collapse_caucasus_focus_tree` with 40 focuses and Armenia-gated content. | Caucasus League, Free Republics' League, and foreign-recognition paths; ordinary league presentation uses news/report events. | complete |
| `AZR` | Caucasus ordinary republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package with regional breakaway bonuses. | `soviet_collapse_caucasus_focus_tree` with 40 focuses and Azerbaijan-gated content. | Caucasus League, Free Republics' League, and foreign-recognition paths; ordinary league presentation uses news/report events. | complete |
| `UZB` | Central Asian ordinary republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package with regional breakaway bonuses. | `soviet_collapse_central_asia_focus_tree` with 45 focuses and Uzbekistan-gated content. | Central Asian League, Free Republics' League, and foreign-recognition paths; ordinary league presentation uses news/report events. | complete |
| `KYR` | Central Asian ordinary republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package. | `soviet_collapse_central_asia_focus_tree` with 45 focuses and Kyrgyz-gated content. | Central Asian League, Free Republics' League, and foreign-recognition paths; ordinary league presentation uses news/report events. | complete |
| `TAJ` | Central Asian ordinary republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package. | `soviet_collapse_central_asia_focus_tree` with 45 focuses and Tajik-gated content. | Central Asian League, Free Republics' League, and foreign-recognition paths; ordinary league presentation uses news/report events. | complete |
| `TMS` | Central Asian ordinary republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package. | `soviet_collapse_central_asia_focus_tree` with 45 focuses and Turkmen-gated content. | Central Asian League, Free Republics' League, and foreign-recognition paths; ordinary league presentation uses news/report events. | complete |
| `KAR` | internal republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package and internal-sovereignty news. | `soviet_collapse_internal_republic_focus_tree` with 62 focuses and Karelian-gated content. | Internal sovereignty news and Free Republics' League/foreign-recognition paths. | complete |
| `KOM` | internal republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package and internal-sovereignty news. | `soviet_collapse_internal_republic_focus_tree` with 62 focuses and Komi-gated content. | Internal sovereignty news and Free Republics' League/foreign-recognition paths. | complete |
| `CRI` | internal republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package and internal-sovereignty news. | `soviet_collapse_internal_republic_focus_tree` with 62 focuses and Crimean-gated content. | Internal sovereignty news and Free Republics' League/foreign-recognition paths. | complete |
| `TAT` | internal republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package and internal-sovereignty news. | `soviet_collapse_internal_republic_focus_tree` with 62 focuses and Tatar/Idel-Ural-gated content. | Internal sovereignty news and Free Republics' League/foreign-recognition paths. | complete |
| `BSK` | internal republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package and internal-sovereignty news. | `soviet_collapse_internal_republic_focus_tree` with 62 focuses and Bashkir-gated content. | Internal sovereignty news and Free Republics' League/foreign-recognition paths. | complete |
| `FER` | internal/Far Eastern republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package and internal-sovereignty news. | `soviet_collapse_internal_republic_focus_tree` with 62 focuses and Far Eastern-gated content. | Internal sovereignty news and Free Republics' League/foreign-recognition paths. | complete |
| `YAK` | internal republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package and internal-sovereignty news. | `soviet_collapse_internal_republic_focus_tree` with 62 focuses and Yakut-gated content. | Internal sovereignty news and Free Republics' League/foreign-recognition paths. | complete |
| `BYA` | internal republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package and internal-sovereignty news. | `soviet_collapse_internal_republic_focus_tree` with 62 focuses and Buryat-gated content. | Internal sovereignty news and Free Republics' League/foreign-recognition paths. | complete |
| `TAN` | internal/Inner Asian republic | Vanilla tag, history, country localisation, and large/medium/small flag variants verified. | Included in terminal release and subject-freeing lists; receives shared setup package and internal-sovereignty news. | `soviet_collapse_internal_republic_focus_tree` with 62 focuses and Tuvan-gated content. | Internal sovereignty news and Free Republics' League/foreign-recognition paths. | complete |

## Evidence Commands

```text
for tag in UKR BLR KAZ MOL LIT LAT EST GEO ARM AZR UZB KYR TAJ TMS KAR KOM CRI TAT BSK FER YAK BYA TAN; do
	printf '%s|' "$tag"
	rg -n "^${tag}\s*=" "$HOME/projects/Hearts of Iron IV/common/country_tags" common/country_tags 2>/dev/null | head -1
	ls "$HOME/projects/Hearts of Iron IV/history/countries"/${tag}* 2>/dev/null | head -1
done

for tag in UKR BLR KAZ MOL LIT LAT EST GEO ARM AZR UZB KYR TAJ TMS KAR KOM CRI TAT BSK FER YAK BYA TAN; do
	rg -n "^[[:space:]]+${tag}(_fascism|_democratic|_neutrality|_communism|_fascism_DEF|_democratic_DEF|_neutrality_DEF|_communism_DEF|_fascism_ADJ|_democratic_ADJ|_neutrality_ADJ|_communism_ADJ|_DEF|_ADJ)?:[0-9]" "$HOME/projects/Hearts of Iron IV/localisation/english/countries_l_english.yml" | wc -l
done

for tag in UKR BLR KAZ MOL LIT LAT EST GEO ARM AZR UZB KYR TAJ TMS KAR KOM CRI TAT BSK FER YAK BYA TAN; do
	find "$HOME/projects/Hearts of Iron IV/gfx/flags" -maxdepth 1 \( -name "${tag}.tga" -o -name "${tag}_*.tga" \) | wc -l
	find "$HOME/projects/Hearts of Iron IV/gfx/flags/medium" -maxdepth 1 \( -name "${tag}.tga" -o -name "${tag}_*.tga" \) | wc -l
	find "$HOME/projects/Hearts of Iron IV/gfx/flags/small" -maxdepth 1 \( -name "${tag}.tga" -o -name "${tag}_*.tga" \) | wc -l
done

awk '/^\tfocus_tree = \{/ {tree=""} /^\tid = / {tree=$3} /focus = \{/ {count[tree]++} END {for (t in count) print t, count[t]}' common/national_focus/005_soviet_collapse_republics.txt | sort

rg -n "soviet_collapse_release_terminal_ordinary_republics|soviet_collapse_setup_breakaway_country|soviet_collapse_apply_breakaway_setup_package|soviet_collapse_load_event_created_focus_tree|chaosx.nr5.47|chaosx.nr5.48|chaosx.nr5.49|chaosx.nr5.95" common/scripted_effects/005_soviet_collapse_effects.txt events/005_soviet_collapse.txt localisation/english/005_soviet_collapse_l_english.yml
```

Key results from the current audit:

- all 23 audited tags have vanilla country-tag registrations and vanilla country history files
- all 23 audited tags have vanilla country localisation entries
- all 23 audited tags have large, medium, and small vanilla flag variants
- terminal release and Soviet-subject freeing lists include all 23 audited tags
- all 23 audited tags are excluded from the generic fallback focus loader and routed into a bespoke or region/internal shared Event 005 tree
- `chaosx.nr5.47`, `.48`, `.49`, and `.95` provide normal event/news coverage for dynamic unit explanation, league membership expansion, public foreign recognition, and internal sovereignty

## Remaining Notes

This audit proves the ordinary/internal republic package checklist that was previously missing from the implementation ledger. It does not close unrelated open rows for high-chaos splinter packages, achievement placeholder art, broader AI strategy review, final asset reconciliation, or final live-session validation.
