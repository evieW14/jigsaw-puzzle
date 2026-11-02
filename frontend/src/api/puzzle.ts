import {api} from "./client.ts";
import type {Puzzle} from "../utils/types.js";

export function getPuzzle(rows: number, columns: number) {
    return api<Puzzle>(`/puzzle?rows=${rows}&columns=${columns}`);
}