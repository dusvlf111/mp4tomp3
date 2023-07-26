import os
from moviepy.editor import *

def find_mp4_files(folder_path):
    """
    특정 폴더에서 mp4 파일을 검색하여 리스트로 반환하는 함수입니다.

    Parameters:
        folder_path (str): 검색할 폴더의 경로.

    Returns:
        list: mp4 파일 경로들이 담긴 리스트.
    """
    mp4_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp4"):
            mp4_files.append(os.path.join(folder_path, filename))
    return mp4_files

def convert_mp4_to_mp3(input_file, output_file):
    """
    mp4 파일을 mp3 파일로 변환하는 함수입니다.

    Parameters:
        input_file (str): 입력으로 사용할 mp4 파일의 경로.
        output_file (str): 출력으로 저장할 mp3 파일의 경로.
    """
    try:
        # 비디오 클립을 불러옵니다.
        video_clip = VideoFileClip(input_file)

        # 비디오 클립으로부터 오디오를 추출합니다.
        audio_clip = video_clip.audio

        # 추출한 오디오를 mp3 파일로 저장합니다.
        audio_clip.write_audiofile(output_file)

        # 오디오와 비디오 클립을 닫습니다.
        audio_clip.close()
        video_clip.close()

        print(f"변환 성공! {output_file}가 생성되었습니다.")
    except Exception as e:
        print(f"오류 발생: {str(e)}")

if __name__ == "__main__":
    # 폴더 경로 설정
    folder_path = "input_folder"

    # 폴더 내의 mp4 파일들 검색
    try:
        mp4_files_list = find_mp4_files(folder_path)
    except:
        print('파일경로에 파일이 존재하지 않습니다. input_folder에 파일을 추가해주세요.')
        if not os.path.exists(folder_path):
            os.makedirs('input_folder')

    # 저장할 폴더 경로 설정
    output_folder = "output_folder"
    
    # 디렉토리가 존재하지 않으면 생성
    
    if not os.path.exists(output_folder):
        os.makedirs('output_folder')

    #진행 상황 체크하기
    list_sizes = len(mp4_files_list)
    file_sizes = 0
    fale_files = []
    # 각 mp4 파일을 mp3로 변환
    for mp4_file in mp4_files_list:
        print(f"{mp4_file} 진행중...")
        # mp4 파일 이름에서 확장자를 제거하고 .mp3 확장자를 추가하여 출력 파일 이름을 만듭니다.
        mp3_output_file = os.path.splitext(os.path.basename(mp4_file))[0] + ".mp3"
        mp3_output_path = os.path.join(output_folder, mp3_output_file)
        
        # mp4를 mp3로 변환
        try:
            convert_mp4_to_mp3(mp4_file, mp3_output_path)
        except:
            print(f'{mp4_file} 파일 변환에 실패했습니다.')
            fale_files.append(mp4_file)
            pass
        
        file_sizes+=1
        print(f'------------ 진행상황 {round(file_sizes/list_sizes*100,1)}% ---------------------')
        
    print('모두 완료했습니다.')
    print(f'실패한 파일은 {len(fale_files)}개입니다.')
    
    print('실패한 항목')
    for i in fale_files:
        print(i)
        
 