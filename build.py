import os
import json

projects_dir = 'Projects'
project_data = {}

if not os.path.exists(projects_dir):
    os.makedirs(projects_dir)
    print("삐뽀! Projects 폴더를 새로 만들었습니다.")

for folder_name in sorted(os.listdir(projects_dir)):
    folder_path = os.path.join(projects_dir, folder_name)
    
    if os.path.isdir(folder_path):
        clean_title = folder_name.split('_', 1)[-1] if '_' in folder_name else folder_name
        
        images = []
        youtube_link = ""
        
        # ★ 새로 추가된 마법: 유튜브 링크가 적힌 텍스트 파일 찾기
        youtube_file = os.path.join(folder_path, "youtube.txt")
        if os.path.exists(youtube_file):
            with open(youtube_file, 'r', encoding='utf-8') as f:
                youtube_link = f.read().strip()
        
        for file_name in sorted(os.listdir(folder_path)):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                img_path = f"{projects_dir}/{folder_name}/{file_name}"
                images.append(img_path)
        
        if images:
            project_data[folder_name] = {
                "title": clean_title,
                "images": images,
                "youtube": youtube_link # 썸네일(images)과는 별개로 유튜브 데이터 추가!
            }

js_content = f"const projectData = {json.dumps(project_data, ensure_ascii=False, indent=4)};"

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("삐뽀! 성공적으로 빌드되었습니다! data.js 업데이트 완료!")