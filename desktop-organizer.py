import os
import shutil
from pathlib import Path

# ========== 配置 ==========
# 自动获取桌面路径（支持 Windows / macOS / Linux）
DESKTOP = Path.home() / "Desktop"

# 文件类型分类（可自定义扩展）
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".md", ".epub"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".dmg", ".pkg", ".msi", ".app"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".go", ".rs", ".ts", ".json", ".yaml", ".yml"],
}

# ========== 主函数 ==========
def organize_desktop():
    if not DESKTOP.exists():
        print(f"桌面路径不存在: {DESKTOP}")
        return

    print(f"正在整理桌面: {DESKTOP}")
    moved_count = 0

    for item in DESKTOP.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            target_folder = "Others"

            # 查找文件类型归属
            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_folder = folder
                    break

            # 创建目标文件夹（如果不存在）
            target_path = DESKTOP / target_folder
            target_path.mkdir(exist_ok=True)

            # 移动文件（避免同名覆盖）
            new_path = target_path / item.name
            if new_path.exists():
                print(f"⚠️  文件已存在，跳过: {item.name}")
                continue

            try:
                shutil.move(str(item), str(new_path))
                print(f"✅ 移动: {item.name} → {target_folder}/")
                moved_count += 1
            except Exception as e:
                print(f"❌ 移动失败 {item.name}: {e}")

    print(f"\n整理完成！共移动 {moved_count} 个文件。")
    print(f"桌面清爽啦！✨")

if __name__ == "__main__":
    organize_desktop()
