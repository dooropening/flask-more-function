# -*- coding: utf-8 -*-
import sys
from pathlib import Path


class DirectionTree:
    """生成目录树
    @ pathname: 目标目录
    @ filename: 要保存成文件的名称
    """

    def __init__(self, pathname='.', filename='tree.txt'):
        self.pathname = Path(pathname)
        self.filename = filename
        self.tree = ''

    def set_path(self, pathname):
        self.pathname = Path(pathname)

    def set_filename(self, filename):
        self.filename = filename

    def generate_tree(self, n=0, ignore_rules=None):
        if ignore_rules is None:
            ignore_rules = []

        if self.pathname.is_file():
            # 检查文件是否应该被排除
            if any(self.pathname.match(rule) for rule in ignore_rules):
                return
            self.tree += '    |' * n + '-' * 4 + self.pathname.name + '\n'
        elif self.pathname.is_dir():
            # 检查目录是否应该被排除，或者是否是.git文件夹
            if any(self.pathname.match(rule) for rule in ignore_rules) or self.pathname.name == '.git':
                return
            self.tree += '    |' * n + '-' * 4 + \
                         str(self.pathname.relative_to(self.pathname.parent)) + '\\' + '\n'

            for cp in self.pathname.iterdir():
                self.pathname = Path(cp)
                self.generate_tree(n + 1, ignore_rules)

    def save_file(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(self.tree)


def parse_gitignore(gitignore_path):
    with open(gitignore_path, 'r') as gitignore_file:
        lines = gitignore_file.readlines()
    # 去除行首尾的空白字符，并忽略注释和空行
    rules = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
    return rules


if __name__ == '__main__':
    dirtree = DirectionTree()
    # 命令参数个数为1，生成当前目录的目录树
    if len(sys.argv) == 1:
        ignore_rules = parse_gitignore(Path.cwd() / '.gitignore')
        dirtree.generate_tree(ignore_rules=ignore_rules)
        print(dirtree.tree)
    # 命令参数个数为2并且目录存在存在
    elif len(sys.argv) == 2 and Path(sys.argv[1]).exists():
        dirtree.set_path(sys.argv[1])
        ignore_rules = parse_gitignore(Path(sys.argv[1]) / '.gitignore')
        dirtree.generate_tree(ignore_rules=ignore_rules)
        print(dirtree.tree)
    # 命令参数个数为3并且目录存在存在
    elif len(sys.argv) == 3 and Path(sys.argv[1]).exists():
        dirtree.set_path(sys.argv[1])
        ignore_rules = parse_gitignore(Path(sys.argv[1]) / '.gitignore')
        dirtree.generate_tree(ignore_rules=ignore_rules)
        dirtree.set_filename(sys.argv[2])
        dirtree.save_file()
    else:  # 参数个数太多，无法解析
        print('命令行参数太多，请检查！')
