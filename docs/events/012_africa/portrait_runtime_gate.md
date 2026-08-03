# Event 012 Africa sovereign portrait runtime gate

Event 012 uses one source policy for historical sovereigns and a separate asset policy for fictional high-chaos identities. A historical African polity may retain a dormant character definition and package mechanics while its sovereign leader role is held until an attributed source, exact crop, source-locked repaint, and independent review are recorded.

## Runtime flow

1. The package keeps the existing Event 006 or vanilla carrier and never creates a new tag or cosmetic carrier.
2. The three constitutional installation effects call the shared `africa_priority_member_portrait_runtime_is_approved` trigger before adding a country-leader role.
3. The current approved male identities are Shehu Sanda Kura for Kanem-Bornu, Emir Abdullahi for Harar, and Pedro VII Afonso for Kongo. Merina's source-locked Queen Ranavalona III portrait remains installed as evidence but is held by the male-only promotion rule until an accepted male source or successor contract exists.
4. A held historical row receives its selected politics and a `africa_priority_member_sovereign_portrait_blocked` flag, but no generated ruler is promoted and no generic ruler is substituted.
5. The Dinuzulu kaCetshwayo source-locked candidate remains held because no accepted 1936 eligibility or alternate-history contract authorizes promoting a 1908 deceased ruler; it is never a Solomon kaDinuzulu substitute.
6. A future source-approved row can reuse the same trigger contract; no portrait identifier, tag, or package store needs to change.

Fictional, alternate-history, nonhuman, and supernatural identities use the separate `fictional_high_chaos` asset family. Those portraits remain dormant behind their accepted country, model, and package gates and never relabel a historical source gap.

The current fictional set is the v4 visual replacement and is intentionally absurd and visually non-interchangeable. Pan is the Thundercloud Ram King, Gorilla Kingdom is the Termite Citadel Silverback, The Green is the Baobab Ring-Eye King, Living Rivers is the River Delta Sovereign, Stoneborn is the Meteor Geode Sovereign, and Ancient Hosts is the Leopard Eclipse Host. All six are male-presenting or nonhuman, use one head-and-shoulders subject, and keep a plain low-detail matte background in the HOI4 painted style. The reviewed contact sheet is `docs/assets/012_africa_world_order/comparison_v4/portrait_012_africa_fictional_v4_decoded_contact_sheet.png` and the machine-readable manifest is `docs/assets/012_africa_world_order/manifests/012_africa_world_order_fictional_portraits_v4_manifest.json`.

## Asset and UI references

The historical leader sprites remain in `interface/012_africa_priority_member_characters.gfx` and point to `gfx/leaders/012_africa/priority_members/`. The fictional high-chaos portrait handoff uses a separate dormant sprite family under `gfx/leaders/012_africa/fictional/`; the stable sprite names now point to the v4 DDS textures and are not wired into the historical sovereign character definitions. No new icon is required for the gate itself.

## Future work

Research and independently review the held historical rows, then promote each row by extending the source manifest and the shared trigger. Do not add lion heads, masks, spears, face paint, crowns, or insignia that are not visible in the selected historical source. Create the deferred fictional country and unit models before opening their runtime gates.
