// Official Text-to-Motion compatibility tools for locked Meshy MCP 0.4.0.
// Loaded only by the repository patch; all provider traffic uses its official client.
import { z } from "zod";
import fs from "node:fs";
import { downloadFileToLocal, fileSha256 } from "./tasks.js";

const endpoint = "/openapi/v1/text-to-motion";
const id = z.string().min(1).regex(/^[a-zA-Z0-9_-]+$/);
const reply = value => ({ structuredContent: value, content: [{ type: "text", text: JSON.stringify(value) }] });
const clean = value => {
    if (Array.isArray(value)) return value.map(clean);
    if (value && typeof value === "object") return Object.fromEntries(Object.entries(value).filter(([key]) => !key.endsWith("_url")).map(([key, item]) => [key, clean(item)]));
    return value;
};
export function registerMotionTools(server, client) {
    const register = (name, description, inputSchema, paid, handler) => server.registerTool(name, {
        description, inputSchema, annotations: { readOnlyHint: !paid && name !== "meshy_download_motion", destructiveHint: false, idempotentHint: !paid && name !== "meshy_download_motion", openWorldHint: true }
    }, async params => {
        try { return reply(await handler(params)); }
        catch (error) {
            // Do not serialize axios errors: they include auth headers and signed URLs.
            return { isError: true, content: [{ type: "text", text: `Meshy motion operation failed (HTTP ${error?.response?.status ?? "unknown"}). ${paid ? "Submission may be uncertain; inspect task list before any further paid submission." : "No paid submission was made."}` }] };
        }
    });
    register("meshy_text_to_motion", "Generate standalone articulated motion. prime costs 10 credits (FBX); swift costs 3 (BVH). No automatic submission retry. Download successful results within 3 days.", {
        prompt: z.string().min(1).max(400), mode: z.enum(["prime", "swift"]), duration: z.number().min(2).max(10).multipleOf(0.5)
    }, true, async params => {
        const result = await client.post(endpoint, params);
        if (typeof result.result !== "string" || !result.result) throw new Error("Missing task id");
        return { task_id: result.result, task_type: "text-to-motion", status: "PENDING", estimate_credits: params.mode === "prime" ? 10 : 3 };
    });
    register("meshy_get_motion_status", "Retrieve standalone motion status and consumed credits; signed URLs are suppressed.", { task_id: id }, false,
        async params => clean(await client.get(`${endpoint}/${params.task_id}`)));
    register("meshy_list_motion_tasks", "Recover uncertain submissions using paginated newest-first task inventory; never blindly repeat POST.", {
        page_num: z.number().int().min(1).default(1), page_size: z.number().int().min(1).max(100).default(20)
    }, false, async params => ({ tasks: clean(await client.get(endpoint, params)) }));
    register("meshy_animation_library", "Read the official preset animation library without credits.", {}, false,
        async () => ({ library: clean(await client.get("/openapi/v1/animations/library")) }));
    register("meshy_download_motion", "Immediately persist the successful task's exact motion format inside the repository, returning SHA-256; refuses overwrite.", {
        task_id: id, save_to: z.string().min(1), format: z.enum(["fbx", "bvh"])
    }, false, async params => {
        const task = await client.get(`${endpoint}/${params.task_id}`);
        if (task.status !== "SUCCEEDED" || task.id !== params.task_id || task.result?.motion_format !== params.format) throw new Error("Task/format mismatch");
        const url = new URL(task.result.motion_url);
        if (url.protocol !== "https:" || url.hostname !== "assets.meshy.ai") throw new Error("Unexpected asset host");
        if (fs.existsSync(params.save_to)) throw new Error("Refusing overwrite");
        const size = await downloadFileToLocal(url.href, params.save_to);
        return { task_id: task.id, task_type: "text-to-motion", format: params.format, local_path: params.save_to,
            file_size_bytes: size, sha256: fileSha256(params.save_to), consumed_credits: task.consumed_credits, duration_ms: task.result.duration_ms, mode: task.result.mode };
    });
}
