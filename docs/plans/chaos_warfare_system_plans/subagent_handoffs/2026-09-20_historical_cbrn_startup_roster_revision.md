# Historical CBRN startup and scientist roster revision handoff

Status: implemented in the owned startup, character, constants, history recruitment, on-action, localisation, and documentation surfaces. The original static-recruitment claim was corrected: documented later wartime identities are now recruited by date-gated helpers and bounded country callbacks, while prewar and established 1939 personnel remain available at the supported bookmarks. The 1936 starting mask matrix now reconciles every profile tag into the approved force-scaled military band plus a separate replacement reserve. No commit was created; the parent agent owns integration and final review.

## Changed files

- `common/characters/cbrn_historical_specialists.txt`: separated scientist competence from advisor authorization and added current-date gates for the documented later appointments.
- `common/characters/cbrn_historical_scientists.txt`: records the installed 1–4 scale and distinguishes date-gated wartime personnel from prewar identities; no skill, specialization, trait, or portrait entry was changed.
- `history/general/chaosx_startup_character_recruitment.txt`: leaves prewar/1939 identities in history and removes the later wartime identities from unconditional scenario-start recruitment.
- `common/on_actions/cbrn_historical_startup_on_actions.txt`: adds only bounded `on_daily_TAG` callbacks for ENG, GER, JAP, POL, SOV, and USA so later personnel arrive on their documented dates in a 1936 game.
- `common/scripted_effects/chaosx_startup_history_effects.txt`: adds idempotent date-gated recruitment/flag helpers, calls them at startup and from the bounded callbacks, adds the country-scoped 1939 setup receipt, queues `cbrn_protection.3` in ENG-root scope for the real-stock British issue, marks the full 1936 force-scaled band matrix, snapshots and reconciles non-ENG fixed profiles into real military issue plus reserve, records explicit 1936 UK inputs for the shared core helper, defers the German tabun discovery until after late 1936, removes British and American early biological breakthrough/project grants, dates British and American biological facility placement, and removes the obsolete retired battlefield-operation selector seed.
- `common/script_constants/startup_history_constants.txt`: sets British and American startup biological breakthrough to zero, adds the 1936 force-scaled protection bands, civilian zero target, and 25% replacement reserve, adds explicit 1936 UK inputs, and retains the 1939 British civilian respirator conversion.
- `common/scripted_effects/cbrn_starting_protection_effects.txt`: removes the dead synthetic readiness delta so the startup snapshot remains the sole readiness refresh path; the shared ENG 1936 helper and generic lifecycle remain core-owned.
- `localisation/english/cbrn_historical_startup_l_english.yml`: added dedicated UTF-8 BOM localisation for the roster and bookmark profiles without duplicating the established character name and description keys.
- `docs/specs/chaos_warfare_system_specs/matrices/gas_mask_starting_stockpile_matrix.md`: records the implemented all-country 1936 bands separately from the older fixed-crate proposal rows so the source matrix does not overstate those archival estimates as runtime values.
- `localisation/english/chaosx_characters_l_english.yml`: synchronized the eight historical advisor operational tooltips with the owned hazard constants: chemical theorist +3% dose/+2% contamination/+20% readiness, toxicological director +3% dose/+5% deaths/+2% contamination/+20% readiness, biological positives +2%, and medical protection reductions 15%.
- `docs/systems/cbrn_warfare/cbrn_historical_scientists.md`: recorded the date gates, 1939 British handoff, early-BW restrictions, and source links.
- `docs/systems/startup_history_compatibility.md`: reconciled stale generated-scientist and early-British-project documentation with the static roster and dated setup.

## Country startup table

| Country | Static scientists | 1936 historical CBRN profile | 1939 setup | Personnel and programme notes |
| --- | ---: | --- | --- | --- |
| AST | 3 | Smaller defensive programme, 25% military issue target and 25% reserve band | Country-scoped 1939 receipt only if the later bookmark is selected | Florey is a medical countermeasure advisor; Burnet and Kellaway remain scientist-only. |
| CAN | 3 | Smaller defensive programme, 25% military issue target and 25% reserve band | Country-scoped 1939 receipt only if the later bookmark is selected | Maass, Banting, and Dolman remain scientist-only defensive or medical researchers. |
| ENG | 14 | Established major military baseline, 75% active issue plus 25% replacement reserve, and zero fixed civilian issue at 1936; explicit `cbrn_historical_1936_force_scaled_protection` contract carries the historical band to the core profile owner | 1939 sets `cbrn_historical_civilian_mask_issue`, `cbrn_uk_1939_mass_respirator_issue`, and a 40,000-crate civilian respirator variable; startup queues ENG-root `cbrn_protection.3`, which reconciles the inclusive historical target against the common profile and real stock | Hansard reported 40,000,000 civilian respirators issued in the preceding twelve months on 2 February 1939. Fildes arrives in 1939 and Henderson in 1940; British biological facility placement waits until after 31 December 1939. Britain receives no startup anthrax project completion or biological breakthrough. |
| FRA | 2 | Established major military baseline, 75% issue target and 25% replacement reserve | Country-scoped 1939 receipt | Dufraisse and Lebeau remain scientist-only chemical-defence specialists. |
| GER | 15 | Established major military baseline, 75% issue target and 25% replacement reserve | Country-scoped 1939 receipt | Tabun technology is absent on 1 January 1936 and granted only after 31 December 1936; no tabun stockpile is granted. Schrader's advisor opens after the discovery; Blome's wartime programme-director card opens after 1 January 1942. |
| ITA | 0 | Active-war profile, 100% military issue target and 25% replacement reserve | Country-scoped 1939 receipt | The existing Ethiopia campaign chemical logistics and commander trait grants remain; no scientist portrait or offensive authorization is fabricated. |
| JAP | 4 | Limited programme, 50% military issue target and 25% replacement reserve | Country-scoped 1939 receipt | Ishii remains available for his pre-war Unit 731 role; Kitano's later command card opens after 1 January 1942. |
| POL | 3 | Smaller defensive programme, 25% military issue target and 25% reserve band | Country-scoped 1939 receipt | Weigl and Fleck remain defensive typhus/vaccine scientists; Witaszek's clandestine CBW advisor card opens after 1 September 1939. |
| SOV | 9 | Established major military baseline, 75% issue target and 25% replacement reserve | Country-scoped 1939 receipt | Velikanov remains available for his pre-war role; Mairanovsky opens after 1 January 1937. Yermolyeva remains scientist-only and her wartime relevance does not grant an early advisor appointment. |
| USA | 14 | Established major military baseline, 75% issue target and 25% replacement reserve | Country-scoped 1939 receipt; no mature offensive BW setup | No startup biological breakthrough is granted. Baldwin's advisor opens after 1 January 1942, Olson after 1 January 1943, and the West Virginia biological facility waits until after 1 January 1943. |

The fixed matrix remains in core-owned `common/script_constants/cbrn_system_constants.txt`, but 1936 startup no longer treats those fixed crate totals as historical receipts. `chaosx_startup_history_effects.txt` marks every matrix tag, snapshots its pre-profile models, clears the common fixed issue/civilian ledgers, and restores real stock at the band plus reserve before issuing the active share. ENG uses the core-owned helper because its common profile suppresses the fixed receipt; the other marked tags use the startup-owned reconciliation helper. The core worker consumes `cbrn_historical_civilian_mask_issue` only when stock exists and the historical 1939 profile is active.

### 1936 force-scaled matrix audit

| Band | Tags | Active military issue | Replacement reserve | Startup date gate |
| --- | --- | ---: | ---: | --- |
| Established major | ENG, FRA, GER, SOV, USA | 75% of deployed requirement | 25% of deployed requirement | Applies only when `date < 1939.01.01`. |
| Active war | ITA | 100% of deployed requirement | 25% of deployed requirement | Applies only when `date < 1939.01.01`; the Ethiopia setup remains separately sourced. |
| Limited programme | JAP | 50% of deployed requirement | 25% of deployed requirement | Applies only when `date < 1939.01.01`; biological authorization remains doctrine-gated. |
| Smaller defensive | POL, CZE, BEL, HOL, CAN, AST, NZL, SAF, ROM, YUG, TUR, SPR, CHI, PRC, SHX, GXC, YUN, XSM, SIK, MAN, BUL, HUN, GRE, RAJ, AUS, POR, SWE, NOR, DEN, FIN, BRA, ARG, MEX, CHL | 25% of deployed requirement | 25% of deployed requirement | Applies only when `date < 1939.01.01`. |

The startup order is explicit: the country grants complete, the bounded `every_country` marker and five-model stock snapshot run, `chaosx_apply_starting_cbrn_mask_profiles` runs once, and the country reconciliation runs immediately afterward before any later startup receipt. No independent historical equipment grant runs between the snapshot and reconciliation. The reconciliation temporarily removes the current basic, reconditioned, improved, advanced, and sealed mask stock, restores the five pre-profile values, adds the force-scaled reserve, clears the common fixed military and civilian ledgers, tops up any active-issue shortfall from real basic-mask stock, then issues the active share through `cbrn_issue_requested_masks_to_military`; unrelated mask stock therefore returns to its pre-profile quantity and only the approved reserve/issue receipt remains. The 1939 ENG event is queued after this sequence and is excluded from the 1936 marker by the strict date gate.

For a concrete arithmetic check, if deployed requirement is 1,000 crates and pre-profile mask stock is zero, an established major receives 1,000 real basic-mask crates, issues 750, and retains 250; Italy receives 1,250, issues 1,000, and retains 250; Japan receives 750, issues 500, and retains 250; and a smaller country receives 500, issues 250, and retains 250. If pre-profile stock is already present, the same helper restores it first and grants only the active-issue plus reserve shortfall, so the pre-existing quantity is not lost or counted as a civilian issue.

## Dated advisor appointments

| Character | Scientist role at start | Advisor authorization gate | Reason |
| --- | --- | --- | --- |
| `AST_howard_florey` | Biological warfare skill 4 | No date gate; medical countermeasure role | Defensive medical research and penicillin work are distinct from offensive authorization. |
| `ENG_paul_fildes` | Biological warfare skill 4 | `date > 1939.01.01` plus `has_doctrine = chaos_warfare` | The Porton Down biological department and offensive programme belong to the 1939-40 wartime period. |
| `ENG_alexander_fleming` | Biological warfare skill 3 | No date gate; medical countermeasure role | Defensive antibacterial research. |
| `GER_gerhard_schrader` | Chemical warfare skill 3 | `date > 1936.12.31` plus doctrine | Late-1936 tabun discovery; no January 1936 stockpile. |
| `GER_kurt_blome` | Biological warfare skill 3 | `date > 1942.01.01` plus doctrine | Later wartime biological programme-director role. |
| `JAP_shiro_ishii` | Biological warfare skill 3 | No date gate plus doctrine | Unit 731 command was already active by the 1936 bookmark. |
| `JAP_masaji_kitano` | Biological warfare skill 3 | `date > 1942.01.01` plus doctrine | Unit 731 command belongs to the 1942-45 period. |
| `POL_franciszek_witaszek` | Biological warfare skill 2 | `date > 1939.09.01` plus doctrine | Resistance CBW role follows the German occupation. |
| `SOV_grigory_mairanovsky` | Chemical warfare skill 2 | `date > 1937.01.01` plus doctrine | Later-1930s secret-police toxicology appointment. |
| `SOV_ivan_mikhailovich_velikanov` | Biological warfare skill 4 | No date gate plus doctrine | Early Red Army biological-warfare role. |
| `USA_frank_olson` | Biological warfare skill 3 | `date > 1943.01.01` plus doctrine | Camp Detrick Special Operations appointment follows the wartime installation. |
| `USA_ira_baldwin` | Biological warfare skill 4 | `date > 1942.01.01` plus doctrine | US Army history places his assignment in late 1942. |

No additional advisor or high-command character was created. The existing Italy, Japan, and Soviet `chemical_operations_commander` startup trait grants remain in the parent-owned history path. Existing officers in those grants do not have a verified CBRN-specific small portrait suitable for a new native high-command card, so the commander-traits worker should keep the trait-only grants unless parent review supplies an existing officer card and source.

## 67-person roster evidence

The installed numeric scale is inexperienced 1, skilled 2, experienced 3, expert 4. The table records every static identity, specialization, skill, and scientist trait. `Scientist-only` means no advisor authorization is granted by the character definition.

### Individual scenario-availability audit

The availability floor below is the earliest date at which the named identity is attached to the country scientist pool. A `1936` row is intentionally available at both supported bookmarks; `1939` means the identity is available in the 1939 bookmark only when the documented wartime or occupation condition has begun; later rows are recruited by the bounded dated helpers. Advisor doctrine/date gates remain separate in `cbrn_historical_specialists.txt`.

| ID | Earliest static recruitment | Evidence disposition and implementation |
| --- | --- | --- |
| `AST_howard_florey` | 1936 | Prewar penicillin and medical-countermeasure work; history recruitment. |
| `AST_charles_kellaway` | 1936 | Interwar chemical-defence research; history recruitment. |
| `AST_frank_macfarlane_burnet` | 1936 | Prewar influenza and infectious-disease work; history recruitment. |
| `CAN_otto_maass` | 1936 | Interwar chemical-defence administration; history recruitment. |
| `CAN_frederick_banting` | 1936 | Prewar mustard-injury and aviation-medicine work; history recruitment. |
| `CAN_claude_e_dolman` | 1936 | Prewar vaccine and infectious-disease work; history recruitment. |
| `ENG_paul_fildes` | 1939 | Porton Down wartime biology department; dated helper after 1938.12.31. |
| `ENG_alexander_fleming` | 1936 | Prewar antibacterial research; history recruitment. |
| `ENG_ernst_chain` | 1936 | Late-1930s penicillin biochemistry; history recruitment. |
| `ENG_charles_lovatt_evans` | 1936 | Interwar physiology and gas-effects research; history recruitment. |
| `ENG_harold_hartley` | 1936 | Interwar physical chemistry and chemical defence; history recruitment. |
| `ENG_john_scott_haldane` | 1936 | Interwar respiratory protection research; history recruitment. |
| `ENG_joseph_barcroft` | 1936 | Prewar oxygen transport and gas protection; history recruitment. |
| `ENG_rudolph_peters` | 1936 | Interwar biochemical-injury research; history recruitment. |
| `ENG_edward_abraham` | 1936 | Late-1930s penicillin chemistry; history recruitment. |
| `ENG_norman_heatley` | 1936 | Late-1930s penicillin extraction work; history recruitment. |
| `ENG_patrick_laidlaw` | 1936 | 1930s influenza and infectious-disease research; history recruitment. |
| `ENG_b_c_j_g_knight` | 1936 | Prewar bacterial cultivation research; history recruitment. |
| `ENG_david_w_w_henderson` | 1940 | Porton biological-threat team established in 1940; dated helper after 1939.12.31. |
| `ENG_donald_d_woods` | 1936 | Prewar bacterial-metabolism research; history recruitment. |
| `FRA_charles_dufraisse` | 1936 | Interwar combat-gas and antioxidant research; history recruitment. |
| `FRA_paul_lebeau` | 1936 | Interwar gas-mask materials and arsine defence; history recruitment. |
| `GER_gerhard_schrader` | 1937 | Tabun discovery in late 1936; dated helper after 1936.12.31. |
| `GER_kurt_blome` | 1942 | Later wartime biological programme director; dated helper after 1942.01.01. |
| `GER_walter_schreiber` | 1936 | 1930s epidemic-defence planning; history recruitment. |
| `GER_erich_traub` | 1936 | Prewar animal-virus and vaccine research; history recruitment. |
| `GER_kurt_gutzeit` | 1939 | Wartime coercive hepatitis research; dated helper after 1939.08.31. |
| `GER_sigmund_rascher` | 1941 | Wartime altitude and hypothermia experiments; dated helper after 1940.12.31. |
| `GER_josef_mengele` | 1943 | Auschwitz selections and lethal experiments; dated helper after 1942.12.31. |
| `GER_august_hirt` | 1941 | Wartime anatomical collection and chemical research; dated helper after 1940.12.31. |
| `GER_ferdinand_flury` | 1936 | Interwar toxicology and military-agent study; history recruitment. |
| `GER_otto_ambros` | 1936 | Prewar IG Farben chemical engineering; history recruitment. |
| `GER_otto_bickenbach` | 1942 | Wartime phosgene experiments; dated helper after 1941.12.31. |
| `GER_richard_kuhn` | 1936 | Prewar chemical research preceding later nerve-agent work; history recruitment. |
| `GER_gerhard_rose` | 1936 | 1930s malaria research; history recruitment. |
| `GER_joachim_mrugowsky` | 1939 | SS Hygiene Institute wartime role; dated helper after 1939.08.31. |
| `GER_erwin_ding_schuler` | 1939 | Buchenwald typhus research in the wartime period; dated helper after 1939.08.31. |
| `JAP_shiro_ishii` | 1936 | Unit 731 command active before the bookmark; history recruitment. |
| `JAP_masaji_kitano` | 1942 | Unit 731 succession and command role; dated helper after 1942.01.01. |
| `JAP_chikahiko_koizumi` | 1936 | Prewar Army medical administration; history recruitment. |
| `JAP_ryoichi_naito` | 1936 | Prewar-to-war biological programme connection; history recruitment. |
| `POL_franciszek_witaszek` | 1939 | Resistance laboratories after occupation; dated helper after 1939.09.01. |
| `POL_rudolf_weigl` | 1936 | Prewar typhus-vaccine research; history recruitment. |
| `POL_ludwik_fleck` | 1936 | Prewar typhus and vaccine research; history recruitment. |
| `SOV_lavrentiy_pavlovich_beria` | 1937 | Late-1930s administrative authority over secret programmes; dated helper after 1936.12.31. |
| `SOV_grigory_mairanovsky` | 1937 | Later-1930s secret-police toxicology; dated helper after 1937.01.01. |
| `SOV_ivan_mikhailovich_velikanov` | 1936 | Early Red Army biological-warfare work; history recruitment. |
| `SOV_georgy_gause` | 1936 | 1930s antibiotic and medical research; history recruitment. |
| `SOV_nikolai_ginsburg` | 1936 | Early Red Army biological research; history recruitment. |
| `SOV_sergei_muromtsev` | 1936 | Interwar bacteriological and security-service context; history recruitment. |
| `SOV_zinaida_yermolyeva` | 1936 | Prewar cholera research; history recruitment. |
| `SOV_nikolay_zelinsky` | 1936 | First World War gas-mask and activated-charcoal work; history recruitment. |
| `SOV_yakov_fishman` | 1936 | Interwar Red Army chemical-defence direction; history recruitment. |
| `USA_frank_olson` | 1943 | Camp Detrick Special Operations; dated helper after 1943.01.01. |
| `USA_ira_baldwin` | 1942 | War Research Service assignment; dated helper after 1942.01.01. |
| `USA_murray_sanders` | 1943 | Camp Detrick wartime project work; dated helper after 1942.12.31. |
| `USA_stanhope_bayne_jones` | 1936 | Prewar public-health and preventive medicine; history recruitment. |
| `USA_william_a_hagan` | 1942 | Wartime botulinum-toxin programme; dated helper after 1941.12.31. |
| `USA_karl_friedrich_meyer` | 1936 | Prewar plague-control research; history recruitment. |
| `USA_theodor_rosebury` | 1936 | Prewar airborne-pathogen research; history recruitment. |
| `USA_edwin_broun_fred` | 1936 | Prewar scientific work preceding wartime mobilisation; history recruitment. |
| `USA_george_w_merck` | 1942 | War Research Service programme administration; dated helper after 1942.01.01. |
| `USA_james_stevens_simmons` | 1936 | Prewar preventive medicine; history recruitment. |
| `USA_cornelius_p_rhoads` | 1942 | Wartime gas-casualty medicine; dated helper after 1941.12.31. |
| `USA_dean_s_tarbell` | 1936 | Established mustard-agent detection work; history recruitment. |
| `USA_james_b_conant` | 1940 | NDRC wartime chemical research coordination; dated helper after 1939.12.31. |
| `USA_winford_lee_lewis` | 1936 | First World War-era lewisite expertise; history recruitment. |

| ID | Specialization | Skill | Traits | Role disposition |
| --- | --- | ---: | --- | --- |
| `AST_howard_florey` | BW | 4 | brilliant theorist, resourceful | dual-role medical advisor, ungated |
| `AST_charles_kellaway` | CW | 3 | bright, resourceful | scientist-only |
| `AST_frank_macfarlane_burnet` | BW | 4 | brilliant theorist, fast learner | scientist-only |
| `CAN_otto_maass` | CW | 4 | brilliant theorist, resourceful | scientist-only |
| `CAN_frederick_banting` | CW | 4 | brilliant theorist, bright | scientist-only |
| `CAN_claude_e_dolman` | BW | 3 | bright, resourceful | scientist-only |
| `ENG_paul_fildes` | BW | 4 | brilliant theorist, resourceful | dual-role advisor after 1939.01.01 |
| `ENG_alexander_fleming` | BW | 3 | bright | dual-role medical advisor, ungated |
| `ENG_ernst_chain` | BW | 4 | brilliant theorist, gifted engineer | scientist-only |
| `ENG_charles_lovatt_evans` | CW | 4 | brilliant theorist, resourceful | scientist-only |
| `ENG_harold_hartley` | CW | 4 | brilliant theorist, resourceful | scientist-only |
| `ENG_john_scott_haldane` | CW | 4 | gifted engineer, resourceful | scientist-only defensive research |
| `ENG_joseph_barcroft` | CW | 4 | brilliant theorist, resourceful | scientist-only defensive research |
| `ENG_rudolph_peters` | CW | 4 | gifted engineer, resourceful | scientist-only |
| `ENG_edward_abraham` | BW | 3 | gifted engineer, brilliant theorist | scientist-only |
| `ENG_norman_heatley` | BW | 3 | gifted engineer, resourceful | scientist-only |
| `ENG_patrick_laidlaw` | BW | 4 | brilliant theorist, fast learner | scientist-only |
| `ENG_b_c_j_g_knight` | BW | 3 | resourceful, gifted engineer | scientist-only |
| `ENG_david_w_w_henderson` | BW | 4 | brilliant theorist, resourceful | scientist-only; Porton biological role 1939-40 |
| `ENG_donald_d_woods` | BW | 3 | brilliant theorist, bright | scientist-only; Porton research |
| `FRA_charles_dufraisse` | CW | 3 | brilliant theorist, gifted engineer | scientist-only |
| `FRA_paul_lebeau` | CW | 4 | gifted engineer, resourceful | scientist-only |
| `GER_gerhard_schrader` | CW | 3 | brilliant theorist | dual-role advisor after 1936.12.31 |
| `GER_kurt_blome` | BW | 3 | none | dual-role advisor after 1942.01.01 |
| `GER_walter_schreiber` | BW | 2 | none | scientist-only defensive epidemic research |
| `GER_erich_traub` | BW | 3 | gifted engineer | scientist-only |
| `GER_kurt_gutzeit` | BW | 1 | inhumane | scientist-only; coercive research record |
| `GER_sigmund_rascher` | BW | 1 | inhumane | scientist-only; coercive research record |
| `GER_josef_mengele` | BW | 1 | inhumane | scientist-only; coercive research record |
| `GER_august_hirt` | CW | 1 | inhumane CW | scientist-only; coercive research record |
| `GER_ferdinand_flury` | CW | 3 | bright | scientist-only |
| `GER_otto_ambros` | CW | 3 | gifted engineer | scientist-only |
| `GER_otto_bickenbach` | CW | 2 | inhumane CW | scientist-only; coercive research record |
| `GER_richard_kuhn` | CW | 4 | genius | scientist-only |
| `GER_gerhard_rose` | BW | 3 | bright, inhumane | scientist-only; coercive research record |
| `GER_joachim_mrugowsky` | BW | 3 | inhumane | scientist-only; coercive research record |
| `GER_erwin_ding_schuler` | BW | 2 | inhumane | scientist-only; coercive research record |
| `JAP_shiro_ishii` | BW | 3 | resourceful, inhumane | dual-role advisor, ungated by date |
| `JAP_masaji_kitano` | BW | 3 | bright, inhumane | dual-role advisor after 1942.01.01 |
| `JAP_chikahiko_koizumi` | BW | 1 | none | scientist-only |
| `JAP_ryoichi_naito` | BW | 3 | bright, resourceful | scientist-only |
| `POL_franciszek_witaszek` | BW | 2 | resourceful | dual-role advisor after 1939.09.01 |
| `POL_rudolf_weigl` | BW | 4 | bright, resourceful | scientist-only defensive vaccine research |
| `POL_ludwik_fleck` | BW | 3 | bright, resourceful | scientist-only defensive vaccine research |
| `SOV_lavrentiy_pavlovich_beria` | BW | 1 | none | scientist-only administrative role |
| `SOV_grigory_mairanovsky` | CW | 2 | inhumane CW | dual-role advisor after 1937.01.01 |
| `SOV_ivan_mikhailovich_velikanov` | BW | 4 | brilliant theorist, resourceful | dual-role advisor, ungated by date |
| `SOV_georgy_gause` | BW | 3 | bright, resourceful | scientist-only |
| `SOV_nikolai_ginsburg` | BW | 3 | brilliant theorist, resourceful | scientist-only |
| `SOV_sergei_muromtsev` | CW | 3 | inhumane CW | scientist-only |
| `SOV_zinaida_yermolyeva` | BW | 4 | bright, resourceful | scientist-only; wartime medical research |
| `SOV_nikolay_zelinsky` | CW | 4 | bright, gifted engineer | scientist-only defensive protection |
| `SOV_yakov_fishman` | CW | 3 | resourceful | scientist-only |
| `USA_frank_olson` | BW | 3 | bright, gifted engineer | dual-role advisor after 1943.01.01 |
| `USA_ira_baldwin` | BW | 4 | resourceful, gifted engineer | dual-role advisor after 1942.01.01 |
| `USA_murray_sanders` | BW | 3 | bright, resourceful | scientist-only |
| `USA_stanhope_bayne_jones` | BW | 3 | bright, resourceful | scientist-only defensive medicine |
| `USA_william_a_hagan` | BW | 3 | gifted engineer, resourceful | scientist-only |
| `USA_karl_friedrich_meyer` | BW | 4 | brilliant theorist, resourceful | scientist-only |
| `USA_theodor_rosebury` | BW | 4 | bright, gifted engineer | scientist-only |
| `USA_edwin_broun_fred` | BW | 4 | brilliant theorist, resourceful | scientist-only |
| `USA_george_w_merck` | BW | 4 | brilliant theorist, resourceful | scientist-only; later programme administration |
| `USA_james_stevens_simmons` | BW | 4 | brilliant theorist, resourceful | scientist-only defensive medicine |
| `USA_cornelius_p_rhoads` | CW | 4 | bright, resourceful | scientist-only |
| `USA_dean_s_tarbell` | CW | 2 | bright, gifted engineer | scientist-only |
| `USA_james_b_conant` | CW | 4 | genius, brilliant theorist | scientist-only |
| `USA_winford_lee_lewis` | CW | 4 | gifted engineer, brilliant theorist | scientist-only |

The following evidence ledger records the earliest historical basis used for the static scientist identity and the separate gameplay gate. A later wartime record does not create an early advisor appointment; it remains a scientist-only roster entry unless the character table names a dated advisor gate.

| ID | Earliest evidence and source rationale | Gameplay gate |
| --- | --- | --- |
| `AST_howard_florey` | 1930s penicillin clinical work and wartime production planning support a medical countermeasure role. | Static scientist in 1936/1939; medical advisor allowed for AST with no date gate. |
| `AST_charles_kellaway` | Interwar Chemical Defence Board service and study of chemical-agent effects support defensive chemical research. | Static scientist in 1936/1939; scientist-only. |
| `AST_frank_macfarlane_burnet` | Prewar influenza and infectious-disease research supports biological medicine expertise. | Static scientist in 1936/1939; scientist-only. |
| `CAN_otto_maass` | Interwar Canadian chemical-defence administration and protective-measures research support chemical expertise. | Static scientist in 1936/1939; scientist-only. |
| `CAN_frederick_banting` | Mustard-gas injury and aviation-medicine research support protective chemical medicine. | Static scientist in 1936/1939; scientist-only. |
| `CAN_claude_e_dolman` | Prewar botulism, cholera-vaccine, and infectious-disease research supports defensive biological work. | Static scientist in 1936/1939; scientist-only. |
| `ENG_paul_fildes` | Porton Down biological work belongs to the 1939-40 wartime department and offensive programme. | Recruited after `date > 1938.12.31`; advisor additionally requires `date > 1939.01.01` and Chaos Warfare doctrine. |
| `ENG_alexander_fleming` | The 1928 penicillin discovery and subsequent antibacterial work support a medical countermeasure role. | Static scientist in 1936/1939; medical advisor allowed for ENG with no date gate. |
| `ENG_ernst_chain` | Penicillin biochemistry and clinical-production work is established by the late 1930s. | Static scientist in 1936/1939; scientist-only. |
| `ENG_charles_lovatt_evans` | Interwar physiology and Porton gas-effects research support defensive chemical expertise. | Static scientist in 1936/1939; scientist-only. |
| `ENG_harold_hartley` | Interwar physical chemistry and chemical-defence planning support defensive chemical research. | Static scientist in 1936/1939; scientist-only. |
| `ENG_john_scott_haldane` | First World War and interwar respiratory research support gas-exposure protection. | Static scientist in 1936/1939; scientist-only defensive research. |
| `ENG_joseph_barcroft` | Prewar oxygen-transport and respiratory physiology support gas-protection research. | Static scientist in 1936/1939; scientist-only defensive research. |
| `ENG_rudolph_peters` | Interwar and Porton biochemical-injury work supports chemical-warfare countermeasures. | Static scientist in 1936/1939; scientist-only. |
| `ENG_edward_abraham` | Late-1930s penicillin chemistry supports biological medicine expertise. | Static scientist in 1936/1939; scientist-only. |
| `ENG_norman_heatley` | Late-1930s technical work on penicillin extraction supports production expertise. | Static scientist in 1936/1939; scientist-only. |
| `ENG_patrick_laidlaw` | 1930s influenza isolation and infectious-disease research support biological medicine. | Static scientist in 1936/1939; scientist-only. |
| `ENG_b_c_j_g_knight` | Prewar bacterial nutrition and laboratory-cultivation work supports biological research. | Static scientist in 1936/1939; scientist-only. |
| `ENG_david_w_w_henderson` | Porton Down aerosol and biological-threat work belongs to the 1939-40 wartime team. | Recruited after `date > 1939.12.31`; scientist-only, with no early offensive appointment. |
| `ENG_donald_d_woods` | Prewar bacterial-metabolism research supports antibiotic and biological-defence work. | Static scientist in 1936/1939; scientist-only. |
| `FRA_charles_dufraisse` | Interwar combat-gas and antioxidant research supports chemical protection. | Static scientist in 1936/1939; scientist-only. |
| `FRA_paul_lebeau` | Interwar gas-mask materials and arsine-defence research support chemical protection. | Static scientist in 1936/1939; scientist-only. |
| `GER_gerhard_schrader` | The 1936 discovery of tabun supports a late-1936 chemical-research appointment. | Recruited after `date > 1936.12.31`; advisor additionally requires `date > 1936.12.31` and Chaos Warfare doctrine; no 1936 nerve stockpile. |
| `GER_kurt_blome` | The programme-director role belongs to the later wartime biological programme. | Recruited after `date > 1942.01.01`; advisor additionally requires `date > 1942.01.01` and Chaos Warfare doctrine. |
| `GER_walter_schreiber` | 1930s epidemic-defence planning supports defensive biological research. | Static scientist in 1936/1939; scientist-only. |
| `GER_erich_traub` | Prewar animal-virus and vaccine work supports dual-use biological expertise. | Static scientist in 1936/1939; scientist-only. |
| `GER_kurt_gutzeit` | Coercive hepatitis research is a wartime record tied to occupied medical networks. | Recruited after `date > 1939.08.31`; scientist-only. |
| `GER_sigmund_rascher` | Coercive altitude and hypothermia experiments are a wartime record. | Recruited after `date > 1940.12.31`; scientist-only. |
| `GER_josef_mengele` | Auschwitz selections and lethal experiments are a later wartime record. | Recruited after `date > 1942.12.31`; scientist-only. |
| `GER_august_hirt` | The racist anatomical collection is a wartime coercive record. | Recruited after `date > 1940.12.31`; scientist-only. |
| `GER_ferdinand_flury` | Interwar toxicology and military-agent study support chemical research. | Static scientist in 1936/1939; scientist-only. |
| `GER_otto_ambros` | IG Farben chemical engineering and later nerve-agent production support chemical industry expertise. | Static scientist in 1936/1939; scientist-only; MIO access remains with the industrial owner. |
| `GER_otto_bickenbach` | Wartime phosgene experiments are a coercive chemical record. | Recruited after `date > 1941.12.31`; scientist-only. |
| `GER_richard_kuhn` | Wartime soman research followed earlier tabun and sarin work. | Static scientist in 1936/1939 by approved roster abstraction; scientist-only. |
| `GER_gerhard_rose` | 1930s malaria work and wartime typhus experiments support biological expertise while recording coercion. | Static scientist in 1936/1939; scientist-only. |
| `GER_joachim_mrugowsky` | The SS Hygiene Institute and prisoner experiments are a wartime record. | Recruited after `date > 1939.08.31`; scientist-only. |
| `GER_erwin_ding_schuler` | Buchenwald typhus experiments belong to the wartime period. | Recruited after `date > 1939.08.31`; scientist-only. |
| `JAP_shiro_ishii` | Unit 731 command was active by the 1936 bookmark. | Static scientist in 1936/1939; advisor requires Chaos Warfare doctrine, with no date gate. |
| `JAP_masaji_kitano` | The Unit 731 succession and command role belongs to 1942-45. | Recruited after `date > 1942.01.01`; advisor additionally requires `date > 1942.01.01` and Chaos Warfare doctrine. |
| `JAP_chikahiko_koizumi` | Prewar Army medical administration and support for Japan's biological programme support research expertise. | Static scientist in 1936/1939; scientist-only. |
| `JAP_ryoichi_naito` | Unit 9420 and blood-plasma research support a prewar-to-war biological programme connection. | Static scientist in 1936/1939; scientist-only. |
| `POL_franciszek_witaszek` | Underground chemical and biological sabotage follows the September 1939 German occupation. | Recruited after `date > 1939.09.01`; advisor additionally requires `date > 1939.09.01` and Chaos Warfare doctrine. |
| `POL_rudolf_weigl` | Prewar typhus-vaccine work continued under occupation and supports defensive research. | Static scientist in 1936/1939; scientist-only defensive vaccine research. |
| `POL_ludwik_fleck` | Prewar typhus research and vaccine work continued through occupation and imprisonment. | Static scientist in 1936/1939; scientist-only defensive vaccine research. |
| `SOV_lavrentiy_pavlovich_beria` | Late-1930s administrative authority over secret state weapons programmes supports the administrative scientist entry. | Recruited after `date > 1936.12.31`; scientist-only. |
| `SOV_grigory_mairanovsky` | Secret-police toxicology and lethal experimentation belong to the later 1930s. | Recruited after `date > 1937.01.01`; advisor additionally requires `date > 1937.01.01` and Chaos Warfare doctrine. |
| `SOV_ivan_mikhailovich_velikanov` | Early Red Army biological-warfare work predates the 1936 bookmark. | Static scientist in 1936/1939; advisor requires Chaos Warfare doctrine, with no date gate. |
| `SOV_georgy_gause` | 1930s antibiotic research and wartime medical work support biological medicine expertise. | Static scientist in 1936/1939; scientist-only. |
| `SOV_nikolai_ginsburg` | Early Red Army biological research and vaccine development support prewar expertise. | Static scientist in 1936/1939; scientist-only. |
| `SOV_sergei_muromtsev` | State bacteriological research and security-service experience support chemical and biological research context. | Static scientist in 1936/1939; scientist-only. |
| `SOV_zinaida_yermolyeva` | Prewar cholera work supports medical research; penicillin production is wartime relevance. | Static scientist in 1936/1939; scientist-only and no wartime advisor appointment. |
| `SOV_nikolay_zelinsky` | The activated-charcoal gas mask dates to the First World War and supports defensive chemical protection. | Static scientist in 1936/1939; scientist-only defensive research. |
| `SOV_yakov_fishman` | Interwar Red Army chemical service and biological-defence direction support defensive chemical research. | Static scientist in 1936/1939; scientist-only. |
| `USA_frank_olson` | Camp Detrick Special Operations belongs to the wartime laboratory established in 1943. | Recruited after `date > 1943.01.01`; advisor additionally requires `date > 1943.01.01` and Chaos Warfare doctrine. |
| `USA_ira_baldwin` | The US Army history places his War Research Service assignment in late 1942. | Recruited after `date > 1942.01.01`; advisor additionally requires `date > 1942.01.01` and Chaos Warfare doctrine. |
| `USA_murray_sanders` | Camp Detrick project work and later Japanese-record investigations are wartime evidence. | Recruited after `date > 1942.12.31`; scientist-only. |
| `USA_stanhope_bayne_jones` | Prewar public-health administration and wartime preventive medicine support biological defence. | Static scientist in 1936/1939; scientist-only. |
| `USA_william_a_hagan` | Botulinum-toxin work belongs to the wartime biological programme. | Recruited after `date > 1941.12.31`; scientist-only. |
| `USA_karl_friedrich_meyer` | Prewar plague-control and infectious-disease research support defensive biological expertise. | Static scientist in 1936/1939; scientist-only. |
| `USA_theodor_rosebury` | Prewar airborne-pathogen and aerosol-transmission research supports biological defence. | Static scientist in 1936/1939; scientist-only. |
| `USA_edwin_broun_fred` | The scientific study preceding the wartime biological programme supports research expertise without early offensive authorization. | Static scientist in 1936/1939; scientist-only. |
| `USA_george_w_merck` | The War Research Service and programme administration belong to the 1942 wartime mobilisation. | Recruited after `date > 1942.01.01`; scientist-only. |
| `USA_james_stevens_simmons` | Prewar preventive medicine and wartime biological-defence advice support medical research. | Static scientist in 1936/1939; scientist-only. |
| `USA_cornelius_p_rhoads` | Wartime gas-casualty medicine and chemical-defence work support chemical research. | Recruited after `date > 1941.12.31`; scientist-only. |
| `USA_dean_s_tarbell` | Mustard-agent detection work supports established chemical-defence expertise. | Static scientist in 1936/1939; scientist-only. |
| `USA_james_b_conant` | NDRC coordination of wartime chemical research belongs to the 1940s mobilisation. | Recruited after `date > 1939.12.31`; scientist-only. |
| `USA_winford_lee_lewis` | Lewisite development dates to the First World War and supports chemical-agent expertise. | Static scientist in 1936/1939; scientist-only. |

At the 1936 bookmark the roster contains 45 established identities. At the 1939-01-01 bookmark it contains 49: the 45 static identities plus Paul Fildes, Gerhard Schrader, Lavrentiy Beria, and Grigory Mairanovsky. The remaining 18 identities enter only after their individual later gates; no post-date character is attached to either supported bookmark. A 1939 bookmark later than 1 September 1939 additionally admits the three German occupation-period entries and Franciszek Witaszek, while Henderson and Conant open on 1 January 1940.

Roster audit results: 67 unique ids, 12 dual-role and 55 scientist-only entries, country counts AST 3 / CAN 3 / ENG 14 / FRA 2 / GER 15 / JAP 4 / POL 3 / SOV 9 / USA 14, specialization counts BW 43 / CW 24, and skill counts 1:6 / 2:6 / 3:27 / 4:28. No skill 5, duplicate id, duplicate portrait, or trait outside the reviewed vocabulary was introduced.

## Source verification

- UK Parliament, [Air-Raid Precautions, 2 February 1939](https://api.parliament.uk/historic-hansard/commons/1939/feb/02/air-raid-precautions): 40,000,000 civilian respirators issued during the previous twelve months.
- UK National Archives, [War Gas](https://www.nationalarchives.gov.uk/education/resources/home-front-1939-1945-part-one/war-gas/): 38 million people issued gas masks by September 1939.
- US Army Center of Military History, [The Chemical Warfare Service: Organizing for War](https://history.army.mil/portals/143/Images/Publications/catalog/10-1.pdf): June 1942 biological-warfare committee report, summer 1942 War Research Service, late-1942 Baldwin assignment, and spring 1943 Camp Detrick construction.
- US Army Center of Military History, [The Chemical Warfare Service: From Laboratory to Field](https://history.army.mil/portals/143/Images/Publications/catalog/10-2.pdf): 1936 Schrader tabun discovery and the late wartime US biological programme context.
- UK Defence Science and Technology Laboratory, [The Truth About Porton Down](https://www.gov.uk/government/news/the-truth-about-porton-down): wartime Porton Down anthrax programme and defensive countermeasure context.
- Imperial War Museums, [Porton Down trials, 1942-43](https://film.iwmcollections.org.uk/record/25572): Porton biological-threat assessment team established in 1940 and Henderson identified in the wartime team.
- US Department of State, [Foreign Relations of the United States, 1936, Ethiopia](https://history.state.gov/historicaldocuments/frus1936v03/d85): Italian mustard-gas use in the 1935-36 war.
- OPCW, [Vesicants](https://www.opcw.org/documents/medical-aspects-chemical-weapons-and-biological-warfare-chapter-7): historical note on Italy's likely mustard use in 1935.
- Polish Institute of National Remembrance, [Rudolf Weigl](https://ipn.gov.pl/pl/historia-z-ipn/224331%2CRudolf-Weigl-18831957.html): pre-war and wartime typhus-vaccine research.
- Polish Armia Krajowa history, [Franciszek Witaszek](https://przystanekhistoria.pl/pa2/tematy/armia-krajowa/74750%2CDr-Franciszek-Witaszek.html): underground chemical and biological laboratories under German occupation.
- PBS American Experience, [Paul Fildes](https://www.pbs.org/wgbh/americanexperience/features/weapon-biography-paul-fildes/): wartime Porton Down biology department and Fildes's offensive programme role.

## Coordination and validation

- The stable 1939 flag for the core CBRN worker is `cbrn_historical_civilian_mask_issue`; it is set only for ENG when the startup date is after 31 December 1938. `cbrn_uk_1939_mass_respirator_issue` is an explicit British alias, and `cbrn_startup_uk_1939_civilian_respirator_crates` carries `constant:startup_history_civil_defence.uk_1939_civilian_respirator_crates` (40,000 crates, representing approximately 40 million respirators).
- The generic 1939 receipt `cbrn_historical_1939_start` is set for AST, CAN, ENG, FRA, GER, ITA, JAP, POL, SOV, and USA. The core worker should keep automatic civilian issue conditional on the exact historical flag and owned stock, with actual threat still satisfying the normal trigger.
- The current core trigger `cbrn_country_needs_civilian_mask_issue` still includes the permanent `cbrn_historical_civilian_mask_issue` flag. Core must consume or clear that one-time historical receipt after `cbrn_protection.3` so Civil Defence visibility and routine civilian issue fall back to actual threat or active response conditions; the historical startup surface does not edit the core trigger.
- The shared core constants and protection effects retain lifecycle, registration, readiness, maintenance, and the ENG-specific no-fixed-grant helper. The startup-owned effect supplies the approved all-country 1936 bands and real-stock reconciliation without rewriting the core matrix file.
- A source parser checked all 67 character blocks, duplicate ids, country counts, specializations, traits, and numeric skill mapping. A second parser matched all 67 `recruit_character` entries in `history/general/chaosx_startup_character_recruitment.txt` to the character roster exactly once.
- UTF-8 BOM was verified for the dedicated localisation file. The touched Clausewitz files were inspected for balanced braces and the unsupported `<=`/`>=` operators.
- No HOI4 process was launched. No standalone character/scientist MCP renderer is exposed. The read-only Technology Tree Viewer route is available through `hoi4.tech_inspect` and `hoi4.tech_render`: `tabun` trace artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f28717e6d0c87ab2797b86683c4dc3c38d441b084a10fd2774fe1e51b7b66a70/decba8b33d7305326a093002dffda772b4e0e887618443ed7f9d52e5f9204e22/technology-trace-f08bf119c0da.json`, rendered technology artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ee1514720a2fa422f5b9633c46a30194244130c0349bb464af4dd5e2e833d47a/00e945bc5a710e719a22b1564ad495e516e6d0b1190fbfd49ffd6fda59ce80cf/technology-technology-f08bf119c0da.json`, and PNG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78d8e896da776364252d3231c5c229fb34a77d7b407c8f6162d3a3efd9f9e92f/4063f7deb4adf5cd58482db8284bd3d58122d263944b1e8c84357acdacca60d6/technology-technology-f08bf119c0da.png`. The service reports 1,400 blocking diagnostics across the whole graph and `sourceAccurate = false`, so the artifact proves route availability and target inspection but does not prove a clean project graph. Focus, event, weighted-logic, GUI, and map routes were not applicable to this character/startup surface.

## Remaining uncertainty and simplifications

- The 1936 protection bands and 25% reserve are approved gameplay calibration, not literal archival stock counts. The startup reconciliation converts them to deployed-manpower-scaled real stock without changing the historical tier assignments.
- The 40,000-crate British 1939 conversion is an abstraction from Hansard's 40,000,000 issued respirators and the CBRN system's approximately 1,000 civilian respirators per crate. The core helper reconciles it with the existing military reserve so the profile does not double-count stock.
- The one-time British 1939 event is wired and idempotent, but Civil Defence visibility after the receipt remains a core-trigger follow-up until the historical flag is consumed or cleared as described above.
- The startup surface does not add a new 1939 production line or industrial concern. The explicit British flag, variable, existing chemical facility, and later biological facility gate provide the integration contract; MIO and industrial-concern ownership remains with the separate worker.
- No new commander high-command card was created because the startup trait recipients do not have a verified CBRN-specific small portrait in the owned surface. Parent and the commander-traits worker retain that decision.
