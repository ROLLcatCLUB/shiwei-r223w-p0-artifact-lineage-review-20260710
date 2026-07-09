# README for GPT review

## Package

1013R_R223W_P0_ARTIFACT_LINEAGE_AND_SOURCE_OF_TRUTH_CONTRACT

## Review question

Does this package correctly separate canonical teacher manuscript sources from sandbox/review shell artifacts before R223W continues?

## Local decision

```text
R223W-P0 = PASS_LOCAL_SOURCE_OF_TRUTH_CONTRACT
NEXT_ALLOWED = R223W_REVIEW_ONLY_PILOT_GATE_SPEC
R223W_VISUAL_PAGE_CREATION = BLOCKED
R223M_STANDARD_V0_2 = NOT_PUBLISHED
FORMAL_UI / R97B / runtime / prompt / model / db = BLOCKED
```

## Suggested review order

1. `R223W_P0_report.md`
2. `R223W_P0_artifact_lineage_and_source_of_truth.md`
3. `R223W_P0_canonical_teacher_manuscript_sources.json`
4. `R223W_P0_sandbox_vs_teacher_draft_boundary.md`
5. `R223W_P0_allowed_upgrade_paths.md`
6. `validate_1013R_R223W_P0_artifact_lineage_result.json`

## Boundary

This package creates no visual page and no teacher draft. It only locks source-of-truth rules.

