# Historical CBRN scientists

## Overview

Chaos Redux provides a static roster of 67 historical scientists for the chemical-warfare and biological-warfare special-project specializations.

Fifteen dual-role characters live in `common/characters/cbrn_historical_specialists.txt`, while 52 scientist-only characters live in `common/characters/cbrn_historical_scientists.txt`.

History initialization assigns 38 identities to their home countries and 29 date-gated identities to stateless `CSH`. The existing bounded country callbacks transfer held identities to their fixed home tags on the same dates through country-scoped `set_nationality`; they never attempt runtime recruitment. The [dated-holder contract](cbrn_dated_scientist_transfers.md) preserves all date, retirement, trait, and `chaosx_scientist_*` flag logic. The user-run November 1936 baseline confirmed Fishman on SOV before this correction; the holder route still awaits fresh live-QA evidence at both bookmarks. All 67 identities have exactly one history-time recruitment declaration.

## Historical calibration

Ratings represent the scientist's demonstrated expertise, program responsibility, and practical relevance during the late interwar and Second World War period rather than fame alone.

The file-scoped rating scale is inexperienced `1`, skilled `2`, experienced `3`, and expert `4`.

Skill 4 is reserved for major field authorities or scientists whose own work decisively established a method or capability; program administration alone does not establish expert research skill.

Skill 1 identifies administrators or perpetrators whose direct scientific record does not justify a higher rating, even when the supplied portrait or historical connection warranted inclusion in the requested roster.

No scientist receives skill 5.

Traits use the existing vanilla scientist vocabulary plus `scientist_trait_inhumane` and `scientist_trait_inhumane_cw` for historically documented coercive human experimentation.

The inhumane traits describe method and conduct, not greater historical stature; low-skill perpetrators remain low-skill even when that trait is present. The roster table identifies later awards by date rather than implying the trait exists at recruitment.

## Roster

| Country | Scientist | Specialization | Skill | Traits |
| --- | --- | --- | ---: | --- |
| Australia | Howard Walter Florey | Biological warfare | 4 | Brilliant Theorist, Resourceful |
| Australia | Charles Kellaway | Chemical warfare | 3 | Bright, Resourceful |
| Australia | Frank Macfarlane Burnet | Biological warfare | 4 | Brilliant Theorist, Fast Learner |
| Canada | Otto Maass | Chemical warfare | 3 | Brilliant Theorist, Resourceful |
| Canada | Frederick Banting | Chemical warfare | 4 | Brilliant Theorist, Bright |
| Canada | Claude E. Dolman | Biological warfare | 3 | Bright, Resourceful |
| United Kingdom | Paul Fildes | Biological warfare | 4 | Brilliant Theorist, Resourceful |
| United Kingdom | Alexander Fleming | Biological warfare | 3 | Bright |
| United Kingdom | Ernst Chain | Biological warfare | 4 | Brilliant Theorist, Gifted Engineer |
| United Kingdom | Charles Lovatt Evans | Chemical warfare | 4 | Brilliant Theorist, Resourceful |
| United Kingdom | Harold Hartley | Chemical warfare | 4 | Brilliant Theorist, Resourceful |
| United Kingdom | John Scott Haldane | Chemical warfare | 4 | Gifted Engineer, Resourceful |
| United Kingdom | Joseph Barcroft | Chemical warfare | 4 | Brilliant Theorist, Resourceful |
| United Kingdom | Rudolph Peters | Chemical warfare | 4 | Gifted Engineer, Resourceful |
| United Kingdom | Edward Abraham | Biological warfare | 3 | Gifted Engineer, Brilliant Theorist |
| United Kingdom | Norman Heatley | Biological warfare | 3 | Gifted Engineer, Resourceful |
| United Kingdom | Patrick Laidlaw | Biological warfare | 4 | Brilliant Theorist, Fast Learner |
| United Kingdom | B. C. J. G. Knight | Biological warfare | 3 | Resourceful, Gifted Engineer |
| United Kingdom | David W. W. Henderson | Biological warfare | 4 | Brilliant Theorist, Resourceful |
| United Kingdom | Donald D. Woods | Biological warfare | 3 | Brilliant Theorist, Bright |
| France | Charles Dufraisse | Chemical warfare | 3 | Brilliant Theorist, Gifted Engineer |
| France | Paul Lebeau | Chemical warfare | 4 | Gifted Engineer, Resourceful |
| Germany | Gerhard Schrader | Chemical warfare | 3 | Brilliant Theorist |
| Germany | Kurt Blome | Biological warfare | 3 | None |
| Germany | Walter Schreiber | Biological warfare | 2 | None |
| Germany | Erich Traub | Biological warfare | 3 | Gifted Engineer |
| Germany | Kurt Gutzeit | Biological warfare | 1 | Inhumane |
| Germany | Sigmund Rascher | Biological warfare | 1 | Inhumane |
| Germany | Josef Mengele | Biological warfare | 1 | Inhumane |
| Germany | August Hirt | Chemical warfare | 1 | Inhumane CW from 25 November 1942 |
| Germany | Ferdinand Flury | Chemical warfare | 3 | Bright |
| Germany | Otto Ambros | Chemical warfare | 3 | Gifted Engineer |
| Germany | Otto Bickenbach | Chemical warfare | 2 | Inhumane CW from 1 June 1943 |
| Germany | Richard Kuhn | Chemical warfare | 4 | Genius |
| Germany | Gerhard Rose | Biological warfare | 3 | Bright; Inhumane from 17 April 1942 |
| Germany | Joachim Mrugowsky | Biological warfare | 3 | Inhumane from 29 December 1941 |
| Germany | Erwin Ding-Schuler | Biological warfare | 2 | Inhumane |
| Japan | Shiro Ishii | Biological warfare | 3 | Resourceful, Inhumane |
| Japan | Masaji Kitano | Biological warfare | 3 | Bright, Inhumane |
| Japan | Chikahiko Koizumi | Chemical warfare | 3 | None |
| Japan | Ryoichi Naito | Biological warfare | 3 | Bright, Resourceful |
| Poland | Franciszek Witaszek | Biological warfare | 2 | Resourceful |
| Poland | Rudolf Weigl | Biological warfare | 4 | Bright, Resourceful |
| Poland | Ludwik Fleck | Biological warfare | 3 | Bright, Resourceful |
| Soviet Union | Grigory Mairanovsky | Chemical warfare | 2 | Inhumane CW |
| Soviet Union | Ivan Mikhailovich Velikanov | Biological warfare | 4 | Brilliant Theorist, Resourceful |
| Soviet Union | Lavrentiy Pavlovich Beria | Biological warfare | 1 | None |
| Soviet Union | Georgy Gause | Biological warfare | 3 | Bright, Resourceful |
| Soviet Union | Nikolai Ginsburg | Biological warfare | 3 | Brilliant Theorist, Resourceful |
| Soviet Union | Sergei Muromtsev | Chemical warfare | 3 | None; field-specific skill source unresolved |
| Soviet Union | Zinaida Yermolyeva | Biological warfare | 4 | Bright, Resourceful |
| Soviet Union | Nikolay Zelinsky | Chemical warfare | 4 | Bright, Gifted Engineer |
| Soviet Union | Yakov Fishman | Chemical warfare | 3 | Resourceful |
| United States | Frank Olson | Biological warfare | 3 | Bright |
| United States | Ira Baldwin | Biological warfare | 4 | Resourceful, Gifted Engineer |
| United States | Murray Sanders | Biological warfare | 3 | Bright, Resourceful |
| United States | Stanhope Bayne-Jones | Biological warfare | 3 | Bright, Resourceful |
| United States | William A. Hagan | Biological warfare | 3 | Gifted Engineer, Resourceful |
| United States | Karl Friedrich Meyer | Biological warfare | 4 | Brilliant Theorist, Resourceful |
| United States | Theodor Rosebury | Biological warfare | 3 | Bright, Gifted Engineer |
| United States | Edwin Broun Fred | Biological warfare | 3 | Brilliant Theorist, Resourceful |
| United States | George W. Merck | Biological warfare | 2 | Resourceful |
| United States | James Stevens Simmons | Biological warfare | 4 | Brilliant Theorist, Resourceful |
| United States | Cornelius P. Rhoads | Chemical warfare | 4 | Bright, Resourceful |
| United States | Dean S. Tarbell | Chemical warfare | 2 | Bright |
| United States | James B. Conant | Chemical warfare | 4 | Genius, Brilliant Theorist |
| United States | Winford Lee Lewis | Chemical warfare | 4 | Gifted Engineer, Brilliant Theorist |

Kuhn's source-supported chemical-warfare access begins through the GER-only callback on 1 January 1940, not at the 1936 static start. Merck retains his 1942 recruitment floor while the [individual calibration](../../specs/chaos_warfare_system_specs/corrections/2026-09-27_george_w_merck_scientist_calibration.md) represents his industrial research leadership at biological skill 2 rather than expert pathogen research.

## Startup behavior

The established `on_startup` dispatcher continues to call country-scoped grant effects; no world-iteration on action was added. The dated roster repair uses country-specific `on_daily_AST`, `on_daily_CAN`, `on_daily_ENG`, `on_daily_GER`, `on_daily_JAP`, `on_daily_POL`, `on_daily_SOV`, and `on_daily_USA` callbacks in `common/on_actions/cbrn_historical_startup_on_actions.txt`.

Each relevant grant recruits the prewar/established characters exactly once after confirming that the country exists. Dated helpers guard every later recruitment with `has_character` and the current date, then write the identity flag after the character exists.

Eligible prewar expertise is available at the applicable scenario start, while later wartime identities enter the scientist pool on documented or explicitly calibrated dates. Kellaway opens in 1942, Banting in 1940, Henderson in June 1940, Hirt on 25 November 1942, Rhoads on 30 March 1943, and Tarbell in 1942; Haldane, Fishman, and Velikanov are excluded from the August 1939 start under their source-supported lifecycle limits. Scientist availability remains separate from offensive authorization. The [lifecycle](../../specs/chaos_warfare_system_specs/corrections/2026-09-27_scientist_lifecycle_and_field.md), [Allied chronology](../../specs/chaos_warfare_system_specs/corrections/2026-09-27_allied_scientist_wartime_recruitment.md), and [German, Soviet, and American calibration](../../specs/chaos_warfare_system_specs/corrections/2026-09-27_german_american_scientist_calibration.md) notes give the acceptance basis, source distinctions, and unresolved person-specific questions.

The dual-role advisor cards use current-date gates for their documented or calibrated appointments: Paul Fildes from 1 January 1940, Gerhard Schrader after 31 December 1936, Kurt Blome from 1 July 1943, Masaji Kitano after 1 January 1942, Franciszek Witaszek from 1 July 1940, Grigory Mairanovsky from 1 January 1938, Frank Olson from 1 January 1943, and Ira Baldwin after 1 January 1942. Fildes remains available as a scientist at the 1939 bookmark; only his Porton Down biological-warfare advisor appointment waits for the department's 1940 establishment. Olson's advisor role is Aerobiology Specialist, while his scientist skill remains 3.

Howard Florey and Alexander Fleming remain available as medical countermeasure advisors, while Shiro Ishii has an established prewar command role. Ivan Mikhailovich Velikanov remains eligible for his prewar research role only at the January 1936 start, consistent with the documented April 1938 death used for the August 1939 bookmark exclusion.

## Defensive appointments

These appointments use existing scientists and remain available without Chaos Warfare or an offensive-use policy. Each costs 100 Political Power and occupies a political-advisor slot, so appointing one displaces another advisor rather than supplying a free permanent layer.

| Advisor | Historical basis | Appointment gate | Conditional contribution |
| --- | --- | --- | --- |
| Nikolay Zelinsky, Soviet Union | [Russian Academy of Sciences institute history](https://zioc.ru/institute/zelinskij-n.-d) documents his activated-carbon respirator work and production before the 1936 start. | Collective Protection Systems project. | Issued military respirators reduce military casualties from chemical exposure by 3%; civilian protection and crate consumption are unchanged. |
| Norman Heatley, United Kingdom | [Oxford History of Science Museum](https://www.mhs.ox.ac.uk/backfromthedead/exhibition/production/index.html) documents the 1940 penicillin production apparatus and 1941 scale-up. | After 1939 and Field Antibiotics project. | Active anthrax, plague, or tularemia antibiotic courses reduce medical saturation by a further 5%; smallpox receives no antibiotic benefit. |
| Stanhope Bayne-Jones, United States | [National Library of Medicine](https://findingaids.nlm.nih.gov/repositories/4/resources/969) dates his wartime epidemiological and preventive-medicine service to 1941–42. | After 1941 and Mass Vaccine Production project. | An active Surveillance Network reduces outbreak growth by a further 5%. |

The medical and outbreak bonuses enter the existing response floors, which cap the added protection from combined response sources. Zelinsky's chemical contribution enters the existing mask-anchored casualty floor; no mask-replacement multiplier is added.

The new small advisor cards belong under `gfx/interface/advisors/cbrn/` and use `GFX_idea_ENG_norman_heatley`, `GFX_idea_SOV_nikolay_zelinsky`, and `GFX_idea_USA_stanhope_bayne_jones` in `interface/cbrn_historical_advisors.gfx`. The approved full scientist portraits remain the source for these cards; the final DDS cards and sprite entries must be checked against the active advisor consumer before this appointment package is claimed complete.

Future work can give operational logistics a distinct appointment once a non-duplicative bounded effect and source-supported candidate are established. The roster's remaining individual skill/date reviews and native AI appointment ranking remain separately open.

Both historical bookmarks mark every country in the starting mask matrix for force-scaled reconciliation: established majors use a 75% military issue target, Italy 100%, Japan 50%, and all remaining profile tags 25%, with a separate 25% replacement reserve and zero fixed civilian distribution. Each bookmark measures its own deployed force. The common profile retains knowledge and program identity but suppresses archival fixed stock and civilian issue; the startup effect snapshots pre-existing mask models and issues the active band from real stock, with ENG using the shared core helper for the same transaction. The 1939 British startup writes `cbrn_historical_civilian_mask_issue` and `cbrn_uk_1939_mass_respirator_issue`, passes the 40,000-crate civilian respirator assumption to the core CBRN profile owner, and queues ENG-root `cbrn_protection.3` so the inclusive target is reconciled against real stock above the military reserve once. The shared percentages are a gameplay calibration accepted by the user on 2026-09-25, not claims about exact historical inventory.

The U.S. 1939 startup also knows `phosgene`, reflecting Edgewood's 1937 plant upgrade and standardization documented by the [U.S. defence history](https://www.denix.osd.mil/rcwmprogram/history/). Its 1936 bookmark does not receive that research. The same source records renewed mustard production in 1937; the [accepted gameplay calibration](../../specs/chaos_warfare_system_specs/corrections/2026-09-25_usa_1939_mustard_starting_stock.md) raises the U.S. 1939 mustard reserve from 240 to 320 abstract lots while leaving 1936 at 240. It grants no phosgene lots or factory line, and does not convert historical tons into lots.

The nine formerly generated named scientists are now static characters, so the temporary generated-scientist marking helpers and portrait reassignment blocks are no longer needed.

The original identity flags are written after recruitment for Howard Florey, Paul Fildes, Alexander Fleming, Ernst Chain, Gerhard Schrader, Kurt Blome, Walter Schreiber, Erich Traub, Kurt Gutzeit, Sigmund Rascher, Josef Mengele, Shiro Ishii, Masaji Kitano, Chikahiko Koizumi, Franciszek Witaszek, Grigory Mairanovsky, Ivan Velikanov, Lavrentiy Beria, Frank Olson, Ira Baldwin, and Murray Sanders.

The 1936 startup grants do not complete Britain's anthrax special project or add British or American biological breakthrough progress, and Germany's tabun technology is withheld until after the late-1936 discovery while no tabun stockpile is granted.

## Localisation

Every scientist has a stable name key and a concise description of the historical work that informed the specialization, skill, and traits.

Descriptions of coerced experimentation identify the conduct directly and avoid sensational epithets.

## Portraits and icons

Large portrait sprites are `GFX_portrait_<character_id>` and resolve to `gfx/leaders/scientists/portrait_<character_id>.dds`.

The complete scientist portrait registry, including the 46 expanded-roster registrations, lives in `interface/_scientists_portraits.gfx`.

The twelve dual-role specialists currently have wired 65x67 advisor cards under `gfx/interface/advisors/cbrn/`.

No new scientist-trait icons, specialization icons, or advisor sprites are required.

The user confirmed on 2026-09-25 that all 67 scientist portraits already in the mod are approved and that recovering their old source archive is not needed for this overhaul. All 67 large portrait sprites resolve to 156x210 DDS files; the [runtime inventory](../../assets/portraits/cbrn_scientist_runtime_inventory_2026-09-25.md) records their exact hashes and dimensions. The earlier [portrait audit](../../plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-25_cbrn_scientist_portrait_provenance_audit.md) records the absent historical archive, without making it a current completion blocker.

## Historical research basis

Calibration used institutional biographies, archival catalogues, official prize biographies, national academies, military-medical histories, and scholarly histories of the relevant wartime programs.

The dated startup decisions are anchored by the [2 February 1939 Hansard respirator statement](https://api.parliament.uk/historic-hansard/commons/1939/feb/02/air-raid-precautions), the [National Archives account of 38 million masks by September 1939](https://www.nationalarchives.gov.uk/education/resources/home-front-1939-1945-part-one/war-gas/), the [US Army history of the 1942 War Research Service and late-1942 Baldwin assignment](https://history.army.mil/portals/143/Images/Publications/catalog/10-1.pdf), the [US Army history of Camp Detrick's 1943 construction](https://history.army.mil/portals/143/Images/Publications/catalog/10-1.pdf), the [US Army history of Schrader's 1936 tabun discovery](https://history.army.mil/portals/143/Images/Publications/catalog/10-2.pdf), the [US State Department record of Italian mustard-gas use in Ethiopia](https://history.state.gov/historicaldocuments/frus1936v03/d85), the [Polish Institute of National Remembrance biography of Rudolf Weigl](https://ipn.gov.pl/pl/historia-z-ipn/224331%2CRudolf-Weigl-18831957.html), and the [Polish Armia Krajowa account of Witaszek's underground laboratories](https://przystanekhistoria.pl/pa2/tematy/armia-krajowa/74750%2CDr-Franciszek-Witaszek.html).

Italy's established chemical capability is institutional rather than a named CBRN scientist in the 67-person roster. The [Italian Ministry of Defence history](https://www.difesa.it/smd/entimi/scuolanbc/la-storia/34082.html) dates the Servizio Chimico Militare to 1923, corps-level chemical companies to 1934, and a Chemical Regiment from 1936 through September 1943; the [1936 U.S. diplomatic report](https://history.state.gov/historicaldocuments/frus1936v03/d85) independently records Italian mustard-gas use in Ethiopia. Current Italy startup grants chemical knowledge, abstract agent stocks, a chemical facility, and qualifying commanders, while Montecatini supplies a separate industrial organization. Those sources do not justify a new August 1939 scientist, factory line, or agent-stock quantity, and no Italian scientist portrait is part of the approved roster.

The principal reference families include the Royal Society and Royal College of Physicians for British scientists, Nobel Prize biographies and Oxford institutional histories for penicillin researchers, the Australian Academy of Science and Australian Dictionary of Biography, the French Académie des sciences, the United States National Academies and military-medical histories, Polish scientific and resistance histories, Soviet microbiology and chemical-defence histories, and scholarly documentation of the German and Japanese wartime programs and subsequent trials.

Where a person's historical role was administrative rather than scientific, the profile uses skill 1 and a factual description rather than inferring technical expertise from institutional power.

## Future plans

The user identified `6925d2612b927.image_00001.dds` as Erich Traub, so it replaces the established Traub runtime portrait without changing his character, sprite, skill, trait, localisation, or startup recruitment.

The second anonymous file, `s-l1200_00001.dds`, is intentionally ignored and retained only as `not_needed` archive evidence.

Prewar identities remain available from scenario start because the roster represents established research capability, while dated wartime recruitment and advisor cards represent later personnel access, appointments, and offensive authorization.
