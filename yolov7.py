import streamlit as st
import os

image = (".jpg", ".png", ".jpeg")
video = (".mp4", ".avi", ".wmv")

def run_Yolo() :
    _btn = st.button("RUN Inference")
    st.write("서버의 한계로 시간이 오래 걸릴수 있습니다.")

    if _btn == True:
        os.system(f"/home/appuser/venv/bin/python detect.py --weights best.pt --source ./data/{uploaded_file.name}")

    try:
        _chk = st.checkbox("결과보기")
        if _chk == True:
            if uploaded_file.name.endswith(image):
                st.image(f'./runs/detect/exp/{uploaded_file.name}')
            elif uploaded_file.name.endswith(video):
                os.system(f"ffmpeg -i ./runs/detect/exp/{uploaded_file.name} -vcodec libx264 -f mp4 res.mp4")
                st.video("res.mp4")

    except:
        st.warning("Inference 결과가 없습니다. Inference 먼저 수행하십시오.")


    # os.system("rm res.mp4")
    # os.system(f"rm ./data/{uploaded_file.name}")

    # os.system(f"rm -r ./runs/detect/")

