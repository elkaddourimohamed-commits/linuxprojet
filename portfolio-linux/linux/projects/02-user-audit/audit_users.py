import argparse
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--passwd",default="/etc/passwd")
    a=p.parse_args()
    with open(a.passwd,encoding="utf-8") as f:
        for line in f:
            x=line.rstrip().split(":")
            if len(x)>=7:
                uid=int(x[2])
                print(f"{x[0]:20} uid={uid:<6} home={x[5]} shell={x[6]}{' [UID 0]' if uid==0 else ''}")
if __name__=="__main__": main()
