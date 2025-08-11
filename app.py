import streamlit as st
from img_upscaler import upscale_img
from streamlit_image_comparison import image_comparison
from PIL import Image
import os
import threading
from threading import Thread

class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, verbose=None):
        super().__init__(group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        super().join()
        return self._return

favicon = Image.open('public/AE.png')

st.set_page_config(
    page_title='Arkscale - AI Image Upscaler',
    page_icon=favicon
)

st.title('Arkscale - AI Image Upscaler')
st.write('Effortlessly upscale your images for free using AI!')
st.write('Currently supporting **2x**, **3x** and **4x** upscales')
st.write('Due to _computational_ (financial) restraints, please only upscale images < 100kb in size')

uploaded_file = st.file_uploader(
    'Upload your image',
    type=['png', 'jpg', 'jpeg', 'jfif', 'bmp', 'webp'],
)

if uploaded_file is not None:
    filename = uploaded_file.name
    img = Image.open(uploaded_file)
    width = img.size[0]

    st.image(img, caption='Uploaded Image', use_container_width=False)

    format_options = ['2x', '3x', '4x']
    output_scale = st.selectbox(
        'Choose upscale level',
        format_options
    )

    if st.button('Upscale'):
        t = CustomThread(target=upscale_img, args=(uploaded_file, int(output_scale[0])))

        t.start()
        st.spinner(text='Upscaling Image... Please wait...')
        ret = t.join()
        st.success('Upscaling complete!')

        upscaled_image = ret[0]
        comparison_image = ret[1]

        image_comparison(
            img1='base_img.png', img2='upscaled_img.png',
            label1='Original', label2='Upscaled',
            width=max(width+4, 304)
        )
        os.remove('base_img.png')
        os.remove('upscaled_img.png')
        os.remove('compare_img.png')

        st.write(f'Image upscaled by {output_scale}!')

        st.download_button(
            label=f'Download upscaled file',
            data=upscaled_image,
            file_name=f'{output_scale}_{filename}',
            mime=f'image/{output_scale}_{filename}',
            on_click='ignore',
        )

        st.download_button(
            label=f'Download a side-by-side comparison',
            data=comparison_image,
            file_name=f'{output_scale}_comparison_{filename}',
            mime=f'image/{output_scale}_comparison_{filename}',
            on_click='ignore',
        )





