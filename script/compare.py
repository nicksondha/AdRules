import sys

def remove_lines_from_file(file_path, exclusion_file_path):
    # 读取vd.txt的内容并存储为一个集合
    with open(exclusion_file_path, 'r', newline='') as vd_file:
        vd_lines = set(vd_file.read().splitlines())

    # 读取1.txt的内容，并将不在vd_lines中的行保存到一个列表中
    with open(file_path, 'r', newline='') as original_file:
        lines_to_keep = [line.strip() for line in original_file if line.strip() not in vd_lines]

    # 将处理后的内容写入1.txt中，覆盖原文件
    with open(file_path, 'w', newline='') as modified_file:
        modified_file.write('\n'.join(lines_to_keep))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <file_path> <exclusion_file_path>")
    else:
        file_path = sys.argv[1]
        exclusion_file_path = sys.argv[2]
        remove_lines_from_file(file_path, exclusion_file_path)
        print("Lines removed successfully.")
