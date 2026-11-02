import type { Piece } from "../utils/types.ts";
import "./PuzzlePiece.css";
import {assetUrl} from "../api/client.ts";

interface PieceProps{
    piece: Piece
}

export default function PuzzlePiece({piece} : PieceProps) {

    return (
        <div className="piece">
            {piece.image_url ? (
                <img src={assetUrl(piece.image_url)} alt={piece.id} />
            ) : (
                <div className="piece-image piece-image-placeholder">
                    {piece.id}
                </div>
            )}
        </div>
    );
}
