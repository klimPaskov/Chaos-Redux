# IW-018 ARX grounded male portrait source research v75 handoff

Date: 2026-08-01.

Owner: Chaos Redux sourced visual-asset researcher.

Scope: archival/public-domain/clearly licensed source research for the three already-authored ARX full-size leader consumers. No gameplay, characters, localisation, `.gfx`, generated portrait, advisor icon, processed PNG, crop JSON, or DDS file was created or edited.

## Outputs

The research package is [`docs/assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/`](../../../assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/).

- [`README.md`](../../../assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/README.md) records the source-mode gate, role dispositions, exact-name blockers, and parent decision boundary.
- [`source_ledger.csv`](../../../assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/source_ledger.csv) records source URL/title, direct source URL, date/author/archive, rights, dimensions, SHA-256, crop feasibility, ownership status, and disposition for eleven researched rows.
- [`portrait_eligibility.md`](../../../assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/portrait_eligibility.md) records the fail-closed eligibility gate and crop/downstream requirements.
- [`urls.txt`](../../../assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/urls.txt) lists the Commons, official archive, biography, and exact-name negative-search URLs.
- [`gfx_handoff.md`](../../../assets/006_independence_wave/iw018_arx_portrait_source_research_v75_2026_08_01/gfx_handoff.md) is a research-only wiring boundary; no sprite snippet or final path is claimed.
- `source_masters/` contains unchanged archival binaries for Lussu, Mella, Solinas, Vernè, Valle, Pizzorno, Eugenio, Adalberto, and Sechi, copied from prior evidence packages and hash-checked after copy.

## Conclusive role dispositions

### Emilio Lussu — civilian/labor route

The Senate-sourced [Emilio Lussu portrait](https://commons.wikimedia.org/wiki/File:Emilio_Lussu.jpg) is a clear male head-and-shoulders source with CC BY 3.0 IT attribution through `senato.it`, but Commons dates it only `before 1958`. Lussu was born in Armungia in Cagliari province and was a Sardinian politician, soldier, writer, and Partito Sardo d'Azione/Partito d'Azione figure alive in 1936.

Disposition: `source_ready_for_parent_review`, not runtime-complete. The parent must route the unchanged source through the exact crop utility, source-locked repaint, independent likeness/style/provenance audit, and deterministic 156x210/DDS workflow. The prior 1916 repaint trial remains a failed likeness reference and must not be reused.

### Vittorio Pala — crown consultative route

No attributable historical person or archival portrait matching the exact name `Vittorio Pala` was found. Commons exact-title search returned zero, Wikidata exact-name search returned zero, and broad Commons hits did not identify a 1936 Sardinian officeholder.

Luigi Arborio Mella di Sant'Elia is the strongest crown-role substitute: he was born in Sassari, served as Grand Master of Court Ceremonies for Vittorio Emanuele III from age twenty-five, was a royal confidant, and was alive in 1936. The Senate portrait is CC BY 3.0 IT, 153x193, and dated only before 26 June 1955. Mella was not a 1936 senator; his Senate appointment began in 1939.

Disposition: current `Vittorio Pala` is `blocked_name_only`; Mella is `needs_user_review` only if the parent explicitly accepts a role/name identity change. Eugenio and Adalberto Savoy-Genova alternatives remain rights-blocked because the retained Commons records are PD-Italy without independently documented United States publication/registration evidence.

### Gavino Piras — mountain-guard directorate

No attributable historical person or archival portrait matching the exact name `Gavino Piras` and a 1936 mountain-command role was found. Commons exact-title search returned no exact portrait title, Wikidata exact-name search returned zero, and the broad hits were modern funerals/heraldic material rather than a period person source.

Gioacchino Solinas is the strongest Sardinian-born command substitute: born in Bonorva, Sassari province, a decorated Bersaglieri general, and alive/active in 1936. The available source is an anonymous 1943 photograph marked PD-Italy only. The prior mechanical photo finish was rejected as not HOI4-painted, and no explicit PD-1996 determination was found.

Vittorio Vernè is a rights-strong alternative with a 1930s Commons source marked PD-Italy plus PD-1996 and documented 1936 divisional command, but he was born in Rome. Giuseppe Valle is Sardinian-born and a strong 1936 fit but is blocked by Kaiserreich's live `SRD_giuseppe_valle` ownership. Giuseppe Pizzorno is Sardinian-born and role-plausible but his only source is an insufficient 145x160 side-profile thumbnail. Giovanni Sechi is Sardinian-born but is also Kaiserreich-owned and is a weak mountain-role fit.

Disposition: current `Gavino Piras` is `blocked_name_only`; Solinas is `needs_user_review` only if the parent explicitly accepts a role/name identity change. Vernè is `blocked_strict_sardinian_birth_requirement` unless the parent accepts a Sardinia-linked rather than Sardinian-born commander.

## Ownership evidence

The ownership scan recorded in `source_ledger.csv` and the prior v15 package found the current ARX Lussu owner, no current/vanilla/approved owner for Mella, Solinas, Vernè, Pizzorno, Eugenio, or Adalberto, Kaiserreich `SRD_giuseppe_valle` ownership for Valle, and Kaiserreich `SRD_giovanni_sechi` ownership for Sechi. No guarded transfer contract is in scope.

## Parent actions and blockers

1. Keep the current `Vittorio Pala` and `Gavino Piras` consumers blocked unless the design explicitly changes their grounded identities and names.
2. Do not relabel Mella or Solinas as Pala or Piras, and do not generate a replacement face.
3. If a candidate identity change is accepted, rerun the exact crop utility and full source-locked portrait pipeline with an independent audit before DDS or `.gfx` wiring.
4. Resolve Lussu's undated `before 1958` source and the prior likeness failure through a new audit; no existing DDS is promoted by this handoff.
5. Keep IW-018 runtime content attestation closed until the parent has an accepted grounded source roster and complete visual evidence.

## Simplifications, omissions, and blockers

- Exact `Vittorio Pala` identity: blocked; no defensible source exists.
- Exact `Gavino Piras` identity: blocked; no defensible source exists.
- Mella and Solinas are role-fit candidate substitutions, not approved replacements.
- Eugenio, Adalberto, and Solinas retain rights/era uncertainty; Vernè fails a strict Sardinian-birth requirement; Valle and Sechi fail subject ownership; Pizzorno fails source quality.
- No processed PNG, final DDS, advisor icon, GFX edit, or runtime wiring was created.
