import re, argparse, sys, os

if __name__ == u"__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str)
    args = parser.parse_args()

    text = os.environ["text"]
    
    print(args, file=sys.stderr)
    
    if args.action == "mermaid-quote":
        # 为节点加引号
        cleaned_text = re.sub(r'(\[)([^\[\]]+)(\])', r'["\2"]', text)
        print(cleaned_text, file=sys.stdout)