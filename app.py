import streamlit as st
from yolov8 import run_Yolo

def main():
    
    st.set_page_config(page_title="yolov8 ObjectDetection", page_icon="./data/LJC.jpg")

    st.title('yolov8 ObjectDetection')
    # 사이드바 메뉴
    choice = st.sidebar.radio('Menu', ('Home','yolov8'))

    if choice =='Home':
        st.write('이 앱은 yolo8을 이용하여 custom train한 모델로 inference하는 앱입니다.')
        st.write('사람과 차량 2class로 되어있습니다.')
        st.subheader('yolov8')
        st.image('./data/yolov8.png')
        st.text('\n')
        st.text('\n')
        st.text('yolov8 custom모델의 Inference 결과를 확인하시려면 사이드바 메뉴에서 선택하세요.')
        st.text('\n')
        st.text('시간이 되는 경우 여러기능들 추가 예정입니다.')


    elif choice == 'yolov8' :
        run_Yolo()

if __name__ == '__main__':
    main()