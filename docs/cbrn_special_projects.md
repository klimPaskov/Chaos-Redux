# CBRN special projects

The approved CBRN portfolio adds eight first-tier projects with distinct defensive, offensive, and medical outputs.
The projects use native special-project facilities, breakthrough points, resources, prototype time, and prototype reward choices.
There is no separate administrative unlock decision or routine world-iteration action.

## Project routes and output

| Project | Start requirement | Completion output and tradeoff |
| --- | --- | --- |
| Mechanized Smoke Screens | Basic masks and motorized infantry | Mechanized breakthrough and a protected-advance exposure reduction only while the country has actual mask stock; steel and rubber are consumed during development. |
| Collective Protection Systems | Improved masks and sealed containment | Shelter and sealed-crew exposure reduction, with vanilla flame-tank and engineering-vehicle integrations after their own prerequisites; development uses steel and rubber. |
| Self-Renewing Filters | Advanced masks and Collective Protection Systems | Mask replacement losses fall by 35%, while mask production IC rises by 12%; the research requires rubber and chromium. |
| Phantom Mist | Tabun, fail-safe containment, an offensive chemical project, and unrestricted authorization | A fictional specialized disruption agent causes only one quarter of ordinary casualty damage while increasing disruption; the project spends three breakthrough points and advanced resources. |
| Mass Vaccine Production | Biological surveillance and pathogen handling | Agent-specific prevention is applied to anthrax, plague, tularemia, and smallpox; no universal vaccine or automatic outbreak cleanup is created. |
| Field Antibiotics | Rapid outbreak response and pathogen handling | Field hospitals and CBRN medical detachments recover more casualties, while treatment effects apply only to susceptible anthrax, plague, and tularemia infections. |
| Regenerative Serum | Fail-safe containment and Field Antibiotics | A fictional recovery serum raises army recovery by 5% and civilian goods demand by 2%, and acts as a cloning research precursor. |
| Broad-Spectrum Antiserum | Integrated epidemic control, vaccines, and field antibiotics | Emergency mortality reduction applies to eligible active outbreaks, without curing or preventing every pathogen. |

The matching definitions are in `common/special_projects/projects/cbrn_special_projects.txt`.
Project constants, country-scope discovery triggers, completion effects, and reusable prototype rewards have dedicated CBRN files.
Visible output wording is in `localisation/english/cbrn_special_projects_l_english.yml`.

## Advanced discovery and existing Event 016 projects

`fail_safe_containment_facilities` is the existing advanced containment technology.
Biomedical Acceleration becomes visible through either native Event 016/Mengele theory gates or fail-safe containment plus completion of Mass Vaccine Production or Field Antibiotics.
Ordinary completion calls `chaosx_grant_conventional_technology_package` at the biomedical deployment tier; Event 016 and Mengele completion retain their own project-stage history.
Cloning becomes visible through either the native Event 016/Mengele route or completed Biomedical Acceleration plus Regenerative Serum.
Ordinary completion calls the idempotent `chaosx_grant_custom_operational_technology` clone selector, while the Event 016 and Mengele paths preserve their stage records.
Paleogenetics and Xenobiological Synthesis become visible through either their native story route or fail-safe containment, a completed offensive CBRN project, and `cbrn_policy_allows_extreme_use`.
Ordinary completion calls the corresponding idempotent custom operational-technology selector.
`sp_mengele_cloning` remains story-only and calls the same clone API on completion after its existing Germany/Mengele effects.
No path grants the same operational package twice or fabricates Event 016 project history for an ordinary discoverer.

## Vanilla project integration

The `on_project_completion` callback and relevant technology completion callbacks call `cbrn_sync_vanilla_project_integrations`, which is safe to repeat.
The sealed flamethrower-crew integration requires the vanilla `sp_land_flamethrower_tank`, Collective Protection Systems, `sealed_tank_crews`, and No Step Back.
Its hidden integration technology is granted immediately at completion of the last prerequisite and unlocks the `cbrn_sealed_flamethrower_crew_module` tank-special-slot module for flame tanks: defense +2 and reliability +0.03 for +1.5 IC, one rubber, and two army experience.
The engineering-vehicle decontamination integration requires the vanilla `sp_land_military_engineering_vehicles`, Collective Protection Systems, and `mobile_wash_columns`.
The vanilla `armored_support_vehicle` has no module slots, so the project immediately grants a hidden technology that unlocks the distinct producible `cbrn_armored_support_vehicle_decontamination` model under the same archetype consumed by `armored_engineer`.
The decontamination model costs 14 IC and one rubber in addition to the vanilla model's steel and tungsten, versus the vanilla model's 12 IC and no rubber; reliability falls from 0.80 to 0.72 while defense rises from 10 to 11.
The two hidden integration technologies are direct project-completion rewards and are granted only when every relevant project and technology condition is satisfied, regardless of completion order; the player performs no second research.

## Runtime hooks

All eight project outputs set durable country flags named `cbrn_project_<project_slug>`.
`cbrn_project_has_renewing_filters` is consumed when the shared protection system computes military and civilian mask replacement losses.
`cbrn_project_has_collective_protection` is consumed in shelter exposure and sealed-crew risk calculations.
`cbrn_project_has_protected_mechanized_advance` requires actual mask stock before the smoke-screen exposure reduction can apply.
The exposure adapter composes project protection with existing shelter reductions and uses the shared `cbrn_hazard_budget.residual_floor` of 0.50 for military and civilian exposure, mortality, and medical-load effects.
Phantom Mist unlocks `chemical_malodor_phantom_mist_raid`, a specialized native malodor land raid that retains the ordinary malodor route, requires current unrestricted-use authorization and existing malodor payload stock, and applies reduced casualties with stronger disruption only when its dedicated raid signal is set.
The biological lifecycle reads the vaccine, antibiotic, serum, and antiserum flags inside its agent-specific countermeasure calculation and applies the shared 0.50 response floor after the foundational pathogen-specific cure and vaccination terms.
Project-specific tuning is in `common/script_constants/cbrn_special_project_constants.txt`; the shared floor is in `common/script_constants/cbrn_system_constants.txt`.

## Test Directorate registration

The modifier-free carrier `cbrn_special_project_cxt_package` registers all eight projects through the shared CXT extension bus.
Its `_apply` effect registers each `sp:` object once, and the shared player-triggered debug decision completes only missing projects while suppressing reports.
The bounded `on_startup` hook registers the carrier through one existing country; the additive `on_daily_CXT` fallback only marks an unseen package pending.
Applying the package also reconciles durable completion flags and the two vanilla integrations without replaying native project bonuses.
The equipment owner registers the producible decontamination model through a separate CXT equipment carrier.

## Source-level route checks

The 1936 and 1939 checks include `chaosx_apply_startup_history_grants`, not only country-history files: Germany receives `basic_gas_masks` and `bio_surveillance_networks` plus `pathogen_handling_protocols`, and its country history already grants `motorised_infantry`.
Seven ordinary choices have no `visible` restriction, so the project interface shows their unmet `available` technology and completed-project prerequisites instead of hiding the choices.
Phantom Mist remains an exotic offensive discovery: advanced containment, a prior offensive chemical project, and unrestricted authorization control visibility; the visible card shows Tabun as a separate start requirement.
Germany can start Mechanized Smoke Screens and Mass Vaccine Production at either bookmark; the other ordinary choices are displayed with their outstanding requirements.
CXT's initial setup grants technologies before its registered projects, and the package registers all eight `sp:` objects for the shared idempotent completion pass; a previously initialized CXT uses the player-triggered Apply Registered Systems decision.
The four existing Event 016/Mengele research predicates remain explicit OR alternatives to ordinary discovery, and their completion paths retain their stage history while the ordinary path uses neutral idempotent technology grants.
Completion tooltips, grants, and risky prototype rewards use dedicated story-stage predicates rather than rechecking research admission: the Mengele admission predicates reject a project once its native completion is marked.
For an Event 016 host, the corresponding project-stage entry must have reached Theory; for a valid Mengele provider, that family's persistent Theory receipt must exist.
These proofs remain true if the native completion callback records Prototype before the project output runs.
Thus a completed story project records its stage once, while an ordinary discoverer receives only the neutral operational package and a bounded progress-versus-stability trial.
The two vanilla vehicle integrations reconcile after either project completion order, `mobile_wash_columns` research, and the doctrine helper's `sealed_tank_crews` grant.
These are source-path checks; the user owns live-game validation.

## Icons

The eight 161×98 special-project DDS textures live under `gfx/interface/special_project/project_icons/` and use the project IDs as basenames.
`interface/cbrn_special_projects.gfx` registers `GFX_sp_cbrn_mechanized_smoke_screens`, `GFX_sp_cbrn_collective_protection_systems`, `GFX_sp_cbrn_self_renewing_filters`, `GFX_sp_cbrn_phantom_mist`, `GFX_sp_cbrn_mass_vaccine_production`, `GFX_sp_cbrn_field_antibiotics`, `GFX_sp_cbrn_regenerative_serum`, and `GFX_sp_cbrn_broad_spectrum_antiserum`.
The dedicated icon package supplies all eight binary DDS files at those paths.
The persistent Regenerative Serum Hospitals idea reuses the installed `GFX_idea_anthrax_antibiotics` medical-idea sprite through `picture = anthrax_antibiotics`; it needs no additional DDS.

## Future plans

If live-game evidence shows that one project's bonus dominates a cheaper countermeasure route, tune only its project-specific constants or resource burden.
The outbreak system could later model vaccine batch inventories by agent, but that would require a separate approved logistics design rather than an implicit replacement for the current countermeasure effects.
