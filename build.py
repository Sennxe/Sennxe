import os
import json

def get_folder_data(base_dir):
    data = {}
    # 폴더가 없으면 자동으로 만들어줍니다
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        return data
        
    for folder_name in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, folder_name)
        if os.path.isdir(folder_path):
            clean_title = folder_name.split('_', 1)[-1] if '_' in folder_name else folder_name
            images = []
            youtube_link = ""
            
            youtube_file = os.path.join(folder_path, "youtube.txt")
            if os.path.exists(youtube_file):
                with open(youtube_file, 'r', encoding='utf-8') as f:
                    youtube_link = f.read().strip()
            
            for file_name in sorted(os.listdir(folder_path)):
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                    img_path = f"{base_dir}/{folder_name}/{file_name}"
                    images.append(img_path)
            
            if images:
                data[folder_name] = {
                    "title": clean_title,
                    "images": images,
                    "youtube": youtube_link
                }
    return data

print("삐뽀! 폴더들을 스캔하는 중입니다...")

motorsports_data = get_folder_data('MotorSports')
portfolio_data = get_folder_data('Portfolio')

js_content = f"const motorSportsData = {json.dumps(motorsports_data, ensure_ascii=False, indent=4)};\n"
js_content += f"const portfolioData = {json.dumps(portfolio_data, ensure_ascii=False, indent=4)};\n"

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("삐뽀! 2개의 카테고리가 data.js에 완벽하게 빌드되었습니다!")