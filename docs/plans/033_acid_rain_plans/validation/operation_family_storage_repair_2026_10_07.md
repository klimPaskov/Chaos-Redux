# Event 033 paid-operation family storage

Disposition: source repair and resolver-frame checks complete, full payment/callback/native acceptance remains open.

The helper-output auditor's A3 finding showed that `acid_rain_open_operation` consumed `acid_rain_op_family` without declaring it before the nested resolver.
Under the required conservative helper-return contract, a national Shelter, Water, Medical, Transport or Demobilization action could therefore follow the zero-family state-operation branch after its quote had already been paid.
The opening helper now declares its family output before resolution.
The resolver assigns that existing storage to the authored family, while evacuations and targeted recovery retain their intentional zero family.
No quote amount, resource debit, operation cap, duration, callback definition or AI weight is changed.

The focused test `.tools/validation/test_033_operation_family_storage.js` executes the actual resolver body for six national variants and six targeted variants.
The six national results are 1, 2, 2, 3, 4 and 5, including both water routes.
All twelve cases have a separate negative control that loses the child-created result when caller storage is absent.
The test also reads the real opening body and requires the declaration immediately before its resolver call.
That opening assertion failed on the original source and passes after the repair.
The actual selected-action saved field and caller sentinel remain unchanged.
The test does not execute the full quote/debit/open-operation transaction, native scope changes, scheduling or save/reload.

Before source SHA-256 is `1f6d6534ab595972e3ffa6d8a509e25c9bd04db87043a0db02549f824f422fa6`.
After source SHA-256 is `bee4526617bd15431e6356f0498b5cbc98caf7bf0ed6e1432504eea3d0f65600`.
The existing probability auditor retains the before file in its immutable current-source snapshot and was notified of this disjoint patch and its validation limits.

Current `hoi4.source_lookup` confirms an unshadowed opening definition at preparedness lines 1029 to 1107, revision `31268db203a051b19a18aa5b45ffc4fbc9487a79b1a40d63244400cb6af1fdc8`.
The bounded structure page puts `set_temp_variable` before `acid_rain_resolve_operation_family`; it omits other children and does not establish full transaction coverage.
The parent follows its revision-bound first-child key path to verify the output name/default.
The initial child read returned `SOURCE_REVISION_STALE` after the shared index changed; it is retained as a failed navigation receipt.
A fresh exact-child lookup succeeded at revision `40f64d66b3a30fd85bbd6fc2fe00490e0b874350cde6c2f05f5fb745a971beb1`, confirming `acid_rain_op_family = constant:acid_rain_runtime.zero` at line 1030 with no omitted child fields.
The relevant temporary-return rule is the already read offline Data structures section, lines 435 to 443, and installed `set_temp_variable`, lines 7820 to 7827, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
No new public helper, asset, meter or fallback is introduced.
