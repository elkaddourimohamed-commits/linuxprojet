import argparse, os, stat
def main():
    p=argparse.ArgumentParser(); p.add_argument("root"); p.add_argument("--max-files",type=int,default=50000); a=p.parse_args()
    count=0
    for cur,dirs,files in os.walk(a.root,followlinks=False):
        for name in files:
            path=os.path.join(cur,name)
            try: mode=os.stat(path,follow_symlinks=False).st_mode
            except OSError: continue
            count+=1
            if mode & stat.S_IWOTH: print("WORLD-WRITABLE",path)
            if count>=a.max_files: print("Limit reached"); return
    print("Scanned files:",count)
if __name__=="__main__": main()
