# Final v8 dependency and provider report

The hard key gate passed before repository intake. `verify_environment.py --probe-meshy` initially observed its exact probe-owned PowerShell PID `10420` and Node PID `26568`; both exited naturally after three seconds. A second run was clean with `findings: []`. This is recorded as the known transient probe cleanup defect, not a provider blocker.

Dependency-lock SHA-256 values were `58FA9FC6486FDA304FDC344962C63ADD276938E2D4402D0E44ACA02A392F1286` for `dependencies.lock.json`, `E45FE80F3B8AC49A365EA2D4221E82E969AE55279639F817BB6FA75407D1C233` for `meshy_tool_schema.lock.json`, and `1ADD938E9FCECB9410AA0430629A4E78E956ADB78362004E075481D6484081BB` for `blender_hoi4_adapter.json`. The environment report SHA-256 was `E700F24042673CFF247345BBA200E40621F8FCD2937DDF1115013031DBEC6A7B`.

The verified routes were official `@meshy-ai/meshy-mcp-server` `0.4.0`, Meshy SDK `1.29.0`, exact generation model `meshy-7`, repository adapter `chaosx_blender_hoi4` `1.10.0`, Blender `5.1.2` build `ec6e62d40fa9`, and checksum-locked `io_pdx_mesh` `0.91.0` archive SHA-256 `A683DF08318CB700014C7FE9A3D15139E5FB2313C7E98715204263E48931F7C2`. The Blender bridge answered at `127.0.0.1:9876`; adapter health request `d38de7661af1467fbeabf08c5c392883` passed.

The pre-generation balance was 91 credits. Meshy 7 image-to-3D task `01a03404-f74d-7d5b-876d-5f426afe11f6` succeeded and consumed 30 credits. The downloaded GLB SHA-256 is `EA2E4E40B88BD67DE45AC0964305786602499902CEC584A12DE666794AD38E4E`; FBX is `66A8EB69F7D1995B52141400B79D9C4F89FC97B85BFF140FED6F64ADC196C79D`.

The first rig request was rejected before billing because the original result contained 1,994,058 faces. The live balance before recovery was 25. Provider remesh task `01a03418-57e3-7399-bf55-2d769bedabee`, triangle topology, 90,000 target polygons, GLB+FBX, 2.7 m mounted envelope, and bottom origin succeeded for 5 credits. Its GLB SHA-256 is `D105CAC2E1D1CC0C37D420FB6E54776D0F15B68126015A3AB734F8900497C348`; FBX is `90ED7511BEAC37D76A1032B2E673D27F80A224061C701F4B9B183C25EF95B743`. The balance before the second rig attempt was 20. The second rig request failed before billing with HTTP 422: `Pose estimation failed, please provide a valid model`.

Total consumed credits: 35. No rig, animation, conversion, or export credits were consumed. Meshy’s standard humanoid pose estimator cannot coherently rig this compound dynamic horse+rider; consequently `meshy_animate` cannot produce any of the eight required actions.
