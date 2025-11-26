import argparse
from pathlib import Path

from toylang.utils import parse_file


def main():
    argparser = argparse.ArgumentParser(description="ToyLang interpreter")
    argparser.add_argument(
        "file", 
        type=Path, 
        help="Input .toy file"
    )
    argparser.add_argument(
        "--dump-tokens", 
        type=Path, 
        help="Output file to dump tokens"
    )
    argparser.add_argument(
        "--dump-tree", 
        type=Path, 
        help="Output file to dump tree"
    )
    args = argparser.parse_args()
    filepath: Path = args.file
    dump_tokens_filepath: Path | None = getattr(args, 'dump_tokens', None)
    dump_tree_filepath: Path | None = getattr(args, 'dump_tree', None)
    
    parse_file(filepath, dump_tokens_filepath, dump_tree_filepath)

if __name__ == '__main__':
    main()