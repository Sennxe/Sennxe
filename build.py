import os
import json

# 폴더 설정
projects_dir = 'Projects'
project_data = {}

# Projects 폴더가 없으면 에러가 나지 않게 만들어줍니다
if not os.path.exists(projects_dir):
    os.makedirs(projects_dir)
    print("삐뽀! Projects 폴더를 새로 만들었습니다. 이 안에 작품 폴더들을 넣어주세요.")

# Projects 폴더 안에 있는 폴더들을 이름(숫자) 순서대로 읽어옵니다
for folder_name in sorted(os.listdir(projects_dir)):
    folder_path = os.path.join(projects_dir, folder_name)
    
    if os.path.isdir(folder_path):
        # 01_Saki 처럼 앞에 붙인 숫자를 웹페이지 제목에서는 깔끔하게 제거합니다!
        # 언더바(_) 뒤에 있는 진짜 이름만 분리해냅니다.
        clean_title = folder_name.split('_', 1)[-1] if '_' in folder_name else folder_name
        
        # 폴더 안의 이미지 파일들을 순서대로 가져옵니다
        images = []
        for file_name in sorted(os.listdir(folder_path)):
            # 그림 파일이 맞는지 확인
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                # 웹페이지가 인식할 수 있는 이미지 경로 생성 (역슬래시 방지)
                img_path = f"{projects_dir}/{folder_name}/{file_name}"
                images.append(img_path)
        
        # 이미지가 한 장이라도 들어있는 폴더만 데이터로 저장합니다
        if images:
            project_data[folder_name] = {
                "title": clean_title,
                "images": images
            }

# 자바스크립트용 data.js 파일 생성
js_content = f"const projectData = {json.dumps(project_data, ensure_ascii=False, indent=4)};"

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("삐뽀! 성공적으로 빌드되었습니다! data.js 파일이 생성 및 업데이트되었습니다.")
print("이제 index.html을 열어보시거나, 깃허브에 폴더 전체를 업로드해 보세요!")
input("엔터 키를 누르면 창이 닫힙니다...")