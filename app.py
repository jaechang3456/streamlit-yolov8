import streamlit as st
import os
from yolov7 import run_Yolo

if not os.path.exists("./data/best.pt"):
    os.system("wget https://github.com/jaechang3456/streamlit-yolov7/raw/main/best.pt -O ./data/best.pt")
    os.system("wget https://github.com/jaechang3456/streamlit-yolov7/raw/main/traced_model.pt -O ./data/traced_model.pt")
    os.system("df -h")
    os.system("ls -al")

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
        run_Yolo()

if __name__ == '__main__':
    main()