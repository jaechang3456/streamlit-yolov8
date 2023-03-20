import streamlit as st
import os
from ultralytics import YOLO
from detect import detect

image = (".jpg", ".png", ".jpeg")
video = (".mp4", ".avi", ".wmv")
model = YOLO('best.pt')

def run_Yolo() :
    st.subheader('yolov8')
    uploaded_file = st.file_uploader("Inference할 이미지나, 동영상 파일을 선택해주세요.")
    st.text("서버의 용량 문제로, 여러개의 파일은 지원하지 않습니다.")
    st.text("공백이 있는 파일이나 특수문자가 들어간 파일의 경우 지원하지 않습니다.")

    try:
        with open(f'./data/{uploaded_file.name}', 'wb') as f:
            f.write(uploaded_file.getbuffer())
    except AttributeError:
        st.warning("이미지나, 동영상 파일을 업로드해주세요.")

    _btn = st.button("RUN Inference")
    st.write("서버의 한계로 시간이 오래 걸릴수 있습니다.")

    if _btn == True:
        if os.path.exists("./runs/detect/predict"):
            os.system(f"rm -r ./runs/detect/predict/")

        detect(uploaded_file)

    try:
        _chk = st.checkbox("결과보기")
        st.text("동영상의 경우, H264코덱으로의 변환과정이 필요해 더욱 시간이 걸립니다.")
        if _chk == True:
            if uploaded_file.name.endswith(image):
                st.image(f'./runs/detect/predict/{uploaded_file.name}')
                with open(f'./runs/detect/predict/{uploaded_file.name}', "rb") as fp:
                    st.download_button("결과를 다운로드 하실거면 클릭하세요", fp,"res.jpg","image/jpg" )
            elif uploaded_file.name.endswith(video):
                if not os.path.exists("./runs/detect/predict/res.mp4"):
                    os.system(f"ffmpeg -i ./runs/detect/predict/{uploaded_file.name} -vcodec libx264 -f mp4 ./runs/detect/predict/res.mp4")
                else:
                    st.video("./runs/detect/predict/res.mp4")
                    with open("./runs/detect/predict/res.mp4", "rb") as fp:
                        st.download_button("결과를 다운로드 하실거면 클릭하세요", fp,"res.mp4","video/mp4" )

    except:
        st.warning("Inference 결과가 없습니다. Inference 먼저 수행하십시오.")


    
    
    
        

    

