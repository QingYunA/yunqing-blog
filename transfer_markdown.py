from langchain_deepseek.chat_models import ChatDeepSeek  # 这个导入切记不要删除
import argparse
from pathlib import Path
import os
import re


def translate_markdown(input_file_path, output_dir=None):
    """
    翻译单个markdown文件

    Args:
        input_file_path (str): 输入文件路径
        output_dir (str): 输出目录，默认为None时使用默认路径

    Returns:
        str: 输出文件路径
    """
    llm = ChatDeepSeek(
        model="deepseek-chat", api_key="sk-4c3a67d95aab46a2bbd7c2cf38c970f3"
    )

    input_file = Path(input_file_path)
    name = input_file.stem

    # 如果没有指定输出目录，使用默认路径
    if output_dir is None:
        output_dir = "./src/content/posts/en"

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    prompt = """
# 角色 
你是能对markdown文件进行中英文翻译的大师
你的目标是：将markdown文档在中文与英文间转换，并保留原始的markdown格式、代码块不变

## 工作步骤 
1. 阅读用户输入的markdown文档，识别文档语言是中文还是英文
2. 如果语言是中文，则翻译为英文，如果语言是英文则翻译为中文
3. 仅进行语言翻译，保留markdown格式与代码块

## 注意
1. 被特殊分割线包裹的部分不应该翻译
2. 涉及到键名(key)的部分应该保留英文
2.代码块中的英文不应该被翻译
"""

    try:
        with open(input_file_path, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        message = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": markdown_content},
        ]
        print("正在翻译中·····")
        response = llm.invoke(message)
        res = response.content
        res = res.replace("```markdown", "")
        res = res[:-3] if res.endswith("```") else res

        output_file = os.path.join(output_dir, f"{name}_en.md")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(res)

        print(f"✅ 翻译完成: {input_file_path} -> {output_file}")
        return output_file

    except Exception as e:
        print(f"❌ 翻译失败 {input_file_path}: {str(e)}")
        return None


def process_input(input_path, output_dir=None):
    """
    处理输入路径，可以是文件或文件夹

    Args:
        input_path (str): 输入路径
        output_dir (str): 输出目录
    """
    input_path = Path(input_path)

    if input_path.is_file():
        # 如果是文件，检查是否为markdown文件
        if input_path.suffix.lower() in [".md", ".markdown"]:
            translate_markdown(str(input_path), output_dir)
        else:
            print(f"❌ 不是markdown文件: {input_path}")

    elif input_path.is_dir():
        # 如果是文件夹，遍历所有markdown文件
        md_files = list(input_path.glob("*.md")) + list(input_path.glob("*.markdown"))

        if not md_files:
            print(f"❌ 文件夹中没有找到markdown文件: {input_path}")
            return

        print(f"📁 找到 {len(md_files)} 个markdown文件")

        for md_file in md_files:
            translate_markdown(str(md_file), output_dir)

    else:
        print(f"❌ 路径不存在: {input_path}")


def rename_en_blog(file_path):
    file_path = Path(file_path)
    if file_path.is_dir():
        md_files = list(file_path.glob("*.md"))
        for md_file in md_files:
            rename_en_blog(md_file)
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.readlines()

        for line in content:
            if line.startswith("title:"):
                title = line.split("title:")[1].strip()
                break
        # 清理标题，移除不适合文件名的字符
        clean_title = re.sub(r'[<>:"/\\|?*]', "", title)
        clean_title = clean_title.replace(" ", "-")

        # 获取文件所在目录和扩展名
        file_dir = os.path.dirname(file_path)
        file_ext = os.path.splitext(file_path)[1]

        # 构建新的文件名
        new_filename = f"{clean_title}{file_ext}"
        new_file_path = os.path.join(file_dir, new_filename)

        # 重命名文件
        try:
            os.rename(file_path, new_file_path)
            print(f"✅ 文件重命名成功: {os.path.basename(file_path)} -> {new_filename}")
        except Exception as e:
            print(f"❌ 文件重命名失败: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="中英文markdown转化")
    parser.add_argument(
        "--input", "-i", type=str, required=True, help="输入文件或文件夹路径"
    )
    parser.add_argument("--translate", "-t", action="store_true", help="是否翻译")
    parser.add_argument("--rename", "-r", action="store_true", help="是否重命名")
    parser.add_argument(
        "--output_dir",
        "-o",
        type=str,
        default=None,
        help="输出目录，默认为./src/content/posts/en",
    )

    args = parser.parse_args()

    # 处理输入路径
    if args.translate:
        process_input(args.input, args.output_dir)
    if args.rename:
        rename_en_blog(args.input)
