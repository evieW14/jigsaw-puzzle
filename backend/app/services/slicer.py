from PIL import Image
from app.models.puzzle import Piece, Puzzle
from pathlib import Path


def slice_image(image_path: Path, rows: int, columns: int, out_dir: Path, url_prefix: str) -> Puzzle:
    out_dir.mkdir(parents=True, exist_ok=True)
    pieces: list[Piece] = []

    with Image.open(image_path) as img:
        img_w, img_h = img.size

        for row in range(rows):
            top = row * img_h // rows
            bottom = (row + 1) * img_h // rows

            for col in range(columns):
                left = col * img_w // columns
                right = (col + 1) * img_w // columns

                tile = img.crop((left, top, right, bottom))
                filename = f"r{row}_c{col}.png"
                tile.save(out_dir / filename)

                pieces.append(Piece(row=row, column=col, x=left, y=top, width=right - left, height=bottom - top,
                    image_url=f"{url_prefix}/{filename}", ))

    return Puzzle(rows=rows, columns=columns, width=img_w, height=img_h, pieces=pieces)
