# IW-006 AFX Wallonia commander alternative-source sweep

Status: `blocked_no_rights_clear_archival_master`.

This bounded sweep searched for a real male Belgian military alternative to Jules-Joseph Pire, Herman Baltia, and every active vanilla/current-project portrait identity. No candidate passed the combined identity, era, role, ownership, and source-rights gates. No image master, crop, processed PNG, DDS, contact sheet, GFX edit, gameplay edit, or localisation edit was made.

## Requested stable consumer

| Field | Value |
|---|---|
| Character token | `AFX_walloon_reserve_commander` |
| Current display name | `Marcel Delcourt` |
| Sprite | `GFX_portrait_AFX_walloon_reserve_commander` |
| Runtime path | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` |
| Source classification | Grounded real-person commander; sourced archival portrait required |

The current consumer remains the fictional Marcel Delcourt token. Any accepted historical identity still requires a guarded identity/localisation transfer before runtime wiring.

## Candidate ledger

| Candidate | Historical and role fit | Source lead | Gate result |
|---|---|---|---|
| François-Joseph Ley (1879-1957) | Lieutenant-general and commander of the 2nd Chasseurs Ardennais Division in 1940; exact Belgian Ardennes command fit | [Generals.dk biography](https://generals.dk/general/Ley/Fran%C3%A7ois-Joseph/Belgium.html) points to `2DivChA_GenMaj_Ley.jpg` on the 18daagseveldtocht archive | `blocked_source_rights`: the portrait is an unattributed repost and the Generals.dk page states `Copyright © Steen Ammentorp since 2000`; no upstream rights-clear master was exposed |
| Maurice Bricart (1894-1940) | Arlon-born captain-commandant/major who commanded the 5th Company, 1st Chasseurs Ardennais, and was killed at Bodange on 10 May 1940 | [Bel-Memorial biography](https://bel-memorial.org/tribute/tribute_1.php?INDIVIDUALS_ID=1933) and [photo page](https://bel-memorial.org/cities/luxembourg/bodange/photos_maurice_bricart.htm) expose a portrait and archival scans | `blocked_source_rights`: the host provides no reusable licence, author, archive accession, or underlying-public-domain statement; the files are a memorial-site repost and were not downloaded |
| François Goormachtigh | Major of I/14Li, a Liège-stationed Belgian infantry unit; plausible Walloon military-reserve fit but less direct than a Chasseurs Ardennais commander | [18daagseveldtocht 14de Linieregiment](https://18daagseveldtocht.be/infanterie/actieve-leger/14de-linieregiment/) identifies the officer and serves `14Li.jpg`; the page credits “Documenten Majoor F. Goormachtigh” to Luc Vandevelde | `blocked_source_rights`: no image author, licence, or public-domain basis; the page is a secondary archive site and the source image was not downloaded |
| Albert Bastin, Alphonse Dantinne, Werner Goffinet | Belgian/Ardennes military or resistance names surfaced while checking Chasseurs Ardennais command and resistance records | Official/secondary text references were found, but no accessible attributed one-person archival photograph with a clear reuse licence surfaced in this sweep | `blocked_no_usable_source`: text evidence alone cannot admit a grounded portrait |
| Victor Descamps | Commander of the 1st Chasseurs Ardennais Division in 1940; excellent role fit | Vanilla defines and portraits `BEL_victor_descamps` | `blocked_current_vanilla_owner` |
| Maurice Keyaerts | Belgian general associated with the Chasseurs Ardennais/Groupement K; role fit | Vanilla defines and portraits `BEL_maurice_keyaerts` | `blocked_current_vanilla_owner` |
| Jules-Joseph Pire | Corps des Chasseurs Ardennais commander from 1936; strongest pre-war Walloon fit | Fresh package at [afx_jules_pire_source_blocked](../afx_jules_pire_source_blocked/manifest.md) | `blocked_current_vanilla_owner_and_source_rights` |
| Herman Baltia | Prior AFX trial identity | Existing Event 006 trial and audit | `blocked_current_project_consumer_transfer_and_likeness`; explicitly excluded by parent constraint |

## Historical context

The [Belgium WWII/CegeSoma Chasseurs Ardennais article](https://www.belgiumwwii.be/belgique-en-guerre/articles/chasseurs-ardennais.html) confirms the Walloon-Ardennes defence role and the 1940 division commanders. The article is historical corroboration only and does not grant image reuse rights.

## Source and era decision

The strongest candidates were contemporary or age-compatible military subjects, but every surfaced photograph failed at least one required condition: clear upstream rights, author/archive attribution, or a defensible public-domain basis. Reposted memorial and enthusiast-site images are not treated as rights-clear merely because they are old or visually period-matching.

No candidate is admitted. Do not use a statue, illustration, reenactor, modern memorial photograph, generic Belgian portrait, or generated substitute to fill the consumer.

## Required next source condition

A future candidate must provide an accessible original or archival master of the actual man, an explicit public-domain or reusable licence basis, source author/archive and date evidence, and a clean ownership scan showing no active vanilla/current-project/meaningful portrait owner. Only after that pass may the immutable source and exact crop be created with `extract_portrait_source_crop.py`.
