import argparse, socket
def main():
    p=argparse.ArgumentParser(); p.add_argument("host"); p.add_argument("--port",type=int,default=443); a=p.parse_args()
    try: print("DNS:",sorted({x[4][0] for x in socket.getaddrinfo(a.host,None)}))
    except socket.gaierror as e: print("DNS FAILED:",e); raise SystemExit(1)
    try:
        with socket.create_connection((a.host,a.port),timeout=3): print(f"TCP {a.port}: reachable")
    except OSError as e: print(f"TCP {a.port}: failed ({e})"); raise SystemExit(2)
if __name__=="__main__": main()
