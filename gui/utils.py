from PIL import Image, ImageTk


def resized_img(path: str, width: float, height: float):
    with Image.open(path) as img:
        img_resized = img.resize((width, height), Image.LANCZOS)

        return ImageTk.PhotoImage(img_resized)
