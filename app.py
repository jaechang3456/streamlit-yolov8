import streamlit as st
import os
from yolov7 import run_Yolo

def main():
    
    st.set_page_config(page_title="yolov7 ObjectDetection", page_icon="./data/LJC.jpg")

    st.title('yolov7 ObjectDetection')
    # 사이드바 메뉴
    choice = st.sidebar.radio('Menu', ('Home','yolov7'))

    if choice =='Home':
        st.write('이 앱은 yolov7을 이용하여 custom train한 모델로 inference하는 앱입니다.')
        st.write('사람과 차량 2class로 되어있습니다.')
        st.subheader('yolov7')
        st.write('yolov7 : Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors')
        st.write('bag-of-freebies 이란 inference 과정 중에 추가 계산 비용을 발생시키지 않으면서 네트워크의 성능을 향상시키는 기법들을 말합니다.')
        st.image('./data/yolov7.png')
        st.write('yolov7은 속도와 정확도에서 현재까지 나온 모든 ObjectDetection의 성능보다 좋다고 합니다.')
        st.write('자세한 내용은 아래 github링크와, paper링크를 확인해 주세요.')
        st.markdown('github : https://github.com/WongKinYiu/yolov7')
        st.markdown('paper : https://arxiv.org/pdf/2207.02696.pdf')
        st.text('\n')
        st.text('\n')
        st.text('yolov7 custom모델의 Inference 결과를 확인하시려면 사이드바 메뉴에서 선택하세요.')

    elif choice == 'yolov7' :
        os.system("git lfs pull")
        st.subheader('yolov7')
        uploaded_file = st.file_uploader("Inference할 이미지나, 동영상 파일을 선택해주세요.")
        st.text("서버의 용량 문제로, 여러개의 파일은 지원하지 않습니다.")
        st.text("공백이 있는 파일의 경우 지원하지 않습니다.")

    try:
        with open(f'./data/{uploaded_file.name}', 'wb') as f:
            f.write(uploaded_file.getbuffer())
    except AttributeError:
        st.warning("이미지나, 동영상 파일을 업로드해주세요.")
        run_Yolo()

if __name__ == '__main__':
    main()