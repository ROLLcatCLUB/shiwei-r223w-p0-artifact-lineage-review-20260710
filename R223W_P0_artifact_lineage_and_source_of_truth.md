# R223W-P0 artifact lineage and source-of-truth contract

stage_id: 1013R_R223W_P0_ARTIFACT_LINEAGE_AND_SOURCE_OF_TRUTH_CONTRACT  
status: source_of_truth_contract_only  
reason: prevent static preview proliferation and teacher-draft baseline confusion

## 1. Core decision

R223W must not become another teacher manuscript line.

The project now has two separate artifact lines:

```text
Teacher manuscript quality line:
R223M / R223N / R223O

Sandbox / review shell line:
R223T / R223U / R223V / R223W / R223X
```

These lines must not be mixed.

## 2. Canonical teacher manuscript sources

| lesson | canonical source | role |
| --- | --- | --- |
| 我为文具代言 第三阶段 | R223M_P4_P1_teacher_readable_process_v6.html | golden classroom event expansion standard sample |
| 有趣的纸印 | R223N_P3_P1_teacher_manuscript_draft_v5.html | material / technique transfer sample |
| 色彩的碰撞 | R223O_P1_teacher_manuscript_draft_v2.html | color perception transfer sample |

Teacher manuscript quality must be improved only by returning to the corresponding R223M/N/O manuscript line.

## 3. Sandbox / review shell sources

| artifact | role | can modify teacher text? |
| --- | --- | --- |
| R223T_fixture_only_sandbox_preview.html | v0.1 / v0.2 candidate comparison shell | no |
| R223U review package | sandbox teacher/reviewer walkthrough | no |
| R223V review package | sandbox reduction / pilot hold decision | no |
| R223W future shell | review-only pilot gate spec/shell | no |

Sandbox/review shell artifacts may compare, cite, summarize or link canonical teacher manuscripts. They must not rewrite the teacher manuscript body.

## 4. Why this contract is needed

Without this contract:

- each gate could create a new static page
- every new static page could look like the latest teacher draft
- reviewers would not know which page is the teacher baseline
- teacher manuscript quality and pilot gate safety would become mixed

## 5. Current R223W rule

R223W is blocked until this source-of-truth contract is accepted.

After P0, R223W may only be:

```text
REVIEW_ONLY_PILOT_GATE_SPEC
```

It may not be:

```text
TEACHER_DRAFT_GENERATION_STAGE
TEACHER_MANUSCRIPT_REWRITE_STAGE
FORMAL_UI_STAGE
R97B_ROUTE_STAGE
```

