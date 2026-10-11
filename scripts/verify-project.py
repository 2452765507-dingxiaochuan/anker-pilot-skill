#!/usr/bin/env python3
from pathlib import Path
import csv, json, re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]

# SKILL local refs
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
for ref in re.findall(r'`([^`]+)`', skill):
    if '/' in ref and not ref.startswith(('http://','https://')):
        ref=ref.rstrip('.,;')
        if any(ch in ref for ch in ['→','>']): continue
        if not (ROOT/ref).exists(): errors.append(f'missing SKILL ref: {ref}')

# Markdown fences
for f in ROOT.rglob('*.md'):
    txt=f.read_text(encoding='utf-8',errors='ignore')
    if txt.count('```')%2: errors.append(f'unbalanced code fence: {f.relative_to(ROOT)}')

# JSON
for f in ROOT.rglob('*.json'):
    try: json.loads(f.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'invalid json {f.relative_to(ROOT)}: {e}')

# Company fact source IDs
with (ROOT/'data/source-register.csv').open(encoding='utf-8-sig',newline='') as fh:
    src={r['source_id'] for r in csv.DictReader(fh)}
with (ROOT/'data/company-fact-ledger.csv').open(encoding='utf-8-sig',newline='') as fh:
    for r in csv.DictReader(fh):
        for sid in re.split(r'[;/]',r.get('source_id','')):
            sid=sid.strip()
            if sid and sid not in src: errors.append(f"unknown company source_id {sid} in {r.get('fact_id')}")

# Scenario source URLs
with (ROOT/'references/scenario-case-packs/source-register.csv').open(encoding='utf-8-sig',newline='') as fh:
    rows=list(csv.DictReader(fh))
    for i,r in enumerate(rows,2):
        if not r.get('url','').startswith(('http://','https://')): errors.append(f'scenario source missing URL row {i}')

# HTML quick checks
for f in [ROOT/'website/prompts.html',ROOT/'website/index.html',ROOT/'website/company-intelligence.html']:
    if not f.exists(): errors.append(f'missing website file {f.name}'); continue
    txt=f.read_text(encoding='utf-8',errors='ignore')
    for bad in ['TODO_REPLACE_ME','{{PLACEHOLDER}}','undefined</','NaN</']:
        if bad in txt: errors.append(f'{f.name} contains {bad}')

print(f'company sources: {len(src)}')
print(f'scenario source rows: {len(rows)}')
if errors:
    print('FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print('PASS: project structure, refs, JSON, source IDs and basic HTML checks')
