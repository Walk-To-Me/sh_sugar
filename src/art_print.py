#!/usr/bin/env python3
import sys
import argparse
import shutil

# 修复后的 ASCII 艺术字体 - 确保每行字符数逻辑一致
PASS_ART = """
██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝███████║███████╗███████╗
██╔═══╝ ██╔══██║╚════██║╚════██║
██║     ██║  ██║███████║███████║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
"""

ERROR_ART = """
███████╗██████╗ ██████╗  ██████╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗
███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
"""

# ANSI 颜色
GREEN_FG = "\033[32m"
RED_FG = "\033[31m"
BOLD = "\033[1m"
RESET = "\033[0m"

def get_terminal_width():
    return shutil.get_terminal_size().columns

def print_art(art_text, fg_color):
    terminal_width = get_terminal_width()
    # 去除首尾空行，并统一处理每一行
    lines = art_text.strip("\n").split("\n")
    
    # 找到最长的一行，作为艺术字的基准宽度
    # 注意：某些特殊字符可能在终端占用 2 个宽度，但在 Python 字符串长度算 1
    # 这里我们假设使用标准等宽字体
    max_line_len = max(len(line) for line in lines)
    
    for line in lines:
        # 使用自定义居中逻辑，避免依赖 line.center() 在处理特殊字符时的不确定性
        padding = max(0, (terminal_width - max_line_len) // 2)
        print(f"{fg_color}{BOLD}{' ' * padding}{line}{RESET}")

def main():
    parser = argparse.ArgumentParser(description="在终端打印巨大的 PASS 或 ERROR")
    parser.add_argument("type", nargs="?", default="pass", 
                        choices=["pass", "error", "PASS", "ERROR"],
                        help="类型: pass 或 error")
    
    args = parser.parse_args()
    
    if args.type.lower() == "pass":
        print_art(PASS_ART, GREEN_FG)
    else:
        print_art(ERROR_ART, RED_FG)

if __name__ == "__main__":
    main()
