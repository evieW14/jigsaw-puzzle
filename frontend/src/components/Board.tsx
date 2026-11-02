import type {Piece, Puzzle} from "../utils/types.ts";
import {useEffect, useState} from "react";
import {getPuzzle} from "../api/puzzle.ts";
import PuzzlePiece from "./PuzzlePiece.tsx";
import "./Board.css";

export default function Board() {
    const [pieces, setPieces] = useState<Piece[]>([]);
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadPuzzle = async () => {
            try {
                const data: Puzzle = await getPuzzle(2, 2);
                setPieces(data.pieces);
            } catch (err) {
                console.error("Failed to load puzzle:", err);
                setError("Failed to load puzzle");
                setPieces([]);
            } finally {
                setLoading(false);
            }
        };

        loadPuzzle();
    }, []);

    return (
        <div className="board">
            <div>
                {pieces.map((piece) => (
                    <PuzzlePiece
                        key={piece.id}
                        piece={piece}
                    />
                ))}
            </div>
        </div>
    );
}
