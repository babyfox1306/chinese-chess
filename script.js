document.addEventListener('DOMContentLoaded', () => {
    const board = document.getElementById('board');
    const initialBoard = [
        ["rR", "rN", "rM", "rG", "rK", "rG", "rM", "rN", "rR"],
        ["", "", "", "", "", "", "", "", ""],
        ["", "rC", "", "", "", "", "", "rC", ""],
        ["rP", "", "rP", "", "rP", "", "rP", "", "rP"],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["bP", "", "bP", "", "bP", "", "bP", "", "bP"],
        ["", "bC", "", "", "", "", "", "bC", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["bR", "bN", "bM", "bG", "bK", "bG", "bM", "bN", "bR"]
    ];

    initialBoard.forEach((row, rowIndex) => {
        row.forEach((piece, colIndex) => {
            const cell = document.createElement('div');
            cell.textContent = piece;
            board.appendChild(cell);
        });
    });
});
