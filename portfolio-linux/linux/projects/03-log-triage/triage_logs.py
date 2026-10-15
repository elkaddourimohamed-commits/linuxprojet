import argparse
WORDS=("error","failed","critical","denied","timeout")
def main():
    p=argparse.ArgumentParser(); p.add_argument("logfile"); p.add_argument("--limit",type=int,default=25); a=p.parse_args()
    hits=[]
    with open(a.logfile,encoding="utf-8",errors="replace") as f:
        for line in f:
            if any(w in line.lower() for w in WORDS): hits.append(line.rstrip())
    print(f"Potential incidents: {len(hits)}")
    print("\n".join(hits[:max(0,a.limit)]))
if __name__=="__main__": main()
