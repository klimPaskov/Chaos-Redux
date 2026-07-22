# ARX grounded retry 01 - ownership and candidate log

Date: 2026-07-22  
Scope: identity, role, source, rights, and ownership checks for the two live
ARX portrait roles. This log is evidence for the fail-closed disposition; it
does not authorize runtime wiring.

## Ownership gate

The exact and variant terms below were searched in:

- current Chaos Redux repository;
- installed vanilla Hearts of Iron IV;
- Kaiserreich workshop root `394360/1521695605`;
- approved reference roots `394360/2265420196` and `394360/1458561226`.

Terms checked included `Eugenio di Savoia-Genova`, `Eugenio Savoia Genova`,
`Prince Eugenio`, `Duke of Genoa`, `Duca di Genova`, `Duke of Ancona`,
`Ubaldo Soddu`, `Carlo Geloso`, `Taddeo Orlando`, `Giovanni Vecchi`,
`Luigi Efisio Marras`, `Efisio Marras`, and their character-token forms.

### Results

| Person | Current Chaos Redux active owner | Vanilla active owner | Reference-mod notes | Disposition |
|---|---|---|---|---|
| Eugenio di Savoia-Genova | No match | No match | Kaiserreich has a localisation mention (`SIC` marriage event) but no active character or portrait consumer in the scanned roots. | Candidate passes identity ownership gate; rights/role review remains. |
| Taddeo Orlando | No match | No match | No active character or portrait consumer found in the scanned roots. | Candidate passes identity ownership gate; rights/role review remains. |
| Ubaldo Soddu | No match | Active vanilla `ITA_ubaldo_soddu` character/portrait; localisation in multiple vanilla languages | Kaiserreich localisation includes `SIC_ubaldo_soddu`; this is secondary because vanilla already owns the active identity. | `blocked_vanilla_owner`; no source copied. |
| Carlo Geloso | No match | Active vanilla `ITA_carlo_geloso` character/portrait | Kaiserreich localisation includes `SIC_carlo_geloso`; vanilla active ownership is the binding gate. | `blocked_vanilla_owner`; no source copied. |
| Luigi Efisio Marras | No match | No active vanilla match found | Kaiserreich Sardinia has `SRD_luigi_efisio_marras`; cross-mod historical use is not itself a blocker, but the only available source is explicitly 1950s and already documented in another ARX retry. | `blocked_existing_retry` for this package; no duplicate copied. |
| Giovanni Sechi | No match | No active vanilla match found | Kaiserreich Sardinia has `SRD_giovanni_sechi`; existing ARX package already records the cross-mod reference, low-resolution source, and role concerns. | Existing package disposition retained; not duplicated here. |

The binding identity rule is current Chaos Redux or vanilla active character
ownership. A historical person being mentioned or used by a mutually
exclusive reference mod is recorded for audit but is not treated as a sole
runtime blocker. This package does not copy reference-mod art or source files.

## Candidate evidence

### Eugenio di Savoia-Genova

- The 1936 Treccani/Enciclopedia Italiana entry identifies Eugenio as a
  Savoia-Genova prince and Duke of Ancona, born in Turin in 1906; it records
  his naval academy commission and command of a San Marco battalion in the
  Italo-Ethiopian conflict. This is direct period evidence that he was active
  and military-qualified in 1936:
  <https://www.treccani.it/enciclopedia/savoia-eugenio-di-duca-di-ancona_%28Enciclopedia-Italiana%29/>.
- The Commons source is a 1920-1930 face-usable portrait, with no visible
  watermark or modern styling:
  <https://commons.wikimedia.org/wiki/File:Eugenio_di_savoia,_quinto_duca_di_genova.jpg>.
- The local master is the 287x368 original. The separate 2435x3122 `FXD`
  derivative is explicitly labelled on Commons as AI-upscaled and was not
  downloaded or used.
- The source is a plausible crown-route identity, not a Sardinian-born local
  official. Parent design must decide whether a Savoy-Genova duke may fill the
  consultative council role.

### Taddeo Orlando

- The Italian Carabinieri biography identifies him as born in Gaeta (23 June
  1885), an artillery officer active in Tripolitania during 1936, and commander
  of the 21st Infantry Division `Granatieri di Sardegna` from 1 March 1940:
  <https://www.carabinieri.it/chi-siamo/ieri/storia/i-comandanti-generali/i-cti-generali/gen-c-a-taddeo-orlando>.
- The Italian Army's historical commander roll lists Taddeo Orlando among the
  commanders of the 1934-43 21st `Granatieri di Sardegna` division:
  <https://www.esercito.difesa.it/en/organization/the-chief-of-general-staff-of-the-army/comfoter/southern-operational-forces-command/grenadiers-of-sardinia-mechanized-brigade/the-commanders/123885.html>.
- Main Commons face source:
  <https://commons.wikimedia.org/wiki/File:Taddeo_Orlando.jpg>. It is only
  173x234, points to a Generals.dk page, names `Regio Esercito` as author, and
  gives no original creation date. Commons applies `PD-Italy` with a US status
  warning; no `PD-1996` evidence was found.
- Alternate comparison source:
  <https://commons.wikimedia.org/wiki/File:Taddeo_Orlando_and_Mario_Robotti.jpg>.
  This is a 1942 Digital Library of Slovenia group photograph. The local
  preview isolates Orlando mechanically but is not a 1936 solo portrait.
- The candidate is therefore a role/plausibility lead, not a source-ready ARX
  portrait. If the parent requires a Sardinian-born 1936 commander, reject it
  and keep the role blocked.

## Leads rejected before copying

| Candidate | Evidence checked | Rejection |
|---|---|---|
| Ubaldo Soddu | Treccani and the Italian Army commander roll place him in command of the 21st `Granatieri di Sardegna` in 1936; Commons has a 1940 portrait. | Vanilla active owner `ITA_ubaldo_soddu`; portrait was not copied. |
| Carlo Geloso | Italian Army roll and historical biographies place him in command of the 21st `Granatieri di Sardegna` in 1935-36; Commons has a `PD-1996` portrait. | Vanilla active owner `ITA_carlo_geloso`; portrait was not copied. |
| Carlo Sanna (1859-1928) | Cagliari/Senorbì-born; commander of the 33rd Division and emblematic Sassari Brigade leader; official Cagliari cemetery biography confirms death in 1928. | Not alive or plausible in the 1936 scenario; source was not copied. |
| Luigi Efisio Marras | Official Italian Defence biography confirms Cagliari birth and 1933-36 6th Heavy Field Artillery command. | Existing ARX retries already hold the 1950s Commons source as wrong-era; no duplicate source was copied. |
| Nino Salvatore Villa Santa | Cagliari-born; commander of 19th Division `Gavinana` from 1935-38 according to Generals.dk. | Only available portraits are copyright-controlled or unlicensed low-resolution thumbnails. |
| Gavino Pizzolato | Sorso/Sassari-born; commander of 1st Celere Artillery Regiment 1934-37. | Available portraits have unclear or controlled reuse terms; no defensible bitstream. |
| Gioacchino Solinas | Bonorva-born; later commander of 21st `Granatieri di Sardegna`; source already in `sardinia_crown_command_retry`. | Existing package and visual review are the source of truth; this retry does not duplicate it. |

## Search boundaries and uncertainty

- Search was limited to the requested ARX crown and military roles. No advisor,
  small portrait, generated person, modern reenactment, film still, or generic
  face was pursued.
- Commons/Italian public-domain labels were not treated as proof of US
  redistribution rights when the page left publication or registration facts
  unresolved.
- No source was accepted as a final HOI4 asset merely because it was visually
  usable. Rights, period fit, ownership, and role fit remain separate gates.
