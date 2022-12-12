# evを計算する
def calculate_ev(bet_per_pot: int, fold_ratio: int) -> int:
    fold_ratio: float = fold_ratio / 100
    call_ratio: float = 1 - fold_ratio
    
    ev = int(100*fold_ratio - bet_per_pot*call_ratio)
    
    return ev