# Event 006 FORM-39 — Melanesian Federation

FORM-39 is a negotiated federation route for the Liberations cluster. It reuses the registered vanilla gameplay tags `FIJ`, `PNG`, and `WPG`; it does not create a new country. Its only new identity is the cosmetic/formable tag `MFX`, which ends in `X` and was selected from the dated installed-mod collision audit as an unused candidate.

## Source-defined member map

| Member | Runtime tag | Event 006 package | Anchor state | Required package gate | Role |
| --- | --- | ---: | ---: | --- | --- |
| Fiji | `FIJ` | `IW-177` | `636` | `independence_wave_fij_melanesian_member_research_complete` plus the Fiji route surface | Carrier; capital remains Suva/state 636 |
| Papua | `PNG` | `IW-178` | `523` | `independence_wave_png_melanesian_member_research_complete` | Named Papuan district package; no generic pan-Papuan substitute |
| West Papua | `WPG` | `IW-157` | `669` | `independence_wave_wpg_melanesian_member_research_complete` | Named West Papuan district package; existing Japanese/Indonesian interactions remain protected |

The adapter also records the installed vanilla substate anchors that may be integrated only through later researched missions: Papua interior `1073`, Bougainville `1070`, and Dutch Southern New Guinea `1057`. The founding transaction itself transfers or cores only a consenting anchor under the explicit full-integration authorization; autonomous membership never transfers territory, changes the member tag, or replaces its focus tree.

## Readiness and fail-closed rules

The registry profile is already `FORM-39`, region Oceania, negotiated federation, three minimum members, three consents, and three anchors. Runtime readiness is not inferred from geography. `can_independence_wave_form39_register_readiness` requires the exact Fiji/PNG/WPG packages, all three research flags, the reserved `MFX` identity, the reviewed flat flag package, and the identity review flag. Until those are present, the family remains undiscoverable and cannot enter the generic commit allowlist.

The accepted flag package is ImageGen-generated flat design evidence under `docs/assets/006_independence_wave/form39_melanesian_federation_identity_2026_07_27/`. It is currently `needs_user_review`; no runtime identity admission is claimed. No advisor or dossier icon is created for FORM-39.

## Runtime surfaces

- `common/scripted_triggers/006_independence_wave_form39_triggers.txt` owns exact carrier/member eligibility, frozen three-row ledger checks, research gates, MFX identity proofs, AI consent, autonomous-member state, and material project cost checks.
- `common/scripted_effects/006_independence_wave_form39_effects.txt` owns readiness attestation, MFX identity dispatch, autonomous relations, anchor-only integration, ledger initialization, project effects, dissolution, rollback, and generation-safe cleanup.
- `common/decisions/categories/006_independence_wave_form39_categories.txt` and `common/decisions/006_independence_wave_form39_decisions.txt` expose human founding replies and four post-formation actions. Projects use command power, stability, strategic reserves, administration/diplomacy/security, manpower, experience, and equipment costs; political power is never used as a storage mechanic. Timed projects cancel and clear their active flags when the carrier or bound member compact invalidates, and the plebiscite command-power gate matches its single strategic command-power spend.
- `common/ideas/006_independence_wave_form39_ideas.txt` supplies visible carrier and autonomous-member lifecycle ideas using the existing league-membership sprite.
- `common/countries/006_independence_wave_formable_cosmetics.txt` records MFX map colours; the MFX flag files are staged in the engine-facing flag folders by the asset handoff.

## Dynamic ledgers

The carrier owns `independence_wave_form39_maritime_logistics`, `independence_wave_form39_cultural_autonomy`, `independence_wave_form39_federal_capacity`, and `independence_wave_form39_member_consent`, each clamped to the centralized 0–100 tuning range. Shipping, civil-service, and plebiscite projects change these ledgers and the shared recognition, capacity, security, instability, and stability values. Autonomous members own a generation-bound autonomy variable and reciprocal access/guarantee flags; cleanup removes only relations created by this transaction.

## Outstanding acceptance

The adapter is implemented but intentionally remains closed because the accepted sensitive-package research rows for IW-157 and IW-178 require named community and district packages, sourced identity material, and explicit consent. The asset handoff also remains `needs_user_review`. A future acceptance pass must add those package flags through researched country packages, set the three identity-review gates only after independent audits, exercise voluntary and unanimous congress paths, and rerun the installed tag-collision and host-survival tests before adding FORM-39 to runtime attestation.
