from cairosvg import svg2png
from PIL import Image

sizes = [16, 32, 48]

for size in sizes:
    svg2png(
        url = "assets/img/AyamKiwiLogo.svg",
        write_to = f"tmp/icon{size}.png",
        output_width = size,
        output_height = size
    )

pngs = [Image.open(f"tmp/icon{size}.png") for size in sizes]

icon = pngs.pop()

icon.save(
    "assets/img/favicon.ico",
    sizes = [(size, size) for size in sizes],
    append_images = pngs
)