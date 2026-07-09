import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

REQUIRED_FILES = [
    "R223W_P0_artifact_lineage_and_source_of_truth.md",
    "R223W_P0_canonical_teacher_manuscript_sources.json",
    "R223W_P0_sandbox_vs_teacher_draft_boundary.md",
    "R223W_P0_allowed_upgrade_paths.md",
    "R223W_P0_report.md",
    "README_FOR_GPT_REVIEW.md",
    "PACKAGE_MANIFEST.json",
]

CANONICAL_FILES = [
    "R223M_P4_P1_teacher_readable_process_v6.html",
    "R223N_P3_P1_teacher_manuscript_draft_v5.html",
    "R223O_P1_teacher_manuscript_draft_v2.html",
]

REQUIRED_PHRASES = [
    "Teacher manuscript quality line",
    "Sandbox / review shell line",
    "R223W must not become another teacher manuscript line",
    "R223W_teacher_draft",
    "R223W_teacher_manuscript",
    "sandbox_preview_as_final_teacher_page",
    "Return to R223M / R223N / R223O teacher manuscript line",
    "R223T fixture-only sandbox preview",
    "REVIEW_ONLY_PILOT_GATE_SPEC",
    "R223M_STANDARD_V0_2 = NOT_PUBLISHED",
    "FORMAL_UI = BLOCKED",
    "R97B_ROUTE = BLOCKED",
]

BANNED_PHRASES = [
    "R223W_teacher_draft.html",
    "R223W_teacher_manuscript.html",
    "R223W_final_teacher_page.html",
    "R223M_STANDARD_V0_2 = PUBLISHED",
    "FORMAL_UI = ALLOWED",
    "R97B_ROUTE = ALLOWED",
]

FALSE_BOUNDARIES = [
    "new_visual_page_created",
    "new_teacher_draft_created",
    "teacher_body_rewritten",
    "schema_v0_2_published",
    "formal_ui",
    "r97b_modified",
    "formal_route_added",
    "frontend_backend_modified",
    "runtime_connected",
    "provider_model_connected",
    "prompt_modified",
    "database_written",
    "lesson_body_written",
    "r222d_component_library_modified",
    "formal_apply",
]

def read_text(name):
    return (ROOT / name).read_text(encoding="utf-8")

def main():
    failures = []
    checks = 0

    for name in REQUIRED_FILES:
        checks += 1
        if not (ROOT / name).exists():
            failures.append(f"missing required file: {name}")

    combined = "\n".join(read_text(name) for name in REQUIRED_FILES if (ROOT / name).exists())

    for phrase in REQUIRED_PHRASES:
        checks += 1
        if phrase not in combined:
            failures.append(f"missing required phrase: {phrase}")

    for phrase in BANNED_PHRASES:
        checks += 1
        if phrase in combined:
            failures.append(f"forbidden phrase present: {phrase}")

    sources_path = ROOT / "R223W_P0_canonical_teacher_manuscript_sources.json"
    if sources_path.exists():
        sources = json.loads(sources_path.read_text(encoding="utf-8"))
        listed = json.dumps(sources, ensure_ascii=False)
        for name in CANONICAL_FILES:
            checks += 1
            if name not in listed:
                failures.append(f"canonical file missing from sources json: {name}")
        for item in sources.get("teacher_manuscript_source_of_truth", []):
            checks += 1
            if item.get("body_edit_allowed_here") is not False:
                failures.append(f"body_edit_allowed_here must be false: {item.get('sample_id')}")

    manifest_path = ROOT / "PACKAGE_MANIFEST.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        checks += 1
        if manifest.get("stage_id") != "1013R_R223W_P0_ARTIFACT_LINEAGE_AND_SOURCE_OF_TRUTH_CONTRACT":
            failures.append("manifest stage_id mismatch")
        checks += 1
        if manifest.get("decision") != "PASS_CONTINUE_TO_R223W_REVIEW_ONLY_PILOT_GATE_SPEC":
            failures.append("manifest decision mismatch")
        for name in CANONICAL_FILES:
            checks += 1
            if name not in manifest.get("canonical_teacher_manuscripts", []):
                failures.append(f"canonical file missing from manifest: {name}")
        boundaries = manifest.get("boundaries", {})
        for key in FALSE_BOUNDARIES:
            checks += 1
            if boundaries.get(key) is not False:
                failures.append(f"manifest boundary must be false: {key}")

    result = {
        "passed": not failures,
        "check_count": checks,
        "failed": len(failures),
        "failures": failures,
        "decision": "PASS_CONTINUE_TO_R223W_REVIEW_ONLY_PILOT_GATE_SPEC",
    }
    (ROOT / "validate_1013R_R223W_P0_artifact_lineage_result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)

if __name__ == "__main__":
    main()

