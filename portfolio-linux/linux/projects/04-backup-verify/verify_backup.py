import argparse, hashlib
from pathlib import Path
def sha(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()
def main():
    p=argparse.ArgumentParser(); p.add_argument("manifest"); p.add_argument("--root",default="."); a=p.parse_args()
    bad=0
    for line in Path(a.manifest).read_text().splitlines():
        if not line.strip() or line.lstrip().startswith("#"): continue
        expected, rel=line.split(maxsplit=1); target=Path(a.root)/rel.strip().lstrip("*")
        if not target.is_file(): print("MISSING",target); bad+=1
        elif sha(target)==expected: print("OK",target)
        else: print("MISMATCH",target); bad+=1
    raise SystemExit(1 if bad else 0)
if __name__=="__main__": main()
