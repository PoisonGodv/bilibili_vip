import argparse
from scripts.login import auth
from scripts.start_senior import start
from scripts.check import check
from scripts.switch_model import switch_model

def main():
    parser = argparse.ArgumentParser(description="B站硬核会员自动答题工具")
    parser.add_argument("--switch-model", action="store_true", help="切换主要使用的模型")
    args = parser.parse_args()
    
    if args.switch_model:
        switch_model()
        return
    
    check()
    auth()
    start()

if __name__ == "__main__":
    main()