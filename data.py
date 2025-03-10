import chess.engine
import csv

csv_rows = [["FEN", "Nodes", "Evaluation (centipawns)", "PV First Move"]]
for i in range(0, 960):
    engine = chess.engine.SimpleEngine.popen_uci("stockfish-17.exe")  # Source: https://stockfishchess.org/download/

    depth = 30
    limit = chess.engine.Limit(depth=depth)

    board = chess.Board(chess960=True)
    board.set_chess960_pos(i)

    fen = board.fen()

    print(i)
    with engine.analysis(board, limit) as j:
        for k in j:
            if "depth" in k.keys():
                print(k)
                if k["depth"] == depth:
                    if "upperbound" not in k.keys():  # Prevents recording data at "lowerbound" depths.
                        if "lowerbound" not in k.keys():  # Prevents recording data at "upperbound" depths.
                            if "score" in k.keys():  # Prevents reading engine output of all legal moves when hashfull maximizes.
                                score = str(k["score"]).removeprefix("PovScore(Cp(").removesuffix("), WHITE)")
                                nodes = k["nodes"]
                                move = str(k["pv"][0])
    engine.close()  # Resets engine hash, preventing contamination from previously analyzed positions.

    row = [fen, nodes, score, move]
    csv_rows.append(row)

with open("data\\data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv_rows)
