from pydantic import BaseModel, Field, computed_field


class Piece(BaseModel):
    row: int = Field(ge=0)
    column: int = Field(ge=0)

    # Where this piece's top-left corner belongs on the solved board
    x: int = Field(ge=0)
    y: int = Field(ge=0)

    width: int = Field(gt=0)
    height: int = Field(gt=0)

    image_url: str

    @computed_field
    @property
    def id(self) -> str:
        return f"r{self.row}_c{self.column}"


class Puzzle(BaseModel):
    rows: int = Field(gt=0)
    columns: int = Field(gt=0)
    width: int = Field(gt=0)    # full image width in px
    height: int = Field(gt=0)   # full image height in px
    pieces: list[Piece]