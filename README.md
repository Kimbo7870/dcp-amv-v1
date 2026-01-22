# scene-cut-detector (Auto Video Editor Prototype)

A prototype tool that detects **scene transitions** and estimates **action intensity** from visual change over time — then demonstrates a **distributed/parallel-friendly** workflow by splitting video work into independent chunks and reassembling results.

This started as a personal project to speed up editing for YouTube footage, and later became a hackathon-style demo because video analysis is naturally parallelisable (**split → process → merge**).

---

## Features

- **Scene transition detection**: flags likely cuts/transitions using frame-level visual change metrics.
- **Action intensity scoring**: highlights calmer vs. higher-motion segments based on change magnitude over time.
- **Chunked processing (distributed-friendly)**: structured so analysis can be parallelised and merged deterministically.
- **Run outputs**: writes processed artifacts to a per-run output folder.

> Note: This is a v2 prototype/hackathon demo repo. Setup is intentionally minimal and somewhat manual.

---

## Requirements

- **Node v14.21.2** (required for the DCP/distributed part)
- **Python 3** + `pip`

---

## Quickstart

### 1) Install Python dependencies
```bash
pip3 install -r requirements.txt
```

### 2) Create the run folders

Create two empty folders inside `data/runs/`:

- `run1`
- `run1_output`

Your folder structure should look like:
```
data/
  runs/
    run1/
    run1_output/
storage/
```

### 3) Choose input videos for the run

Open `create_run.py` and comment/uncomment the video inputs you want (the script expects multiple videos; use at least ~4).

Then run:
```bash
python3 create_run.py
```

### 4) Run the pipeline

```bash
python3 main.py
```

During execution, a plot window will appear. Close the plot window (click **X**) to allow the rest of the pipeline to finish.

### 5) Outputs

Processed outputs are written to:
```
data/runs/run1_output/
```

---

## Project layout (high level)

- `create_run.py` — prepares a run (inputs/config)
- `main.py` — runs analysis + distributed/DCP step + output generation
- `data/` — run inputs/outputs
- `storage/` — intermediate storage used during execution

---
