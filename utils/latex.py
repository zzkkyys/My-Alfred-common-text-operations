import re, argparse, sys, os

if __name__ == u"__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str)
    args = parser.parse_args()

    text = os.environ["text"]

    
    if args.action == "latex_rm_cite":
        cleaned_text = re.sub("~\\\\cite\\{[^{}]+\\}", "", text)
        print(cleaned_text, file=sys.stdout)
