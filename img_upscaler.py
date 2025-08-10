from super_image import EdsrModel, ImageLoader
from PIL import Image
import io

def upscale_img(image_file, upscale_level):
    with Image.open(image_file) as img:
        img.save('base_img.png', 'png')

        model = EdsrModel.from_pretrained('eugenesiow/edsr', scale=upscale_level)
        inputs = ImageLoader.load_image(img)
        preds = model(inputs)

        ImageLoader.save_image(preds, 'upscaled_img.png')
        ImageLoader.save_compare(inputs, preds, 'compare_img.png')

        with Image.open('upscaled_img.png') as i:
            with Image.open('compare_img.png') as j:
                output_image = io.BytesIO()
                compare_image = io.BytesIO()

                i.save(output_image, 'png')
                j.save(compare_image, 'png')

                output_image.seek(0)
                compare_image.seek(0)

                return (output_image, compare_image)
