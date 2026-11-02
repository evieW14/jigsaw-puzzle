export interface Piece {
    row: number;
    column: number;
    x: number;
    y: number;
    width: number;
    height: number;
    image_url: string;
    id: string;
}

export interface Puzzle {
    rows: number;
    columns: number;
    width: number;
    height: number;
    pieces: Piece[];
}